# SNMP MIB module (ELTEX-LTP8X) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ELTEX-LTP8X
# Produced by pysmi-1.5.4 at Mon Oct 14 21:37:15 2024
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

(elHardware,
 mcTrapDescr,
 mcTrapExState,
 mcTrapID,
 mcTrapLParam1,
 mcTrapLParam2,
 mcTrapLParam3) = mibBuilder.importSymbols(
    "ELTEX-SMI-ACTUAL",
    "elHardware",
    "mcTrapDescr",
    "mcTrapExState",
    "mcTrapID",
    "mcTrapLParam1",
    "mcTrapLParam2",
    "mcTrapLParam3")

(Ipv6Address,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address")

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 MacAddress,
 RowStatus,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ltp8x = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22)
)
ltp8x.setRevisions(
        ("2010-07-21 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ONTSerial(OctetString, TextualConvention):
    status = "current"
    displayHint = "1x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )



class LTPONTState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("allocated", 1),
          ("authFailed", 3),
          ("authInProgress", 2),
          ("authOk", 4),
          ("blocked", 9),
          ("cfgFailed", 6),
          ("cfgInProgress", 5),
          ("disabled", 15),
          ("failed", 8),
          ("free", 0),
          ("fwUpdating", 12),
          ("mibreset", 10),
          ("ok", 7),
          ("preconfig", 11),
          ("redundant", 14),
          ("unactivated", 13),
          ("unknown", 16))
    )



class DBAServiceClass(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dbaData", 0),
          ("dbaTDMCBR", 2),
          ("dbaVoIP", 1))
    )



class DBAStatusReport(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("statusReportNSR", 0),
          ("statusReportType0", 1),
          ("statusReportType1", 2))
    )



class AddressEntryType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 0),
          ("dynamicAndStatic", 2),
          ("static", 1))
    )



class VideoRxPowerConv(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            32767
        )
    )
    namedValues = NamedValues(
        ("noVideoSignal", 32767)
    )



# MIB Managed Objects in the order of their OIDs

_Ltp8xPONChannels_ObjectIdentity = ObjectIdentity
ltp8xPONChannels = _Ltp8xPONChannels_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 2)
)
_Ltp8xPONChannelStateTable_Object = MibTable
ltp8xPONChannelStateTable = _Ltp8xPONChannelStateTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 2, 1)
)
if mibBuilder.loadTexts:
    ltp8xPONChannelStateTable.setStatus("current")
_Ltp8xPONChannelStateEntry_Object = MibTableRow
ltp8xPONChannelStateEntry = _Ltp8xPONChannelStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 2, 1, 1)
)
ltp8xPONChannelStateEntry.setIndexNames(
    (0, "ELTEX-LTP8X", "ltp8xPONChannelSlot"),
    (0, "ELTEX-LTP8X", "ltp8xPONChannelID"),
)
if mibBuilder.loadTexts:
    ltp8xPONChannelStateEntry.setStatus("current")
_Ltp8xPONChannelSlot_Type = Unsigned32
_Ltp8xPONChannelSlot_Object = MibTableColumn
ltp8xPONChannelSlot = _Ltp8xPONChannelSlot_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 2, 1, 1, 1),
    _Ltp8xPONChannelSlot_Type()
)
ltp8xPONChannelSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xPONChannelSlot.setStatus("current")
_Ltp8xPONChannelID_Type = Unsigned32
_Ltp8xPONChannelID_Object = MibTableColumn
ltp8xPONChannelID = _Ltp8xPONChannelID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 2, 1, 1, 2),
    _Ltp8xPONChannelID_Type()
)
ltp8xPONChannelID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xPONChannelID.setStatus("current")
_Ltp8xPONChannelState_Type = Unsigned32
_Ltp8xPONChannelState_Object = MibTableColumn
ltp8xPONChannelState = _Ltp8xPONChannelState_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 2, 1, 1, 3),
    _Ltp8xPONChannelState_Type()
)
ltp8xPONChannelState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xPONChannelState.setStatus("current")
_Ltp8xPONChannelONTCount_Type = Unsigned32
_Ltp8xPONChannelONTCount_Object = MibTableColumn
ltp8xPONChannelONTCount = _Ltp8xPONChannelONTCount_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 2, 1, 1, 4),
    _Ltp8xPONChannelONTCount_Type()
)
ltp8xPONChannelONTCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xPONChannelONTCount.setStatus("current")
_Ltp8xPONChannelEnabled_Type = TruthValue
_Ltp8xPONChannelEnabled_Object = MibTableColumn
ltp8xPONChannelEnabled = _Ltp8xPONChannelEnabled_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 2, 1, 1, 5),
    _Ltp8xPONChannelEnabled_Type()
)
ltp8xPONChannelEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xPONChannelEnabled.setStatus("current")
_Ltp8xPONChannelSFPVendor_Type = DisplayString
_Ltp8xPONChannelSFPVendor_Object = MibTableColumn
ltp8xPONChannelSFPVendor = _Ltp8xPONChannelSFPVendor_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 2, 1, 1, 6),
    _Ltp8xPONChannelSFPVendor_Type()
)
ltp8xPONChannelSFPVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xPONChannelSFPVendor.setStatus("current")
_Ltp8xPONChannelSFPProductNumber_Type = DisplayString
_Ltp8xPONChannelSFPProductNumber_Object = MibTableColumn
ltp8xPONChannelSFPProductNumber = _Ltp8xPONChannelSFPProductNumber_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 2, 1, 1, 7),
    _Ltp8xPONChannelSFPProductNumber_Type()
)
ltp8xPONChannelSFPProductNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xPONChannelSFPProductNumber.setStatus("current")
_Ltp8xPONChannelSFPRevision_Type = DisplayString
_Ltp8xPONChannelSFPRevision_Object = MibTableColumn
ltp8xPONChannelSFPRevision = _Ltp8xPONChannelSFPRevision_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 2, 1, 1, 8),
    _Ltp8xPONChannelSFPRevision_Type()
)
ltp8xPONChannelSFPRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xPONChannelSFPRevision.setStatus("current")
_Ltp8xPONChannelTxPower_Type = Integer32
_Ltp8xPONChannelTxPower_Object = MibTableColumn
ltp8xPONChannelTxPower = _Ltp8xPONChannelTxPower_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 2, 1, 1, 9),
    _Ltp8xPONChannelTxPower_Type()
)
ltp8xPONChannelTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xPONChannelTxPower.setStatus("current")
_Ltp8xPONChannelSFPTemperature_Type = Integer32
_Ltp8xPONChannelSFPTemperature_Object = MibTableColumn
ltp8xPONChannelSFPTemperature = _Ltp8xPONChannelSFPTemperature_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 2, 1, 1, 10),
    _Ltp8xPONChannelSFPTemperature_Type()
)
ltp8xPONChannelSFPTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xPONChannelSFPTemperature.setStatus("current")
_Ltp8xPONChannelSFPVoltage_Type = Integer32
_Ltp8xPONChannelSFPVoltage_Object = MibTableColumn
ltp8xPONChannelSFPVoltage = _Ltp8xPONChannelSFPVoltage_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 2, 1, 1, 11),
    _Ltp8xPONChannelSFPVoltage_Type()
)
ltp8xPONChannelSFPVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xPONChannelSFPVoltage.setStatus("current")
_Ltp8xPONChannelSFPTxBiasCurrent_Type = Integer32
_Ltp8xPONChannelSFPTxBiasCurrent_Object = MibTableColumn
ltp8xPONChannelSFPTxBiasCurrent = _Ltp8xPONChannelSFPTxBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 2, 1, 1, 12),
    _Ltp8xPONChannelSFPTxBiasCurrent_Type()
)
ltp8xPONChannelSFPTxBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xPONChannelSFPTxBiasCurrent.setStatus("current")
_Ltp8xPONChannelReconfigure_Type = Unsigned32
_Ltp8xPONChannelReconfigure_Object = MibTableColumn
ltp8xPONChannelReconfigure = _Ltp8xPONChannelReconfigure_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 2, 1, 1, 20),
    _Ltp8xPONChannelReconfigure_Type()
)
ltp8xPONChannelReconfigure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xPONChannelReconfigure.setStatus("current")
_Ltp8xPONChannelResetCounters_Type = Unsigned32
_Ltp8xPONChannelResetCounters_Object = MibTableColumn
ltp8xPONChannelResetCounters = _Ltp8xPONChannelResetCounters_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 2, 1, 1, 21),
    _Ltp8xPONChannelResetCounters_Type()
)
ltp8xPONChannelResetCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xPONChannelResetCounters.setStatus("current")
_Ltp8xPONChannelActModeTable_Object = MibTable
ltp8xPONChannelActModeTable = _Ltp8xPONChannelActModeTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 2, 2)
)
if mibBuilder.loadTexts:
    ltp8xPONChannelActModeTable.setStatus("current")
_Ltp8xPONChannelActModeEntry_Object = MibTableRow
ltp8xPONChannelActModeEntry = _Ltp8xPONChannelActModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 2, 2, 1)
)
ltp8xPONChannelActModeEntry.setIndexNames(
    (0, "ELTEX-LTP8X", "ltp8xPONChannelActModeSlot"),
    (0, "ELTEX-LTP8X", "ltp8xPONChannelActModeChannel"),
)
if mibBuilder.loadTexts:
    ltp8xPONChannelActModeEntry.setStatus("current")
_Ltp8xPONChannelActModeSlot_Type = Unsigned32
_Ltp8xPONChannelActModeSlot_Object = MibTableColumn
ltp8xPONChannelActModeSlot = _Ltp8xPONChannelActModeSlot_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 2, 2, 1, 1),
    _Ltp8xPONChannelActModeSlot_Type()
)
ltp8xPONChannelActModeSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ltp8xPONChannelActModeSlot.setStatus("current")
_Ltp8xPONChannelActModeChannel_Type = Unsigned32
_Ltp8xPONChannelActModeChannel_Object = MibTableColumn
ltp8xPONChannelActModeChannel = _Ltp8xPONChannelActModeChannel_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 2, 2, 1, 2),
    _Ltp8xPONChannelActModeChannel_Type()
)
ltp8xPONChannelActModeChannel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ltp8xPONChannelActModeChannel.setStatus("current")
_Ltp8xPONChannelActModeHostControlledLumpedSN_Type = TruthValue
_Ltp8xPONChannelActModeHostControlledLumpedSN_Object = MibTableColumn
ltp8xPONChannelActModeHostControlledLumpedSN = _Ltp8xPONChannelActModeHostControlledLumpedSN_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 2, 2, 1, 3),
    _Ltp8xPONChannelActModeHostControlledLumpedSN_Type()
)
ltp8xPONChannelActModeHostControlledLumpedSN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xPONChannelActModeHostControlledLumpedSN.setStatus("current")
_Ltp8xPONChannelAddressTable_Object = MibTable
ltp8xPONChannelAddressTable = _Ltp8xPONChannelAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 2, 3)
)
if mibBuilder.loadTexts:
    ltp8xPONChannelAddressTable.setStatus("current")
_Ltp8xPONChannelAddressEntry_Object = MibTableRow
ltp8xPONChannelAddressEntry = _Ltp8xPONChannelAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 2, 3, 1)
)
ltp8xPONChannelAddressEntry.setIndexNames(
    (0, "ELTEX-LTP8X", "ltp8xPONChannelAddressSlot"),
    (0, "ELTEX-LTP8X", "ltp8xPONChannelAddressChannel"),
    (0, "ELTEX-LTP8X", "ltp8xPONChannelAddressEntryID"),
)
if mibBuilder.loadTexts:
    ltp8xPONChannelAddressEntry.setStatus("current")
_Ltp8xPONChannelAddressSlot_Type = Unsigned32
_Ltp8xPONChannelAddressSlot_Object = MibTableColumn
ltp8xPONChannelAddressSlot = _Ltp8xPONChannelAddressSlot_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 2, 3, 1, 1),
    _Ltp8xPONChannelAddressSlot_Type()
)
ltp8xPONChannelAddressSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ltp8xPONChannelAddressSlot.setStatus("current")
_Ltp8xPONChannelAddressChannel_Type = Unsigned32
_Ltp8xPONChannelAddressChannel_Object = MibTableColumn
ltp8xPONChannelAddressChannel = _Ltp8xPONChannelAddressChannel_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 2, 3, 1, 2),
    _Ltp8xPONChannelAddressChannel_Type()
)
ltp8xPONChannelAddressChannel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ltp8xPONChannelAddressChannel.setStatus("current")
_Ltp8xPONChannelAddressEntryID_Type = Unsigned32
_Ltp8xPONChannelAddressEntryID_Object = MibTableColumn
ltp8xPONChannelAddressEntryID = _Ltp8xPONChannelAddressEntryID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 2, 3, 1, 3),
    _Ltp8xPONChannelAddressEntryID_Type()
)
ltp8xPONChannelAddressEntryID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ltp8xPONChannelAddressEntryID.setStatus("current")
_Ltp8xPONChannelAddressONTSerial_Type = ONTSerial
_Ltp8xPONChannelAddressONTSerial_Object = MibTableColumn
ltp8xPONChannelAddressONTSerial = _Ltp8xPONChannelAddressONTSerial_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 2, 3, 1, 4),
    _Ltp8xPONChannelAddressONTSerial_Type()
)
ltp8xPONChannelAddressONTSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xPONChannelAddressONTSerial.setStatus("current")
_Ltp8xPONChannelAddressONTID_Type = Unsigned32
_Ltp8xPONChannelAddressONTID_Object = MibTableColumn
ltp8xPONChannelAddressONTID = _Ltp8xPONChannelAddressONTID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 2, 3, 1, 5),
    _Ltp8xPONChannelAddressONTID_Type()
)
ltp8xPONChannelAddressONTID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xPONChannelAddressONTID.setStatus("current")
_Ltp8xPONChannelAddressPriority_Type = Integer32
_Ltp8xPONChannelAddressPriority_Object = MibTableColumn
ltp8xPONChannelAddressPriority = _Ltp8xPONChannelAddressPriority_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 2, 3, 1, 6),
    _Ltp8xPONChannelAddressPriority_Type()
)
ltp8xPONChannelAddressPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xPONChannelAddressPriority.setStatus("current")
_Ltp8xPONChannelAddressCVID_Type = Integer32
_Ltp8xPONChannelAddressCVID_Object = MibTableColumn
ltp8xPONChannelAddressCVID = _Ltp8xPONChannelAddressCVID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 2, 3, 1, 7),
    _Ltp8xPONChannelAddressCVID_Type()
)
ltp8xPONChannelAddressCVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xPONChannelAddressCVID.setStatus("current")
_Ltp8xPONChannelAddressSVID_Type = Integer32
_Ltp8xPONChannelAddressSVID_Object = MibTableColumn
ltp8xPONChannelAddressSVID = _Ltp8xPONChannelAddressSVID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 2, 3, 1, 8),
    _Ltp8xPONChannelAddressSVID_Type()
)
ltp8xPONChannelAddressSVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xPONChannelAddressSVID.setStatus("current")
_Ltp8xPONChannelAddressMacAddress_Type = MacAddress
_Ltp8xPONChannelAddressMacAddress_Object = MibTableColumn
ltp8xPONChannelAddressMacAddress = _Ltp8xPONChannelAddressMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 2, 3, 1, 9),
    _Ltp8xPONChannelAddressMacAddress_Type()
)
ltp8xPONChannelAddressMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xPONChannelAddressMacAddress.setStatus("current")
_Ltp8xPONChannelAddressCPUDestined_Type = TruthValue
_Ltp8xPONChannelAddressCPUDestined_Object = MibTableColumn
ltp8xPONChannelAddressCPUDestined = _Ltp8xPONChannelAddressCPUDestined_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 2, 3, 1, 10),
    _Ltp8xPONChannelAddressCPUDestined_Type()
)
ltp8xPONChannelAddressCPUDestined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xPONChannelAddressCPUDestined.setStatus("current")
_Ltp8xPONChannelAddressDatapathForwarding_Type = TruthValue
_Ltp8xPONChannelAddressDatapathForwarding_Object = MibTableColumn
ltp8xPONChannelAddressDatapathForwarding = _Ltp8xPONChannelAddressDatapathForwarding_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 2, 3, 1, 11),
    _Ltp8xPONChannelAddressDatapathForwarding_Type()
)
ltp8xPONChannelAddressDatapathForwarding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xPONChannelAddressDatapathForwarding.setStatus("current")
_Ltp8xPONChannelAddressUniPort_Type = Unsigned32
_Ltp8xPONChannelAddressUniPort_Object = MibTableColumn
ltp8xPONChannelAddressUniPort = _Ltp8xPONChannelAddressUniPort_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 2, 3, 1, 12),
    _Ltp8xPONChannelAddressUniPort_Type()
)
ltp8xPONChannelAddressUniPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xPONChannelAddressUniPort.setStatus("current")
_Ltp8xPONChannelAddressEntryType_Type = AddressEntryType
_Ltp8xPONChannelAddressEntryType_Object = MibTableColumn
ltp8xPONChannelAddressEntryType = _Ltp8xPONChannelAddressEntryType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 2, 3, 1, 13),
    _Ltp8xPONChannelAddressEntryType_Type()
)
ltp8xPONChannelAddressEntryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xPONChannelAddressEntryType.setStatus("current")
_Ltp8xPONChannelAddressAge_Type = Unsigned32
_Ltp8xPONChannelAddressAge_Object = MibTableColumn
ltp8xPONChannelAddressAge = _Ltp8xPONChannelAddressAge_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 2, 3, 1, 14),
    _Ltp8xPONChannelAddressAge_Type()
)
ltp8xPONChannelAddressAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xPONChannelAddressAge.setStatus("current")
_Ltp8xPONChannelAddressGEMPortId_Type = Unsigned32
_Ltp8xPONChannelAddressGEMPortId_Object = MibTableColumn
ltp8xPONChannelAddressGEMPortId = _Ltp8xPONChannelAddressGEMPortId_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 2, 3, 1, 15),
    _Ltp8xPONChannelAddressGEMPortId_Type()
)
ltp8xPONChannelAddressGEMPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xPONChannelAddressGEMPortId.setStatus("current")
_Ltp8xPONChannelAddressUVID_Type = Integer32
_Ltp8xPONChannelAddressUVID_Object = MibTableColumn
ltp8xPONChannelAddressUVID = _Ltp8xPONChannelAddressUVID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 2, 3, 1, 16),
    _Ltp8xPONChannelAddressUVID_Type()
)
ltp8xPONChannelAddressUVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xPONChannelAddressUVID.setStatus("current")
_Ltp8xONT_ObjectIdentity = ObjectIdentity
ltp8xONT = _Ltp8xONT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3)
)
_Ltp8xONTStateTable_Object = MibTable
ltp8xONTStateTable = _Ltp8xONTStateTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 1)
)
if mibBuilder.loadTexts:
    ltp8xONTStateTable.setStatus("current")
_Ltp8xONTStateEntry_Object = MibTableRow
ltp8xONTStateEntry = _Ltp8xONTStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 1, 1)
)
ltp8xONTStateEntry.setIndexNames(
    (0, "ELTEX-LTP8X", "ltp8xONTSlot"),
    (0, "ELTEX-LTP8X", "ltp8xONTSerial"),
)
if mibBuilder.loadTexts:
    ltp8xONTStateEntry.setStatus("current")
_Ltp8xONTSlot_Type = Unsigned32
_Ltp8xONTSlot_Object = MibTableColumn
ltp8xONTSlot = _Ltp8xONTSlot_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 1, 1, 1),
    _Ltp8xONTSlot_Type()
)
ltp8xONTSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTSlot.setStatus("current")
_Ltp8xONTSerial_Type = ONTSerial
_Ltp8xONTSerial_Object = MibTableColumn
ltp8xONTSerial = _Ltp8xONTSerial_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 1, 1, 2),
    _Ltp8xONTSerial_Type()
)
ltp8xONTSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTSerial.setStatus("current")
_Ltp8xONTStateChannel_Type = Unsigned32
_Ltp8xONTStateChannel_Object = MibTableColumn
ltp8xONTStateChannel = _Ltp8xONTStateChannel_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 1, 1, 3),
    _Ltp8xONTStateChannel_Type()
)
ltp8xONTStateChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTStateChannel.setStatus("current")
_Ltp8xONTStateID_Type = Unsigned32
_Ltp8xONTStateID_Object = MibTableColumn
ltp8xONTStateID = _Ltp8xONTStateID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 1, 1, 4),
    _Ltp8xONTStateID_Type()
)
ltp8xONTStateID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTStateID.setStatus("current")
_Ltp8xONTStateState_Type = LTPONTState
_Ltp8xONTStateState_Object = MibTableColumn
ltp8xONTStateState = _Ltp8xONTStateState_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 1, 1, 5),
    _Ltp8xONTStateState_Type()
)
ltp8xONTStateState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTStateState.setStatus("current")
_Ltp8xONTStateEqualizationDelay_Type = Unsigned32
_Ltp8xONTStateEqualizationDelay_Object = MibTableColumn
ltp8xONTStateEqualizationDelay = _Ltp8xONTStateEqualizationDelay_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 1, 1, 6),
    _Ltp8xONTStateEqualizationDelay_Type()
)
ltp8xONTStateEqualizationDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTStateEqualizationDelay.setStatus("current")
_Ltp8xONTStateFecState_Type = TruthValue
_Ltp8xONTStateFecState_Object = MibTableColumn
ltp8xONTStateFecState = _Ltp8xONTStateFecState_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 1, 1, 7),
    _Ltp8xONTStateFecState_Type()
)
ltp8xONTStateFecState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTStateFecState.setStatus("current")
_Ltp8xONTStateEncryptionKey_Type = DisplayString
_Ltp8xONTStateEncryptionKey_Object = MibTableColumn
ltp8xONTStateEncryptionKey = _Ltp8xONTStateEncryptionKey_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 1, 1, 8),
    _Ltp8xONTStateEncryptionKey_Type()
)
ltp8xONTStateEncryptionKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTStateEncryptionKey.setStatus("current")
_Ltp8xONTStateOMCIPortId_Type = Integer32
_Ltp8xONTStateOMCIPortId_Object = MibTableColumn
ltp8xONTStateOMCIPortId = _Ltp8xONTStateOMCIPortId_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 1, 1, 9),
    _Ltp8xONTStateOMCIPortId_Type()
)
ltp8xONTStateOMCIPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTStateOMCIPortId.setStatus("current")
_Ltp8xONTStateDistance_Type = Unsigned32
_Ltp8xONTStateDistance_Object = MibTableColumn
ltp8xONTStateDistance = _Ltp8xONTStateDistance_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 1, 1, 10),
    _Ltp8xONTStateDistance_Type()
)
ltp8xONTStateDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTStateDistance.setStatus("current")
_Ltp8xONTStateRSSI_Type = Integer32
_Ltp8xONTStateRSSI_Object = MibTableColumn
ltp8xONTStateRSSI = _Ltp8xONTStateRSSI_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 1, 1, 11),
    _Ltp8xONTStateRSSI_Type()
)
ltp8xONTStateRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTStateRSSI.setStatus("current")
_Ltp8xONTStateEquipmentID_Type = DisplayString
_Ltp8xONTStateEquipmentID_Object = MibTableColumn
ltp8xONTStateEquipmentID = _Ltp8xONTStateEquipmentID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 1, 1, 12),
    _Ltp8xONTStateEquipmentID_Type()
)
ltp8xONTStateEquipmentID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTStateEquipmentID.setStatus("current")
_Ltp8xONTStateTxPower_Type = Integer32
_Ltp8xONTStateTxPower_Object = MibTableColumn
ltp8xONTStateTxPower = _Ltp8xONTStateTxPower_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 1, 1, 13),
    _Ltp8xONTStateTxPower_Type()
)
ltp8xONTStateTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTStateTxPower.setStatus("current")
_Ltp8xONTStateRxPower_Type = Integer32
_Ltp8xONTStateRxPower_Object = MibTableColumn
ltp8xONTStateRxPower = _Ltp8xONTStateRxPower_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 1, 1, 14),
    _Ltp8xONTStateRxPower_Type()
)
ltp8xONTStateRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTStateRxPower.setStatus("current")
_Ltp8xONTStateTemperature_Type = Integer32
_Ltp8xONTStateTemperature_Object = MibTableColumn
ltp8xONTStateTemperature = _Ltp8xONTStateTemperature_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 1, 1, 15),
    _Ltp8xONTStateTemperature_Type()
)
ltp8xONTStateTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTStateTemperature.setStatus("current")
_Ltp8xONTStateVideoRxPower_Type = VideoRxPowerConv
_Ltp8xONTStateVideoRxPower_Object = MibTableColumn
ltp8xONTStateVideoRxPower = _Ltp8xONTStateVideoRxPower_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 1, 1, 16),
    _Ltp8xONTStateVideoRxPower_Type()
)
ltp8xONTStateVideoRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTStateVideoRxPower.setStatus("current")
_Ltp8xONTStateVersion_Type = DisplayString
_Ltp8xONTStateVersion_Object = MibTableColumn
ltp8xONTStateVersion = _Ltp8xONTStateVersion_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 1, 1, 17),
    _Ltp8xONTStateVersion_Type()
)
ltp8xONTStateVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTStateVersion.setStatus("current")
_Ltp8xONTStateHWVersion_Type = DisplayString
_Ltp8xONTStateHWVersion_Object = MibTableColumn
ltp8xONTStateHWVersion = _Ltp8xONTStateHWVersion_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 1, 1, 18),
    _Ltp8xONTStateHWVersion_Type()
)
ltp8xONTStateHWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTStateHWVersion.setStatus("current")
_Ltp8xONTStateReconfigure_Type = Unsigned32
_Ltp8xONTStateReconfigure_Object = MibTableColumn
ltp8xONTStateReconfigure = _Ltp8xONTStateReconfigure_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 1, 1, 20),
    _Ltp8xONTStateReconfigure_Type()
)
ltp8xONTStateReconfigure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTStateReconfigure.setStatus("current")
_Ltp8xONTStateUpdateFirmware_Type = Unsigned32
_Ltp8xONTStateUpdateFirmware_Object = MibTableColumn
ltp8xONTStateUpdateFirmware = _Ltp8xONTStateUpdateFirmware_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 1, 1, 21),
    _Ltp8xONTStateUpdateFirmware_Type()
)
ltp8xONTStateUpdateFirmware.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTStateUpdateFirmware.setStatus("current")
_Ltp8xONTStateReset_Type = Unsigned32
_Ltp8xONTStateReset_Object = MibTableColumn
ltp8xONTStateReset = _Ltp8xONTStateReset_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 1, 1, 22),
    _Ltp8xONTStateReset_Type()
)
ltp8xONTStateReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTStateReset.setStatus("current")
_Ltp8xONTStateResetToDefaults_Type = Unsigned32
_Ltp8xONTStateResetToDefaults_Object = MibTableColumn
ltp8xONTStateResetToDefaults = _Ltp8xONTStateResetToDefaults_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 1, 1, 23),
    _Ltp8xONTStateResetToDefaults_Type()
)
ltp8xONTStateResetToDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTStateResetToDefaults.setStatus("current")
_Ltp8xONTStateRFPortOn_Type = TruthValue
_Ltp8xONTStateRFPortOn_Object = MibTableColumn
ltp8xONTStateRFPortOn = _Ltp8xONTStateRFPortOn_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 1, 1, 24),
    _Ltp8xONTStateRFPortOn_Type()
)
ltp8xONTStateRFPortOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTStateRFPortOn.setStatus("current")
_Ltp8xONTStateLaserVoltage_Type = Integer32
_Ltp8xONTStateLaserVoltage_Object = MibTableColumn
ltp8xONTStateLaserVoltage = _Ltp8xONTStateLaserVoltage_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 1, 1, 25),
    _Ltp8xONTStateLaserVoltage_Type()
)
ltp8xONTStateLaserVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTStateLaserVoltage.setStatus("current")
_Ltp8xONTStateLaserBiasCurrent_Type = Unsigned32
_Ltp8xONTStateLaserBiasCurrent_Object = MibTableColumn
ltp8xONTStateLaserBiasCurrent = _Ltp8xONTStateLaserBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 1, 1, 26),
    _Ltp8xONTStateLaserBiasCurrent_Type()
)
ltp8xONTStateLaserBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTStateLaserBiasCurrent.setStatus("current")
_Ltp8xONTUNIPortsStateTable_Object = MibTable
ltp8xONTUNIPortsStateTable = _Ltp8xONTUNIPortsStateTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 2)
)
if mibBuilder.loadTexts:
    ltp8xONTUNIPortsStateTable.setStatus("current")
_Ltp8xONTUNIPortsStateEntry_Object = MibTableRow
ltp8xONTUNIPortsStateEntry = _Ltp8xONTUNIPortsStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 2, 1)
)
ltp8xONTUNIPortsStateEntry.setIndexNames(
    (0, "ELTEX-LTP8X", "ltp8xONTUNIPortsStateSlot"),
    (0, "ELTEX-LTP8X", "ltp8xONTUNIPortsStateSerial"),
    (0, "ELTEX-LTP8X", "ltp8xONTUNIPortsStatePort"),
)
if mibBuilder.loadTexts:
    ltp8xONTUNIPortsStateEntry.setStatus("current")
_Ltp8xONTUNIPortsStateSlot_Type = Unsigned32
_Ltp8xONTUNIPortsStateSlot_Object = MibTableColumn
ltp8xONTUNIPortsStateSlot = _Ltp8xONTUNIPortsStateSlot_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 2, 1, 1),
    _Ltp8xONTUNIPortsStateSlot_Type()
)
ltp8xONTUNIPortsStateSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTUNIPortsStateSlot.setStatus("current")
_Ltp8xONTUNIPortsStateSerial_Type = ONTSerial
_Ltp8xONTUNIPortsStateSerial_Object = MibTableColumn
ltp8xONTUNIPortsStateSerial = _Ltp8xONTUNIPortsStateSerial_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 2, 1, 2),
    _Ltp8xONTUNIPortsStateSerial_Type()
)
ltp8xONTUNIPortsStateSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTUNIPortsStateSerial.setStatus("current")
_Ltp8xONTUNIPortsStatePort_Type = Unsigned32
_Ltp8xONTUNIPortsStatePort_Object = MibTableColumn
ltp8xONTUNIPortsStatePort = _Ltp8xONTUNIPortsStatePort_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 2, 1, 3),
    _Ltp8xONTUNIPortsStatePort_Type()
)
ltp8xONTUNIPortsStatePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTUNIPortsStatePort.setStatus("current")
_Ltp8xONTUNIPortsStateAvailable_Type = TruthValue
_Ltp8xONTUNIPortsStateAvailable_Object = MibTableColumn
ltp8xONTUNIPortsStateAvailable = _Ltp8xONTUNIPortsStateAvailable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 2, 1, 4),
    _Ltp8xONTUNIPortsStateAvailable_Type()
)
ltp8xONTUNIPortsStateAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTUNIPortsStateAvailable.setStatus("current")
_Ltp8xONTUNIPortsStateLinkUp_Type = TruthValue
_Ltp8xONTUNIPortsStateLinkUp_Object = MibTableColumn
ltp8xONTUNIPortsStateLinkUp = _Ltp8xONTUNIPortsStateLinkUp_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 2, 1, 5),
    _Ltp8xONTUNIPortsStateLinkUp_Type()
)
ltp8xONTUNIPortsStateLinkUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTUNIPortsStateLinkUp.setStatus("current")


class _Ltp8xONTUNIPortsStateSpeed_Type(Integer32):
    """Custom type ltp8xONTUNIPortsStateSpeed based on Integer32"""
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
        *(("speed100M", 2),
          ("speed10M", 1),
          ("speed1G", 3),
          ("speedAuto", 0),
          ("speedNotAvailable", 4))
    )


_Ltp8xONTUNIPortsStateSpeed_Type.__name__ = "Integer32"
_Ltp8xONTUNIPortsStateSpeed_Object = MibTableColumn
ltp8xONTUNIPortsStateSpeed = _Ltp8xONTUNIPortsStateSpeed_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 2, 1, 6),
    _Ltp8xONTUNIPortsStateSpeed_Type()
)
ltp8xONTUNIPortsStateSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTUNIPortsStateSpeed.setStatus("current")


class _Ltp8xONTUNIPortsStateDuplex_Type(Integer32):
    """Custom type ltp8xONTUNIPortsStateDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("duplexAuto", 0),
          ("duplexFull", 1),
          ("duplexHalf", 2),
          ("duplexNotAvaiable", 3))
    )


_Ltp8xONTUNIPortsStateDuplex_Type.__name__ = "Integer32"
_Ltp8xONTUNIPortsStateDuplex_Object = MibTableColumn
ltp8xONTUNIPortsStateDuplex = _Ltp8xONTUNIPortsStateDuplex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 2, 1, 7),
    _Ltp8xONTUNIPortsStateDuplex_Type()
)
ltp8xONTUNIPortsStateDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTUNIPortsStateDuplex.setStatus("current")
_Ltp8xONTStatistics_ObjectIdentity = ObjectIdentity
ltp8xONTStatistics = _Ltp8xONTStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3)
)
_Ltp8xONTWANCountersTable_Object = MibTable
ltp8xONTWANCountersTable = _Ltp8xONTWANCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 1)
)
if mibBuilder.loadTexts:
    ltp8xONTWANCountersTable.setStatus("current")
_Ltp8xONTWANCountersEntry_Object = MibTableRow
ltp8xONTWANCountersEntry = _Ltp8xONTWANCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 1, 1)
)
ltp8xONTWANCountersEntry.setIndexNames(
    (0, "ELTEX-LTP8X", "ltp8xONTWANCountersSlot"),
    (0, "ELTEX-LTP8X", "ltp8xONTWANCountersSerial"),
    (0, "ELTEX-LTP8X", "ltp8xONTWANCountersCrossConnect"),
)
if mibBuilder.loadTexts:
    ltp8xONTWANCountersEntry.setStatus("current")
_Ltp8xONTWANCountersSlot_Type = Unsigned32
_Ltp8xONTWANCountersSlot_Object = MibTableColumn
ltp8xONTWANCountersSlot = _Ltp8xONTWANCountersSlot_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 1, 1, 1),
    _Ltp8xONTWANCountersSlot_Type()
)
ltp8xONTWANCountersSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTWANCountersSlot.setStatus("current")
_Ltp8xONTWANCountersSerial_Type = ONTSerial
_Ltp8xONTWANCountersSerial_Object = MibTableColumn
ltp8xONTWANCountersSerial = _Ltp8xONTWANCountersSerial_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 1, 1, 2),
    _Ltp8xONTWANCountersSerial_Type()
)
ltp8xONTWANCountersSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTWANCountersSerial.setStatus("current")
_Ltp8xONTWANCountersCrossConnect_Type = Unsigned32
_Ltp8xONTWANCountersCrossConnect_Object = MibTableColumn
ltp8xONTWANCountersCrossConnect = _Ltp8xONTWANCountersCrossConnect_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 1, 1, 3),
    _Ltp8xONTWANCountersCrossConnect_Type()
)
ltp8xONTWANCountersCrossConnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTWANCountersCrossConnect.setStatus("current")
_Ltp8xONTWANCountersRXDrops_Type = Unsigned32
_Ltp8xONTWANCountersRXDrops_Object = MibTableColumn
ltp8xONTWANCountersRXDrops = _Ltp8xONTWANCountersRXDrops_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 1, 1, 4),
    _Ltp8xONTWANCountersRXDrops_Type()
)
ltp8xONTWANCountersRXDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTWANCountersRXDrops.setStatus("current")
_Ltp8xONTWANCountersRXErrors_Type = Unsigned32
_Ltp8xONTWANCountersRXErrors_Object = MibTableColumn
ltp8xONTWANCountersRXErrors = _Ltp8xONTWANCountersRXErrors_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 1, 1, 5),
    _Ltp8xONTWANCountersRXErrors_Type()
)
ltp8xONTWANCountersRXErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTWANCountersRXErrors.setStatus("current")
_Ltp8xONTWANCountersRecvBytes_Type = Unsigned32
_Ltp8xONTWANCountersRecvBytes_Object = MibTableColumn
ltp8xONTWANCountersRecvBytes = _Ltp8xONTWANCountersRecvBytes_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 1, 1, 6),
    _Ltp8xONTWANCountersRecvBytes_Type()
)
ltp8xONTWANCountersRecvBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTWANCountersRecvBytes.setStatus("current")
_Ltp8xONTWANCountersRecvFrames_Type = Unsigned32
_Ltp8xONTWANCountersRecvFrames_Object = MibTableColumn
ltp8xONTWANCountersRecvFrames = _Ltp8xONTWANCountersRecvFrames_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 1, 1, 7),
    _Ltp8xONTWANCountersRecvFrames_Type()
)
ltp8xONTWANCountersRecvFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTWANCountersRecvFrames.setStatus("current")
_Ltp8xONTWANCountersTXDrops_Type = Unsigned32
_Ltp8xONTWANCountersTXDrops_Object = MibTableColumn
ltp8xONTWANCountersTXDrops = _Ltp8xONTWANCountersTXDrops_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 1, 1, 8),
    _Ltp8xONTWANCountersTXDrops_Type()
)
ltp8xONTWANCountersTXDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTWANCountersTXDrops.setStatus("current")
_Ltp8xONTWANCountersTXErrors_Type = Unsigned32
_Ltp8xONTWANCountersTXErrors_Object = MibTableColumn
ltp8xONTWANCountersTXErrors = _Ltp8xONTWANCountersTXErrors_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 1, 1, 9),
    _Ltp8xONTWANCountersTXErrors_Type()
)
ltp8xONTWANCountersTXErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTWANCountersTXErrors.setStatus("current")
_Ltp8xONTWANCountersTrmtBytes_Type = Unsigned32
_Ltp8xONTWANCountersTrmtBytes_Object = MibTableColumn
ltp8xONTWANCountersTrmtBytes = _Ltp8xONTWANCountersTrmtBytes_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 1, 1, 10),
    _Ltp8xONTWANCountersTrmtBytes_Type()
)
ltp8xONTWANCountersTrmtBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTWANCountersTrmtBytes.setStatus("current")
_Ltp8xONTWANCountersTrmtFrames_Type = Unsigned32
_Ltp8xONTWANCountersTrmtFrames_Object = MibTableColumn
ltp8xONTWANCountersTrmtFrames = _Ltp8xONTWANCountersTrmtFrames_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 1, 1, 11),
    _Ltp8xONTWANCountersTrmtFrames_Type()
)
ltp8xONTWANCountersTrmtFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTWANCountersTrmtFrames.setStatus("current")
_Ltp8xONTGEMPortCountersTable_Object = MibTable
ltp8xONTGEMPortCountersTable = _Ltp8xONTGEMPortCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 2)
)
if mibBuilder.loadTexts:
    ltp8xONTGEMPortCountersTable.setStatus("current")
_Ltp8xONTGEMPortCountersEntry_Object = MibTableRow
ltp8xONTGEMPortCountersEntry = _Ltp8xONTGEMPortCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 2, 1)
)
ltp8xONTGEMPortCountersEntry.setIndexNames(
    (0, "ELTEX-LTP8X", "ltp8xONTGEMPortCountersSlot"),
    (0, "ELTEX-LTP8X", "ltp8xONTGEMPortCountersSerial"),
    (0, "ELTEX-LTP8X", "ltp8xONTGEMPortCountersCrossConnect"),
)
if mibBuilder.loadTexts:
    ltp8xONTGEMPortCountersEntry.setStatus("current")
_Ltp8xONTGEMPortCountersSlot_Type = Unsigned32
_Ltp8xONTGEMPortCountersSlot_Object = MibTableColumn
ltp8xONTGEMPortCountersSlot = _Ltp8xONTGEMPortCountersSlot_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 2, 1, 1),
    _Ltp8xONTGEMPortCountersSlot_Type()
)
ltp8xONTGEMPortCountersSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTGEMPortCountersSlot.setStatus("current")
_Ltp8xONTGEMPortCountersSerial_Type = ONTSerial
_Ltp8xONTGEMPortCountersSerial_Object = MibTableColumn
ltp8xONTGEMPortCountersSerial = _Ltp8xONTGEMPortCountersSerial_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 2, 1, 2),
    _Ltp8xONTGEMPortCountersSerial_Type()
)
ltp8xONTGEMPortCountersSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTGEMPortCountersSerial.setStatus("current")
_Ltp8xONTGEMPortCountersCrossConnect_Type = Unsigned32
_Ltp8xONTGEMPortCountersCrossConnect_Object = MibTableColumn
ltp8xONTGEMPortCountersCrossConnect = _Ltp8xONTGEMPortCountersCrossConnect_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 2, 1, 3),
    _Ltp8xONTGEMPortCountersCrossConnect_Type()
)
ltp8xONTGEMPortCountersCrossConnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTGEMPortCountersCrossConnect.setStatus("current")
_Ltp8xONTGEMPortCountersDSFinishedIntervals_Type = Unsigned32
_Ltp8xONTGEMPortCountersDSFinishedIntervals_Object = MibTableColumn
ltp8xONTGEMPortCountersDSFinishedIntervals = _Ltp8xONTGEMPortCountersDSFinishedIntervals_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 2, 1, 4),
    _Ltp8xONTGEMPortCountersDSFinishedIntervals_Type()
)
ltp8xONTGEMPortCountersDSFinishedIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTGEMPortCountersDSFinishedIntervals.setStatus("current")
_Ltp8xONTGEMPortCountersDSGEMFrames_Type = Unsigned32
_Ltp8xONTGEMPortCountersDSGEMFrames_Object = MibTableColumn
ltp8xONTGEMPortCountersDSGEMFrames = _Ltp8xONTGEMPortCountersDSGEMFrames_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 2, 1, 5),
    _Ltp8xONTGEMPortCountersDSGEMFrames_Type()
)
ltp8xONTGEMPortCountersDSGEMFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTGEMPortCountersDSGEMFrames.setStatus("current")
_Ltp8xONTGEMPortCountersDSPayloadBytesLOW_Type = Unsigned32
_Ltp8xONTGEMPortCountersDSPayloadBytesLOW_Object = MibTableColumn
ltp8xONTGEMPortCountersDSPayloadBytesLOW = _Ltp8xONTGEMPortCountersDSPayloadBytesLOW_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 2, 1, 6),
    _Ltp8xONTGEMPortCountersDSPayloadBytesLOW_Type()
)
ltp8xONTGEMPortCountersDSPayloadBytesLOW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTGEMPortCountersDSPayloadBytesLOW.setStatus("current")
_Ltp8xONTGEMPortCountersDSPayloadBytesHIGH_Type = Unsigned32
_Ltp8xONTGEMPortCountersDSPayloadBytesHIGH_Object = MibTableColumn
ltp8xONTGEMPortCountersDSPayloadBytesHIGH = _Ltp8xONTGEMPortCountersDSPayloadBytesHIGH_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 2, 1, 7),
    _Ltp8xONTGEMPortCountersDSPayloadBytesHIGH_Type()
)
ltp8xONTGEMPortCountersDSPayloadBytesHIGH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTGEMPortCountersDSPayloadBytesHIGH.setStatus("current")
_Ltp8xONTGEMPortCountersUSFinishedIntervals_Type = Unsigned32
_Ltp8xONTGEMPortCountersUSFinishedIntervals_Object = MibTableColumn
ltp8xONTGEMPortCountersUSFinishedIntervals = _Ltp8xONTGEMPortCountersUSFinishedIntervals_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 2, 1, 8),
    _Ltp8xONTGEMPortCountersUSFinishedIntervals_Type()
)
ltp8xONTGEMPortCountersUSFinishedIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTGEMPortCountersUSFinishedIntervals.setStatus("current")
_Ltp8xONTGEMPortCountersUSGEMFrames_Type = Unsigned32
_Ltp8xONTGEMPortCountersUSGEMFrames_Object = MibTableColumn
ltp8xONTGEMPortCountersUSGEMFrames = _Ltp8xONTGEMPortCountersUSGEMFrames_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 2, 1, 9),
    _Ltp8xONTGEMPortCountersUSGEMFrames_Type()
)
ltp8xONTGEMPortCountersUSGEMFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTGEMPortCountersUSGEMFrames.setStatus("current")
_Ltp8xONTGEMPortCountersUSPayloadBytesLOW_Type = Unsigned32
_Ltp8xONTGEMPortCountersUSPayloadBytesLOW_Object = MibTableColumn
ltp8xONTGEMPortCountersUSPayloadBytesLOW = _Ltp8xONTGEMPortCountersUSPayloadBytesLOW_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 2, 1, 10),
    _Ltp8xONTGEMPortCountersUSPayloadBytesLOW_Type()
)
ltp8xONTGEMPortCountersUSPayloadBytesLOW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTGEMPortCountersUSPayloadBytesLOW.setStatus("current")
_Ltp8xONTGEMPortCountersUSPayloadBytesHIGH_Type = Unsigned32
_Ltp8xONTGEMPortCountersUSPayloadBytesHIGH_Object = MibTableColumn
ltp8xONTGEMPortCountersUSPayloadBytesHIGH = _Ltp8xONTGEMPortCountersUSPayloadBytesHIGH_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 2, 1, 11),
    _Ltp8xONTGEMPortCountersUSPayloadBytesHIGH_Type()
)
ltp8xONTGEMPortCountersUSPayloadBytesHIGH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTGEMPortCountersUSPayloadBytesHIGH.setStatus("current")
_Ltp8xONTEthPerformMonitoringHistDataTable_Object = MibTable
ltp8xONTEthPerformMonitoringHistDataTable = _Ltp8xONTEthPerformMonitoringHistDataTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 3)
)
if mibBuilder.loadTexts:
    ltp8xONTEthPerformMonitoringHistDataTable.setStatus("current")
_Ltp8xONTEthPerformMonitoringHistDataEntry_Object = MibTableRow
ltp8xONTEthPerformMonitoringHistDataEntry = _Ltp8xONTEthPerformMonitoringHistDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 3, 1)
)
ltp8xONTEthPerformMonitoringHistDataEntry.setIndexNames(
    (0, "ELTEX-LTP8X", "ltp8xONTEthPerformMonitoringHistDataSlot"),
    (0, "ELTEX-LTP8X", "ltp8xONTEthPerformMonitoringHistDataSerial"),
    (0, "ELTEX-LTP8X", "ltp8xONTEthPerformMonitoringHistDataPort"),
    (0, "ELTEX-LTP8X", "ltp8xONTEthPerformMonitoringHistDataCounterID"),
)
if mibBuilder.loadTexts:
    ltp8xONTEthPerformMonitoringHistDataEntry.setStatus("current")
_Ltp8xONTEthPerformMonitoringHistDataSlot_Type = Unsigned32
_Ltp8xONTEthPerformMonitoringHistDataSlot_Object = MibTableColumn
ltp8xONTEthPerformMonitoringHistDataSlot = _Ltp8xONTEthPerformMonitoringHistDataSlot_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 3, 1, 1),
    _Ltp8xONTEthPerformMonitoringHistDataSlot_Type()
)
ltp8xONTEthPerformMonitoringHistDataSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTEthPerformMonitoringHistDataSlot.setStatus("current")
_Ltp8xONTEthPerformMonitoringHistDataSerial_Type = ONTSerial
_Ltp8xONTEthPerformMonitoringHistDataSerial_Object = MibTableColumn
ltp8xONTEthPerformMonitoringHistDataSerial = _Ltp8xONTEthPerformMonitoringHistDataSerial_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 3, 1, 2),
    _Ltp8xONTEthPerformMonitoringHistDataSerial_Type()
)
ltp8xONTEthPerformMonitoringHistDataSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTEthPerformMonitoringHistDataSerial.setStatus("current")
_Ltp8xONTEthPerformMonitoringHistDataPort_Type = Unsigned32
_Ltp8xONTEthPerformMonitoringHistDataPort_Object = MibTableColumn
ltp8xONTEthPerformMonitoringHistDataPort = _Ltp8xONTEthPerformMonitoringHistDataPort_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 3, 1, 3),
    _Ltp8xONTEthPerformMonitoringHistDataPort_Type()
)
ltp8xONTEthPerformMonitoringHistDataPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTEthPerformMonitoringHistDataPort.setStatus("current")
_Ltp8xONTEthPerformMonitoringHistDataCounterID_Type = Unsigned32
_Ltp8xONTEthPerformMonitoringHistDataCounterID_Object = MibTableColumn
ltp8xONTEthPerformMonitoringHistDataCounterID = _Ltp8xONTEthPerformMonitoringHistDataCounterID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 3, 1, 4),
    _Ltp8xONTEthPerformMonitoringHistDataCounterID_Type()
)
ltp8xONTEthPerformMonitoringHistDataCounterID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTEthPerformMonitoringHistDataCounterID.setStatus("current")
_Ltp8xONTEthPerformMonitoringHistDataCounterName_Type = DisplayString
_Ltp8xONTEthPerformMonitoringHistDataCounterName_Object = MibTableColumn
ltp8xONTEthPerformMonitoringHistDataCounterName = _Ltp8xONTEthPerformMonitoringHistDataCounterName_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 3, 1, 5),
    _Ltp8xONTEthPerformMonitoringHistDataCounterName_Type()
)
ltp8xONTEthPerformMonitoringHistDataCounterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTEthPerformMonitoringHistDataCounterName.setStatus("current")
_Ltp8xONTEthPerformMonitoringHistDataCounterValue_Type = Unsigned32
_Ltp8xONTEthPerformMonitoringHistDataCounterValue_Object = MibTableColumn
ltp8xONTEthPerformMonitoringHistDataCounterValue = _Ltp8xONTEthPerformMonitoringHistDataCounterValue_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 3, 1, 6),
    _Ltp8xONTEthPerformMonitoringHistDataCounterValue_Type()
)
ltp8xONTEthPerformMonitoringHistDataCounterValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTEthPerformMonitoringHistDataCounterValue.setStatus("current")
_Ltp8xONTGalEthPerformMonitoringHistDataTable_Object = MibTable
ltp8xONTGalEthPerformMonitoringHistDataTable = _Ltp8xONTGalEthPerformMonitoringHistDataTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 4)
)
if mibBuilder.loadTexts:
    ltp8xONTGalEthPerformMonitoringHistDataTable.setStatus("current")
_Ltp8xONTGalEthPerformMonitoringHistDataEntry_Object = MibTableRow
ltp8xONTGalEthPerformMonitoringHistDataEntry = _Ltp8xONTGalEthPerformMonitoringHistDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 4, 1)
)
ltp8xONTGalEthPerformMonitoringHistDataEntry.setIndexNames(
    (0, "ELTEX-LTP8X", "ltp8xONTGalEthPerformMonitoringHistDataSlot"),
    (0, "ELTEX-LTP8X", "ltp8xONTGalEthPerformMonitoringHistDataSerial"),
    (0, "ELTEX-LTP8X", "ltp8xONTGalEthPerformMonitoringHistDataCrossConnect"),
    (0, "ELTEX-LTP8X", "ltp8xONTGalEthPerformMonitoringHistDataCounterID"),
)
if mibBuilder.loadTexts:
    ltp8xONTGalEthPerformMonitoringHistDataEntry.setStatus("current")
_Ltp8xONTGalEthPerformMonitoringHistDataSlot_Type = Unsigned32
_Ltp8xONTGalEthPerformMonitoringHistDataSlot_Object = MibTableColumn
ltp8xONTGalEthPerformMonitoringHistDataSlot = _Ltp8xONTGalEthPerformMonitoringHistDataSlot_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 4, 1, 1),
    _Ltp8xONTGalEthPerformMonitoringHistDataSlot_Type()
)
ltp8xONTGalEthPerformMonitoringHistDataSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTGalEthPerformMonitoringHistDataSlot.setStatus("current")
_Ltp8xONTGalEthPerformMonitoringHistDataSerial_Type = ONTSerial
_Ltp8xONTGalEthPerformMonitoringHistDataSerial_Object = MibTableColumn
ltp8xONTGalEthPerformMonitoringHistDataSerial = _Ltp8xONTGalEthPerformMonitoringHistDataSerial_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 4, 1, 2),
    _Ltp8xONTGalEthPerformMonitoringHistDataSerial_Type()
)
ltp8xONTGalEthPerformMonitoringHistDataSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTGalEthPerformMonitoringHistDataSerial.setStatus("current")
_Ltp8xONTGalEthPerformMonitoringHistDataCrossConnect_Type = Unsigned32
_Ltp8xONTGalEthPerformMonitoringHistDataCrossConnect_Object = MibTableColumn
ltp8xONTGalEthPerformMonitoringHistDataCrossConnect = _Ltp8xONTGalEthPerformMonitoringHistDataCrossConnect_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 4, 1, 3),
    _Ltp8xONTGalEthPerformMonitoringHistDataCrossConnect_Type()
)
ltp8xONTGalEthPerformMonitoringHistDataCrossConnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTGalEthPerformMonitoringHistDataCrossConnect.setStatus("current")
_Ltp8xONTGalEthPerformMonitoringHistDataCounterID_Type = Unsigned32
_Ltp8xONTGalEthPerformMonitoringHistDataCounterID_Object = MibTableColumn
ltp8xONTGalEthPerformMonitoringHistDataCounterID = _Ltp8xONTGalEthPerformMonitoringHistDataCounterID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 4, 1, 4),
    _Ltp8xONTGalEthPerformMonitoringHistDataCounterID_Type()
)
ltp8xONTGalEthPerformMonitoringHistDataCounterID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTGalEthPerformMonitoringHistDataCounterID.setStatus("current")
_Ltp8xONTGalEthPerformMonitoringHistDataCounterName_Type = DisplayString
_Ltp8xONTGalEthPerformMonitoringHistDataCounterName_Object = MibTableColumn
ltp8xONTGalEthPerformMonitoringHistDataCounterName = _Ltp8xONTGalEthPerformMonitoringHistDataCounterName_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 4, 1, 5),
    _Ltp8xONTGalEthPerformMonitoringHistDataCounterName_Type()
)
ltp8xONTGalEthPerformMonitoringHistDataCounterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTGalEthPerformMonitoringHistDataCounterName.setStatus("current")
_Ltp8xONTGalEthPerformMonitoringHistDataCounterValue_Type = Unsigned32
_Ltp8xONTGalEthPerformMonitoringHistDataCounterValue_Object = MibTableColumn
ltp8xONTGalEthPerformMonitoringHistDataCounterValue = _Ltp8xONTGalEthPerformMonitoringHistDataCounterValue_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 4, 1, 6),
    _Ltp8xONTGalEthPerformMonitoringHistDataCounterValue_Type()
)
ltp8xONTGalEthPerformMonitoringHistDataCounterValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTGalEthPerformMonitoringHistDataCounterValue.setStatus("current")
_Ltp8xONTFecPerformMonitoringHistDataTable_Object = MibTable
ltp8xONTFecPerformMonitoringHistDataTable = _Ltp8xONTFecPerformMonitoringHistDataTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 5)
)
if mibBuilder.loadTexts:
    ltp8xONTFecPerformMonitoringHistDataTable.setStatus("current")
_Ltp8xONTFecPerformMonitoringHistDataEntry_Object = MibTableRow
ltp8xONTFecPerformMonitoringHistDataEntry = _Ltp8xONTFecPerformMonitoringHistDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 5, 1)
)
ltp8xONTFecPerformMonitoringHistDataEntry.setIndexNames(
    (0, "ELTEX-LTP8X", "ltp8xONTFecPerformMonitoringHistDataSlot"),
    (0, "ELTEX-LTP8X", "ltp8xONTFecPerformMonitoringHistDataSerial"),
    (0, "ELTEX-LTP8X", "ltp8xONTFecPerformMonitoringHistDataDummyIndex"),
    (0, "ELTEX-LTP8X", "ltp8xONTFecPerformMonitoringHistDataCounterID"),
)
if mibBuilder.loadTexts:
    ltp8xONTFecPerformMonitoringHistDataEntry.setStatus("current")
_Ltp8xONTFecPerformMonitoringHistDataSlot_Type = Unsigned32
_Ltp8xONTFecPerformMonitoringHistDataSlot_Object = MibTableColumn
ltp8xONTFecPerformMonitoringHistDataSlot = _Ltp8xONTFecPerformMonitoringHistDataSlot_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 5, 1, 1),
    _Ltp8xONTFecPerformMonitoringHistDataSlot_Type()
)
ltp8xONTFecPerformMonitoringHistDataSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTFecPerformMonitoringHistDataSlot.setStatus("current")
_Ltp8xONTFecPerformMonitoringHistDataSerial_Type = ONTSerial
_Ltp8xONTFecPerformMonitoringHistDataSerial_Object = MibTableColumn
ltp8xONTFecPerformMonitoringHistDataSerial = _Ltp8xONTFecPerformMonitoringHistDataSerial_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 5, 1, 2),
    _Ltp8xONTFecPerformMonitoringHistDataSerial_Type()
)
ltp8xONTFecPerformMonitoringHistDataSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTFecPerformMonitoringHistDataSerial.setStatus("current")
_Ltp8xONTFecPerformMonitoringHistDataDummyIndex_Type = Unsigned32
_Ltp8xONTFecPerformMonitoringHistDataDummyIndex_Object = MibTableColumn
ltp8xONTFecPerformMonitoringHistDataDummyIndex = _Ltp8xONTFecPerformMonitoringHistDataDummyIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 5, 1, 3),
    _Ltp8xONTFecPerformMonitoringHistDataDummyIndex_Type()
)
ltp8xONTFecPerformMonitoringHistDataDummyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTFecPerformMonitoringHistDataDummyIndex.setStatus("current")
_Ltp8xONTFecPerformMonitoringHistDataCounterID_Type = Unsigned32
_Ltp8xONTFecPerformMonitoringHistDataCounterID_Object = MibTableColumn
ltp8xONTFecPerformMonitoringHistDataCounterID = _Ltp8xONTFecPerformMonitoringHistDataCounterID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 5, 1, 4),
    _Ltp8xONTFecPerformMonitoringHistDataCounterID_Type()
)
ltp8xONTFecPerformMonitoringHistDataCounterID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTFecPerformMonitoringHistDataCounterID.setStatus("current")
_Ltp8xONTFecPerformMonitoringHistDataCounterName_Type = DisplayString
_Ltp8xONTFecPerformMonitoringHistDataCounterName_Object = MibTableColumn
ltp8xONTFecPerformMonitoringHistDataCounterName = _Ltp8xONTFecPerformMonitoringHistDataCounterName_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 5, 1, 5),
    _Ltp8xONTFecPerformMonitoringHistDataCounterName_Type()
)
ltp8xONTFecPerformMonitoringHistDataCounterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTFecPerformMonitoringHistDataCounterName.setStatus("current")
_Ltp8xONTFecPerformMonitoringHistDataCounterValue_Type = Unsigned32
_Ltp8xONTFecPerformMonitoringHistDataCounterValue_Object = MibTableColumn
ltp8xONTFecPerformMonitoringHistDataCounterValue = _Ltp8xONTFecPerformMonitoringHistDataCounterValue_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 5, 1, 6),
    _Ltp8xONTFecPerformMonitoringHistDataCounterValue_Type()
)
ltp8xONTFecPerformMonitoringHistDataCounterValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTFecPerformMonitoringHistDataCounterValue.setStatus("current")
_Ltp8xONTEthFrameDSPerformMonitoringHistDataTable_Object = MibTable
ltp8xONTEthFrameDSPerformMonitoringHistDataTable = _Ltp8xONTEthFrameDSPerformMonitoringHistDataTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 6)
)
if mibBuilder.loadTexts:
    ltp8xONTEthFrameDSPerformMonitoringHistDataTable.setStatus("current")
_Ltp8xONTEthFrameDSPerformMonitoringHistDataEntry_Object = MibTableRow
ltp8xONTEthFrameDSPerformMonitoringHistDataEntry = _Ltp8xONTEthFrameDSPerformMonitoringHistDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 6, 1)
)
ltp8xONTEthFrameDSPerformMonitoringHistDataEntry.setIndexNames(
    (0, "ELTEX-LTP8X", "ltp8xONTEthFrameDSPerformMonitoringHistDataSlot"),
    (0, "ELTEX-LTP8X", "ltp8xONTEthFrameDSPerformMonitoringHistDataSerial"),
    (0, "ELTEX-LTP8X", "ltp8xONTEthFrameDSPerformMonitoringHistDataPort"),
    (0, "ELTEX-LTP8X", "ltp8xONTEthFrameDSPerformMonitoringHistDataCounterID"),
)
if mibBuilder.loadTexts:
    ltp8xONTEthFrameDSPerformMonitoringHistDataEntry.setStatus("current")
_Ltp8xONTEthFrameDSPerformMonitoringHistDataSlot_Type = Unsigned32
_Ltp8xONTEthFrameDSPerformMonitoringHistDataSlot_Object = MibTableColumn
ltp8xONTEthFrameDSPerformMonitoringHistDataSlot = _Ltp8xONTEthFrameDSPerformMonitoringHistDataSlot_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 6, 1, 1),
    _Ltp8xONTEthFrameDSPerformMonitoringHistDataSlot_Type()
)
ltp8xONTEthFrameDSPerformMonitoringHistDataSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTEthFrameDSPerformMonitoringHistDataSlot.setStatus("current")
_Ltp8xONTEthFrameDSPerformMonitoringHistDataSerial_Type = ONTSerial
_Ltp8xONTEthFrameDSPerformMonitoringHistDataSerial_Object = MibTableColumn
ltp8xONTEthFrameDSPerformMonitoringHistDataSerial = _Ltp8xONTEthFrameDSPerformMonitoringHistDataSerial_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 6, 1, 2),
    _Ltp8xONTEthFrameDSPerformMonitoringHistDataSerial_Type()
)
ltp8xONTEthFrameDSPerformMonitoringHistDataSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTEthFrameDSPerformMonitoringHistDataSerial.setStatus("current")
_Ltp8xONTEthFrameDSPerformMonitoringHistDataPort_Type = Unsigned32
_Ltp8xONTEthFrameDSPerformMonitoringHistDataPort_Object = MibTableColumn
ltp8xONTEthFrameDSPerformMonitoringHistDataPort = _Ltp8xONTEthFrameDSPerformMonitoringHistDataPort_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 6, 1, 3),
    _Ltp8xONTEthFrameDSPerformMonitoringHistDataPort_Type()
)
ltp8xONTEthFrameDSPerformMonitoringHistDataPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTEthFrameDSPerformMonitoringHistDataPort.setStatus("current")
_Ltp8xONTEthFrameDSPerformMonitoringHistDataCounterID_Type = Unsigned32
_Ltp8xONTEthFrameDSPerformMonitoringHistDataCounterID_Object = MibTableColumn
ltp8xONTEthFrameDSPerformMonitoringHistDataCounterID = _Ltp8xONTEthFrameDSPerformMonitoringHistDataCounterID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 6, 1, 4),
    _Ltp8xONTEthFrameDSPerformMonitoringHistDataCounterID_Type()
)
ltp8xONTEthFrameDSPerformMonitoringHistDataCounterID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTEthFrameDSPerformMonitoringHistDataCounterID.setStatus("current")
_Ltp8xONTEthFrameDSPerformMonitoringHistDataCounterName_Type = DisplayString
_Ltp8xONTEthFrameDSPerformMonitoringHistDataCounterName_Object = MibTableColumn
ltp8xONTEthFrameDSPerformMonitoringHistDataCounterName = _Ltp8xONTEthFrameDSPerformMonitoringHistDataCounterName_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 6, 1, 5),
    _Ltp8xONTEthFrameDSPerformMonitoringHistDataCounterName_Type()
)
ltp8xONTEthFrameDSPerformMonitoringHistDataCounterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTEthFrameDSPerformMonitoringHistDataCounterName.setStatus("current")
_Ltp8xONTEthFrameDSPerformMonitoringHistDataCounterValue_Type = Unsigned32
_Ltp8xONTEthFrameDSPerformMonitoringHistDataCounterValue_Object = MibTableColumn
ltp8xONTEthFrameDSPerformMonitoringHistDataCounterValue = _Ltp8xONTEthFrameDSPerformMonitoringHistDataCounterValue_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 6, 1, 6),
    _Ltp8xONTEthFrameDSPerformMonitoringHistDataCounterValue_Type()
)
ltp8xONTEthFrameDSPerformMonitoringHistDataCounterValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTEthFrameDSPerformMonitoringHistDataCounterValue.setStatus("current")
_Ltp8xONTEthFrameUSPerformMonitoringHistDataTable_Object = MibTable
ltp8xONTEthFrameUSPerformMonitoringHistDataTable = _Ltp8xONTEthFrameUSPerformMonitoringHistDataTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 7)
)
if mibBuilder.loadTexts:
    ltp8xONTEthFrameUSPerformMonitoringHistDataTable.setStatus("current")
_Ltp8xONTEthFrameUSPerformMonitoringHistDataEntry_Object = MibTableRow
ltp8xONTEthFrameUSPerformMonitoringHistDataEntry = _Ltp8xONTEthFrameUSPerformMonitoringHistDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 7, 1)
)
ltp8xONTEthFrameUSPerformMonitoringHistDataEntry.setIndexNames(
    (0, "ELTEX-LTP8X", "ltp8xONTEthFrameUSPerformMonitoringHistDataSlot"),
    (0, "ELTEX-LTP8X", "ltp8xONTEthFrameUSPerformMonitoringHistDataSerial"),
    (0, "ELTEX-LTP8X", "ltp8xONTEthFrameUSPerformMonitoringHistDataPort"),
    (0, "ELTEX-LTP8X", "ltp8xONTEthFrameUSPerformMonitoringHistDataCounterID"),
)
if mibBuilder.loadTexts:
    ltp8xONTEthFrameUSPerformMonitoringHistDataEntry.setStatus("current")
_Ltp8xONTEthFrameUSPerformMonitoringHistDataSlot_Type = Unsigned32
_Ltp8xONTEthFrameUSPerformMonitoringHistDataSlot_Object = MibTableColumn
ltp8xONTEthFrameUSPerformMonitoringHistDataSlot = _Ltp8xONTEthFrameUSPerformMonitoringHistDataSlot_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 7, 1, 1),
    _Ltp8xONTEthFrameUSPerformMonitoringHistDataSlot_Type()
)
ltp8xONTEthFrameUSPerformMonitoringHistDataSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTEthFrameUSPerformMonitoringHistDataSlot.setStatus("current")
_Ltp8xONTEthFrameUSPerformMonitoringHistDataSerial_Type = ONTSerial
_Ltp8xONTEthFrameUSPerformMonitoringHistDataSerial_Object = MibTableColumn
ltp8xONTEthFrameUSPerformMonitoringHistDataSerial = _Ltp8xONTEthFrameUSPerformMonitoringHistDataSerial_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 7, 1, 2),
    _Ltp8xONTEthFrameUSPerformMonitoringHistDataSerial_Type()
)
ltp8xONTEthFrameUSPerformMonitoringHistDataSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTEthFrameUSPerformMonitoringHistDataSerial.setStatus("current")
_Ltp8xONTEthFrameUSPerformMonitoringHistDataPort_Type = Unsigned32
_Ltp8xONTEthFrameUSPerformMonitoringHistDataPort_Object = MibTableColumn
ltp8xONTEthFrameUSPerformMonitoringHistDataPort = _Ltp8xONTEthFrameUSPerformMonitoringHistDataPort_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 7, 1, 3),
    _Ltp8xONTEthFrameUSPerformMonitoringHistDataPort_Type()
)
ltp8xONTEthFrameUSPerformMonitoringHistDataPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTEthFrameUSPerformMonitoringHistDataPort.setStatus("current")
_Ltp8xONTEthFrameUSPerformMonitoringHistDataCounterID_Type = Unsigned32
_Ltp8xONTEthFrameUSPerformMonitoringHistDataCounterID_Object = MibTableColumn
ltp8xONTEthFrameUSPerformMonitoringHistDataCounterID = _Ltp8xONTEthFrameUSPerformMonitoringHistDataCounterID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 7, 1, 4),
    _Ltp8xONTEthFrameUSPerformMonitoringHistDataCounterID_Type()
)
ltp8xONTEthFrameUSPerformMonitoringHistDataCounterID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTEthFrameUSPerformMonitoringHistDataCounterID.setStatus("current")
_Ltp8xONTEthFrameUSPerformMonitoringHistDataCounterName_Type = DisplayString
_Ltp8xONTEthFrameUSPerformMonitoringHistDataCounterName_Object = MibTableColumn
ltp8xONTEthFrameUSPerformMonitoringHistDataCounterName = _Ltp8xONTEthFrameUSPerformMonitoringHistDataCounterName_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 7, 1, 5),
    _Ltp8xONTEthFrameUSPerformMonitoringHistDataCounterName_Type()
)
ltp8xONTEthFrameUSPerformMonitoringHistDataCounterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTEthFrameUSPerformMonitoringHistDataCounterName.setStatus("current")
_Ltp8xONTEthFrameUSPerformMonitoringHistDataCounterValue_Type = Unsigned32
_Ltp8xONTEthFrameUSPerformMonitoringHistDataCounterValue_Object = MibTableColumn
ltp8xONTEthFrameUSPerformMonitoringHistDataCounterValue = _Ltp8xONTEthFrameUSPerformMonitoringHistDataCounterValue_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 7, 1, 6),
    _Ltp8xONTEthFrameUSPerformMonitoringHistDataCounterValue_Type()
)
ltp8xONTEthFrameUSPerformMonitoringHistDataCounterValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTEthFrameUSPerformMonitoringHistDataCounterValue.setStatus("current")
_Ltp8xONTGEMPortPerformMonitoringDSTable_Object = MibTable
ltp8xONTGEMPortPerformMonitoringDSTable = _Ltp8xONTGEMPortPerformMonitoringDSTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 8)
)
if mibBuilder.loadTexts:
    ltp8xONTGEMPortPerformMonitoringDSTable.setStatus("current")
_Ltp8xONTGEMPortPerformMonitoringDSEntry_Object = MibTableRow
ltp8xONTGEMPortPerformMonitoringDSEntry = _Ltp8xONTGEMPortPerformMonitoringDSEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 8, 1)
)
ltp8xONTGEMPortPerformMonitoringDSEntry.setIndexNames(
    (0, "ELTEX-LTP8X", "ltp8xONTGEMPortPerformMonitoringDSSlot"),
    (0, "ELTEX-LTP8X", "ltp8xONTGEMPortPerformMonitoringDSSerial"),
    (0, "ELTEX-LTP8X", "ltp8xONTGEMPortPerformMonitoringDSCrossConnect"),
    (0, "ELTEX-LTP8X", "ltp8xONTGEMPortPerformMonitoringDSCounterID"),
)
if mibBuilder.loadTexts:
    ltp8xONTGEMPortPerformMonitoringDSEntry.setStatus("current")
_Ltp8xONTGEMPortPerformMonitoringDSSlot_Type = Unsigned32
_Ltp8xONTGEMPortPerformMonitoringDSSlot_Object = MibTableColumn
ltp8xONTGEMPortPerformMonitoringDSSlot = _Ltp8xONTGEMPortPerformMonitoringDSSlot_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 8, 1, 1),
    _Ltp8xONTGEMPortPerformMonitoringDSSlot_Type()
)
ltp8xONTGEMPortPerformMonitoringDSSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTGEMPortPerformMonitoringDSSlot.setStatus("current")
_Ltp8xONTGEMPortPerformMonitoringDSSerial_Type = ONTSerial
_Ltp8xONTGEMPortPerformMonitoringDSSerial_Object = MibTableColumn
ltp8xONTGEMPortPerformMonitoringDSSerial = _Ltp8xONTGEMPortPerformMonitoringDSSerial_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 8, 1, 2),
    _Ltp8xONTGEMPortPerformMonitoringDSSerial_Type()
)
ltp8xONTGEMPortPerformMonitoringDSSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTGEMPortPerformMonitoringDSSerial.setStatus("current")
_Ltp8xONTGEMPortPerformMonitoringDSCrossConnect_Type = Unsigned32
_Ltp8xONTGEMPortPerformMonitoringDSCrossConnect_Object = MibTableColumn
ltp8xONTGEMPortPerformMonitoringDSCrossConnect = _Ltp8xONTGEMPortPerformMonitoringDSCrossConnect_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 8, 1, 3),
    _Ltp8xONTGEMPortPerformMonitoringDSCrossConnect_Type()
)
ltp8xONTGEMPortPerformMonitoringDSCrossConnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTGEMPortPerformMonitoringDSCrossConnect.setStatus("current")
_Ltp8xONTGEMPortPerformMonitoringDSCounterID_Type = Unsigned32
_Ltp8xONTGEMPortPerformMonitoringDSCounterID_Object = MibTableColumn
ltp8xONTGEMPortPerformMonitoringDSCounterID = _Ltp8xONTGEMPortPerformMonitoringDSCounterID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 8, 1, 4),
    _Ltp8xONTGEMPortPerformMonitoringDSCounterID_Type()
)
ltp8xONTGEMPortPerformMonitoringDSCounterID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTGEMPortPerformMonitoringDSCounterID.setStatus("current")
_Ltp8xONTGEMPortPerformMonitoringDSCounterName_Type = DisplayString
_Ltp8xONTGEMPortPerformMonitoringDSCounterName_Object = MibTableColumn
ltp8xONTGEMPortPerformMonitoringDSCounterName = _Ltp8xONTGEMPortPerformMonitoringDSCounterName_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 8, 1, 5),
    _Ltp8xONTGEMPortPerformMonitoringDSCounterName_Type()
)
ltp8xONTGEMPortPerformMonitoringDSCounterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTGEMPortPerformMonitoringDSCounterName.setStatus("current")
_Ltp8xONTGEMPortPerformMonitoringDSCounterValue_Type = Unsigned32
_Ltp8xONTGEMPortPerformMonitoringDSCounterValue_Object = MibTableColumn
ltp8xONTGEMPortPerformMonitoringDSCounterValue = _Ltp8xONTGEMPortPerformMonitoringDSCounterValue_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 8, 1, 6),
    _Ltp8xONTGEMPortPerformMonitoringDSCounterValue_Type()
)
ltp8xONTGEMPortPerformMonitoringDSCounterValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTGEMPortPerformMonitoringDSCounterValue.setStatus("current")
_Ltp8xONTGEMPortPerformMonitoringUSTable_Object = MibTable
ltp8xONTGEMPortPerformMonitoringUSTable = _Ltp8xONTGEMPortPerformMonitoringUSTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 9)
)
if mibBuilder.loadTexts:
    ltp8xONTGEMPortPerformMonitoringUSTable.setStatus("current")
_Ltp8xONTGEMPortPerformMonitoringUSEntry_Object = MibTableRow
ltp8xONTGEMPortPerformMonitoringUSEntry = _Ltp8xONTGEMPortPerformMonitoringUSEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 9, 1)
)
ltp8xONTGEMPortPerformMonitoringUSEntry.setIndexNames(
    (0, "ELTEX-LTP8X", "ltp8xONTGEMPortPerformMonitoringUSSlot"),
    (0, "ELTEX-LTP8X", "ltp8xONTGEMPortPerformMonitoringUSSerial"),
    (0, "ELTEX-LTP8X", "ltp8xONTGEMPortPerformMonitoringUSCrossConnect"),
    (0, "ELTEX-LTP8X", "ltp8xONTGEMPortPerformMonitoringUSCounterID"),
)
if mibBuilder.loadTexts:
    ltp8xONTGEMPortPerformMonitoringUSEntry.setStatus("current")
_Ltp8xONTGEMPortPerformMonitoringUSSlot_Type = Unsigned32
_Ltp8xONTGEMPortPerformMonitoringUSSlot_Object = MibTableColumn
ltp8xONTGEMPortPerformMonitoringUSSlot = _Ltp8xONTGEMPortPerformMonitoringUSSlot_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 9, 1, 1),
    _Ltp8xONTGEMPortPerformMonitoringUSSlot_Type()
)
ltp8xONTGEMPortPerformMonitoringUSSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTGEMPortPerformMonitoringUSSlot.setStatus("current")
_Ltp8xONTGEMPortPerformMonitoringUSSerial_Type = ONTSerial
_Ltp8xONTGEMPortPerformMonitoringUSSerial_Object = MibTableColumn
ltp8xONTGEMPortPerformMonitoringUSSerial = _Ltp8xONTGEMPortPerformMonitoringUSSerial_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 9, 1, 2),
    _Ltp8xONTGEMPortPerformMonitoringUSSerial_Type()
)
ltp8xONTGEMPortPerformMonitoringUSSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTGEMPortPerformMonitoringUSSerial.setStatus("current")
_Ltp8xONTGEMPortPerformMonitoringUSCrossConnect_Type = Unsigned32
_Ltp8xONTGEMPortPerformMonitoringUSCrossConnect_Object = MibTableColumn
ltp8xONTGEMPortPerformMonitoringUSCrossConnect = _Ltp8xONTGEMPortPerformMonitoringUSCrossConnect_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 9, 1, 3),
    _Ltp8xONTGEMPortPerformMonitoringUSCrossConnect_Type()
)
ltp8xONTGEMPortPerformMonitoringUSCrossConnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTGEMPortPerformMonitoringUSCrossConnect.setStatus("current")
_Ltp8xONTGEMPortPerformMonitoringUSCounterID_Type = Unsigned32
_Ltp8xONTGEMPortPerformMonitoringUSCounterID_Object = MibTableColumn
ltp8xONTGEMPortPerformMonitoringUSCounterID = _Ltp8xONTGEMPortPerformMonitoringUSCounterID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 9, 1, 4),
    _Ltp8xONTGEMPortPerformMonitoringUSCounterID_Type()
)
ltp8xONTGEMPortPerformMonitoringUSCounterID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTGEMPortPerformMonitoringUSCounterID.setStatus("current")
_Ltp8xONTGEMPortPerformMonitoringUSCounterName_Type = DisplayString
_Ltp8xONTGEMPortPerformMonitoringUSCounterName_Object = MibTableColumn
ltp8xONTGEMPortPerformMonitoringUSCounterName = _Ltp8xONTGEMPortPerformMonitoringUSCounterName_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 9, 1, 5),
    _Ltp8xONTGEMPortPerformMonitoringUSCounterName_Type()
)
ltp8xONTGEMPortPerformMonitoringUSCounterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTGEMPortPerformMonitoringUSCounterName.setStatus("current")
_Ltp8xONTGEMPortPerformMonitoringUSCounterValue_Type = Unsigned32
_Ltp8xONTGEMPortPerformMonitoringUSCounterValue_Object = MibTableColumn
ltp8xONTGEMPortPerformMonitoringUSCounterValue = _Ltp8xONTGEMPortPerformMonitoringUSCounterValue_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 9, 1, 6),
    _Ltp8xONTGEMPortPerformMonitoringUSCounterValue_Type()
)
ltp8xONTGEMPortPerformMonitoringUSCounterValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTGEMPortPerformMonitoringUSCounterValue.setStatus("current")
_Ltp8xONTCrossConnectDSTable_Object = MibTable
ltp8xONTCrossConnectDSTable = _Ltp8xONTCrossConnectDSTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 10)
)
if mibBuilder.loadTexts:
    ltp8xONTCrossConnectDSTable.setStatus("current")
_Ltp8xONTCrossConnectDSEntry_Object = MibTableRow
ltp8xONTCrossConnectDSEntry = _Ltp8xONTCrossConnectDSEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 10, 1)
)
ltp8xONTCrossConnectDSEntry.setIndexNames(
    (0, "ELTEX-LTP8X", "ltp8xONTCrossConnectDSSlot"),
    (0, "ELTEX-LTP8X", "ltp8xONTCrossConnectDSSerial"),
    (0, "ELTEX-LTP8X", "ltp8xONTCrossConnectDSCrossConnect"),
    (0, "ELTEX-LTP8X", "ltp8xONTCrossConnectDSCounterID"),
)
if mibBuilder.loadTexts:
    ltp8xONTCrossConnectDSEntry.setStatus("current")
_Ltp8xONTCrossConnectDSSlot_Type = Unsigned32
_Ltp8xONTCrossConnectDSSlot_Object = MibTableColumn
ltp8xONTCrossConnectDSSlot = _Ltp8xONTCrossConnectDSSlot_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 10, 1, 1),
    _Ltp8xONTCrossConnectDSSlot_Type()
)
ltp8xONTCrossConnectDSSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTCrossConnectDSSlot.setStatus("current")
_Ltp8xONTCrossConnectDSSerial_Type = ONTSerial
_Ltp8xONTCrossConnectDSSerial_Object = MibTableColumn
ltp8xONTCrossConnectDSSerial = _Ltp8xONTCrossConnectDSSerial_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 10, 1, 2),
    _Ltp8xONTCrossConnectDSSerial_Type()
)
ltp8xONTCrossConnectDSSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTCrossConnectDSSerial.setStatus("current")
_Ltp8xONTCrossConnectDSCrossConnect_Type = Unsigned32
_Ltp8xONTCrossConnectDSCrossConnect_Object = MibTableColumn
ltp8xONTCrossConnectDSCrossConnect = _Ltp8xONTCrossConnectDSCrossConnect_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 10, 1, 3),
    _Ltp8xONTCrossConnectDSCrossConnect_Type()
)
ltp8xONTCrossConnectDSCrossConnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTCrossConnectDSCrossConnect.setStatus("current")
_Ltp8xONTCrossConnectDSCounterID_Type = Unsigned32
_Ltp8xONTCrossConnectDSCounterID_Object = MibTableColumn
ltp8xONTCrossConnectDSCounterID = _Ltp8xONTCrossConnectDSCounterID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 10, 1, 4),
    _Ltp8xONTCrossConnectDSCounterID_Type()
)
ltp8xONTCrossConnectDSCounterID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTCrossConnectDSCounterID.setStatus("current")
_Ltp8xONTCrossConnectDSCounterName_Type = DisplayString
_Ltp8xONTCrossConnectDSCounterName_Object = MibTableColumn
ltp8xONTCrossConnectDSCounterName = _Ltp8xONTCrossConnectDSCounterName_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 10, 1, 5),
    _Ltp8xONTCrossConnectDSCounterName_Type()
)
ltp8xONTCrossConnectDSCounterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTCrossConnectDSCounterName.setStatus("current")
_Ltp8xONTCrossConnectDSCounterValue_Type = Unsigned32
_Ltp8xONTCrossConnectDSCounterValue_Object = MibTableColumn
ltp8xONTCrossConnectDSCounterValue = _Ltp8xONTCrossConnectDSCounterValue_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 10, 1, 6),
    _Ltp8xONTCrossConnectDSCounterValue_Type()
)
ltp8xONTCrossConnectDSCounterValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTCrossConnectDSCounterValue.setStatus("current")
_Ltp8xONTCrossConnectUSTable_Object = MibTable
ltp8xONTCrossConnectUSTable = _Ltp8xONTCrossConnectUSTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 11)
)
if mibBuilder.loadTexts:
    ltp8xONTCrossConnectUSTable.setStatus("current")
_Ltp8xONTCrossConnectUSEntry_Object = MibTableRow
ltp8xONTCrossConnectUSEntry = _Ltp8xONTCrossConnectUSEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 11, 1)
)
ltp8xONTCrossConnectUSEntry.setIndexNames(
    (0, "ELTEX-LTP8X", "ltp8xONTCrossConnectUSSlot"),
    (0, "ELTEX-LTP8X", "ltp8xONTCrossConnectUSSerial"),
    (0, "ELTEX-LTP8X", "ltp8xONTCrossConnectUSCrossConnect"),
    (0, "ELTEX-LTP8X", "ltp8xONTCrossConnectUSCounterID"),
)
if mibBuilder.loadTexts:
    ltp8xONTCrossConnectUSEntry.setStatus("current")
_Ltp8xONTCrossConnectUSSlot_Type = Unsigned32
_Ltp8xONTCrossConnectUSSlot_Object = MibTableColumn
ltp8xONTCrossConnectUSSlot = _Ltp8xONTCrossConnectUSSlot_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 11, 1, 1),
    _Ltp8xONTCrossConnectUSSlot_Type()
)
ltp8xONTCrossConnectUSSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTCrossConnectUSSlot.setStatus("current")
_Ltp8xONTCrossConnectUSSerial_Type = ONTSerial
_Ltp8xONTCrossConnectUSSerial_Object = MibTableColumn
ltp8xONTCrossConnectUSSerial = _Ltp8xONTCrossConnectUSSerial_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 11, 1, 2),
    _Ltp8xONTCrossConnectUSSerial_Type()
)
ltp8xONTCrossConnectUSSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTCrossConnectUSSerial.setStatus("current")
_Ltp8xONTCrossConnectUSCrossConnect_Type = Unsigned32
_Ltp8xONTCrossConnectUSCrossConnect_Object = MibTableColumn
ltp8xONTCrossConnectUSCrossConnect = _Ltp8xONTCrossConnectUSCrossConnect_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 11, 1, 3),
    _Ltp8xONTCrossConnectUSCrossConnect_Type()
)
ltp8xONTCrossConnectUSCrossConnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTCrossConnectUSCrossConnect.setStatus("current")
_Ltp8xONTCrossConnectUSCounterID_Type = Unsigned32
_Ltp8xONTCrossConnectUSCounterID_Object = MibTableColumn
ltp8xONTCrossConnectUSCounterID = _Ltp8xONTCrossConnectUSCounterID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 11, 1, 4),
    _Ltp8xONTCrossConnectUSCounterID_Type()
)
ltp8xONTCrossConnectUSCounterID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTCrossConnectUSCounterID.setStatus("current")
_Ltp8xONTCrossConnectUSCounterName_Type = DisplayString
_Ltp8xONTCrossConnectUSCounterName_Object = MibTableColumn
ltp8xONTCrossConnectUSCounterName = _Ltp8xONTCrossConnectUSCounterName_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 11, 1, 5),
    _Ltp8xONTCrossConnectUSCounterName_Type()
)
ltp8xONTCrossConnectUSCounterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTCrossConnectUSCounterName.setStatus("current")
_Ltp8xONTCrossConnectUSCounterValue_Type = Unsigned32
_Ltp8xONTCrossConnectUSCounterValue_Object = MibTableColumn
ltp8xONTCrossConnectUSCounterValue = _Ltp8xONTCrossConnectUSCounterValue_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 11, 1, 6),
    _Ltp8xONTCrossConnectUSCounterValue_Type()
)
ltp8xONTCrossConnectUSCounterValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTCrossConnectUSCounterValue.setStatus("current")
_Ltp8xONTServiceDSTable_Object = MibTable
ltp8xONTServiceDSTable = _Ltp8xONTServiceDSTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 12)
)
if mibBuilder.loadTexts:
    ltp8xONTServiceDSTable.setStatus("current")
_Ltp8xONTServiceDSEntry_Object = MibTableRow
ltp8xONTServiceDSEntry = _Ltp8xONTServiceDSEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 12, 1)
)
ltp8xONTServiceDSEntry.setIndexNames(
    (0, "ELTEX-LTP8X", "ltp8xONTServiceDSSlot"),
    (0, "ELTEX-LTP8X", "ltp8xONTServiceDSSerial"),
    (0, "ELTEX-LTP8X", "ltp8xONTServiceDSService"),
    (0, "ELTEX-LTP8X", "ltp8xONTServiceDSCounterID"),
)
if mibBuilder.loadTexts:
    ltp8xONTServiceDSEntry.setStatus("current")
_Ltp8xONTServiceDSSlot_Type = Unsigned32
_Ltp8xONTServiceDSSlot_Object = MibTableColumn
ltp8xONTServiceDSSlot = _Ltp8xONTServiceDSSlot_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 12, 1, 1),
    _Ltp8xONTServiceDSSlot_Type()
)
ltp8xONTServiceDSSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTServiceDSSlot.setStatus("current")
_Ltp8xONTServiceDSSerial_Type = ONTSerial
_Ltp8xONTServiceDSSerial_Object = MibTableColumn
ltp8xONTServiceDSSerial = _Ltp8xONTServiceDSSerial_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 12, 1, 2),
    _Ltp8xONTServiceDSSerial_Type()
)
ltp8xONTServiceDSSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTServiceDSSerial.setStatus("current")
_Ltp8xONTServiceDSService_Type = Unsigned32
_Ltp8xONTServiceDSService_Object = MibTableColumn
ltp8xONTServiceDSService = _Ltp8xONTServiceDSService_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 12, 1, 3),
    _Ltp8xONTServiceDSService_Type()
)
ltp8xONTServiceDSService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTServiceDSService.setStatus("current")
_Ltp8xONTServiceDSCounterID_Type = Unsigned32
_Ltp8xONTServiceDSCounterID_Object = MibTableColumn
ltp8xONTServiceDSCounterID = _Ltp8xONTServiceDSCounterID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 12, 1, 4),
    _Ltp8xONTServiceDSCounterID_Type()
)
ltp8xONTServiceDSCounterID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTServiceDSCounterID.setStatus("current")
_Ltp8xONTServiceDSCounterName_Type = DisplayString
_Ltp8xONTServiceDSCounterName_Object = MibTableColumn
ltp8xONTServiceDSCounterName = _Ltp8xONTServiceDSCounterName_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 12, 1, 5),
    _Ltp8xONTServiceDSCounterName_Type()
)
ltp8xONTServiceDSCounterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTServiceDSCounterName.setStatus("current")
_Ltp8xONTServiceDSCounterValue_Type = Unsigned32
_Ltp8xONTServiceDSCounterValue_Object = MibTableColumn
ltp8xONTServiceDSCounterValue = _Ltp8xONTServiceDSCounterValue_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 12, 1, 6),
    _Ltp8xONTServiceDSCounterValue_Type()
)
ltp8xONTServiceDSCounterValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTServiceDSCounterValue.setStatus("current")
_Ltp8xONTServiceUSTable_Object = MibTable
ltp8xONTServiceUSTable = _Ltp8xONTServiceUSTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 13)
)
if mibBuilder.loadTexts:
    ltp8xONTServiceUSTable.setStatus("current")
_Ltp8xONTServiceUSEntry_Object = MibTableRow
ltp8xONTServiceUSEntry = _Ltp8xONTServiceUSEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 13, 1)
)
ltp8xONTServiceUSEntry.setIndexNames(
    (0, "ELTEX-LTP8X", "ltp8xONTServiceUSSlot"),
    (0, "ELTEX-LTP8X", "ltp8xONTServiceUSSerial"),
    (0, "ELTEX-LTP8X", "ltp8xONTServiceUSService"),
    (0, "ELTEX-LTP8X", "ltp8xONTServiceUSCounterID"),
)
if mibBuilder.loadTexts:
    ltp8xONTServiceUSEntry.setStatus("current")
_Ltp8xONTServiceUSSlot_Type = Unsigned32
_Ltp8xONTServiceUSSlot_Object = MibTableColumn
ltp8xONTServiceUSSlot = _Ltp8xONTServiceUSSlot_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 13, 1, 1),
    _Ltp8xONTServiceUSSlot_Type()
)
ltp8xONTServiceUSSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTServiceUSSlot.setStatus("current")
_Ltp8xONTServiceUSSerial_Type = ONTSerial
_Ltp8xONTServiceUSSerial_Object = MibTableColumn
ltp8xONTServiceUSSerial = _Ltp8xONTServiceUSSerial_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 13, 1, 2),
    _Ltp8xONTServiceUSSerial_Type()
)
ltp8xONTServiceUSSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTServiceUSSerial.setStatus("current")
_Ltp8xONTServiceUSService_Type = Unsigned32
_Ltp8xONTServiceUSService_Object = MibTableColumn
ltp8xONTServiceUSService = _Ltp8xONTServiceUSService_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 13, 1, 3),
    _Ltp8xONTServiceUSService_Type()
)
ltp8xONTServiceUSService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTServiceUSService.setStatus("current")
_Ltp8xONTServiceUSCounterID_Type = Unsigned32
_Ltp8xONTServiceUSCounterID_Object = MibTableColumn
ltp8xONTServiceUSCounterID = _Ltp8xONTServiceUSCounterID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 13, 1, 4),
    _Ltp8xONTServiceUSCounterID_Type()
)
ltp8xONTServiceUSCounterID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTServiceUSCounterID.setStatus("current")
_Ltp8xONTServiceUSCounterName_Type = DisplayString
_Ltp8xONTServiceUSCounterName_Object = MibTableColumn
ltp8xONTServiceUSCounterName = _Ltp8xONTServiceUSCounterName_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 13, 1, 5),
    _Ltp8xONTServiceUSCounterName_Type()
)
ltp8xONTServiceUSCounterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTServiceUSCounterName.setStatus("current")
_Ltp8xONTServiceUSCounterValue_Type = Unsigned32
_Ltp8xONTServiceUSCounterValue_Object = MibTableColumn
ltp8xONTServiceUSCounterValue = _Ltp8xONTServiceUSCounterValue_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 13, 1, 6),
    _Ltp8xONTServiceUSCounterValue_Type()
)
ltp8xONTServiceUSCounterValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTServiceUSCounterValue.setStatus("current")
_Ltp8xONTEthFrameExtendedPerformMonitoringDSTable_Object = MibTable
ltp8xONTEthFrameExtendedPerformMonitoringDSTable = _Ltp8xONTEthFrameExtendedPerformMonitoringDSTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 14)
)
if mibBuilder.loadTexts:
    ltp8xONTEthFrameExtendedPerformMonitoringDSTable.setStatus("current")
_Ltp8xONTEthFrameExtendedPerformMonitoringDSEntry_Object = MibTableRow
ltp8xONTEthFrameExtendedPerformMonitoringDSEntry = _Ltp8xONTEthFrameExtendedPerformMonitoringDSEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 14, 1)
)
ltp8xONTEthFrameExtendedPerformMonitoringDSEntry.setIndexNames(
    (0, "ELTEX-LTP8X", "ltp8xONTEthFrameExtendedPerformMonitoringDSSlot"),
    (0, "ELTEX-LTP8X", "ltp8xONTEthFrameExtendedPerformMonitoringDSSerial"),
    (0, "ELTEX-LTP8X", "ltp8xONTEthFrameExtendedPerformMonitoringDSPort"),
    (0, "ELTEX-LTP8X", "ltp8xONTEthFrameExtendedPerformMonitoringDSCounterID"),
)
if mibBuilder.loadTexts:
    ltp8xONTEthFrameExtendedPerformMonitoringDSEntry.setStatus("current")
_Ltp8xONTEthFrameExtendedPerformMonitoringDSSlot_Type = Unsigned32
_Ltp8xONTEthFrameExtendedPerformMonitoringDSSlot_Object = MibTableColumn
ltp8xONTEthFrameExtendedPerformMonitoringDSSlot = _Ltp8xONTEthFrameExtendedPerformMonitoringDSSlot_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 14, 1, 1),
    _Ltp8xONTEthFrameExtendedPerformMonitoringDSSlot_Type()
)
ltp8xONTEthFrameExtendedPerformMonitoringDSSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTEthFrameExtendedPerformMonitoringDSSlot.setStatus("current")
_Ltp8xONTEthFrameExtendedPerformMonitoringDSSerial_Type = ONTSerial
_Ltp8xONTEthFrameExtendedPerformMonitoringDSSerial_Object = MibTableColumn
ltp8xONTEthFrameExtendedPerformMonitoringDSSerial = _Ltp8xONTEthFrameExtendedPerformMonitoringDSSerial_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 14, 1, 2),
    _Ltp8xONTEthFrameExtendedPerformMonitoringDSSerial_Type()
)
ltp8xONTEthFrameExtendedPerformMonitoringDSSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTEthFrameExtendedPerformMonitoringDSSerial.setStatus("current")
_Ltp8xONTEthFrameExtendedPerformMonitoringDSPort_Type = Unsigned32
_Ltp8xONTEthFrameExtendedPerformMonitoringDSPort_Object = MibTableColumn
ltp8xONTEthFrameExtendedPerformMonitoringDSPort = _Ltp8xONTEthFrameExtendedPerformMonitoringDSPort_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 14, 1, 3),
    _Ltp8xONTEthFrameExtendedPerformMonitoringDSPort_Type()
)
ltp8xONTEthFrameExtendedPerformMonitoringDSPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTEthFrameExtendedPerformMonitoringDSPort.setStatus("current")
_Ltp8xONTEthFrameExtendedPerformMonitoringDSCounterID_Type = Unsigned32
_Ltp8xONTEthFrameExtendedPerformMonitoringDSCounterID_Object = MibTableColumn
ltp8xONTEthFrameExtendedPerformMonitoringDSCounterID = _Ltp8xONTEthFrameExtendedPerformMonitoringDSCounterID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 14, 1, 4),
    _Ltp8xONTEthFrameExtendedPerformMonitoringDSCounterID_Type()
)
ltp8xONTEthFrameExtendedPerformMonitoringDSCounterID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTEthFrameExtendedPerformMonitoringDSCounterID.setStatus("current")
_Ltp8xONTEthFrameExtendedPerformMonitoringDSCounterName_Type = DisplayString
_Ltp8xONTEthFrameExtendedPerformMonitoringDSCounterName_Object = MibTableColumn
ltp8xONTEthFrameExtendedPerformMonitoringDSCounterName = _Ltp8xONTEthFrameExtendedPerformMonitoringDSCounterName_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 14, 1, 5),
    _Ltp8xONTEthFrameExtendedPerformMonitoringDSCounterName_Type()
)
ltp8xONTEthFrameExtendedPerformMonitoringDSCounterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTEthFrameExtendedPerformMonitoringDSCounterName.setStatus("current")
_Ltp8xONTEthFrameExtendedPerformMonitoringDSCounterValue_Type = Unsigned32
_Ltp8xONTEthFrameExtendedPerformMonitoringDSCounterValue_Object = MibTableColumn
ltp8xONTEthFrameExtendedPerformMonitoringDSCounterValue = _Ltp8xONTEthFrameExtendedPerformMonitoringDSCounterValue_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 14, 1, 6),
    _Ltp8xONTEthFrameExtendedPerformMonitoringDSCounterValue_Type()
)
ltp8xONTEthFrameExtendedPerformMonitoringDSCounterValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTEthFrameExtendedPerformMonitoringDSCounterValue.setStatus("current")
_Ltp8xONTEthFrameExtendedPerformMonitoringUSTable_Object = MibTable
ltp8xONTEthFrameExtendedPerformMonitoringUSTable = _Ltp8xONTEthFrameExtendedPerformMonitoringUSTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 15)
)
if mibBuilder.loadTexts:
    ltp8xONTEthFrameExtendedPerformMonitoringUSTable.setStatus("current")
_Ltp8xONTEthFrameExtendedPerformMonitoringUSEntry_Object = MibTableRow
ltp8xONTEthFrameExtendedPerformMonitoringUSEntry = _Ltp8xONTEthFrameExtendedPerformMonitoringUSEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 15, 1)
)
ltp8xONTEthFrameExtendedPerformMonitoringUSEntry.setIndexNames(
    (0, "ELTEX-LTP8X", "ltp8xONTEthFrameExtendedPerformMonitoringUSSlot"),
    (0, "ELTEX-LTP8X", "ltp8xONTEthFrameExtendedPerformMonitoringUSSerial"),
    (0, "ELTEX-LTP8X", "ltp8xONTEthFrameExtendedPerformMonitoringUSPort"),
    (0, "ELTEX-LTP8X", "ltp8xONTEthFrameExtendedPerformMonitoringUSCounterID"),
)
if mibBuilder.loadTexts:
    ltp8xONTEthFrameExtendedPerformMonitoringUSEntry.setStatus("current")
_Ltp8xONTEthFrameExtendedPerformMonitoringUSSlot_Type = Unsigned32
_Ltp8xONTEthFrameExtendedPerformMonitoringUSSlot_Object = MibTableColumn
ltp8xONTEthFrameExtendedPerformMonitoringUSSlot = _Ltp8xONTEthFrameExtendedPerformMonitoringUSSlot_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 15, 1, 1),
    _Ltp8xONTEthFrameExtendedPerformMonitoringUSSlot_Type()
)
ltp8xONTEthFrameExtendedPerformMonitoringUSSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTEthFrameExtendedPerformMonitoringUSSlot.setStatus("current")
_Ltp8xONTEthFrameExtendedPerformMonitoringUSSerial_Type = ONTSerial
_Ltp8xONTEthFrameExtendedPerformMonitoringUSSerial_Object = MibTableColumn
ltp8xONTEthFrameExtendedPerformMonitoringUSSerial = _Ltp8xONTEthFrameExtendedPerformMonitoringUSSerial_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 15, 1, 2),
    _Ltp8xONTEthFrameExtendedPerformMonitoringUSSerial_Type()
)
ltp8xONTEthFrameExtendedPerformMonitoringUSSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTEthFrameExtendedPerformMonitoringUSSerial.setStatus("current")
_Ltp8xONTEthFrameExtendedPerformMonitoringUSPort_Type = Unsigned32
_Ltp8xONTEthFrameExtendedPerformMonitoringUSPort_Object = MibTableColumn
ltp8xONTEthFrameExtendedPerformMonitoringUSPort = _Ltp8xONTEthFrameExtendedPerformMonitoringUSPort_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 15, 1, 3),
    _Ltp8xONTEthFrameExtendedPerformMonitoringUSPort_Type()
)
ltp8xONTEthFrameExtendedPerformMonitoringUSPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTEthFrameExtendedPerformMonitoringUSPort.setStatus("current")
_Ltp8xONTEthFrameExtendedPerformMonitoringUSCounterID_Type = Unsigned32
_Ltp8xONTEthFrameExtendedPerformMonitoringUSCounterID_Object = MibTableColumn
ltp8xONTEthFrameExtendedPerformMonitoringUSCounterID = _Ltp8xONTEthFrameExtendedPerformMonitoringUSCounterID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 15, 1, 4),
    _Ltp8xONTEthFrameExtendedPerformMonitoringUSCounterID_Type()
)
ltp8xONTEthFrameExtendedPerformMonitoringUSCounterID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTEthFrameExtendedPerformMonitoringUSCounterID.setStatus("current")
_Ltp8xONTEthFrameExtendedPerformMonitoringUSCounterName_Type = DisplayString
_Ltp8xONTEthFrameExtendedPerformMonitoringUSCounterName_Object = MibTableColumn
ltp8xONTEthFrameExtendedPerformMonitoringUSCounterName = _Ltp8xONTEthFrameExtendedPerformMonitoringUSCounterName_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 15, 1, 5),
    _Ltp8xONTEthFrameExtendedPerformMonitoringUSCounterName_Type()
)
ltp8xONTEthFrameExtendedPerformMonitoringUSCounterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTEthFrameExtendedPerformMonitoringUSCounterName.setStatus("current")
_Ltp8xONTEthFrameExtendedPerformMonitoringUSCounterValue_Type = Unsigned32
_Ltp8xONTEthFrameExtendedPerformMonitoringUSCounterValue_Object = MibTableColumn
ltp8xONTEthFrameExtendedPerformMonitoringUSCounterValue = _Ltp8xONTEthFrameExtendedPerformMonitoringUSCounterValue_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 15, 1, 6),
    _Ltp8xONTEthFrameExtendedPerformMonitoringUSCounterValue_Type()
)
ltp8xONTEthFrameExtendedPerformMonitoringUSCounterValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTEthFrameExtendedPerformMonitoringUSCounterValue.setStatus("current")
_Ltp8xONTResetCountersTable_Object = MibTable
ltp8xONTResetCountersTable = _Ltp8xONTResetCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 20)
)
if mibBuilder.loadTexts:
    ltp8xONTResetCountersTable.setStatus("current")
_Ltp8xONTResetCountersEntry_Object = MibTableRow
ltp8xONTResetCountersEntry = _Ltp8xONTResetCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 20, 1)
)
ltp8xONTResetCountersEntry.setIndexNames(
    (0, "ELTEX-LTP8X", "ltp8xONTResetCountersSlot"),
    (0, "ELTEX-LTP8X", "ltp8xONTResetCountersSerial"),
)
if mibBuilder.loadTexts:
    ltp8xONTResetCountersEntry.setStatus("current")
_Ltp8xONTResetCountersSlot_Type = Unsigned32
_Ltp8xONTResetCountersSlot_Object = MibTableColumn
ltp8xONTResetCountersSlot = _Ltp8xONTResetCountersSlot_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 20, 1, 1),
    _Ltp8xONTResetCountersSlot_Type()
)
ltp8xONTResetCountersSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTResetCountersSlot.setStatus("current")
_Ltp8xONTResetCountersSerial_Type = ONTSerial
_Ltp8xONTResetCountersSerial_Object = MibTableColumn
ltp8xONTResetCountersSerial = _Ltp8xONTResetCountersSerial_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 20, 1, 2),
    _Ltp8xONTResetCountersSerial_Type()
)
ltp8xONTResetCountersSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTResetCountersSerial.setStatus("current")
_Ltp8xONTResetCountersAction_Type = Unsigned32
_Ltp8xONTResetCountersAction_Object = MibTableColumn
ltp8xONTResetCountersAction = _Ltp8xONTResetCountersAction_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 3, 20, 1, 3),
    _Ltp8xONTResetCountersAction_Type()
)
ltp8xONTResetCountersAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTResetCountersAction.setStatus("current")
_Ltp8xONTConfigTable_Object = MibTable
ltp8xONTConfigTable = _Ltp8xONTConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 4)
)
if mibBuilder.loadTexts:
    ltp8xONTConfigTable.setStatus("current")
_Ltp8xONTConfigEntry_Object = MibTableRow
ltp8xONTConfigEntry = _Ltp8xONTConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 4, 1)
)
ltp8xONTConfigEntry.setIndexNames(
    (0, "ELTEX-LTP8X", "ltp8xONTConfigSlot"),
    (0, "ELTEX-LTP8X", "ltp8xONTConfigSerial"),
)
if mibBuilder.loadTexts:
    ltp8xONTConfigEntry.setStatus("current")
_Ltp8xONTConfigSlot_Type = Unsigned32
_Ltp8xONTConfigSlot_Object = MibTableColumn
ltp8xONTConfigSlot = _Ltp8xONTConfigSlot_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 4, 1, 1),
    _Ltp8xONTConfigSlot_Type()
)
ltp8xONTConfigSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTConfigSlot.setStatus("current")
_Ltp8xONTConfigSerial_Type = ONTSerial
_Ltp8xONTConfigSerial_Object = MibTableColumn
ltp8xONTConfigSerial = _Ltp8xONTConfigSerial_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 4, 1, 2),
    _Ltp8xONTConfigSerial_Type()
)
ltp8xONTConfigSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTConfigSerial.setStatus("current")
_Ltp8xONTConfigChannel_Type = Unsigned32
_Ltp8xONTConfigChannel_Object = MibTableColumn
ltp8xONTConfigChannel = _Ltp8xONTConfigChannel_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 4, 1, 3),
    _Ltp8xONTConfigChannel_Type()
)
ltp8xONTConfigChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTConfigChannel.setStatus("current")
_Ltp8xONTConfigID_Type = Unsigned32
_Ltp8xONTConfigID_Object = MibTableColumn
ltp8xONTConfigID = _Ltp8xONTConfigID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 4, 1, 4),
    _Ltp8xONTConfigID_Type()
)
ltp8xONTConfigID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTConfigID.setStatus("current")
_Ltp8xONTConfigServicesProfile_Type = Unsigned32
_Ltp8xONTConfigServicesProfile_Object = MibTableColumn
ltp8xONTConfigServicesProfile = _Ltp8xONTConfigServicesProfile_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 4, 1, 5),
    _Ltp8xONTConfigServicesProfile_Type()
)
ltp8xONTConfigServicesProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTConfigServicesProfile.setStatus("deprecated")
_Ltp8xONTConfigPassword_Type = DisplayString
_Ltp8xONTConfigPassword_Object = MibTableColumn
ltp8xONTConfigPassword = _Ltp8xONTConfigPassword_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 4, 1, 6),
    _Ltp8xONTConfigPassword_Type()
)
ltp8xONTConfigPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTConfigPassword.setStatus("current")
_Ltp8xONTConfigFecUp_Type = TruthValue
_Ltp8xONTConfigFecUp_Object = MibTableColumn
ltp8xONTConfigFecUp = _Ltp8xONTConfigFecUp_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 4, 1, 7),
    _Ltp8xONTConfigFecUp_Type()
)
ltp8xONTConfigFecUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTConfigFecUp.setStatus("current")
_Ltp8xONTConfigDescription_Type = DisplayString
_Ltp8xONTConfigDescription_Object = MibTableColumn
ltp8xONTConfigDescription = _Ltp8xONTConfigDescription_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 4, 1, 8),
    _Ltp8xONTConfigDescription_Type()
)
ltp8xONTConfigDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTConfigDescription.setStatus("current")
_Ltp8xONTConfigManagementProfile_Type = Unsigned32
_Ltp8xONTConfigManagementProfile_Object = MibTableColumn
ltp8xONTConfigManagementProfile = _Ltp8xONTConfigManagementProfile_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 4, 1, 9),
    _Ltp8xONTConfigManagementProfile_Type()
)
ltp8xONTConfigManagementProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTConfigManagementProfile.setStatus("current")
_Ltp8xONTConfigMulticastProfile_Type = Unsigned32
_Ltp8xONTConfigMulticastProfile_Object = MibTableColumn
ltp8xONTConfigMulticastProfile = _Ltp8xONTConfigMulticastProfile_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 4, 1, 10),
    _Ltp8xONTConfigMulticastProfile_Type()
)
ltp8xONTConfigMulticastProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTConfigMulticastProfile.setStatus("current")
_Ltp8xONTConfigCrossConnectProfile0_Type = Unsigned32
_Ltp8xONTConfigCrossConnectProfile0_Object = MibTableColumn
ltp8xONTConfigCrossConnectProfile0 = _Ltp8xONTConfigCrossConnectProfile0_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 4, 1, 11),
    _Ltp8xONTConfigCrossConnectProfile0_Type()
)
ltp8xONTConfigCrossConnectProfile0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTConfigCrossConnectProfile0.setStatus("current")
_Ltp8xONTConfigCrossConnectProfile1_Type = Unsigned32
_Ltp8xONTConfigCrossConnectProfile1_Object = MibTableColumn
ltp8xONTConfigCrossConnectProfile1 = _Ltp8xONTConfigCrossConnectProfile1_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 4, 1, 12),
    _Ltp8xONTConfigCrossConnectProfile1_Type()
)
ltp8xONTConfigCrossConnectProfile1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTConfigCrossConnectProfile1.setStatus("current")
_Ltp8xONTConfigCrossConnectProfile2_Type = Unsigned32
_Ltp8xONTConfigCrossConnectProfile2_Object = MibTableColumn
ltp8xONTConfigCrossConnectProfile2 = _Ltp8xONTConfigCrossConnectProfile2_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 4, 1, 13),
    _Ltp8xONTConfigCrossConnectProfile2_Type()
)
ltp8xONTConfigCrossConnectProfile2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTConfigCrossConnectProfile2.setStatus("current")
_Ltp8xONTConfigCrossConnectProfile3_Type = Unsigned32
_Ltp8xONTConfigCrossConnectProfile3_Object = MibTableColumn
ltp8xONTConfigCrossConnectProfile3 = _Ltp8xONTConfigCrossConnectProfile3_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 4, 1, 14),
    _Ltp8xONTConfigCrossConnectProfile3_Type()
)
ltp8xONTConfigCrossConnectProfile3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTConfigCrossConnectProfile3.setStatus("current")
_Ltp8xONTConfigCrossConnectProfile4_Type = Unsigned32
_Ltp8xONTConfigCrossConnectProfile4_Object = MibTableColumn
ltp8xONTConfigCrossConnectProfile4 = _Ltp8xONTConfigCrossConnectProfile4_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 4, 1, 15),
    _Ltp8xONTConfigCrossConnectProfile4_Type()
)
ltp8xONTConfigCrossConnectProfile4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTConfigCrossConnectProfile4.setStatus("current")
_Ltp8xONTConfigCrossConnectProfile5_Type = Unsigned32
_Ltp8xONTConfigCrossConnectProfile5_Object = MibTableColumn
ltp8xONTConfigCrossConnectProfile5 = _Ltp8xONTConfigCrossConnectProfile5_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 4, 1, 16),
    _Ltp8xONTConfigCrossConnectProfile5_Type()
)
ltp8xONTConfigCrossConnectProfile5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTConfigCrossConnectProfile5.setStatus("current")
_Ltp8xONTConfigCrossConnectProfile6_Type = Unsigned32
_Ltp8xONTConfigCrossConnectProfile6_Object = MibTableColumn
ltp8xONTConfigCrossConnectProfile6 = _Ltp8xONTConfigCrossConnectProfile6_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 4, 1, 17),
    _Ltp8xONTConfigCrossConnectProfile6_Type()
)
ltp8xONTConfigCrossConnectProfile6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTConfigCrossConnectProfile6.setStatus("current")
_Ltp8xONTConfigCrossConnectProfile7_Type = Unsigned32
_Ltp8xONTConfigCrossConnectProfile7_Object = MibTableColumn
ltp8xONTConfigCrossConnectProfile7 = _Ltp8xONTConfigCrossConnectProfile7_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 4, 1, 18),
    _Ltp8xONTConfigCrossConnectProfile7_Type()
)
ltp8xONTConfigCrossConnectProfile7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTConfigCrossConnectProfile7.setStatus("current")
_Ltp8xONTConfigShapingProfile_Type = Unsigned32
_Ltp8xONTConfigShapingProfile_Object = MibTableColumn
ltp8xONTConfigShapingProfile = _Ltp8xONTConfigShapingProfile_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 4, 1, 19),
    _Ltp8xONTConfigShapingProfile_Type()
)
ltp8xONTConfigShapingProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTConfigShapingProfile.setStatus("current")
_Ltp8xONTConfigRowStatus_Type = RowStatus
_Ltp8xONTConfigRowStatus_Object = MibTableColumn
ltp8xONTConfigRowStatus = _Ltp8xONTConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 4, 1, 20),
    _Ltp8xONTConfigRowStatus_Type()
)
ltp8xONTConfigRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTConfigRowStatus.setStatus("current")
_Ltp8xONTConfigEncryptionEnabled_Type = TruthValue
_Ltp8xONTConfigEncryptionEnabled_Object = MibTableColumn
ltp8xONTConfigEncryptionEnabled = _Ltp8xONTConfigEncryptionEnabled_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 4, 1, 21),
    _Ltp8xONTConfigEncryptionEnabled_Type()
)
ltp8xONTConfigEncryptionEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTConfigEncryptionEnabled.setStatus("current")
_Ltp8xONTConfigDownstreamBroadcastEnabled_Type = TruthValue
_Ltp8xONTConfigDownstreamBroadcastEnabled_Object = MibTableColumn
ltp8xONTConfigDownstreamBroadcastEnabled = _Ltp8xONTConfigDownstreamBroadcastEnabled_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 4, 1, 22),
    _Ltp8xONTConfigDownstreamBroadcastEnabled_Type()
)
ltp8xONTConfigDownstreamBroadcastEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTConfigDownstreamBroadcastEnabled.setStatus("current")
_Ltp8xONTConfigAllocProfile0_Type = Unsigned32
_Ltp8xONTConfigAllocProfile0_Object = MibTableColumn
ltp8xONTConfigAllocProfile0 = _Ltp8xONTConfigAllocProfile0_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 4, 1, 23),
    _Ltp8xONTConfigAllocProfile0_Type()
)
ltp8xONTConfigAllocProfile0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTConfigAllocProfile0.setStatus("current")
_Ltp8xONTConfigAllocProfile1_Type = Unsigned32
_Ltp8xONTConfigAllocProfile1_Object = MibTableColumn
ltp8xONTConfigAllocProfile1 = _Ltp8xONTConfigAllocProfile1_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 4, 1, 24),
    _Ltp8xONTConfigAllocProfile1_Type()
)
ltp8xONTConfigAllocProfile1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTConfigAllocProfile1.setStatus("current")
_Ltp8xONTConfigAllocProfile2_Type = Unsigned32
_Ltp8xONTConfigAllocProfile2_Object = MibTableColumn
ltp8xONTConfigAllocProfile2 = _Ltp8xONTConfigAllocProfile2_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 4, 1, 25),
    _Ltp8xONTConfigAllocProfile2_Type()
)
ltp8xONTConfigAllocProfile2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTConfigAllocProfile2.setStatus("current")
_Ltp8xONTConfigAllocProfile3_Type = Unsigned32
_Ltp8xONTConfigAllocProfile3_Object = MibTableColumn
ltp8xONTConfigAllocProfile3 = _Ltp8xONTConfigAllocProfile3_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 4, 1, 26),
    _Ltp8xONTConfigAllocProfile3_Type()
)
ltp8xONTConfigAllocProfile3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTConfigAllocProfile3.setStatus("current")
_Ltp8xONTConfigAllocProfile4_Type = Unsigned32
_Ltp8xONTConfigAllocProfile4_Object = MibTableColumn
ltp8xONTConfigAllocProfile4 = _Ltp8xONTConfigAllocProfile4_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 4, 1, 27),
    _Ltp8xONTConfigAllocProfile4_Type()
)
ltp8xONTConfigAllocProfile4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTConfigAllocProfile4.setStatus("current")
_Ltp8xONTConfigAllocProfile5_Type = Unsigned32
_Ltp8xONTConfigAllocProfile5_Object = MibTableColumn
ltp8xONTConfigAllocProfile5 = _Ltp8xONTConfigAllocProfile5_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 4, 1, 28),
    _Ltp8xONTConfigAllocProfile5_Type()
)
ltp8xONTConfigAllocProfile5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTConfigAllocProfile5.setStatus("current")
_Ltp8xONTConfigAllocProfile6_Type = Unsigned32
_Ltp8xONTConfigAllocProfile6_Object = MibTableColumn
ltp8xONTConfigAllocProfile6 = _Ltp8xONTConfigAllocProfile6_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 4, 1, 29),
    _Ltp8xONTConfigAllocProfile6_Type()
)
ltp8xONTConfigAllocProfile6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTConfigAllocProfile6.setStatus("current")
_Ltp8xONTConfigAllocProfile7_Type = Unsigned32
_Ltp8xONTConfigAllocProfile7_Object = MibTableColumn
ltp8xONTConfigAllocProfile7 = _Ltp8xONTConfigAllocProfile7_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 4, 1, 30),
    _Ltp8xONTConfigAllocProfile7_Type()
)
ltp8xONTConfigAllocProfile7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTConfigAllocProfile7.setStatus("current")
_Ltp8xONTConfigPortsProfile_Type = Unsigned32
_Ltp8xONTConfigPortsProfile_Object = MibTableColumn
ltp8xONTConfigPortsProfile = _Ltp8xONTConfigPortsProfile_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 4, 1, 31),
    _Ltp8xONTConfigPortsProfile_Type()
)
ltp8xONTConfigPortsProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTConfigPortsProfile.setStatus("current")


class _Ltp8xONTConfigRFPortEnabled_Type(Integer32):
    """Custom type ltp8xONTConfigRFPortEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("noChange", 2))
    )


_Ltp8xONTConfigRFPortEnabled_Type.__name__ = "Integer32"
_Ltp8xONTConfigRFPortEnabled_Object = MibTableColumn
ltp8xONTConfigRFPortEnabled = _Ltp8xONTConfigRFPortEnabled_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 4, 1, 32),
    _Ltp8xONTConfigRFPortEnabled_Type()
)
ltp8xONTConfigRFPortEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTConfigRFPortEnabled.setStatus("current")
_Ltp8xONTConfigHostControlledOMCI_Type = TruthValue
_Ltp8xONTConfigHostControlledOMCI_Object = MibTableColumn
ltp8xONTConfigHostControlledOMCI = _Ltp8xONTConfigHostControlledOMCI_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 4, 1, 33),
    _Ltp8xONTConfigHostControlledOMCI_Type()
)
ltp8xONTConfigHostControlledOMCI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTConfigHostControlledOMCI.setStatus("deprecated")
_Ltp8xONTConfigVoiceProfile_Type = Unsigned32
_Ltp8xONTConfigVoiceProfile_Object = MibTableColumn
ltp8xONTConfigVoiceProfile = _Ltp8xONTConfigVoiceProfile_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 4, 1, 34),
    _Ltp8xONTConfigVoiceProfile_Type()
)
ltp8xONTConfigVoiceProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTConfigVoiceProfile.setStatus("current")
_Ltp8xONTConfigEnabled_Type = TruthValue
_Ltp8xONTConfigEnabled_Object = MibTableColumn
ltp8xONTConfigEnabled = _Ltp8xONTConfigEnabled_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 4, 1, 35),
    _Ltp8xONTConfigEnabled_Type()
)
ltp8xONTConfigEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTConfigEnabled.setStatus("current")
_Ltp8xONTConfigScriptingProfile_Type = Unsigned32
_Ltp8xONTConfigScriptingProfile_Object = MibTableColumn
ltp8xONTConfigScriptingProfile = _Ltp8xONTConfigScriptingProfile_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 4, 1, 36),
    _Ltp8xONTConfigScriptingProfile_Type()
)
ltp8xONTConfigScriptingProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTConfigScriptingProfile.setStatus("current")
_Ltp8xONTConfigBerInterval_Type = Unsigned32
_Ltp8xONTConfigBerInterval_Object = MibTableColumn
ltp8xONTConfigBerInterval = _Ltp8xONTConfigBerInterval_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 4, 1, 37),
    _Ltp8xONTConfigBerInterval_Type()
)
ltp8xONTConfigBerInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTConfigBerInterval.setStatus("current")
_Ltp8xONTConfigBerUpdatePeriod_Type = Unsigned32
_Ltp8xONTConfigBerUpdatePeriod_Object = MibTableColumn
ltp8xONTConfigBerUpdatePeriod = _Ltp8xONTConfigBerUpdatePeriod_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 4, 1, 38),
    _Ltp8xONTConfigBerUpdatePeriod_Type()
)
ltp8xONTConfigBerUpdatePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTConfigBerUpdatePeriod.setStatus("current")
_Ltp8xONTConfigOMCIErrorTolerant_Type = TruthValue
_Ltp8xONTConfigOMCIErrorTolerant_Object = MibTableColumn
ltp8xONTConfigOMCIErrorTolerant = _Ltp8xONTConfigOMCIErrorTolerant_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 4, 1, 39),
    _Ltp8xONTConfigOMCIErrorTolerant_Type()
)
ltp8xONTConfigOMCIErrorTolerant.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTConfigOMCIErrorTolerant.setStatus("current")


class _Ltp8xONTConfigCustomModel_Type(Integer32):
    """Custom type ltp8xONTConfigCustomModel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", 4),
          ("script", 3))
    )


_Ltp8xONTConfigCustomModel_Type.__name__ = "Integer32"
_Ltp8xONTConfigCustomModel_Object = MibTableColumn
ltp8xONTConfigCustomModel = _Ltp8xONTConfigCustomModel_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 4, 1, 40),
    _Ltp8xONTConfigCustomModel_Type()
)
ltp8xONTConfigCustomModel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTConfigCustomModel.setStatus("current")
_Ltp8xONTConfigEMSProfile_Type = Unsigned32
_Ltp8xONTConfigEMSProfile_Object = MibTableColumn
ltp8xONTConfigEMSProfile = _Ltp8xONTConfigEMSProfile_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 4, 1, 41),
    _Ltp8xONTConfigEMSProfile_Type()
)
ltp8xONTConfigEMSProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTConfigEMSProfile.setStatus("current")
_Ltp8xONTConfigBandwidthManagementACSProfile_Type = Unsigned32
_Ltp8xONTConfigBandwidthManagementACSProfile_Object = MibTableColumn
ltp8xONTConfigBandwidthManagementACSProfile = _Ltp8xONTConfigBandwidthManagementACSProfile_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 4, 1, 42),
    _Ltp8xONTConfigBandwidthManagementACSProfile_Type()
)
ltp8xONTConfigBandwidthManagementACSProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTConfigBandwidthManagementACSProfile.setStatus("current")
_Ltp8xONTConfigTemplate_Type = Unsigned32
_Ltp8xONTConfigTemplate_Object = MibTableColumn
ltp8xONTConfigTemplate = _Ltp8xONTConfigTemplate_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 4, 1, 43),
    _Ltp8xONTConfigTemplate_Type()
)
ltp8xONTConfigTemplate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTConfigTemplate.setStatus("current")
_Ltp8xONTServiceOverrideTable_Object = MibTable
ltp8xONTServiceOverrideTable = _Ltp8xONTServiceOverrideTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 5)
)
if mibBuilder.loadTexts:
    ltp8xONTServiceOverrideTable.setStatus("deprecated")
_Ltp8xONTServiceOverrideEntry_Object = MibTableRow
ltp8xONTServiceOverrideEntry = _Ltp8xONTServiceOverrideEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 5, 1)
)
ltp8xONTServiceOverrideEntry.setIndexNames(
    (0, "ELTEX-LTP8X", "ltp8xONTServiceOverrideID"),
    (0, "ELTEX-LTP8X", "ltp8xONTServiceOverrideSlot"),
    (0, "ELTEX-LTP8X", "ltp8xONTServiceOverrideSerial"),
)
if mibBuilder.loadTexts:
    ltp8xONTServiceOverrideEntry.setStatus("current")
_Ltp8xONTServiceOverrideID_Type = Unsigned32
_Ltp8xONTServiceOverrideID_Object = MibTableColumn
ltp8xONTServiceOverrideID = _Ltp8xONTServiceOverrideID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 5, 1, 1),
    _Ltp8xONTServiceOverrideID_Type()
)
ltp8xONTServiceOverrideID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTServiceOverrideID.setStatus("current")
_Ltp8xONTServiceOverrideSlot_Type = Unsigned32
_Ltp8xONTServiceOverrideSlot_Object = MibTableColumn
ltp8xONTServiceOverrideSlot = _Ltp8xONTServiceOverrideSlot_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 5, 1, 2),
    _Ltp8xONTServiceOverrideSlot_Type()
)
ltp8xONTServiceOverrideSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTServiceOverrideSlot.setStatus("current")
_Ltp8xONTServiceOverrideSerial_Type = ONTSerial
_Ltp8xONTServiceOverrideSerial_Object = MibTableColumn
ltp8xONTServiceOverrideSerial = _Ltp8xONTServiceOverrideSerial_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 5, 1, 3),
    _Ltp8xONTServiceOverrideSerial_Type()
)
ltp8xONTServiceOverrideSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTServiceOverrideSerial.setStatus("current")
_Ltp8xONTServiceOverrideEnabled_Type = TruthValue
_Ltp8xONTServiceOverrideEnabled_Object = MibTableColumn
ltp8xONTServiceOverrideEnabled = _Ltp8xONTServiceOverrideEnabled_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 5, 1, 4),
    _Ltp8xONTServiceOverrideEnabled_Type()
)
ltp8xONTServiceOverrideEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTServiceOverrideEnabled.setStatus("current")
_Ltp8xONTServiceOverrideCustomerVID_Type = Unsigned32
_Ltp8xONTServiceOverrideCustomerVID_Object = MibTableColumn
ltp8xONTServiceOverrideCustomerVID = _Ltp8xONTServiceOverrideCustomerVID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 5, 1, 5),
    _Ltp8xONTServiceOverrideCustomerVID_Type()
)
ltp8xONTServiceOverrideCustomerVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTServiceOverrideCustomerVID.setStatus("current")
_Ltp8xONTServiceOverrideCustomerCOS_Type = Unsigned32
_Ltp8xONTServiceOverrideCustomerCOS_Object = MibTableColumn
ltp8xONTServiceOverrideCustomerCOS = _Ltp8xONTServiceOverrideCustomerCOS_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 5, 1, 6),
    _Ltp8xONTServiceOverrideCustomerCOS_Type()
)
ltp8xONTServiceOverrideCustomerCOS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTServiceOverrideCustomerCOS.setStatus("deprecated")
_Ltp8xONTManagementProfileTable_Object = MibTable
ltp8xONTManagementProfileTable = _Ltp8xONTManagementProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 6)
)
if mibBuilder.loadTexts:
    ltp8xONTManagementProfileTable.setStatus("current")
_Ltp8xONTManagementProfileEntry_Object = MibTableRow
ltp8xONTManagementProfileEntry = _Ltp8xONTManagementProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 6, 1)
)
ltp8xONTManagementProfileEntry.setIndexNames(
    (0, "ELTEX-LTP8X", "ltp8xONTManagementID"),
)
if mibBuilder.loadTexts:
    ltp8xONTManagementProfileEntry.setStatus("current")
_Ltp8xONTManagementID_Type = Unsigned32
_Ltp8xONTManagementID_Object = MibTableColumn
ltp8xONTManagementID = _Ltp8xONTManagementID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 6, 1, 1),
    _Ltp8xONTManagementID_Type()
)
ltp8xONTManagementID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTManagementID.setStatus("current")
_Ltp8xONTManagementDescription_Type = DisplayString
_Ltp8xONTManagementDescription_Object = MibTableColumn
ltp8xONTManagementDescription = _Ltp8xONTManagementDescription_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 6, 1, 2),
    _Ltp8xONTManagementDescription_Type()
)
ltp8xONTManagementDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTManagementDescription.setStatus("current")
_Ltp8xONTManagementName_Type = DisplayString
_Ltp8xONTManagementName_Object = MibTableColumn
ltp8xONTManagementName = _Ltp8xONTManagementName_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 6, 1, 3),
    _Ltp8xONTManagementName_Type()
)
ltp8xONTManagementName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTManagementName.setStatus("current")
_Ltp8xONTManagementCrossConnect_Type = Unsigned32
_Ltp8xONTManagementCrossConnect_Object = MibTableColumn
ltp8xONTManagementCrossConnect = _Ltp8xONTManagementCrossConnect_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 6, 1, 4),
    _Ltp8xONTManagementCrossConnect_Type()
)
ltp8xONTManagementCrossConnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTManagementCrossConnect.setStatus("current")
_Ltp8xONTManagementURL_Type = DisplayString
_Ltp8xONTManagementURL_Object = MibTableColumn
ltp8xONTManagementURL = _Ltp8xONTManagementURL_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 6, 1, 5),
    _Ltp8xONTManagementURL_Type()
)
ltp8xONTManagementURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTManagementURL.setStatus("current")
_Ltp8xONTManagementUsername_Type = DisplayString
_Ltp8xONTManagementUsername_Object = MibTableColumn
ltp8xONTManagementUsername = _Ltp8xONTManagementUsername_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 6, 1, 6),
    _Ltp8xONTManagementUsername_Type()
)
ltp8xONTManagementUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTManagementUsername.setStatus("current")
_Ltp8xONTManagementPassword_Type = DisplayString
_Ltp8xONTManagementPassword_Object = MibTableColumn
ltp8xONTManagementPassword = _Ltp8xONTManagementPassword_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 6, 1, 7),
    _Ltp8xONTManagementPassword_Type()
)
ltp8xONTManagementPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTManagementPassword.setStatus("current")
_Ltp8xONTManagementOMCIConfiguration_Type = TruthValue
_Ltp8xONTManagementOMCIConfiguration_Object = MibTableColumn
ltp8xONTManagementOMCIConfiguration = _Ltp8xONTManagementOMCIConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 6, 1, 8),
    _Ltp8xONTManagementOMCIConfiguration_Type()
)
ltp8xONTManagementOMCIConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTManagementOMCIConfiguration.setStatus("current")
_Ltp8xONTManagementRowStatus_Type = RowStatus
_Ltp8xONTManagementRowStatus_Object = MibTableColumn
ltp8xONTManagementRowStatus = _Ltp8xONTManagementRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 6, 1, 20),
    _Ltp8xONTManagementRowStatus_Type()
)
ltp8xONTManagementRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTManagementRowStatus.setStatus("current")
_Ltp8xONTMulticastProfileTable_Object = MibTable
ltp8xONTMulticastProfileTable = _Ltp8xONTMulticastProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 7)
)
if mibBuilder.loadTexts:
    ltp8xONTMulticastProfileTable.setStatus("current")
_Ltp8xONTMulticastProfileEntry_Object = MibTableRow
ltp8xONTMulticastProfileEntry = _Ltp8xONTMulticastProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 7, 1)
)
ltp8xONTMulticastProfileEntry.setIndexNames(
    (0, "ELTEX-LTP8X", "ltp8xONTMulticastID"),
)
if mibBuilder.loadTexts:
    ltp8xONTMulticastProfileEntry.setStatus("current")
_Ltp8xONTMulticastID_Type = Unsigned32
_Ltp8xONTMulticastID_Object = MibTableColumn
ltp8xONTMulticastID = _Ltp8xONTMulticastID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 7, 1, 1),
    _Ltp8xONTMulticastID_Type()
)
ltp8xONTMulticastID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTMulticastID.setStatus("current")
_Ltp8xONTMulticastDescription_Type = DisplayString
_Ltp8xONTMulticastDescription_Object = MibTableColumn
ltp8xONTMulticastDescription = _Ltp8xONTMulticastDescription_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 7, 1, 2),
    _Ltp8xONTMulticastDescription_Type()
)
ltp8xONTMulticastDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTMulticastDescription.setStatus("current")
_Ltp8xONTMulticastName_Type = DisplayString
_Ltp8xONTMulticastName_Object = MibTableColumn
ltp8xONTMulticastName = _Ltp8xONTMulticastName_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 7, 1, 3),
    _Ltp8xONTMulticastName_Type()
)
ltp8xONTMulticastName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTMulticastName.setStatus("current")
_Ltp8xONTServicesProfileTable_Object = MibTable
ltp8xONTServicesProfileTable = _Ltp8xONTServicesProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 8)
)
if mibBuilder.loadTexts:
    ltp8xONTServicesProfileTable.setStatus("deprecated")
_Ltp8xONTServicesProfileEntry_Object = MibTableRow
ltp8xONTServicesProfileEntry = _Ltp8xONTServicesProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 8, 1)
)
ltp8xONTServicesProfileEntry.setIndexNames(
    (0, "ELTEX-LTP8X", "ltp8xONTServicesID"),
)
if mibBuilder.loadTexts:
    ltp8xONTServicesProfileEntry.setStatus("current")
_Ltp8xONTServicesID_Type = Unsigned32
_Ltp8xONTServicesID_Object = MibTableColumn
ltp8xONTServicesID = _Ltp8xONTServicesID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 8, 1, 1),
    _Ltp8xONTServicesID_Type()
)
ltp8xONTServicesID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTServicesID.setStatus("current")
_Ltp8xONTServicesDescription_Type = DisplayString
_Ltp8xONTServicesDescription_Object = MibTableColumn
ltp8xONTServicesDescription = _Ltp8xONTServicesDescription_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 8, 1, 2),
    _Ltp8xONTServicesDescription_Type()
)
ltp8xONTServicesDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTServicesDescription.setStatus("current")
_Ltp8xONTServicesName_Type = DisplayString
_Ltp8xONTServicesName_Object = MibTableColumn
ltp8xONTServicesName = _Ltp8xONTServicesName_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 8, 1, 3),
    _Ltp8xONTServicesName_Type()
)
ltp8xONTServicesName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTServicesName.setStatus("current")
_Ltp8xONTCrossConnectProfileTable_Object = MibTable
ltp8xONTCrossConnectProfileTable = _Ltp8xONTCrossConnectProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 9)
)
if mibBuilder.loadTexts:
    ltp8xONTCrossConnectProfileTable.setStatus("current")
_Ltp8xONTCrossConnectProfileEntry_Object = MibTableRow
ltp8xONTCrossConnectProfileEntry = _Ltp8xONTCrossConnectProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 9, 1)
)
ltp8xONTCrossConnectProfileEntry.setIndexNames(
    (0, "ELTEX-LTP8X", "ltp8xONTCrossConnectID"),
)
if mibBuilder.loadTexts:
    ltp8xONTCrossConnectProfileEntry.setStatus("current")
_Ltp8xONTCrossConnectID_Type = Unsigned32
_Ltp8xONTCrossConnectID_Object = MibTableColumn
ltp8xONTCrossConnectID = _Ltp8xONTCrossConnectID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 9, 1, 1),
    _Ltp8xONTCrossConnectID_Type()
)
ltp8xONTCrossConnectID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTCrossConnectID.setStatus("current")
_Ltp8xONTCrossConnectDescription_Type = DisplayString
_Ltp8xONTCrossConnectDescription_Object = MibTableColumn
ltp8xONTCrossConnectDescription = _Ltp8xONTCrossConnectDescription_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 9, 1, 2),
    _Ltp8xONTCrossConnectDescription_Type()
)
ltp8xONTCrossConnectDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTCrossConnectDescription.setStatus("current")
_Ltp8xONTCrossConnectName_Type = DisplayString
_Ltp8xONTCrossConnectName_Object = MibTableColumn
ltp8xONTCrossConnectName = _Ltp8xONTCrossConnectName_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 9, 1, 3),
    _Ltp8xONTCrossConnectName_Type()
)
ltp8xONTCrossConnectName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTCrossConnectName.setStatus("current")


class _Ltp8xONTCrossConnectModel_Type(Integer32):
    """Custom type ltp8xONTCrossConnectModel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ont", 1),
          ("ontRg", 0))
    )


_Ltp8xONTCrossConnectModel_Type.__name__ = "Integer32"
_Ltp8xONTCrossConnectModel_Object = MibTableColumn
ltp8xONTCrossConnectModel = _Ltp8xONTCrossConnectModel_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 9, 1, 4),
    _Ltp8xONTCrossConnectModel_Type()
)
ltp8xONTCrossConnectModel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTCrossConnectModel.setStatus("current")
_Ltp8xONTCrossConnectBridgeGroup_Type = Unsigned32
_Ltp8xONTCrossConnectBridgeGroup_Object = MibTableColumn
ltp8xONTCrossConnectBridgeGroup = _Ltp8xONTCrossConnectBridgeGroup_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 9, 1, 5),
    _Ltp8xONTCrossConnectBridgeGroup_Type()
)
ltp8xONTCrossConnectBridgeGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTCrossConnectBridgeGroup.setStatus("current")


class _Ltp8xONTCrossConnectTagMode_Type(Integer32):
    """Custom type ltp8xONTCrossConnectTagMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("doubleTagged", 1),
          ("singleTagged", 0))
    )


_Ltp8xONTCrossConnectTagMode_Type.__name__ = "Integer32"
_Ltp8xONTCrossConnectTagMode_Object = MibTableColumn
ltp8xONTCrossConnectTagMode = _Ltp8xONTCrossConnectTagMode_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 9, 1, 6),
    _Ltp8xONTCrossConnectTagMode_Type()
)
ltp8xONTCrossConnectTagMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTCrossConnectTagMode.setStatus("current")


class _Ltp8xONTCrossConnectOuterVID_Type(Integer32):
    """Custom type ltp8xONTCrossConnectOuterVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            65535
        )
    )
    namedValues = NamedValues(
        ("auto", 65535)
    )


_Ltp8xONTCrossConnectOuterVID_Type.__name__ = "Integer32"
_Ltp8xONTCrossConnectOuterVID_Object = MibTableColumn
ltp8xONTCrossConnectOuterVID = _Ltp8xONTCrossConnectOuterVID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 9, 1, 7),
    _Ltp8xONTCrossConnectOuterVID_Type()
)
ltp8xONTCrossConnectOuterVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTCrossConnectOuterVID.setStatus("current")


class _Ltp8xONTCrossConnectOuterCOS_Type(Integer32):
    """Custom type ltp8xONTCrossConnectOuterCOS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            255
        )
    )
    namedValues = NamedValues(
        ("unused", 255)
    )


_Ltp8xONTCrossConnectOuterCOS_Type.__name__ = "Integer32"
_Ltp8xONTCrossConnectOuterCOS_Object = MibTableColumn
ltp8xONTCrossConnectOuterCOS = _Ltp8xONTCrossConnectOuterCOS_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 9, 1, 8),
    _Ltp8xONTCrossConnectOuterCOS_Type()
)
ltp8xONTCrossConnectOuterCOS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTCrossConnectOuterCOS.setStatus("current")


class _Ltp8xONTCrossConnectInnerVID_Type(Integer32):
    """Custom type ltp8xONTCrossConnectInnerVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            65535
        )
    )
    namedValues = NamedValues(
        ("auto", 65535)
    )


_Ltp8xONTCrossConnectInnerVID_Type.__name__ = "Integer32"
_Ltp8xONTCrossConnectInnerVID_Object = MibTableColumn
ltp8xONTCrossConnectInnerVID = _Ltp8xONTCrossConnectInnerVID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 9, 1, 9),
    _Ltp8xONTCrossConnectInnerVID_Type()
)
ltp8xONTCrossConnectInnerVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTCrossConnectInnerVID.setStatus("current")


class _Ltp8xONTCrossConnectUVID_Type(Integer32):
    """Custom type ltp8xONTCrossConnectUVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            65535
        )
    )
    namedValues = NamedValues(
        ("auto", 65535)
    )


_Ltp8xONTCrossConnectUVID_Type.__name__ = "Integer32"
_Ltp8xONTCrossConnectUVID_Object = MibTableColumn
ltp8xONTCrossConnectUVID = _Ltp8xONTCrossConnectUVID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 9, 1, 10),
    _Ltp8xONTCrossConnectUVID_Type()
)
ltp8xONTCrossConnectUVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTCrossConnectUVID.setStatus("current")


class _Ltp8xONTCrossConnectUCOS_Type(Integer32):
    """Custom type ltp8xONTCrossConnectUCOS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            255
        )
    )
    namedValues = NamedValues(
        ("unused", 255)
    )


_Ltp8xONTCrossConnectUCOS_Type.__name__ = "Integer32"
_Ltp8xONTCrossConnectUCOS_Object = MibTableColumn
ltp8xONTCrossConnectUCOS = _Ltp8xONTCrossConnectUCOS_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 9, 1, 11),
    _Ltp8xONTCrossConnectUCOS_Type()
)
ltp8xONTCrossConnectUCOS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTCrossConnectUCOS.setStatus("current")


class _Ltp8xONTCrossConnectMacTableEntryLimit_Type(Integer32):
    """Custom type ltp8xONTCrossConnectMacTableEntryLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            127
        )
    )
    namedValues = NamedValues(
        ("unlimited", 127)
    )


_Ltp8xONTCrossConnectMacTableEntryLimit_Type.__name__ = "Integer32"
_Ltp8xONTCrossConnectMacTableEntryLimit_Object = MibTableColumn
ltp8xONTCrossConnectMacTableEntryLimit = _Ltp8xONTCrossConnectMacTableEntryLimit_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 9, 1, 12),
    _Ltp8xONTCrossConnectMacTableEntryLimit_Type()
)
ltp8xONTCrossConnectMacTableEntryLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTCrossConnectMacTableEntryLimit.setStatus("current")


class _Ltp8xONTCrossConnectType_Type(Integer32):
    """Custom type ltp8xONTCrossConnectType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("general", 0),
          ("management", 2),
          ("multicast", 1),
          ("voice", 3))
    )


_Ltp8xONTCrossConnectType_Type.__name__ = "Integer32"
_Ltp8xONTCrossConnectType_Object = MibTableColumn
ltp8xONTCrossConnectType = _Ltp8xONTCrossConnectType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 9, 1, 13),
    _Ltp8xONTCrossConnectType_Type()
)
ltp8xONTCrossConnectType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTCrossConnectType.setStatus("current")
_Ltp8xONTCrossConnectIphostEid_Type = Integer32
_Ltp8xONTCrossConnectIphostEid_Object = MibTableColumn
ltp8xONTCrossConnectIphostEid = _Ltp8xONTCrossConnectIphostEid_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 9, 1, 14),
    _Ltp8xONTCrossConnectIphostEid_Type()
)
ltp8xONTCrossConnectIphostEid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTCrossConnectIphostEid.setStatus("current")
_Ltp8xONTCrossConnectPriorityQueue_Type = Unsigned32
_Ltp8xONTCrossConnectPriorityQueue_Object = MibTableColumn
ltp8xONTCrossConnectPriorityQueue = _Ltp8xONTCrossConnectPriorityQueue_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 9, 1, 15),
    _Ltp8xONTCrossConnectPriorityQueue_Type()
)
ltp8xONTCrossConnectPriorityQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTCrossConnectPriorityQueue.setStatus("current")
_Ltp8xONTCrossConnectRowStatus_Type = RowStatus
_Ltp8xONTCrossConnectRowStatus_Object = MibTableColumn
ltp8xONTCrossConnectRowStatus = _Ltp8xONTCrossConnectRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 9, 1, 20),
    _Ltp8xONTCrossConnectRowStatus_Type()
)
ltp8xONTCrossConnectRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTCrossConnectRowStatus.setStatus("current")
_Ltp8xONTMulticastGroupsTable_Object = MibTable
ltp8xONTMulticastGroupsTable = _Ltp8xONTMulticastGroupsTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 10)
)
if mibBuilder.loadTexts:
    ltp8xONTMulticastGroupsTable.setStatus("current")
_Ltp8xONTMulticastGroupsEntry_Object = MibTableRow
ltp8xONTMulticastGroupsEntry = _Ltp8xONTMulticastGroupsEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 10, 1)
)
ltp8xONTMulticastGroupsEntry.setIndexNames(
    (0, "ELTEX-LTP8X", "ltp8xONTMulticastGroupsSlot"),
    (0, "ELTEX-LTP8X", "ltp8xONTMulticastGroupsSerial"),
    (0, "ELTEX-LTP8X", "ltp8xONTMulticastGroupsEntryID"),
)
if mibBuilder.loadTexts:
    ltp8xONTMulticastGroupsEntry.setStatus("current")
_Ltp8xONTMulticastGroupsSlot_Type = Unsigned32
_Ltp8xONTMulticastGroupsSlot_Object = MibTableColumn
ltp8xONTMulticastGroupsSlot = _Ltp8xONTMulticastGroupsSlot_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 10, 1, 1),
    _Ltp8xONTMulticastGroupsSlot_Type()
)
ltp8xONTMulticastGroupsSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTMulticastGroupsSlot.setStatus("current")
_Ltp8xONTMulticastGroupsSerial_Type = ONTSerial
_Ltp8xONTMulticastGroupsSerial_Object = MibTableColumn
ltp8xONTMulticastGroupsSerial = _Ltp8xONTMulticastGroupsSerial_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 10, 1, 2),
    _Ltp8xONTMulticastGroupsSerial_Type()
)
ltp8xONTMulticastGroupsSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTMulticastGroupsSerial.setStatus("current")
_Ltp8xONTMulticastGroupsEntryID_Type = Unsigned32
_Ltp8xONTMulticastGroupsEntryID_Object = MibTableColumn
ltp8xONTMulticastGroupsEntryID = _Ltp8xONTMulticastGroupsEntryID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 10, 1, 3),
    _Ltp8xONTMulticastGroupsEntryID_Type()
)
ltp8xONTMulticastGroupsEntryID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTMulticastGroupsEntryID.setStatus("current")
_Ltp8xONTMulticastGroupsVLAN_Type = Unsigned32
_Ltp8xONTMulticastGroupsVLAN_Object = MibTableColumn
ltp8xONTMulticastGroupsVLAN = _Ltp8xONTMulticastGroupsVLAN_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 10, 1, 4),
    _Ltp8xONTMulticastGroupsVLAN_Type()
)
ltp8xONTMulticastGroupsVLAN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTMulticastGroupsVLAN.setStatus("current")
_Ltp8xONTMulticastGroupsSourceIP_Type = IpAddress
_Ltp8xONTMulticastGroupsSourceIP_Object = MibTableColumn
ltp8xONTMulticastGroupsSourceIP = _Ltp8xONTMulticastGroupsSourceIP_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 10, 1, 5),
    _Ltp8xONTMulticastGroupsSourceIP_Type()
)
ltp8xONTMulticastGroupsSourceIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTMulticastGroupsSourceIP.setStatus("current")
_Ltp8xONTMulticastGroupsDestIP_Type = IpAddress
_Ltp8xONTMulticastGroupsDestIP_Object = MibTableColumn
ltp8xONTMulticastGroupsDestIP = _Ltp8xONTMulticastGroupsDestIP_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 10, 1, 6),
    _Ltp8xONTMulticastGroupsDestIP_Type()
)
ltp8xONTMulticastGroupsDestIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTMulticastGroupsDestIP.setStatus("current")
_Ltp8xONTMulticastGroupsBEBandwidth_Type = Unsigned32
_Ltp8xONTMulticastGroupsBEBandwidth_Object = MibTableColumn
ltp8xONTMulticastGroupsBEBandwidth = _Ltp8xONTMulticastGroupsBEBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 10, 1, 7),
    _Ltp8xONTMulticastGroupsBEBandwidth_Type()
)
ltp8xONTMulticastGroupsBEBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTMulticastGroupsBEBandwidth.setStatus("current")
_Ltp8xONTMulticastGroupsClientIP_Type = IpAddress
_Ltp8xONTMulticastGroupsClientIP_Object = MibTableColumn
ltp8xONTMulticastGroupsClientIP = _Ltp8xONTMulticastGroupsClientIP_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 10, 1, 8),
    _Ltp8xONTMulticastGroupsClientIP_Type()
)
ltp8xONTMulticastGroupsClientIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTMulticastGroupsClientIP.setStatus("current")
_Ltp8xONTMulticastGroupsRecentJoinTime_Type = TimeTicks
_Ltp8xONTMulticastGroupsRecentJoinTime_Object = MibTableColumn
ltp8xONTMulticastGroupsRecentJoinTime = _Ltp8xONTMulticastGroupsRecentJoinTime_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 10, 1, 9),
    _Ltp8xONTMulticastGroupsRecentJoinTime_Type()
)
ltp8xONTMulticastGroupsRecentJoinTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTMulticastGroupsRecentJoinTime.setStatus("current")
_Ltp8xONTBufferZoneTable_Object = MibTable
ltp8xONTBufferZoneTable = _Ltp8xONTBufferZoneTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 11)
)
if mibBuilder.loadTexts:
    ltp8xONTBufferZoneTable.setStatus("current")
_Ltp8xONTBufferZoneEntry_Object = MibTableRow
ltp8xONTBufferZoneEntry = _Ltp8xONTBufferZoneEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 11, 1)
)
ltp8xONTBufferZoneEntry.setIndexNames(
    (0, "ELTEX-LTP8X", "ltp8xONTBufferZoneValue"),
)
if mibBuilder.loadTexts:
    ltp8xONTBufferZoneEntry.setStatus("current")
_Ltp8xONTBufferZoneValue_Type = Unsigned32
_Ltp8xONTBufferZoneValue_Object = MibTableColumn
ltp8xONTBufferZoneValue = _Ltp8xONTBufferZoneValue_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 11, 1, 1),
    _Ltp8xONTBufferZoneValue_Type()
)
ltp8xONTBufferZoneValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTBufferZoneValue.setStatus("current")
_Ltp8xONTAddressTable_Object = MibTable
ltp8xONTAddressTable = _Ltp8xONTAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 12)
)
if mibBuilder.loadTexts:
    ltp8xONTAddressTable.setStatus("current")
_Ltp8xONTAddressEntry_Object = MibTableRow
ltp8xONTAddressEntry = _Ltp8xONTAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 12, 1)
)
ltp8xONTAddressEntry.setIndexNames(
    (0, "ELTEX-LTP8X", "ltp8xONTAddressSlot"),
    (0, "ELTEX-LTP8X", "ltp8xONTAddressSerial"),
    (0, "ELTEX-LTP8X", "ltp8xONTAddressEntryID"),
)
if mibBuilder.loadTexts:
    ltp8xONTAddressEntry.setStatus("current")
_Ltp8xONTAddressSlot_Type = Unsigned32
_Ltp8xONTAddressSlot_Object = MibTableColumn
ltp8xONTAddressSlot = _Ltp8xONTAddressSlot_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 12, 1, 1),
    _Ltp8xONTAddressSlot_Type()
)
ltp8xONTAddressSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTAddressSlot.setStatus("current")
_Ltp8xONTAddressSerial_Type = ONTSerial
_Ltp8xONTAddressSerial_Object = MibTableColumn
ltp8xONTAddressSerial = _Ltp8xONTAddressSerial_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 12, 1, 2),
    _Ltp8xONTAddressSerial_Type()
)
ltp8xONTAddressSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTAddressSerial.setStatus("current")
_Ltp8xONTAddressEntryID_Type = Unsigned32
_Ltp8xONTAddressEntryID_Object = MibTableColumn
ltp8xONTAddressEntryID = _Ltp8xONTAddressEntryID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 12, 1, 3),
    _Ltp8xONTAddressEntryID_Type()
)
ltp8xONTAddressEntryID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTAddressEntryID.setStatus("current")
_Ltp8xONTAddressPriority_Type = Integer32
_Ltp8xONTAddressPriority_Object = MibTableColumn
ltp8xONTAddressPriority = _Ltp8xONTAddressPriority_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 12, 1, 4),
    _Ltp8xONTAddressPriority_Type()
)
ltp8xONTAddressPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTAddressPriority.setStatus("current")
_Ltp8xONTAddressCVID_Type = Integer32
_Ltp8xONTAddressCVID_Object = MibTableColumn
ltp8xONTAddressCVID = _Ltp8xONTAddressCVID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 12, 1, 5),
    _Ltp8xONTAddressCVID_Type()
)
ltp8xONTAddressCVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTAddressCVID.setStatus("current")
_Ltp8xONTAddressSVID_Type = Integer32
_Ltp8xONTAddressSVID_Object = MibTableColumn
ltp8xONTAddressSVID = _Ltp8xONTAddressSVID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 12, 1, 6),
    _Ltp8xONTAddressSVID_Type()
)
ltp8xONTAddressSVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTAddressSVID.setStatus("current")
_Ltp8xONTAddressMacAddress_Type = MacAddress
_Ltp8xONTAddressMacAddress_Object = MibTableColumn
ltp8xONTAddressMacAddress = _Ltp8xONTAddressMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 12, 1, 7),
    _Ltp8xONTAddressMacAddress_Type()
)
ltp8xONTAddressMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTAddressMacAddress.setStatus("current")
_Ltp8xONTAddressCPUDestined_Type = TruthValue
_Ltp8xONTAddressCPUDestined_Object = MibTableColumn
ltp8xONTAddressCPUDestined = _Ltp8xONTAddressCPUDestined_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 12, 1, 8),
    _Ltp8xONTAddressCPUDestined_Type()
)
ltp8xONTAddressCPUDestined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTAddressCPUDestined.setStatus("current")
_Ltp8xONTAddressDatapathForwarding_Type = TruthValue
_Ltp8xONTAddressDatapathForwarding_Object = MibTableColumn
ltp8xONTAddressDatapathForwarding = _Ltp8xONTAddressDatapathForwarding_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 12, 1, 9),
    _Ltp8xONTAddressDatapathForwarding_Type()
)
ltp8xONTAddressDatapathForwarding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTAddressDatapathForwarding.setStatus("current")
_Ltp8xONTAddressUniPort_Type = Unsigned32
_Ltp8xONTAddressUniPort_Object = MibTableColumn
ltp8xONTAddressUniPort = _Ltp8xONTAddressUniPort_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 12, 1, 10),
    _Ltp8xONTAddressUniPort_Type()
)
ltp8xONTAddressUniPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTAddressUniPort.setStatus("current")
_Ltp8xONTAddressEntryType_Type = AddressEntryType
_Ltp8xONTAddressEntryType_Object = MibTableColumn
ltp8xONTAddressEntryType = _Ltp8xONTAddressEntryType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 12, 1, 11),
    _Ltp8xONTAddressEntryType_Type()
)
ltp8xONTAddressEntryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTAddressEntryType.setStatus("current")
_Ltp8xONTAddressAge_Type = Unsigned32
_Ltp8xONTAddressAge_Object = MibTableColumn
ltp8xONTAddressAge = _Ltp8xONTAddressAge_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 12, 1, 12),
    _Ltp8xONTAddressAge_Type()
)
ltp8xONTAddressAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTAddressAge.setStatus("current")
_Ltp8xONTAddressGEMPortId_Type = Unsigned32
_Ltp8xONTAddressGEMPortId_Object = MibTableColumn
ltp8xONTAddressGEMPortId = _Ltp8xONTAddressGEMPortId_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 12, 1, 13),
    _Ltp8xONTAddressGEMPortId_Type()
)
ltp8xONTAddressGEMPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTAddressGEMPortId.setStatus("current")
_Ltp8xONTAddressUVID_Type = Integer32
_Ltp8xONTAddressUVID_Object = MibTableColumn
ltp8xONTAddressUVID = _Ltp8xONTAddressUVID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 12, 1, 14),
    _Ltp8xONTAddressUVID_Type()
)
ltp8xONTAddressUVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTAddressUVID.setStatus("current")
_Ltp8xONTMassUpdateFirmwareTable_Object = MibTable
ltp8xONTMassUpdateFirmwareTable = _Ltp8xONTMassUpdateFirmwareTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 13)
)
if mibBuilder.loadTexts:
    ltp8xONTMassUpdateFirmwareTable.setStatus("current")
_Ltp8xONTMassUpdateFirmwareEntry_Object = MibTableRow
ltp8xONTMassUpdateFirmwareEntry = _Ltp8xONTMassUpdateFirmwareEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 13, 1)
)
ltp8xONTMassUpdateFirmwareEntry.setIndexNames(
    (0, "ELTEX-LTP8X", "ltp8xONTMassUpdateFirmwareSlot"),
)
if mibBuilder.loadTexts:
    ltp8xONTMassUpdateFirmwareEntry.setStatus("current")
_Ltp8xONTMassUpdateFirmwareSlot_Type = Unsigned32
_Ltp8xONTMassUpdateFirmwareSlot_Object = MibTableColumn
ltp8xONTMassUpdateFirmwareSlot = _Ltp8xONTMassUpdateFirmwareSlot_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 13, 1, 1),
    _Ltp8xONTMassUpdateFirmwareSlot_Type()
)
ltp8xONTMassUpdateFirmwareSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTMassUpdateFirmwareSlot.setStatus("current")
_Ltp8xONTMassUpdateFirmwareAction_Type = Unsigned32
_Ltp8xONTMassUpdateFirmwareAction_Object = MibTableColumn
ltp8xONTMassUpdateFirmwareAction = _Ltp8xONTMassUpdateFirmwareAction_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 13, 1, 2),
    _Ltp8xONTMassUpdateFirmwareAction_Type()
)
ltp8xONTMassUpdateFirmwareAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTMassUpdateFirmwareAction.setStatus("current")
_Ltp8xONTCustomCrossConnectTable_Object = MibTable
ltp8xONTCustomCrossConnectTable = _Ltp8xONTCustomCrossConnectTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 14)
)
if mibBuilder.loadTexts:
    ltp8xONTCustomCrossConnectTable.setStatus("current")
_Ltp8xONTCustomCrossConnectEntry_Object = MibTableRow
ltp8xONTCustomCrossConnectEntry = _Ltp8xONTCustomCrossConnectEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 14, 1)
)
ltp8xONTCustomCrossConnectEntry.setIndexNames(
    (0, "ELTEX-LTP8X", "ltp8xONTCustomCrossConnectSlot"),
    (0, "ELTEX-LTP8X", "ltp8xONTCustomCrossConnectSerial"),
    (0, "ELTEX-LTP8X", "ltp8xONTCustomCrossConnectID"),
)
if mibBuilder.loadTexts:
    ltp8xONTCustomCrossConnectEntry.setStatus("current")
_Ltp8xONTCustomCrossConnectSlot_Type = Unsigned32
_Ltp8xONTCustomCrossConnectSlot_Object = MibTableColumn
ltp8xONTCustomCrossConnectSlot = _Ltp8xONTCustomCrossConnectSlot_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 14, 1, 1),
    _Ltp8xONTCustomCrossConnectSlot_Type()
)
ltp8xONTCustomCrossConnectSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTCustomCrossConnectSlot.setStatus("current")
_Ltp8xONTCustomCrossConnectSerial_Type = ONTSerial
_Ltp8xONTCustomCrossConnectSerial_Object = MibTableColumn
ltp8xONTCustomCrossConnectSerial = _Ltp8xONTCustomCrossConnectSerial_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 14, 1, 2),
    _Ltp8xONTCustomCrossConnectSerial_Type()
)
ltp8xONTCustomCrossConnectSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTCustomCrossConnectSerial.setStatus("current")
_Ltp8xONTCustomCrossConnectID_Type = Unsigned32
_Ltp8xONTCustomCrossConnectID_Object = MibTableColumn
ltp8xONTCustomCrossConnectID = _Ltp8xONTCustomCrossConnectID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 14, 1, 3),
    _Ltp8xONTCustomCrossConnectID_Type()
)
ltp8xONTCustomCrossConnectID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTCustomCrossConnectID.setStatus("current")
_Ltp8xONTCustomCrossConnectEnabled_Type = TruthValue
_Ltp8xONTCustomCrossConnectEnabled_Object = MibTableColumn
ltp8xONTCustomCrossConnectEnabled = _Ltp8xONTCustomCrossConnectEnabled_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 14, 1, 4),
    _Ltp8xONTCustomCrossConnectEnabled_Type()
)
ltp8xONTCustomCrossConnectEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTCustomCrossConnectEnabled.setStatus("current")
_Ltp8xONTCustomCrossConnectVID_Type = Integer32
_Ltp8xONTCustomCrossConnectVID_Object = MibTableColumn
ltp8xONTCustomCrossConnectVID = _Ltp8xONTCustomCrossConnectVID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 14, 1, 5),
    _Ltp8xONTCustomCrossConnectVID_Type()
)
ltp8xONTCustomCrossConnectVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTCustomCrossConnectVID.setStatus("current")


class _Ltp8xONTCustomCrossConnectCOS_Type(Integer32):
    """Custom type ltp8xONTCustomCrossConnectCOS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            255
        )
    )
    namedValues = NamedValues(
        ("unused", 255)
    )


_Ltp8xONTCustomCrossConnectCOS_Type.__name__ = "Integer32"
_Ltp8xONTCustomCrossConnectCOS_Object = MibTableColumn
ltp8xONTCustomCrossConnectCOS = _Ltp8xONTCustomCrossConnectCOS_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 14, 1, 6),
    _Ltp8xONTCustomCrossConnectCOS_Type()
)
ltp8xONTCustomCrossConnectCOS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTCustomCrossConnectCOS.setStatus("current")
_Ltp8xONTCustomCrossConnectSVID_Type = Integer32
_Ltp8xONTCustomCrossConnectSVID_Object = MibTableColumn
ltp8xONTCustomCrossConnectSVID = _Ltp8xONTCustomCrossConnectSVID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 14, 1, 7),
    _Ltp8xONTCustomCrossConnectSVID_Type()
)
ltp8xONTCustomCrossConnectSVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTCustomCrossConnectSVID.setStatus("current")
_Ltp8xONTACSConfigTable_Object = MibTable
ltp8xONTACSConfigTable = _Ltp8xONTACSConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 15)
)
if mibBuilder.loadTexts:
    ltp8xONTACSConfigTable.setStatus("current")
_Ltp8xONTACSConfigEntry_Object = MibTableRow
ltp8xONTACSConfigEntry = _Ltp8xONTACSConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 15, 1)
)
ltp8xONTACSConfigEntry.setIndexNames(
    (0, "ELTEX-LTP8X", "ltp8xONTACSConfigSerial"),
)
if mibBuilder.loadTexts:
    ltp8xONTACSConfigEntry.setStatus("current")
_Ltp8xONTACSConfigSerial_Type = ONTSerial
_Ltp8xONTACSConfigSerial_Object = MibTableColumn
ltp8xONTACSConfigSerial = _Ltp8xONTACSConfigSerial_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 15, 1, 1),
    _Ltp8xONTACSConfigSerial_Type()
)
ltp8xONTACSConfigSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTACSConfigSerial.setStatus("current")
_Ltp8xONTACSUserID_Type = DisplayString
_Ltp8xONTACSUserID_Object = MibTableColumn
ltp8xONTACSUserID = _Ltp8xONTACSUserID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 15, 1, 2),
    _Ltp8xONTACSUserID_Type()
)
ltp8xONTACSUserID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTACSUserID.setStatus("current")
_Ltp8xONTACSConfigProfile_Type = DisplayString
_Ltp8xONTACSConfigProfile_Object = MibTableColumn
ltp8xONTACSConfigProfile = _Ltp8xONTACSConfigProfile_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 15, 1, 3),
    _Ltp8xONTACSConfigProfile_Type()
)
ltp8xONTACSConfigProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTACSConfigProfile.setStatus("current")
_Ltp8xONTACSConfigVoice1Enable_Type = DisplayString
_Ltp8xONTACSConfigVoice1Enable_Object = MibTableColumn
ltp8xONTACSConfigVoice1Enable = _Ltp8xONTACSConfigVoice1Enable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 15, 1, 4),
    _Ltp8xONTACSConfigVoice1Enable_Type()
)
ltp8xONTACSConfigVoice1Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTACSConfigVoice1Enable.setStatus("current")
_Ltp8xONTACSConfigVoice1Number_Type = DisplayString
_Ltp8xONTACSConfigVoice1Number_Object = MibTableColumn
ltp8xONTACSConfigVoice1Number = _Ltp8xONTACSConfigVoice1Number_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 15, 1, 5),
    _Ltp8xONTACSConfigVoice1Number_Type()
)
ltp8xONTACSConfigVoice1Number.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTACSConfigVoice1Number.setStatus("current")
_Ltp8xONTACSConfigVoice1Password_Type = DisplayString
_Ltp8xONTACSConfigVoice1Password_Object = MibTableColumn
ltp8xONTACSConfigVoice1Password = _Ltp8xONTACSConfigVoice1Password_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 15, 1, 6),
    _Ltp8xONTACSConfigVoice1Password_Type()
)
ltp8xONTACSConfigVoice1Password.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTACSConfigVoice1Password.setStatus("current")
_Ltp8xONTACSConfigVoice2Enable_Type = DisplayString
_Ltp8xONTACSConfigVoice2Enable_Object = MibTableColumn
ltp8xONTACSConfigVoice2Enable = _Ltp8xONTACSConfigVoice2Enable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 15, 1, 7),
    _Ltp8xONTACSConfigVoice2Enable_Type()
)
ltp8xONTACSConfigVoice2Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTACSConfigVoice2Enable.setStatus("current")
_Ltp8xONTACSConfigVoice2Number_Type = DisplayString
_Ltp8xONTACSConfigVoice2Number_Object = MibTableColumn
ltp8xONTACSConfigVoice2Number = _Ltp8xONTACSConfigVoice2Number_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 15, 1, 8),
    _Ltp8xONTACSConfigVoice2Number_Type()
)
ltp8xONTACSConfigVoice2Number.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTACSConfigVoice2Number.setStatus("current")
_Ltp8xONTACSConfigVoice2Password_Type = DisplayString
_Ltp8xONTACSConfigVoice2Password_Object = MibTableColumn
ltp8xONTACSConfigVoice2Password = _Ltp8xONTACSConfigVoice2Password_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 15, 1, 9),
    _Ltp8xONTACSConfigVoice2Password_Type()
)
ltp8xONTACSConfigVoice2Password.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTACSConfigVoice2Password.setStatus("current")
_Ltp8xONTACSConfigSIPProxy_Type = DisplayString
_Ltp8xONTACSConfigSIPProxy_Object = MibTableColumn
ltp8xONTACSConfigSIPProxy = _Ltp8xONTACSConfigSIPProxy_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 15, 1, 10),
    _Ltp8xONTACSConfigSIPProxy_Type()
)
ltp8xONTACSConfigSIPProxy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTACSConfigSIPProxy.setStatus("current")
_Ltp8xONTACSConfigPPPLogin_Type = DisplayString
_Ltp8xONTACSConfigPPPLogin_Object = MibTableColumn
ltp8xONTACSConfigPPPLogin = _Ltp8xONTACSConfigPPPLogin_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 15, 1, 11),
    _Ltp8xONTACSConfigPPPLogin_Type()
)
ltp8xONTACSConfigPPPLogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTACSConfigPPPLogin.setStatus("current")
_Ltp8xONTACSConfigPPPPassword_Type = DisplayString
_Ltp8xONTACSConfigPPPPassword_Object = MibTableColumn
ltp8xONTACSConfigPPPPassword = _Ltp8xONTACSConfigPPPPassword_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 15, 1, 12),
    _Ltp8xONTACSConfigPPPPassword_Type()
)
ltp8xONTACSConfigPPPPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTACSConfigPPPPassword.setStatus("current")
_Ltp8xONTACSConfigInternetVlan_Type = DisplayString
_Ltp8xONTACSConfigInternetVlan_Object = MibTableColumn
ltp8xONTACSConfigInternetVlan = _Ltp8xONTACSConfigInternetVlan_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 15, 1, 13),
    _Ltp8xONTACSConfigInternetVlan_Type()
)
ltp8xONTACSConfigInternetVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTACSConfigInternetVlan.setStatus("current")
_Ltp8xONTACSConfigResetToDefaults_Type = Unsigned32
_Ltp8xONTACSConfigResetToDefaults_Object = MibTableColumn
ltp8xONTACSConfigResetToDefaults = _Ltp8xONTACSConfigResetToDefaults_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 15, 1, 14),
    _Ltp8xONTACSConfigResetToDefaults_Type()
)
ltp8xONTACSConfigResetToDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTACSConfigResetToDefaults.setStatus("current")
_Ltp8xONTACSConfigReboot_Type = Unsigned32
_Ltp8xONTACSConfigReboot_Object = MibTableColumn
ltp8xONTACSConfigReboot = _Ltp8xONTACSConfigReboot_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 15, 1, 15),
    _Ltp8xONTACSConfigReboot_Type()
)
ltp8xONTACSConfigReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTACSConfigReboot.setStatus("current")
_Ltp8xONTACSConfigReconfigure_Type = Unsigned32
_Ltp8xONTACSConfigReconfigure_Object = MibTableColumn
ltp8xONTACSConfigReconfigure = _Ltp8xONTACSConfigReconfigure_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 15, 1, 16),
    _Ltp8xONTACSConfigReconfigure_Type()
)
ltp8xONTACSConfigReconfigure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTACSConfigReconfigure.setStatus("current")
_Ltp8xONTACSConfigDelete_Type = Unsigned32
_Ltp8xONTACSConfigDelete_Object = MibTableColumn
ltp8xONTACSConfigDelete = _Ltp8xONTACSConfigDelete_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 15, 1, 20),
    _Ltp8xONTACSConfigDelete_Type()
)
ltp8xONTACSConfigDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTACSConfigDelete.setStatus("current")
_Ltp8xONTACSProfilesTable_Object = MibTable
ltp8xONTACSProfilesTable = _Ltp8xONTACSProfilesTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 16)
)
if mibBuilder.loadTexts:
    ltp8xONTACSProfilesTable.setStatus("current")
_Ltp8xONTACSProfilesEntry_Object = MibTableRow
ltp8xONTACSProfilesEntry = _Ltp8xONTACSProfilesEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 16, 1)
)
ltp8xONTACSProfilesEntry.setIndexNames(
    (0, "ELTEX-LTP8X", "ltp8xONTACSProfilesName"),
)
if mibBuilder.loadTexts:
    ltp8xONTACSProfilesEntry.setStatus("current")
_Ltp8xONTACSProfilesName_Type = DisplayString
_Ltp8xONTACSProfilesName_Object = MibTableColumn
ltp8xONTACSProfilesName = _Ltp8xONTACSProfilesName_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 16, 1, 1),
    _Ltp8xONTACSProfilesName_Type()
)
ltp8xONTACSProfilesName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTACSProfilesName.setStatus("current")
_Ltp8xONTACSProfilesDescription_Type = DisplayString
_Ltp8xONTACSProfilesDescription_Object = MibTableColumn
ltp8xONTACSProfilesDescription = _Ltp8xONTACSProfilesDescription_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 16, 1, 2),
    _Ltp8xONTACSProfilesDescription_Type()
)
ltp8xONTACSProfilesDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTACSProfilesDescription.setStatus("current")
_Ltp8xONTACSConfigAltTable_Object = MibTable
ltp8xONTACSConfigAltTable = _Ltp8xONTACSConfigAltTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 17)
)
if mibBuilder.loadTexts:
    ltp8xONTACSConfigAltTable.setStatus("current")
_Ltp8xONTACSConfigAltEntry_Object = MibTableRow
ltp8xONTACSConfigAltEntry = _Ltp8xONTACSConfigAltEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 17, 1)
)
ltp8xONTACSConfigAltEntry.setIndexNames(
    (0, "ELTEX-LTP8X", "ltp8xONTACSConfigAltSerial"),
)
if mibBuilder.loadTexts:
    ltp8xONTACSConfigAltEntry.setStatus("current")
_Ltp8xONTACSConfigAltSerial_Type = ONTSerial
_Ltp8xONTACSConfigAltSerial_Object = MibTableColumn
ltp8xONTACSConfigAltSerial = _Ltp8xONTACSConfigAltSerial_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 17, 1, 1),
    _Ltp8xONTACSConfigAltSerial_Type()
)
ltp8xONTACSConfigAltSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTACSConfigAltSerial.setStatus("current")
_Ltp8xONTACSConfigAltSubscriberID_Type = DisplayString
_Ltp8xONTACSConfigAltSubscriberID_Object = MibTableColumn
ltp8xONTACSConfigAltSubscriberID = _Ltp8xONTACSConfigAltSubscriberID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 17, 1, 2),
    _Ltp8xONTACSConfigAltSubscriberID_Type()
)
ltp8xONTACSConfigAltSubscriberID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTACSConfigAltSubscriberID.setStatus("current")
_Ltp8xONTACSConfigAltProfile_Type = DisplayString
_Ltp8xONTACSConfigAltProfile_Object = MibTableColumn
ltp8xONTACSConfigAltProfile = _Ltp8xONTACSConfigAltProfile_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 17, 1, 3),
    _Ltp8xONTACSConfigAltProfile_Type()
)
ltp8xONTACSConfigAltProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTACSConfigAltProfile.setStatus("current")
_Ltp8xONTACSConfigAltVoice1Enable_Type = DisplayString
_Ltp8xONTACSConfigAltVoice1Enable_Object = MibTableColumn
ltp8xONTACSConfigAltVoice1Enable = _Ltp8xONTACSConfigAltVoice1Enable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 17, 1, 4),
    _Ltp8xONTACSConfigAltVoice1Enable_Type()
)
ltp8xONTACSConfigAltVoice1Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTACSConfigAltVoice1Enable.setStatus("current")
_Ltp8xONTACSConfigAltVoice1Number_Type = DisplayString
_Ltp8xONTACSConfigAltVoice1Number_Object = MibTableColumn
ltp8xONTACSConfigAltVoice1Number = _Ltp8xONTACSConfigAltVoice1Number_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 17, 1, 5),
    _Ltp8xONTACSConfigAltVoice1Number_Type()
)
ltp8xONTACSConfigAltVoice1Number.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTACSConfigAltVoice1Number.setStatus("current")
_Ltp8xONTACSConfigAltVoice1Password_Type = DisplayString
_Ltp8xONTACSConfigAltVoice1Password_Object = MibTableColumn
ltp8xONTACSConfigAltVoice1Password = _Ltp8xONTACSConfigAltVoice1Password_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 17, 1, 6),
    _Ltp8xONTACSConfigAltVoice1Password_Type()
)
ltp8xONTACSConfigAltVoice1Password.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTACSConfigAltVoice1Password.setStatus("current")
_Ltp8xONTACSConfigAltVoice2Enable_Type = DisplayString
_Ltp8xONTACSConfigAltVoice2Enable_Object = MibTableColumn
ltp8xONTACSConfigAltVoice2Enable = _Ltp8xONTACSConfigAltVoice2Enable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 17, 1, 7),
    _Ltp8xONTACSConfigAltVoice2Enable_Type()
)
ltp8xONTACSConfigAltVoice2Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTACSConfigAltVoice2Enable.setStatus("current")
_Ltp8xONTACSConfigAltVoice2Number_Type = DisplayString
_Ltp8xONTACSConfigAltVoice2Number_Object = MibTableColumn
ltp8xONTACSConfigAltVoice2Number = _Ltp8xONTACSConfigAltVoice2Number_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 17, 1, 8),
    _Ltp8xONTACSConfigAltVoice2Number_Type()
)
ltp8xONTACSConfigAltVoice2Number.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTACSConfigAltVoice2Number.setStatus("current")
_Ltp8xONTACSConfigAltVoice2Password_Type = DisplayString
_Ltp8xONTACSConfigAltVoice2Password_Object = MibTableColumn
ltp8xONTACSConfigAltVoice2Password = _Ltp8xONTACSConfigAltVoice2Password_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 17, 1, 9),
    _Ltp8xONTACSConfigAltVoice2Password_Type()
)
ltp8xONTACSConfigAltVoice2Password.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTACSConfigAltVoice2Password.setStatus("current")
_Ltp8xONTACSConfigAltSIPProxy_Type = DisplayString
_Ltp8xONTACSConfigAltSIPProxy_Object = MibTableColumn
ltp8xONTACSConfigAltSIPProxy = _Ltp8xONTACSConfigAltSIPProxy_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 17, 1, 10),
    _Ltp8xONTACSConfigAltSIPProxy_Type()
)
ltp8xONTACSConfigAltSIPProxy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTACSConfigAltSIPProxy.setStatus("current")
_Ltp8xONTACSConfigAltPPPLogin_Type = DisplayString
_Ltp8xONTACSConfigAltPPPLogin_Object = MibTableColumn
ltp8xONTACSConfigAltPPPLogin = _Ltp8xONTACSConfigAltPPPLogin_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 17, 1, 11),
    _Ltp8xONTACSConfigAltPPPLogin_Type()
)
ltp8xONTACSConfigAltPPPLogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTACSConfigAltPPPLogin.setStatus("current")
_Ltp8xONTACSConfigAltPPPPassword_Type = DisplayString
_Ltp8xONTACSConfigAltPPPPassword_Object = MibTableColumn
ltp8xONTACSConfigAltPPPPassword = _Ltp8xONTACSConfigAltPPPPassword_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 17, 1, 12),
    _Ltp8xONTACSConfigAltPPPPassword_Type()
)
ltp8xONTACSConfigAltPPPPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTACSConfigAltPPPPassword.setStatus("current")
_Ltp8xONTACSConfigAltInternetVlan_Type = DisplayString
_Ltp8xONTACSConfigAltInternetVlan_Object = MibTableColumn
ltp8xONTACSConfigAltInternetVlan = _Ltp8xONTACSConfigAltInternetVlan_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 17, 1, 13),
    _Ltp8xONTACSConfigAltInternetVlan_Type()
)
ltp8xONTACSConfigAltInternetVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTACSConfigAltInternetVlan.setStatus("current")
_Ltp8xONTACSConfigAltResetToDefaults_Type = Unsigned32
_Ltp8xONTACSConfigAltResetToDefaults_Object = MibTableColumn
ltp8xONTACSConfigAltResetToDefaults = _Ltp8xONTACSConfigAltResetToDefaults_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 17, 1, 14),
    _Ltp8xONTACSConfigAltResetToDefaults_Type()
)
ltp8xONTACSConfigAltResetToDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTACSConfigAltResetToDefaults.setStatus("current")
_Ltp8xONTACSConfigAltRowStatus_Type = RowStatus
_Ltp8xONTACSConfigAltRowStatus_Object = MibTableColumn
ltp8xONTACSConfigAltRowStatus = _Ltp8xONTACSConfigAltRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 17, 1, 20),
    _Ltp8xONTACSConfigAltRowStatus_Type()
)
ltp8xONTACSConfigAltRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTACSConfigAltRowStatus.setStatus("current")
_Ltp8xONTShapingProfileTable_Object = MibTable
ltp8xONTShapingProfileTable = _Ltp8xONTShapingProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 18)
)
if mibBuilder.loadTexts:
    ltp8xONTShapingProfileTable.setStatus("current")
_Ltp8xONTShapingProfileEntry_Object = MibTableRow
ltp8xONTShapingProfileEntry = _Ltp8xONTShapingProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 18, 1)
)
ltp8xONTShapingProfileEntry.setIndexNames(
    (0, "ELTEX-LTP8X", "ltp8xONTShapingID"),
)
if mibBuilder.loadTexts:
    ltp8xONTShapingProfileEntry.setStatus("current")
_Ltp8xONTShapingID_Type = Unsigned32
_Ltp8xONTShapingID_Object = MibTableColumn
ltp8xONTShapingID = _Ltp8xONTShapingID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 18, 1, 1),
    _Ltp8xONTShapingID_Type()
)
ltp8xONTShapingID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTShapingID.setStatus("current")
_Ltp8xONTShapingDescription_Type = DisplayString
_Ltp8xONTShapingDescription_Object = MibTableColumn
ltp8xONTShapingDescription = _Ltp8xONTShapingDescription_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 18, 1, 2),
    _Ltp8xONTShapingDescription_Type()
)
ltp8xONTShapingDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTShapingDescription.setStatus("current")
_Ltp8xONTShapingName_Type = DisplayString
_Ltp8xONTShapingName_Object = MibTableColumn
ltp8xONTShapingName = _Ltp8xONTShapingName_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 18, 1, 3),
    _Ltp8xONTShapingName_Type()
)
ltp8xONTShapingName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTShapingName.setStatus("current")
_Ltp8xONTShapingDownstreamOnePolicer_Type = TruthValue
_Ltp8xONTShapingDownstreamOnePolicer_Object = MibTableColumn
ltp8xONTShapingDownstreamOnePolicer = _Ltp8xONTShapingDownstreamOnePolicer_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 18, 1, 4),
    _Ltp8xONTShapingDownstreamOnePolicer_Type()
)
ltp8xONTShapingDownstreamOnePolicer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTShapingDownstreamOnePolicer.setStatus("current")
_Ltp8xONTShapingRowStatus_Type = RowStatus
_Ltp8xONTShapingRowStatus_Object = MibTableColumn
ltp8xONTShapingRowStatus = _Ltp8xONTShapingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 18, 1, 10),
    _Ltp8xONTShapingRowStatus_Type()
)
ltp8xONTShapingRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTShapingRowStatus.setStatus("current")
_Ltp8xONTShapingProfileServicesTable_Object = MibTable
ltp8xONTShapingProfileServicesTable = _Ltp8xONTShapingProfileServicesTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 19)
)
if mibBuilder.loadTexts:
    ltp8xONTShapingProfileServicesTable.setStatus("current")
_Ltp8xONTShapingProfileServicesEntry_Object = MibTableRow
ltp8xONTShapingProfileServicesEntry = _Ltp8xONTShapingProfileServicesEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 19, 1)
)
ltp8xONTShapingProfileServicesEntry.setIndexNames(
    (0, "ELTEX-LTP8X", "ltp8xONTShapingID"),
    (0, "ELTEX-LTP8X", "ltp8xONTShapingCrossConnect"),
)
if mibBuilder.loadTexts:
    ltp8xONTShapingProfileServicesEntry.setStatus("current")
_Ltp8xONTShapingCrossConnect_Type = Unsigned32
_Ltp8xONTShapingCrossConnect_Object = MibTableColumn
ltp8xONTShapingCrossConnect = _Ltp8xONTShapingCrossConnect_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 19, 1, 1),
    _Ltp8xONTShapingCrossConnect_Type()
)
ltp8xONTShapingCrossConnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTShapingCrossConnect.setStatus("current")
_Ltp8xONTShapingUpstreamEnable_Type = TruthValue
_Ltp8xONTShapingUpstreamEnable_Object = MibTableColumn
ltp8xONTShapingUpstreamEnable = _Ltp8xONTShapingUpstreamEnable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 19, 1, 2),
    _Ltp8xONTShapingUpstreamEnable_Type()
)
ltp8xONTShapingUpstreamEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTShapingUpstreamEnable.setStatus("current")
_Ltp8xONTShapingUpstreamCommitedRate_Type = Unsigned32
_Ltp8xONTShapingUpstreamCommitedRate_Object = MibTableColumn
ltp8xONTShapingUpstreamCommitedRate = _Ltp8xONTShapingUpstreamCommitedRate_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 19, 1, 3),
    _Ltp8xONTShapingUpstreamCommitedRate_Type()
)
ltp8xONTShapingUpstreamCommitedRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTShapingUpstreamCommitedRate.setStatus("current")
_Ltp8xONTShapingUpstreamPeakRate_Type = Unsigned32
_Ltp8xONTShapingUpstreamPeakRate_Object = MibTableColumn
ltp8xONTShapingUpstreamPeakRate = _Ltp8xONTShapingUpstreamPeakRate_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 19, 1, 4),
    _Ltp8xONTShapingUpstreamPeakRate_Type()
)
ltp8xONTShapingUpstreamPeakRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTShapingUpstreamPeakRate.setStatus("current")
_Ltp8xONTShapingDownstreamEnable_Type = TruthValue
_Ltp8xONTShapingDownstreamEnable_Object = MibTableColumn
ltp8xONTShapingDownstreamEnable = _Ltp8xONTShapingDownstreamEnable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 19, 1, 5),
    _Ltp8xONTShapingDownstreamEnable_Type()
)
ltp8xONTShapingDownstreamEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTShapingDownstreamEnable.setStatus("current")
_Ltp8xONTShapingDownstreamPeakRate_Type = Unsigned32
_Ltp8xONTShapingDownstreamPeakRate_Object = MibTableColumn
ltp8xONTShapingDownstreamPeakRate = _Ltp8xONTShapingDownstreamPeakRate_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 19, 1, 6),
    _Ltp8xONTShapingDownstreamPeakRate_Type()
)
ltp8xONTShapingDownstreamPeakRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTShapingDownstreamPeakRate.setStatus("current")
_Ltp8xONTACSState_ObjectIdentity = ObjectIdentity
ltp8xONTACSState = _Ltp8xONTACSState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 20)
)
_Ltp8xONTACSStateTable_Object = MibTable
ltp8xONTACSStateTable = _Ltp8xONTACSStateTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 20, 1)
)
if mibBuilder.loadTexts:
    ltp8xONTACSStateTable.setStatus("current")
_Ltp8xONTACSStateEntry_Object = MibTableRow
ltp8xONTACSStateEntry = _Ltp8xONTACSStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 20, 1, 1)
)
ltp8xONTACSStateEntry.setIndexNames(
    (0, "ELTEX-LTP8X", "ltp8xONTACSStateBindingID"),
)
if mibBuilder.loadTexts:
    ltp8xONTACSStateEntry.setStatus("current")


class _Ltp8xONTACSStateBindingID_Type(Integer32):
    """Custom type ltp8xONTACSStateBindingID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Ltp8xONTACSStateBindingID_Type.__name__ = "Integer32"
_Ltp8xONTACSStateBindingID_Object = MibTableColumn
ltp8xONTACSStateBindingID = _Ltp8xONTACSStateBindingID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 20, 1, 1, 1),
    _Ltp8xONTACSStateBindingID_Type()
)
ltp8xONTACSStateBindingID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTACSStateBindingID.setStatus("current")
_Ltp8xONTACSStateSerial_Type = ONTSerial
_Ltp8xONTACSStateSerial_Object = MibTableColumn
ltp8xONTACSStateSerial = _Ltp8xONTACSStateSerial_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 20, 1, 1, 2),
    _Ltp8xONTACSStateSerial_Type()
)
ltp8xONTACSStateSerial.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTACSStateSerial.setStatus("current")
_Ltp8xONTACSStateBindingName_Type = DisplayString
_Ltp8xONTACSStateBindingName_Object = MibTableColumn
ltp8xONTACSStateBindingName = _Ltp8xONTACSStateBindingName_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 20, 1, 1, 3),
    _Ltp8xONTACSStateBindingName_Type()
)
ltp8xONTACSStateBindingName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTACSStateBindingName.setStatus("current")
_Ltp8xONTACSStateBindingValue_Type = DisplayString
_Ltp8xONTACSStateBindingValue_Object = MibTableColumn
ltp8xONTACSStateBindingValue = _Ltp8xONTACSStateBindingValue_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 20, 1, 1, 4),
    _Ltp8xONTACSStateBindingValue_Type()
)
ltp8xONTACSStateBindingValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTACSStateBindingValue.setStatus("current")
_Ltp8xONTACSStateDeleteRow_Type = Unsigned32
_Ltp8xONTACSStateDeleteRow_Object = MibTableColumn
ltp8xONTACSStateDeleteRow = _Ltp8xONTACSStateDeleteRow_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 20, 1, 1, 5),
    _Ltp8xONTACSStateDeleteRow_Type()
)
ltp8xONTACSStateDeleteRow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTACSStateDeleteRow.setStatus("current")
_Ltp8xONTACSStateCommitRequest_Type = Unsigned32
_Ltp8xONTACSStateCommitRequest_Object = MibScalar
ltp8xONTACSStateCommitRequest = _Ltp8xONTACSStateCommitRequest_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 20, 10),
    _Ltp8xONTACSStateCommitRequest_Type()
)
ltp8xONTACSStateCommitRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTACSStateCommitRequest.setStatus("current")
_Ltp8xONTACSStateClear_Type = Unsigned32
_Ltp8xONTACSStateClear_Object = MibScalar
ltp8xONTACSStateClear = _Ltp8xONTACSStateClear_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 20, 11),
    _Ltp8xONTACSStateClear_Type()
)
ltp8xONTACSStateClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTACSStateClear.setStatus("current")
_Ltp8xONTACSStateMaxIndex_Type = Unsigned32
_Ltp8xONTACSStateMaxIndex_Object = MibScalar
ltp8xONTACSStateMaxIndex = _Ltp8xONTACSStateMaxIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 20, 12),
    _Ltp8xONTACSStateMaxIndex_Type()
)
ltp8xONTACSStateMaxIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTACSStateMaxIndex.setStatus("current")
_Ltp8xONTACSStateLastSetIndex_Type = Unsigned32
_Ltp8xONTACSStateLastSetIndex_Object = MibScalar
ltp8xONTACSStateLastSetIndex = _Ltp8xONTACSStateLastSetIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 20, 13),
    _Ltp8xONTACSStateLastSetIndex_Type()
)
ltp8xONTACSStateLastSetIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTACSStateLastSetIndex.setStatus("current")
_Ltp8xONTACSStateLock_Type = Unsigned32
_Ltp8xONTACSStateLock_Object = MibScalar
ltp8xONTACSStateLock = _Ltp8xONTACSStateLock_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 20, 14),
    _Ltp8xONTACSStateLock_Type()
)
ltp8xONTACSStateLock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTACSStateLock.setStatus("current")
_Ltp8xONTStaticWANConfigTable_Object = MibTable
ltp8xONTStaticWANConfigTable = _Ltp8xONTStaticWANConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 21)
)
if mibBuilder.loadTexts:
    ltp8xONTStaticWANConfigTable.setStatus("current")
_Ltp8xONTStaticWANConfigEntry_Object = MibTableRow
ltp8xONTStaticWANConfigEntry = _Ltp8xONTStaticWANConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 21, 1)
)
ltp8xONTStaticWANConfigEntry.setIndexNames(
    (0, "ELTEX-LTP8X", "ltp8xONTStaticWANConfigSerial"),
    (0, "ELTEX-LTP8X", "ltp8xONTStaticWANConfigConnection"),
)
if mibBuilder.loadTexts:
    ltp8xONTStaticWANConfigEntry.setStatus("current")
_Ltp8xONTStaticWANConfigSerial_Type = ONTSerial
_Ltp8xONTStaticWANConfigSerial_Object = MibTableColumn
ltp8xONTStaticWANConfigSerial = _Ltp8xONTStaticWANConfigSerial_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 21, 1, 1),
    _Ltp8xONTStaticWANConfigSerial_Type()
)
ltp8xONTStaticWANConfigSerial.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ltp8xONTStaticWANConfigSerial.setStatus("current")
_Ltp8xONTStaticWANConfigConnection_Type = Unsigned32
_Ltp8xONTStaticWANConfigConnection_Object = MibTableColumn
ltp8xONTStaticWANConfigConnection = _Ltp8xONTStaticWANConfigConnection_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 21, 1, 2),
    _Ltp8xONTStaticWANConfigConnection_Type()
)
ltp8xONTStaticWANConfigConnection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ltp8xONTStaticWANConfigConnection.setStatus("current")
_Ltp8xONTStaticWANConfigDefaultGateway_Type = DisplayString
_Ltp8xONTStaticWANConfigDefaultGateway_Object = MibTableColumn
ltp8xONTStaticWANConfigDefaultGateway = _Ltp8xONTStaticWANConfigDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 21, 1, 3),
    _Ltp8xONTStaticWANConfigDefaultGateway_Type()
)
ltp8xONTStaticWANConfigDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTStaticWANConfigDefaultGateway.setStatus("current")
_Ltp8xONTStaticWANConfigExternalIPAddress_Type = DisplayString
_Ltp8xONTStaticWANConfigExternalIPAddress_Object = MibTableColumn
ltp8xONTStaticWANConfigExternalIPAddress = _Ltp8xONTStaticWANConfigExternalIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 21, 1, 4),
    _Ltp8xONTStaticWANConfigExternalIPAddress_Type()
)
ltp8xONTStaticWANConfigExternalIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTStaticWANConfigExternalIPAddress.setStatus("current")
_Ltp8xONTStaticWANConfigSubnetMask_Type = DisplayString
_Ltp8xONTStaticWANConfigSubnetMask_Object = MibTableColumn
ltp8xONTStaticWANConfigSubnetMask = _Ltp8xONTStaticWANConfigSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 21, 1, 5),
    _Ltp8xONTStaticWANConfigSubnetMask_Type()
)
ltp8xONTStaticWANConfigSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTStaticWANConfigSubnetMask.setStatus("current")
_Ltp8xONTBandwidthManagementProfileTable_Object = MibTable
ltp8xONTBandwidthManagementProfileTable = _Ltp8xONTBandwidthManagementProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 22)
)
if mibBuilder.loadTexts:
    ltp8xONTBandwidthManagementProfileTable.setStatus("current")
_Ltp8xONTBandwidthManagementProfileEntry_Object = MibTableRow
ltp8xONTBandwidthManagementProfileEntry = _Ltp8xONTBandwidthManagementProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 22, 1)
)
ltp8xONTBandwidthManagementProfileEntry.setIndexNames(
    (0, "ELTEX-LTP8X", "ltp8xONTBandwidthManagementID"),
)
if mibBuilder.loadTexts:
    ltp8xONTBandwidthManagementProfileEntry.setStatus("current")
_Ltp8xONTBandwidthManagementID_Type = Unsigned32
_Ltp8xONTBandwidthManagementID_Object = MibTableColumn
ltp8xONTBandwidthManagementID = _Ltp8xONTBandwidthManagementID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 22, 1, 1),
    _Ltp8xONTBandwidthManagementID_Type()
)
ltp8xONTBandwidthManagementID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTBandwidthManagementID.setStatus("current")
_Ltp8xONTBandwidthManagementDescription_Type = DisplayString
_Ltp8xONTBandwidthManagementDescription_Object = MibTableColumn
ltp8xONTBandwidthManagementDescription = _Ltp8xONTBandwidthManagementDescription_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 22, 1, 2),
    _Ltp8xONTBandwidthManagementDescription_Type()
)
ltp8xONTBandwidthManagementDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTBandwidthManagementDescription.setStatus("current")
_Ltp8xONTBandwidthManagementName_Type = DisplayString
_Ltp8xONTBandwidthManagementName_Object = MibTableColumn
ltp8xONTBandwidthManagementName = _Ltp8xONTBandwidthManagementName_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 22, 1, 3),
    _Ltp8xONTBandwidthManagementName_Type()
)
ltp8xONTBandwidthManagementName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTBandwidthManagementName.setStatus("current")
_Ltp8xONTServiceBandwidthManagementTable_Object = MibTable
ltp8xONTServiceBandwidthManagementTable = _Ltp8xONTServiceBandwidthManagementTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 23)
)
if mibBuilder.loadTexts:
    ltp8xONTServiceBandwidthManagementTable.setStatus("current")
_Ltp8xONTServiceBandwidthManagementEntry_Object = MibTableRow
ltp8xONTServiceBandwidthManagementEntry = _Ltp8xONTServiceBandwidthManagementEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 23, 1)
)
ltp8xONTServiceBandwidthManagementEntry.setIndexNames(
    (0, "ELTEX-LTP8X", "ltp8xONTServiceBandwidthManagementServiceID"),
    (0, "ELTEX-LTP8X", "ltp8xONTServiceBandwidthManagementSlot"),
    (0, "ELTEX-LTP8X", "ltp8xONTServiceBandwidthManagementSerial"),
)
if mibBuilder.loadTexts:
    ltp8xONTServiceBandwidthManagementEntry.setStatus("current")
_Ltp8xONTServiceBandwidthManagementServiceID_Type = Unsigned32
_Ltp8xONTServiceBandwidthManagementServiceID_Object = MibTableColumn
ltp8xONTServiceBandwidthManagementServiceID = _Ltp8xONTServiceBandwidthManagementServiceID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 23, 1, 1),
    _Ltp8xONTServiceBandwidthManagementServiceID_Type()
)
ltp8xONTServiceBandwidthManagementServiceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTServiceBandwidthManagementServiceID.setStatus("current")
_Ltp8xONTServiceBandwidthManagementSlot_Type = Unsigned32
_Ltp8xONTServiceBandwidthManagementSlot_Object = MibTableColumn
ltp8xONTServiceBandwidthManagementSlot = _Ltp8xONTServiceBandwidthManagementSlot_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 23, 1, 2),
    _Ltp8xONTServiceBandwidthManagementSlot_Type()
)
ltp8xONTServiceBandwidthManagementSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTServiceBandwidthManagementSlot.setStatus("current")
_Ltp8xONTServiceBandwidthManagementSerial_Type = ONTSerial
_Ltp8xONTServiceBandwidthManagementSerial_Object = MibTableColumn
ltp8xONTServiceBandwidthManagementSerial = _Ltp8xONTServiceBandwidthManagementSerial_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 23, 1, 3),
    _Ltp8xONTServiceBandwidthManagementSerial_Type()
)
ltp8xONTServiceBandwidthManagementSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTServiceBandwidthManagementSerial.setStatus("current")
_Ltp8xONTServiceBandwidthManagementProfile_Type = Unsigned32
_Ltp8xONTServiceBandwidthManagementProfile_Object = MibTableColumn
ltp8xONTServiceBandwidthManagementProfile = _Ltp8xONTServiceBandwidthManagementProfile_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 23, 1, 4),
    _Ltp8xONTServiceBandwidthManagementProfile_Type()
)
ltp8xONTServiceBandwidthManagementProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTServiceBandwidthManagementProfile.setStatus("current")
_Ltp8xONTTemplates_ObjectIdentity = ObjectIdentity
ltp8xONTTemplates = _Ltp8xONTTemplates_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 24)
)
_Ltp8xONTTemplateValuesTable_Object = MibTable
ltp8xONTTemplateValuesTable = _Ltp8xONTTemplateValuesTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 24, 1)
)
if mibBuilder.loadTexts:
    ltp8xONTTemplateValuesTable.setStatus("current")
_Ltp8xONTTemplateValuesEntry_Object = MibTableRow
ltp8xONTTemplateValuesEntry = _Ltp8xONTTemplateValuesEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 24, 1, 1)
)
ltp8xONTTemplateValuesEntry.setIndexNames(
    (0, "ELTEX-LTP8X", "ltp8xONTTemplateValuesID"),
)
if mibBuilder.loadTexts:
    ltp8xONTTemplateValuesEntry.setStatus("current")
_Ltp8xONTTemplateValuesID_Type = Unsigned32
_Ltp8xONTTemplateValuesID_Object = MibTableColumn
ltp8xONTTemplateValuesID = _Ltp8xONTTemplateValuesID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 24, 1, 1, 1),
    _Ltp8xONTTemplateValuesID_Type()
)
ltp8xONTTemplateValuesID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ltp8xONTTemplateValuesID.setStatus("current")
_Ltp8xONTTemplateValuesName_Type = DisplayString
_Ltp8xONTTemplateValuesName_Object = MibTableColumn
ltp8xONTTemplateValuesName = _Ltp8xONTTemplateValuesName_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 24, 1, 1, 2),
    _Ltp8xONTTemplateValuesName_Type()
)
ltp8xONTTemplateValuesName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTTemplateValuesName.setStatus("current")
_Ltp8xONTTemplateValuesDescription_Type = DisplayString
_Ltp8xONTTemplateValuesDescription_Object = MibTableColumn
ltp8xONTTemplateValuesDescription = _Ltp8xONTTemplateValuesDescription_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 24, 1, 1, 3),
    _Ltp8xONTTemplateValuesDescription_Type()
)
ltp8xONTTemplateValuesDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTTemplateValuesDescription.setStatus("current")
_Ltp8xONTTemplateValuesSerial_Type = ONTSerial
_Ltp8xONTTemplateValuesSerial_Object = MibTableColumn
ltp8xONTTemplateValuesSerial = _Ltp8xONTTemplateValuesSerial_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 24, 1, 1, 4),
    _Ltp8xONTTemplateValuesSerial_Type()
)
ltp8xONTTemplateValuesSerial.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTTemplateValuesSerial.setStatus("current")
_Ltp8xONTTemplateValuesPassword_Type = DisplayString
_Ltp8xONTTemplateValuesPassword_Object = MibTableColumn
ltp8xONTTemplateValuesPassword = _Ltp8xONTTemplateValuesPassword_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 24, 1, 1, 6),
    _Ltp8xONTTemplateValuesPassword_Type()
)
ltp8xONTTemplateValuesPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTTemplateValuesPassword.setStatus("current")
_Ltp8xONTTemplateValuesFecUp_Type = TruthValue
_Ltp8xONTTemplateValuesFecUp_Object = MibTableColumn
ltp8xONTTemplateValuesFecUp = _Ltp8xONTTemplateValuesFecUp_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 24, 1, 1, 7),
    _Ltp8xONTTemplateValuesFecUp_Type()
)
ltp8xONTTemplateValuesFecUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTTemplateValuesFecUp.setStatus("current")
_Ltp8xONTTemplateValuesManagementProfile_Type = Unsigned32
_Ltp8xONTTemplateValuesManagementProfile_Object = MibTableColumn
ltp8xONTTemplateValuesManagementProfile = _Ltp8xONTTemplateValuesManagementProfile_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 24, 1, 1, 9),
    _Ltp8xONTTemplateValuesManagementProfile_Type()
)
ltp8xONTTemplateValuesManagementProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTTemplateValuesManagementProfile.setStatus("current")
_Ltp8xONTTemplateValuesCrossConnectProfile0_Type = Unsigned32
_Ltp8xONTTemplateValuesCrossConnectProfile0_Object = MibTableColumn
ltp8xONTTemplateValuesCrossConnectProfile0 = _Ltp8xONTTemplateValuesCrossConnectProfile0_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 24, 1, 1, 11),
    _Ltp8xONTTemplateValuesCrossConnectProfile0_Type()
)
ltp8xONTTemplateValuesCrossConnectProfile0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTTemplateValuesCrossConnectProfile0.setStatus("current")
_Ltp8xONTTemplateValuesCrossConnectProfile1_Type = Unsigned32
_Ltp8xONTTemplateValuesCrossConnectProfile1_Object = MibTableColumn
ltp8xONTTemplateValuesCrossConnectProfile1 = _Ltp8xONTTemplateValuesCrossConnectProfile1_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 24, 1, 1, 12),
    _Ltp8xONTTemplateValuesCrossConnectProfile1_Type()
)
ltp8xONTTemplateValuesCrossConnectProfile1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTTemplateValuesCrossConnectProfile1.setStatus("current")
_Ltp8xONTTemplateValuesCrossConnectProfile2_Type = Unsigned32
_Ltp8xONTTemplateValuesCrossConnectProfile2_Object = MibTableColumn
ltp8xONTTemplateValuesCrossConnectProfile2 = _Ltp8xONTTemplateValuesCrossConnectProfile2_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 24, 1, 1, 13),
    _Ltp8xONTTemplateValuesCrossConnectProfile2_Type()
)
ltp8xONTTemplateValuesCrossConnectProfile2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTTemplateValuesCrossConnectProfile2.setStatus("current")
_Ltp8xONTTemplateValuesCrossConnectProfile3_Type = Unsigned32
_Ltp8xONTTemplateValuesCrossConnectProfile3_Object = MibTableColumn
ltp8xONTTemplateValuesCrossConnectProfile3 = _Ltp8xONTTemplateValuesCrossConnectProfile3_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 24, 1, 1, 14),
    _Ltp8xONTTemplateValuesCrossConnectProfile3_Type()
)
ltp8xONTTemplateValuesCrossConnectProfile3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTTemplateValuesCrossConnectProfile3.setStatus("current")
_Ltp8xONTTemplateValuesCrossConnectProfile4_Type = Unsigned32
_Ltp8xONTTemplateValuesCrossConnectProfile4_Object = MibTableColumn
ltp8xONTTemplateValuesCrossConnectProfile4 = _Ltp8xONTTemplateValuesCrossConnectProfile4_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 24, 1, 1, 15),
    _Ltp8xONTTemplateValuesCrossConnectProfile4_Type()
)
ltp8xONTTemplateValuesCrossConnectProfile4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTTemplateValuesCrossConnectProfile4.setStatus("current")
_Ltp8xONTTemplateValuesCrossConnectProfile5_Type = Unsigned32
_Ltp8xONTTemplateValuesCrossConnectProfile5_Object = MibTableColumn
ltp8xONTTemplateValuesCrossConnectProfile5 = _Ltp8xONTTemplateValuesCrossConnectProfile5_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 24, 1, 1, 16),
    _Ltp8xONTTemplateValuesCrossConnectProfile5_Type()
)
ltp8xONTTemplateValuesCrossConnectProfile5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTTemplateValuesCrossConnectProfile5.setStatus("current")
_Ltp8xONTTemplateValuesCrossConnectProfile6_Type = Unsigned32
_Ltp8xONTTemplateValuesCrossConnectProfile6_Object = MibTableColumn
ltp8xONTTemplateValuesCrossConnectProfile6 = _Ltp8xONTTemplateValuesCrossConnectProfile6_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 24, 1, 1, 17),
    _Ltp8xONTTemplateValuesCrossConnectProfile6_Type()
)
ltp8xONTTemplateValuesCrossConnectProfile6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTTemplateValuesCrossConnectProfile6.setStatus("current")
_Ltp8xONTTemplateValuesCrossConnectProfile7_Type = Unsigned32
_Ltp8xONTTemplateValuesCrossConnectProfile7_Object = MibTableColumn
ltp8xONTTemplateValuesCrossConnectProfile7 = _Ltp8xONTTemplateValuesCrossConnectProfile7_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 24, 1, 1, 18),
    _Ltp8xONTTemplateValuesCrossConnectProfile7_Type()
)
ltp8xONTTemplateValuesCrossConnectProfile7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTTemplateValuesCrossConnectProfile7.setStatus("current")
_Ltp8xONTTemplateValuesShapingProfile_Type = Unsigned32
_Ltp8xONTTemplateValuesShapingProfile_Object = MibTableColumn
ltp8xONTTemplateValuesShapingProfile = _Ltp8xONTTemplateValuesShapingProfile_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 24, 1, 1, 19),
    _Ltp8xONTTemplateValuesShapingProfile_Type()
)
ltp8xONTTemplateValuesShapingProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTTemplateValuesShapingProfile.setStatus("current")
_Ltp8xONTTemplateValuesDownstreamBroadcastEnabled_Type = TruthValue
_Ltp8xONTTemplateValuesDownstreamBroadcastEnabled_Object = MibTableColumn
ltp8xONTTemplateValuesDownstreamBroadcastEnabled = _Ltp8xONTTemplateValuesDownstreamBroadcastEnabled_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 24, 1, 1, 22),
    _Ltp8xONTTemplateValuesDownstreamBroadcastEnabled_Type()
)
ltp8xONTTemplateValuesDownstreamBroadcastEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTTemplateValuesDownstreamBroadcastEnabled.setStatus("current")
_Ltp8xONTTemplateValuesAllocProfile0_Type = Unsigned32
_Ltp8xONTTemplateValuesAllocProfile0_Object = MibTableColumn
ltp8xONTTemplateValuesAllocProfile0 = _Ltp8xONTTemplateValuesAllocProfile0_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 24, 1, 1, 23),
    _Ltp8xONTTemplateValuesAllocProfile0_Type()
)
ltp8xONTTemplateValuesAllocProfile0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTTemplateValuesAllocProfile0.setStatus("current")
_Ltp8xONTTemplateValuesAllocProfile1_Type = Unsigned32
_Ltp8xONTTemplateValuesAllocProfile1_Object = MibTableColumn
ltp8xONTTemplateValuesAllocProfile1 = _Ltp8xONTTemplateValuesAllocProfile1_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 24, 1, 1, 24),
    _Ltp8xONTTemplateValuesAllocProfile1_Type()
)
ltp8xONTTemplateValuesAllocProfile1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTTemplateValuesAllocProfile1.setStatus("current")
_Ltp8xONTTemplateValuesAllocProfile2_Type = Unsigned32
_Ltp8xONTTemplateValuesAllocProfile2_Object = MibTableColumn
ltp8xONTTemplateValuesAllocProfile2 = _Ltp8xONTTemplateValuesAllocProfile2_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 24, 1, 1, 25),
    _Ltp8xONTTemplateValuesAllocProfile2_Type()
)
ltp8xONTTemplateValuesAllocProfile2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTTemplateValuesAllocProfile2.setStatus("current")
_Ltp8xONTTemplateValuesAllocProfile3_Type = Unsigned32
_Ltp8xONTTemplateValuesAllocProfile3_Object = MibTableColumn
ltp8xONTTemplateValuesAllocProfile3 = _Ltp8xONTTemplateValuesAllocProfile3_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 24, 1, 1, 26),
    _Ltp8xONTTemplateValuesAllocProfile3_Type()
)
ltp8xONTTemplateValuesAllocProfile3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTTemplateValuesAllocProfile3.setStatus("current")
_Ltp8xONTTemplateValuesAllocProfile4_Type = Unsigned32
_Ltp8xONTTemplateValuesAllocProfile4_Object = MibTableColumn
ltp8xONTTemplateValuesAllocProfile4 = _Ltp8xONTTemplateValuesAllocProfile4_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 24, 1, 1, 27),
    _Ltp8xONTTemplateValuesAllocProfile4_Type()
)
ltp8xONTTemplateValuesAllocProfile4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTTemplateValuesAllocProfile4.setStatus("current")
_Ltp8xONTTemplateValuesAllocProfile5_Type = Unsigned32
_Ltp8xONTTemplateValuesAllocProfile5_Object = MibTableColumn
ltp8xONTTemplateValuesAllocProfile5 = _Ltp8xONTTemplateValuesAllocProfile5_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 24, 1, 1, 28),
    _Ltp8xONTTemplateValuesAllocProfile5_Type()
)
ltp8xONTTemplateValuesAllocProfile5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTTemplateValuesAllocProfile5.setStatus("current")
_Ltp8xONTTemplateValuesAllocProfile6_Type = Unsigned32
_Ltp8xONTTemplateValuesAllocProfile6_Object = MibTableColumn
ltp8xONTTemplateValuesAllocProfile6 = _Ltp8xONTTemplateValuesAllocProfile6_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 24, 1, 1, 29),
    _Ltp8xONTTemplateValuesAllocProfile6_Type()
)
ltp8xONTTemplateValuesAllocProfile6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTTemplateValuesAllocProfile6.setStatus("current")
_Ltp8xONTTemplateValuesAllocProfile7_Type = Unsigned32
_Ltp8xONTTemplateValuesAllocProfile7_Object = MibTableColumn
ltp8xONTTemplateValuesAllocProfile7 = _Ltp8xONTTemplateValuesAllocProfile7_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 24, 1, 1, 30),
    _Ltp8xONTTemplateValuesAllocProfile7_Type()
)
ltp8xONTTemplateValuesAllocProfile7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTTemplateValuesAllocProfile7.setStatus("current")
_Ltp8xONTTemplateValuesPortsProfile_Type = Unsigned32
_Ltp8xONTTemplateValuesPortsProfile_Object = MibTableColumn
ltp8xONTTemplateValuesPortsProfile = _Ltp8xONTTemplateValuesPortsProfile_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 24, 1, 1, 31),
    _Ltp8xONTTemplateValuesPortsProfile_Type()
)
ltp8xONTTemplateValuesPortsProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTTemplateValuesPortsProfile.setStatus("current")


class _Ltp8xONTTemplateValuesRFPortEnabled_Type(Integer32):
    """Custom type ltp8xONTTemplateValuesRFPortEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("noChange", 2))
    )


_Ltp8xONTTemplateValuesRFPortEnabled_Type.__name__ = "Integer32"
_Ltp8xONTTemplateValuesRFPortEnabled_Object = MibTableColumn
ltp8xONTTemplateValuesRFPortEnabled = _Ltp8xONTTemplateValuesRFPortEnabled_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 24, 1, 1, 32),
    _Ltp8xONTTemplateValuesRFPortEnabled_Type()
)
ltp8xONTTemplateValuesRFPortEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTTemplateValuesRFPortEnabled.setStatus("current")
_Ltp8xONTTemplateValuesScriptingProfile_Type = Unsigned32
_Ltp8xONTTemplateValuesScriptingProfile_Object = MibTableColumn
ltp8xONTTemplateValuesScriptingProfile = _Ltp8xONTTemplateValuesScriptingProfile_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 24, 1, 1, 36),
    _Ltp8xONTTemplateValuesScriptingProfile_Type()
)
ltp8xONTTemplateValuesScriptingProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTTemplateValuesScriptingProfile.setStatus("current")
_Ltp8xONTTemplateValuesBerInterval_Type = Unsigned32
_Ltp8xONTTemplateValuesBerInterval_Object = MibTableColumn
ltp8xONTTemplateValuesBerInterval = _Ltp8xONTTemplateValuesBerInterval_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 24, 1, 1, 37),
    _Ltp8xONTTemplateValuesBerInterval_Type()
)
ltp8xONTTemplateValuesBerInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTTemplateValuesBerInterval.setStatus("current")
_Ltp8xONTTemplateValuesBerUpdatePeriod_Type = Unsigned32
_Ltp8xONTTemplateValuesBerUpdatePeriod_Object = MibTableColumn
ltp8xONTTemplateValuesBerUpdatePeriod = _Ltp8xONTTemplateValuesBerUpdatePeriod_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 24, 1, 1, 38),
    _Ltp8xONTTemplateValuesBerUpdatePeriod_Type()
)
ltp8xONTTemplateValuesBerUpdatePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTTemplateValuesBerUpdatePeriod.setStatus("current")
_Ltp8xONTTemplateValuesOMCIErrorTolerant_Type = TruthValue
_Ltp8xONTTemplateValuesOMCIErrorTolerant_Object = MibTableColumn
ltp8xONTTemplateValuesOMCIErrorTolerant = _Ltp8xONTTemplateValuesOMCIErrorTolerant_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 24, 1, 1, 39),
    _Ltp8xONTTemplateValuesOMCIErrorTolerant_Type()
)
ltp8xONTTemplateValuesOMCIErrorTolerant.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTTemplateValuesOMCIErrorTolerant.setStatus("current")
_Ltp8xONTTemplateValuesRowStatus_Type = RowStatus
_Ltp8xONTTemplateValuesRowStatus_Object = MibTableColumn
ltp8xONTTemplateValuesRowStatus = _Ltp8xONTTemplateValuesRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 24, 1, 1, 100),
    _Ltp8xONTTemplateValuesRowStatus_Type()
)
ltp8xONTTemplateValuesRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTTemplateValuesRowStatus.setStatus("current")
_Ltp8xONTTemplateOverridesTable_Object = MibTable
ltp8xONTTemplateOverridesTable = _Ltp8xONTTemplateOverridesTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 24, 2)
)
if mibBuilder.loadTexts:
    ltp8xONTTemplateOverridesTable.setStatus("current")
_Ltp8xONTTemplateOverridesEntry_Object = MibTableRow
ltp8xONTTemplateOverridesEntry = _Ltp8xONTTemplateOverridesEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 24, 2, 1)
)
ltp8xONTTemplateOverridesEntry.setIndexNames(
    (0, "ELTEX-LTP8X", "ltp8xONTTemplateValuesID"),
)
if mibBuilder.loadTexts:
    ltp8xONTTemplateOverridesEntry.setStatus("current")
_Ltp8xONTTemplateOverridesSerial_Type = TruthValue
_Ltp8xONTTemplateOverridesSerial_Object = MibTableColumn
ltp8xONTTemplateOverridesSerial = _Ltp8xONTTemplateOverridesSerial_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 24, 2, 1, 4),
    _Ltp8xONTTemplateOverridesSerial_Type()
)
ltp8xONTTemplateOverridesSerial.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTTemplateOverridesSerial.setStatus("current")
_Ltp8xONTTemplateOverridesPassword_Type = TruthValue
_Ltp8xONTTemplateOverridesPassword_Object = MibTableColumn
ltp8xONTTemplateOverridesPassword = _Ltp8xONTTemplateOverridesPassword_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 24, 2, 1, 6),
    _Ltp8xONTTemplateOverridesPassword_Type()
)
ltp8xONTTemplateOverridesPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTTemplateOverridesPassword.setStatus("current")
_Ltp8xONTTemplateOverridesFecUp_Type = TruthValue
_Ltp8xONTTemplateOverridesFecUp_Object = MibTableColumn
ltp8xONTTemplateOverridesFecUp = _Ltp8xONTTemplateOverridesFecUp_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 24, 2, 1, 7),
    _Ltp8xONTTemplateOverridesFecUp_Type()
)
ltp8xONTTemplateOverridesFecUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTTemplateOverridesFecUp.setStatus("current")
_Ltp8xONTTemplateOverridesManagementProfile_Type = TruthValue
_Ltp8xONTTemplateOverridesManagementProfile_Object = MibTableColumn
ltp8xONTTemplateOverridesManagementProfile = _Ltp8xONTTemplateOverridesManagementProfile_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 24, 2, 1, 9),
    _Ltp8xONTTemplateOverridesManagementProfile_Type()
)
ltp8xONTTemplateOverridesManagementProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTTemplateOverridesManagementProfile.setStatus("current")
_Ltp8xONTTemplateOverridesCrossConnectProfile0_Type = TruthValue
_Ltp8xONTTemplateOverridesCrossConnectProfile0_Object = MibTableColumn
ltp8xONTTemplateOverridesCrossConnectProfile0 = _Ltp8xONTTemplateOverridesCrossConnectProfile0_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 24, 2, 1, 11),
    _Ltp8xONTTemplateOverridesCrossConnectProfile0_Type()
)
ltp8xONTTemplateOverridesCrossConnectProfile0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTTemplateOverridesCrossConnectProfile0.setStatus("current")
_Ltp8xONTTemplateOverridesCrossConnectProfile1_Type = TruthValue
_Ltp8xONTTemplateOverridesCrossConnectProfile1_Object = MibTableColumn
ltp8xONTTemplateOverridesCrossConnectProfile1 = _Ltp8xONTTemplateOverridesCrossConnectProfile1_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 24, 2, 1, 12),
    _Ltp8xONTTemplateOverridesCrossConnectProfile1_Type()
)
ltp8xONTTemplateOverridesCrossConnectProfile1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTTemplateOverridesCrossConnectProfile1.setStatus("current")
_Ltp8xONTTemplateOverridesCrossConnectProfile2_Type = TruthValue
_Ltp8xONTTemplateOverridesCrossConnectProfile2_Object = MibTableColumn
ltp8xONTTemplateOverridesCrossConnectProfile2 = _Ltp8xONTTemplateOverridesCrossConnectProfile2_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 24, 2, 1, 13),
    _Ltp8xONTTemplateOverridesCrossConnectProfile2_Type()
)
ltp8xONTTemplateOverridesCrossConnectProfile2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTTemplateOverridesCrossConnectProfile2.setStatus("current")
_Ltp8xONTTemplateOverridesCrossConnectProfile3_Type = TruthValue
_Ltp8xONTTemplateOverridesCrossConnectProfile3_Object = MibTableColumn
ltp8xONTTemplateOverridesCrossConnectProfile3 = _Ltp8xONTTemplateOverridesCrossConnectProfile3_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 24, 2, 1, 14),
    _Ltp8xONTTemplateOverridesCrossConnectProfile3_Type()
)
ltp8xONTTemplateOverridesCrossConnectProfile3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTTemplateOverridesCrossConnectProfile3.setStatus("current")
_Ltp8xONTTemplateOverridesCrossConnectProfile4_Type = TruthValue
_Ltp8xONTTemplateOverridesCrossConnectProfile4_Object = MibTableColumn
ltp8xONTTemplateOverridesCrossConnectProfile4 = _Ltp8xONTTemplateOverridesCrossConnectProfile4_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 24, 2, 1, 15),
    _Ltp8xONTTemplateOverridesCrossConnectProfile4_Type()
)
ltp8xONTTemplateOverridesCrossConnectProfile4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTTemplateOverridesCrossConnectProfile4.setStatus("current")
_Ltp8xONTTemplateOverridesCrossConnectProfile5_Type = TruthValue
_Ltp8xONTTemplateOverridesCrossConnectProfile5_Object = MibTableColumn
ltp8xONTTemplateOverridesCrossConnectProfile5 = _Ltp8xONTTemplateOverridesCrossConnectProfile5_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 24, 2, 1, 16),
    _Ltp8xONTTemplateOverridesCrossConnectProfile5_Type()
)
ltp8xONTTemplateOverridesCrossConnectProfile5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTTemplateOverridesCrossConnectProfile5.setStatus("current")
_Ltp8xONTTemplateOverridesCrossConnectProfile6_Type = TruthValue
_Ltp8xONTTemplateOverridesCrossConnectProfile6_Object = MibTableColumn
ltp8xONTTemplateOverridesCrossConnectProfile6 = _Ltp8xONTTemplateOverridesCrossConnectProfile6_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 24, 2, 1, 17),
    _Ltp8xONTTemplateOverridesCrossConnectProfile6_Type()
)
ltp8xONTTemplateOverridesCrossConnectProfile6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTTemplateOverridesCrossConnectProfile6.setStatus("current")
_Ltp8xONTTemplateOverridesCrossConnectProfile7_Type = TruthValue
_Ltp8xONTTemplateOverridesCrossConnectProfile7_Object = MibTableColumn
ltp8xONTTemplateOverridesCrossConnectProfile7 = _Ltp8xONTTemplateOverridesCrossConnectProfile7_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 24, 2, 1, 18),
    _Ltp8xONTTemplateOverridesCrossConnectProfile7_Type()
)
ltp8xONTTemplateOverridesCrossConnectProfile7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTTemplateOverridesCrossConnectProfile7.setStatus("current")
_Ltp8xONTTemplateOverridesShapingProfile_Type = TruthValue
_Ltp8xONTTemplateOverridesShapingProfile_Object = MibTableColumn
ltp8xONTTemplateOverridesShapingProfile = _Ltp8xONTTemplateOverridesShapingProfile_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 24, 2, 1, 19),
    _Ltp8xONTTemplateOverridesShapingProfile_Type()
)
ltp8xONTTemplateOverridesShapingProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTTemplateOverridesShapingProfile.setStatus("current")
_Ltp8xONTTemplateOverridesDownstreamBroadcastEnabled_Type = TruthValue
_Ltp8xONTTemplateOverridesDownstreamBroadcastEnabled_Object = MibTableColumn
ltp8xONTTemplateOverridesDownstreamBroadcastEnabled = _Ltp8xONTTemplateOverridesDownstreamBroadcastEnabled_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 24, 2, 1, 22),
    _Ltp8xONTTemplateOverridesDownstreamBroadcastEnabled_Type()
)
ltp8xONTTemplateOverridesDownstreamBroadcastEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTTemplateOverridesDownstreamBroadcastEnabled.setStatus("current")
_Ltp8xONTTemplateOverridesAllocProfile0_Type = TruthValue
_Ltp8xONTTemplateOverridesAllocProfile0_Object = MibTableColumn
ltp8xONTTemplateOverridesAllocProfile0 = _Ltp8xONTTemplateOverridesAllocProfile0_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 24, 2, 1, 23),
    _Ltp8xONTTemplateOverridesAllocProfile0_Type()
)
ltp8xONTTemplateOverridesAllocProfile0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTTemplateOverridesAllocProfile0.setStatus("current")
_Ltp8xONTTemplateOverridesAllocProfile1_Type = TruthValue
_Ltp8xONTTemplateOverridesAllocProfile1_Object = MibTableColumn
ltp8xONTTemplateOverridesAllocProfile1 = _Ltp8xONTTemplateOverridesAllocProfile1_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 24, 2, 1, 24),
    _Ltp8xONTTemplateOverridesAllocProfile1_Type()
)
ltp8xONTTemplateOverridesAllocProfile1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTTemplateOverridesAllocProfile1.setStatus("current")
_Ltp8xONTTemplateOverridesAllocProfile2_Type = TruthValue
_Ltp8xONTTemplateOverridesAllocProfile2_Object = MibTableColumn
ltp8xONTTemplateOverridesAllocProfile2 = _Ltp8xONTTemplateOverridesAllocProfile2_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 24, 2, 1, 25),
    _Ltp8xONTTemplateOverridesAllocProfile2_Type()
)
ltp8xONTTemplateOverridesAllocProfile2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTTemplateOverridesAllocProfile2.setStatus("current")
_Ltp8xONTTemplateOverridesAllocProfile3_Type = TruthValue
_Ltp8xONTTemplateOverridesAllocProfile3_Object = MibTableColumn
ltp8xONTTemplateOverridesAllocProfile3 = _Ltp8xONTTemplateOverridesAllocProfile3_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 24, 2, 1, 26),
    _Ltp8xONTTemplateOverridesAllocProfile3_Type()
)
ltp8xONTTemplateOverridesAllocProfile3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTTemplateOverridesAllocProfile3.setStatus("current")
_Ltp8xONTTemplateOverridesAllocProfile4_Type = TruthValue
_Ltp8xONTTemplateOverridesAllocProfile4_Object = MibTableColumn
ltp8xONTTemplateOverridesAllocProfile4 = _Ltp8xONTTemplateOverridesAllocProfile4_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 24, 2, 1, 27),
    _Ltp8xONTTemplateOverridesAllocProfile4_Type()
)
ltp8xONTTemplateOverridesAllocProfile4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTTemplateOverridesAllocProfile4.setStatus("current")
_Ltp8xONTTemplateOverridesAllocProfile5_Type = TruthValue
_Ltp8xONTTemplateOverridesAllocProfile5_Object = MibTableColumn
ltp8xONTTemplateOverridesAllocProfile5 = _Ltp8xONTTemplateOverridesAllocProfile5_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 24, 2, 1, 28),
    _Ltp8xONTTemplateOverridesAllocProfile5_Type()
)
ltp8xONTTemplateOverridesAllocProfile5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTTemplateOverridesAllocProfile5.setStatus("current")
_Ltp8xONTTemplateOverridesAllocProfile6_Type = TruthValue
_Ltp8xONTTemplateOverridesAllocProfile6_Object = MibTableColumn
ltp8xONTTemplateOverridesAllocProfile6 = _Ltp8xONTTemplateOverridesAllocProfile6_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 24, 2, 1, 29),
    _Ltp8xONTTemplateOverridesAllocProfile6_Type()
)
ltp8xONTTemplateOverridesAllocProfile6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTTemplateOverridesAllocProfile6.setStatus("current")
_Ltp8xONTTemplateOverridesAllocProfile7_Type = TruthValue
_Ltp8xONTTemplateOverridesAllocProfile7_Object = MibTableColumn
ltp8xONTTemplateOverridesAllocProfile7 = _Ltp8xONTTemplateOverridesAllocProfile7_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 24, 2, 1, 30),
    _Ltp8xONTTemplateOverridesAllocProfile7_Type()
)
ltp8xONTTemplateOverridesAllocProfile7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTTemplateOverridesAllocProfile7.setStatus("current")
_Ltp8xONTTemplateOverridesPortsProfile_Type = TruthValue
_Ltp8xONTTemplateOverridesPortsProfile_Object = MibTableColumn
ltp8xONTTemplateOverridesPortsProfile = _Ltp8xONTTemplateOverridesPortsProfile_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 24, 2, 1, 31),
    _Ltp8xONTTemplateOverridesPortsProfile_Type()
)
ltp8xONTTemplateOverridesPortsProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTTemplateOverridesPortsProfile.setStatus("current")
_Ltp8xONTTemplateOverridesRFPortEnabled_Type = TruthValue
_Ltp8xONTTemplateOverridesRFPortEnabled_Object = MibTableColumn
ltp8xONTTemplateOverridesRFPortEnabled = _Ltp8xONTTemplateOverridesRFPortEnabled_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 24, 2, 1, 32),
    _Ltp8xONTTemplateOverridesRFPortEnabled_Type()
)
ltp8xONTTemplateOverridesRFPortEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTTemplateOverridesRFPortEnabled.setStatus("current")
_Ltp8xONTTemplateOverridesScriptingProfile_Type = TruthValue
_Ltp8xONTTemplateOverridesScriptingProfile_Object = MibTableColumn
ltp8xONTTemplateOverridesScriptingProfile = _Ltp8xONTTemplateOverridesScriptingProfile_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 24, 2, 1, 36),
    _Ltp8xONTTemplateOverridesScriptingProfile_Type()
)
ltp8xONTTemplateOverridesScriptingProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTTemplateOverridesScriptingProfile.setStatus("current")
_Ltp8xONTTemplateOverridesBerInterval_Type = TruthValue
_Ltp8xONTTemplateOverridesBerInterval_Object = MibTableColumn
ltp8xONTTemplateOverridesBerInterval = _Ltp8xONTTemplateOverridesBerInterval_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 24, 2, 1, 37),
    _Ltp8xONTTemplateOverridesBerInterval_Type()
)
ltp8xONTTemplateOverridesBerInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTTemplateOverridesBerInterval.setStatus("current")
_Ltp8xONTTemplateOverridesBerUpdatePeriod_Type = TruthValue
_Ltp8xONTTemplateOverridesBerUpdatePeriod_Object = MibTableColumn
ltp8xONTTemplateOverridesBerUpdatePeriod = _Ltp8xONTTemplateOverridesBerUpdatePeriod_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 24, 2, 1, 38),
    _Ltp8xONTTemplateOverridesBerUpdatePeriod_Type()
)
ltp8xONTTemplateOverridesBerUpdatePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTTemplateOverridesBerUpdatePeriod.setStatus("current")
_Ltp8xONTTemplateOverridesOMCIErrorTolerant_Type = TruthValue
_Ltp8xONTTemplateOverridesOMCIErrorTolerant_Object = MibTableColumn
ltp8xONTTemplateOverridesOMCIErrorTolerant = _Ltp8xONTTemplateOverridesOMCIErrorTolerant_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 24, 2, 1, 39),
    _Ltp8xONTTemplateOverridesOMCIErrorTolerant_Type()
)
ltp8xONTTemplateOverridesOMCIErrorTolerant.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTTemplateOverridesOMCIErrorTolerant.setStatus("current")
_Ltp8xONTTemplateServicesValuesTable_Object = MibTable
ltp8xONTTemplateServicesValuesTable = _Ltp8xONTTemplateServicesValuesTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 24, 10)
)
if mibBuilder.loadTexts:
    ltp8xONTTemplateServicesValuesTable.setStatus("current")
_Ltp8xONTTemplateServicesValuesEntry_Object = MibTableRow
ltp8xONTTemplateServicesValuesEntry = _Ltp8xONTTemplateServicesValuesEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 24, 10, 1)
)
ltp8xONTTemplateServicesValuesEntry.setIndexNames(
    (0, "ELTEX-LTP8X", "ltp8xONTTemplateValuesID"),
    (0, "ELTEX-LTP8X", "ltp8xONTTemplateServicesValuesServiceID"),
)
if mibBuilder.loadTexts:
    ltp8xONTTemplateServicesValuesEntry.setStatus("current")
_Ltp8xONTTemplateServicesValuesServiceID_Type = Unsigned32
_Ltp8xONTTemplateServicesValuesServiceID_Object = MibTableColumn
ltp8xONTTemplateServicesValuesServiceID = _Ltp8xONTTemplateServicesValuesServiceID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 24, 10, 1, 1),
    _Ltp8xONTTemplateServicesValuesServiceID_Type()
)
ltp8xONTTemplateServicesValuesServiceID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ltp8xONTTemplateServicesValuesServiceID.setStatus("current")
_Ltp8xONTTemplateServicesValuesCrossConnectProfile_Type = Unsigned32
_Ltp8xONTTemplateServicesValuesCrossConnectProfile_Object = MibTableColumn
ltp8xONTTemplateServicesValuesCrossConnectProfile = _Ltp8xONTTemplateServicesValuesCrossConnectProfile_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 24, 10, 1, 2),
    _Ltp8xONTTemplateServicesValuesCrossConnectProfile_Type()
)
ltp8xONTTemplateServicesValuesCrossConnectProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTTemplateServicesValuesCrossConnectProfile.setStatus("current")
_Ltp8xONTTemplateServicesValuesDBAProfile_Type = Unsigned32
_Ltp8xONTTemplateServicesValuesDBAProfile_Object = MibTableColumn
ltp8xONTTemplateServicesValuesDBAProfile = _Ltp8xONTTemplateServicesValuesDBAProfile_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 24, 10, 1, 3),
    _Ltp8xONTTemplateServicesValuesDBAProfile_Type()
)
ltp8xONTTemplateServicesValuesDBAProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTTemplateServicesValuesDBAProfile.setStatus("current")
_Ltp8xONTTemplateServicesOverridesTable_Object = MibTable
ltp8xONTTemplateServicesOverridesTable = _Ltp8xONTTemplateServicesOverridesTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 24, 11)
)
if mibBuilder.loadTexts:
    ltp8xONTTemplateServicesOverridesTable.setStatus("current")
_Ltp8xONTTemplateServicesOverridesEntry_Object = MibTableRow
ltp8xONTTemplateServicesOverridesEntry = _Ltp8xONTTemplateServicesOverridesEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 24, 11, 1)
)
ltp8xONTTemplateServicesOverridesEntry.setIndexNames(
    (0, "ELTEX-LTP8X", "ltp8xONTTemplateValuesID"),
    (0, "ELTEX-LTP8X", "ltp8xONTTemplateServicesOverridesServiceID"),
)
if mibBuilder.loadTexts:
    ltp8xONTTemplateServicesOverridesEntry.setStatus("current")
_Ltp8xONTTemplateServicesOverridesServiceID_Type = Unsigned32
_Ltp8xONTTemplateServicesOverridesServiceID_Object = MibTableColumn
ltp8xONTTemplateServicesOverridesServiceID = _Ltp8xONTTemplateServicesOverridesServiceID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 24, 11, 1, 1),
    _Ltp8xONTTemplateServicesOverridesServiceID_Type()
)
ltp8xONTTemplateServicesOverridesServiceID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ltp8xONTTemplateServicesOverridesServiceID.setStatus("current")
_Ltp8xONTTemplateServicesOverridesCrossConnectProfile_Type = TruthValue
_Ltp8xONTTemplateServicesOverridesCrossConnectProfile_Object = MibTableColumn
ltp8xONTTemplateServicesOverridesCrossConnectProfile = _Ltp8xONTTemplateServicesOverridesCrossConnectProfile_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 24, 11, 1, 2),
    _Ltp8xONTTemplateServicesOverridesCrossConnectProfile_Type()
)
ltp8xONTTemplateServicesOverridesCrossConnectProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTTemplateServicesOverridesCrossConnectProfile.setStatus("current")
_Ltp8xONTTemplateServicesOverridesDBAProfile_Type = TruthValue
_Ltp8xONTTemplateServicesOverridesDBAProfile_Object = MibTableColumn
ltp8xONTTemplateServicesOverridesDBAProfile = _Ltp8xONTTemplateServicesOverridesDBAProfile_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 24, 11, 1, 3),
    _Ltp8xONTTemplateServicesOverridesDBAProfile_Type()
)
ltp8xONTTemplateServicesOverridesDBAProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTTemplateServicesOverridesDBAProfile.setStatus("current")
_Ltp8xONTFullServicesConfigTable_Object = MibTable
ltp8xONTFullServicesConfigTable = _Ltp8xONTFullServicesConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 25)
)
if mibBuilder.loadTexts:
    ltp8xONTFullServicesConfigTable.setStatus("current")
_Ltp8xONTFullServicesConfigEntry_Object = MibTableRow
ltp8xONTFullServicesConfigEntry = _Ltp8xONTFullServicesConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 25, 1)
)
ltp8xONTFullServicesConfigEntry.setIndexNames(
    (0, "ELTEX-LTP8X", "ltp8xONTFullServicesConfigSlot"),
    (0, "ELTEX-LTP8X", "ltp8xONTFullServicesConfigSerial"),
    (0, "ELTEX-LTP8X", "ltp8xONTFullServicesConfigServiceID"),
)
if mibBuilder.loadTexts:
    ltp8xONTFullServicesConfigEntry.setStatus("current")
_Ltp8xONTFullServicesConfigSlot_Type = Unsigned32
_Ltp8xONTFullServicesConfigSlot_Object = MibTableColumn
ltp8xONTFullServicesConfigSlot = _Ltp8xONTFullServicesConfigSlot_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 25, 1, 1),
    _Ltp8xONTFullServicesConfigSlot_Type()
)
ltp8xONTFullServicesConfigSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ltp8xONTFullServicesConfigSlot.setStatus("current")
_Ltp8xONTFullServicesConfigSerial_Type = ONTSerial
_Ltp8xONTFullServicesConfigSerial_Object = MibTableColumn
ltp8xONTFullServicesConfigSerial = _Ltp8xONTFullServicesConfigSerial_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 25, 1, 2),
    _Ltp8xONTFullServicesConfigSerial_Type()
)
ltp8xONTFullServicesConfigSerial.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ltp8xONTFullServicesConfigSerial.setStatus("current")
_Ltp8xONTFullServicesConfigServiceID_Type = Unsigned32
_Ltp8xONTFullServicesConfigServiceID_Object = MibTableColumn
ltp8xONTFullServicesConfigServiceID = _Ltp8xONTFullServicesConfigServiceID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 25, 1, 3),
    _Ltp8xONTFullServicesConfigServiceID_Type()
)
ltp8xONTFullServicesConfigServiceID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ltp8xONTFullServicesConfigServiceID.setStatus("current")
_Ltp8xONTFullServicesConfigCrossConnectProfile_Type = Unsigned32
_Ltp8xONTFullServicesConfigCrossConnectProfile_Object = MibTableColumn
ltp8xONTFullServicesConfigCrossConnectProfile = _Ltp8xONTFullServicesConfigCrossConnectProfile_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 25, 1, 4),
    _Ltp8xONTFullServicesConfigCrossConnectProfile_Type()
)
ltp8xONTFullServicesConfigCrossConnectProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTFullServicesConfigCrossConnectProfile.setStatus("current")
_Ltp8xONTFullServicesConfigDBAProfile_Type = Unsigned32
_Ltp8xONTFullServicesConfigDBAProfile_Object = MibTableColumn
ltp8xONTFullServicesConfigDBAProfile = _Ltp8xONTFullServicesConfigDBAProfile_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 25, 1, 5),
    _Ltp8xONTFullServicesConfigDBAProfile_Type()
)
ltp8xONTFullServicesConfigDBAProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTFullServicesConfigDBAProfile.setStatus("current")
_Ltp8xONTSelectiveTunnelTable_Object = MibTable
ltp8xONTSelectiveTunnelTable = _Ltp8xONTSelectiveTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 26)
)
if mibBuilder.loadTexts:
    ltp8xONTSelectiveTunnelTable.setStatus("current")
_Ltp8xONTSelectiveTunnelEntry_Object = MibTableRow
ltp8xONTSelectiveTunnelEntry = _Ltp8xONTSelectiveTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 26, 1)
)
ltp8xONTSelectiveTunnelEntry.setIndexNames(
    (0, "ELTEX-LTP8X", "ltp8xONTSelectiveTunnelSlot"),
    (0, "ELTEX-LTP8X", "ltp8xONTSelectiveTunnelSerial"),
    (0, "ELTEX-LTP8X", "ltp8xONTSelectiveTunnelServiceID"),
    (0, "ELTEX-LTP8X", "ltp8xONTSelectiveTunnelUVIDIndex"),
)
if mibBuilder.loadTexts:
    ltp8xONTSelectiveTunnelEntry.setStatus("current")
_Ltp8xONTSelectiveTunnelSlot_Type = Unsigned32
_Ltp8xONTSelectiveTunnelSlot_Object = MibTableColumn
ltp8xONTSelectiveTunnelSlot = _Ltp8xONTSelectiveTunnelSlot_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 26, 1, 1),
    _Ltp8xONTSelectiveTunnelSlot_Type()
)
ltp8xONTSelectiveTunnelSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ltp8xONTSelectiveTunnelSlot.setStatus("current")
_Ltp8xONTSelectiveTunnelSerial_Type = ONTSerial
_Ltp8xONTSelectiveTunnelSerial_Object = MibTableColumn
ltp8xONTSelectiveTunnelSerial = _Ltp8xONTSelectiveTunnelSerial_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 26, 1, 2),
    _Ltp8xONTSelectiveTunnelSerial_Type()
)
ltp8xONTSelectiveTunnelSerial.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ltp8xONTSelectiveTunnelSerial.setStatus("current")
_Ltp8xONTSelectiveTunnelServiceID_Type = Unsigned32
_Ltp8xONTSelectiveTunnelServiceID_Object = MibTableColumn
ltp8xONTSelectiveTunnelServiceID = _Ltp8xONTSelectiveTunnelServiceID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 26, 1, 3),
    _Ltp8xONTSelectiveTunnelServiceID_Type()
)
ltp8xONTSelectiveTunnelServiceID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ltp8xONTSelectiveTunnelServiceID.setStatus("current")
_Ltp8xONTSelectiveTunnelUVIDIndex_Type = Unsigned32
_Ltp8xONTSelectiveTunnelUVIDIndex_Object = MibTableColumn
ltp8xONTSelectiveTunnelUVIDIndex = _Ltp8xONTSelectiveTunnelUVIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 26, 1, 4),
    _Ltp8xONTSelectiveTunnelUVIDIndex_Type()
)
ltp8xONTSelectiveTunnelUVIDIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ltp8xONTSelectiveTunnelUVIDIndex.setStatus("current")
_Ltp8xONTSelectiveTunnelUVID_Type = Integer32
_Ltp8xONTSelectiveTunnelUVID_Object = MibTableColumn
ltp8xONTSelectiveTunnelUVID = _Ltp8xONTSelectiveTunnelUVID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 26, 1, 5),
    _Ltp8xONTSelectiveTunnelUVID_Type()
)
ltp8xONTSelectiveTunnelUVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTSelectiveTunnelUVID.setStatus("current")
_Ltp8xONTFirmwares_ObjectIdentity = ObjectIdentity
ltp8xONTFirmwares = _Ltp8xONTFirmwares_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 30)
)
_Ltp8xONTFirmwaresFilesTable_Object = MibTable
ltp8xONTFirmwaresFilesTable = _Ltp8xONTFirmwaresFilesTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 30, 1)
)
if mibBuilder.loadTexts:
    ltp8xONTFirmwaresFilesTable.setStatus("current")
_Ltp8xONTFirmwaresFilesEntry_Object = MibTableRow
ltp8xONTFirmwaresFilesEntry = _Ltp8xONTFirmwaresFilesEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 30, 1, 1)
)
ltp8xONTFirmwaresFilesEntry.setIndexNames(
    (0, "ELTEX-LTP8X", "ltp8xONTFirmwaresFilesEntryID"),
)
if mibBuilder.loadTexts:
    ltp8xONTFirmwaresFilesEntry.setStatus("current")


class _Ltp8xONTFirmwaresFilesEntryID_Type(Integer32):
    """Custom type ltp8xONTFirmwaresFilesEntryID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Ltp8xONTFirmwaresFilesEntryID_Type.__name__ = "Integer32"
_Ltp8xONTFirmwaresFilesEntryID_Object = MibTableColumn
ltp8xONTFirmwaresFilesEntryID = _Ltp8xONTFirmwaresFilesEntryID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 30, 1, 1, 1),
    _Ltp8xONTFirmwaresFilesEntryID_Type()
)
ltp8xONTFirmwaresFilesEntryID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTFirmwaresFilesEntryID.setStatus("current")
_Ltp8xONTFirmwaresFilesName_Type = DisplayString
_Ltp8xONTFirmwaresFilesName_Object = MibTableColumn
ltp8xONTFirmwaresFilesName = _Ltp8xONTFirmwaresFilesName_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 30, 1, 1, 2),
    _Ltp8xONTFirmwaresFilesName_Type()
)
ltp8xONTFirmwaresFilesName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTFirmwaresFilesName.setStatus("current")
_Ltp8xONTFirmwaresFilesVersion_Type = DisplayString
_Ltp8xONTFirmwaresFilesVersion_Object = MibTableColumn
ltp8xONTFirmwaresFilesVersion = _Ltp8xONTFirmwaresFilesVersion_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 30, 1, 1, 3),
    _Ltp8xONTFirmwaresFilesVersion_Type()
)
ltp8xONTFirmwaresFilesVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTFirmwaresFilesVersion.setStatus("current")
_Ltp8xONTFirmwaresFilesHardware_Type = DisplayString
_Ltp8xONTFirmwaresFilesHardware_Object = MibTableColumn
ltp8xONTFirmwaresFilesHardware = _Ltp8xONTFirmwaresFilesHardware_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 30, 1, 1, 4),
    _Ltp8xONTFirmwaresFilesHardware_Type()
)
ltp8xONTFirmwaresFilesHardware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTFirmwaresFilesHardware.setStatus("current")
_Ltp8xONTFirmwaresFilesDelete_Type = Unsigned32
_Ltp8xONTFirmwaresFilesDelete_Object = MibTableColumn
ltp8xONTFirmwaresFilesDelete = _Ltp8xONTFirmwaresFilesDelete_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 30, 1, 1, 10),
    _Ltp8xONTFirmwaresFilesDelete_Type()
)
ltp8xONTFirmwaresFilesDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTFirmwaresFilesDelete.setStatus("current")
_Ltp8xONTFirmwaresTable_Object = MibTable
ltp8xONTFirmwaresTable = _Ltp8xONTFirmwaresTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 30, 2)
)
if mibBuilder.loadTexts:
    ltp8xONTFirmwaresTable.setStatus("current")
_Ltp8xONTFirmwaresEntry_Object = MibTableRow
ltp8xONTFirmwaresEntry = _Ltp8xONTFirmwaresEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 30, 2, 1)
)
ltp8xONTFirmwaresEntry.setIndexNames(
    (0, "ELTEX-LTP8X", "ltp8xONTFirmwaresEntryID"),
)
if mibBuilder.loadTexts:
    ltp8xONTFirmwaresEntry.setStatus("current")


class _Ltp8xONTFirmwaresEntryID_Type(Integer32):
    """Custom type ltp8xONTFirmwaresEntryID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Ltp8xONTFirmwaresEntryID_Type.__name__ = "Integer32"
_Ltp8xONTFirmwaresEntryID_Object = MibTableColumn
ltp8xONTFirmwaresEntryID = _Ltp8xONTFirmwaresEntryID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 30, 2, 1, 1),
    _Ltp8xONTFirmwaresEntryID_Type()
)
ltp8xONTFirmwaresEntryID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTFirmwaresEntryID.setStatus("current")
_Ltp8xONTFirmwaresName_Type = DisplayString
_Ltp8xONTFirmwaresName_Object = MibTableColumn
ltp8xONTFirmwaresName = _Ltp8xONTFirmwaresName_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 30, 2, 1, 2),
    _Ltp8xONTFirmwaresName_Type()
)
ltp8xONTFirmwaresName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTFirmwaresName.setStatus("current")
_Ltp8xONTFirmwaresVersion_Type = DisplayString
_Ltp8xONTFirmwaresVersion_Object = MibTableColumn
ltp8xONTFirmwaresVersion = _Ltp8xONTFirmwaresVersion_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 30, 2, 1, 3),
    _Ltp8xONTFirmwaresVersion_Type()
)
ltp8xONTFirmwaresVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTFirmwaresVersion.setStatus("current")
_Ltp8xONTFirmwaresHardware_Type = DisplayString
_Ltp8xONTFirmwaresHardware_Object = MibTableColumn
ltp8xONTFirmwaresHardware = _Ltp8xONTFirmwaresHardware_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 30, 2, 1, 4),
    _Ltp8xONTFirmwaresHardware_Type()
)
ltp8xONTFirmwaresHardware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTFirmwaresHardware.setStatus("current")
_Ltp8xONTFirmwaresURL_Type = DisplayString
_Ltp8xONTFirmwaresURL_Object = MibTableColumn
ltp8xONTFirmwaresURL = _Ltp8xONTFirmwaresURL_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 30, 2, 1, 5),
    _Ltp8xONTFirmwaresURL_Type()
)
ltp8xONTFirmwaresURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTFirmwaresURL.setStatus("current")
_Ltp8xONTFirmwaresScheduler_Type = TruthValue
_Ltp8xONTFirmwaresScheduler_Object = MibTableColumn
ltp8xONTFirmwaresScheduler = _Ltp8xONTFirmwaresScheduler_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 30, 2, 1, 6),
    _Ltp8xONTFirmwaresScheduler_Type()
)
ltp8xONTFirmwaresScheduler.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTFirmwaresScheduler.setStatus("current")
_Ltp8xONTFirmwaresSafeMode_Type = TruthValue
_Ltp8xONTFirmwaresSafeMode_Object = MibTableColumn
ltp8xONTFirmwaresSafeMode = _Ltp8xONTFirmwaresSafeMode_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 30, 2, 1, 7),
    _Ltp8xONTFirmwaresSafeMode_Type()
)
ltp8xONTFirmwaresSafeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTFirmwaresSafeMode.setStatus("current")
_Ltp8xONTFirmwaresDowngrade_Type = TruthValue
_Ltp8xONTFirmwaresDowngrade_Object = MibTableColumn
ltp8xONTFirmwaresDowngrade = _Ltp8xONTFirmwaresDowngrade_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 30, 2, 1, 8),
    _Ltp8xONTFirmwaresDowngrade_Type()
)
ltp8xONTFirmwaresDowngrade.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTFirmwaresDowngrade.setStatus("current")
_Ltp8xONTFirmwaresRowStatus_Type = RowStatus
_Ltp8xONTFirmwaresRowStatus_Object = MibTableColumn
ltp8xONTFirmwaresRowStatus = _Ltp8xONTFirmwaresRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 30, 2, 1, 10),
    _Ltp8xONTFirmwaresRowStatus_Type()
)
ltp8xONTFirmwaresRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ltp8xONTFirmwaresRowStatus.setStatus("current")
_Ltp8xONTFirmwaresProfilesTable_Object = MibTable
ltp8xONTFirmwaresProfilesTable = _Ltp8xONTFirmwaresProfilesTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 30, 3)
)
if mibBuilder.loadTexts:
    ltp8xONTFirmwaresProfilesTable.setStatus("current")
_Ltp8xONTFirmwaresProfilesEntry_Object = MibTableRow
ltp8xONTFirmwaresProfilesEntry = _Ltp8xONTFirmwaresProfilesEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 30, 3, 1)
)
ltp8xONTFirmwaresProfilesEntry.setIndexNames(
    (0, "ELTEX-LTP8X", "ltp8xONTFirmwaresProfilesFWID"),
    (0, "ELTEX-LTP8X", "ltp8xONTFirmwaresProfilesName"),
)
if mibBuilder.loadTexts:
    ltp8xONTFirmwaresProfilesEntry.setStatus("current")


class _Ltp8xONTFirmwaresProfilesFWID_Type(Integer32):
    """Custom type ltp8xONTFirmwaresProfilesFWID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Ltp8xONTFirmwaresProfilesFWID_Type.__name__ = "Integer32"
_Ltp8xONTFirmwaresProfilesFWID_Object = MibTableColumn
ltp8xONTFirmwaresProfilesFWID = _Ltp8xONTFirmwaresProfilesFWID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 30, 3, 1, 1),
    _Ltp8xONTFirmwaresProfilesFWID_Type()
)
ltp8xONTFirmwaresProfilesFWID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTFirmwaresProfilesFWID.setStatus("current")
_Ltp8xONTFirmwaresProfilesName_Type = DisplayString
_Ltp8xONTFirmwaresProfilesName_Object = MibTableColumn
ltp8xONTFirmwaresProfilesName = _Ltp8xONTFirmwaresProfilesName_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 30, 3, 1, 2),
    _Ltp8xONTFirmwaresProfilesName_Type()
)
ltp8xONTFirmwaresProfilesName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTFirmwaresProfilesName.setStatus("current")
_Ltp8xONTFirmwaresProfilesRowStatus_Type = RowStatus
_Ltp8xONTFirmwaresProfilesRowStatus_Object = MibTableColumn
ltp8xONTFirmwaresProfilesRowStatus = _Ltp8xONTFirmwaresProfilesRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 30, 3, 1, 10),
    _Ltp8xONTFirmwaresProfilesRowStatus_Type()
)
ltp8xONTFirmwaresProfilesRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ltp8xONTFirmwaresProfilesRowStatus.setStatus("current")
_Ltp8xONTFirmwaresSchedulerConfig_ObjectIdentity = ObjectIdentity
ltp8xONTFirmwaresSchedulerConfig = _Ltp8xONTFirmwaresSchedulerConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 30, 5)
)
_Ltp8xONTFirmwaresSchedulerDailyFrom_Type = DisplayString
_Ltp8xONTFirmwaresSchedulerDailyFrom_Object = MibScalar
ltp8xONTFirmwaresSchedulerDailyFrom = _Ltp8xONTFirmwaresSchedulerDailyFrom_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 30, 5, 1),
    _Ltp8xONTFirmwaresSchedulerDailyFrom_Type()
)
ltp8xONTFirmwaresSchedulerDailyFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTFirmwaresSchedulerDailyFrom.setStatus("current")
_Ltp8xONTFirmwaresSchedulerDailyTo_Type = DisplayString
_Ltp8xONTFirmwaresSchedulerDailyTo_Object = MibScalar
ltp8xONTFirmwaresSchedulerDailyTo = _Ltp8xONTFirmwaresSchedulerDailyTo_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 30, 5, 2),
    _Ltp8xONTFirmwaresSchedulerDailyTo_Type()
)
ltp8xONTFirmwaresSchedulerDailyTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTFirmwaresSchedulerDailyTo.setStatus("current")
_Ltp8xONTFirmwaresSchedulerPeriodFrom_Type = DisplayString
_Ltp8xONTFirmwaresSchedulerPeriodFrom_Object = MibScalar
ltp8xONTFirmwaresSchedulerPeriodFrom = _Ltp8xONTFirmwaresSchedulerPeriodFrom_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 30, 5, 3),
    _Ltp8xONTFirmwaresSchedulerPeriodFrom_Type()
)
ltp8xONTFirmwaresSchedulerPeriodFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTFirmwaresSchedulerPeriodFrom.setStatus("current")
_Ltp8xONTFirmwaresSchedulerPeriodTo_Type = DisplayString
_Ltp8xONTFirmwaresSchedulerPeriodTo_Object = MibScalar
ltp8xONTFirmwaresSchedulerPeriodTo = _Ltp8xONTFirmwaresSchedulerPeriodTo_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 30, 5, 4),
    _Ltp8xONTFirmwaresSchedulerPeriodTo_Type()
)
ltp8xONTFirmwaresSchedulerPeriodTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTFirmwaresSchedulerPeriodTo.setStatus("current")
_Ltp8xONTFirmwaresSchedulerWeeklyFrom_Type = Unsigned32
_Ltp8xONTFirmwaresSchedulerWeeklyFrom_Object = MibScalar
ltp8xONTFirmwaresSchedulerWeeklyFrom = _Ltp8xONTFirmwaresSchedulerWeeklyFrom_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 30, 5, 5),
    _Ltp8xONTFirmwaresSchedulerWeeklyFrom_Type()
)
ltp8xONTFirmwaresSchedulerWeeklyFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTFirmwaresSchedulerWeeklyFrom.setStatus("current")
_Ltp8xONTFirmwaresSchedulerWeeklyTo_Type = Unsigned32
_Ltp8xONTFirmwaresSchedulerWeeklyTo_Object = MibScalar
ltp8xONTFirmwaresSchedulerWeeklyTo = _Ltp8xONTFirmwaresSchedulerWeeklyTo_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 30, 5, 6),
    _Ltp8xONTFirmwaresSchedulerWeeklyTo_Type()
)
ltp8xONTFirmwaresSchedulerWeeklyTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTFirmwaresSchedulerWeeklyTo.setStatus("current")
_Ltp8xONTFirmwaresSpecificsTable_Object = MibTable
ltp8xONTFirmwaresSpecificsTable = _Ltp8xONTFirmwaresSpecificsTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 30, 7)
)
if mibBuilder.loadTexts:
    ltp8xONTFirmwaresSpecificsTable.setStatus("current")
_Ltp8xONTFirmwaresSpecificsEntry_Object = MibTableRow
ltp8xONTFirmwaresSpecificsEntry = _Ltp8xONTFirmwaresSpecificsEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 30, 7, 1)
)
ltp8xONTFirmwaresSpecificsEntry.setIndexNames(
    (0, "ELTEX-LTP8X", "ltp8xONTFirmwaresSpecificsName"),
)
if mibBuilder.loadTexts:
    ltp8xONTFirmwaresSpecificsEntry.setStatus("current")


class _Ltp8xONTFirmwaresSpecificsName_Type(DisplayString):
    """Custom type ltp8xONTFirmwaresSpecificsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Ltp8xONTFirmwaresSpecificsName_Type.__name__ = "DisplayString"
_Ltp8xONTFirmwaresSpecificsName_Object = MibTableColumn
ltp8xONTFirmwaresSpecificsName = _Ltp8xONTFirmwaresSpecificsName_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 30, 7, 1, 1),
    _Ltp8xONTFirmwaresSpecificsName_Type()
)
ltp8xONTFirmwaresSpecificsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTFirmwaresSpecificsName.setStatus("current")
_Ltp8xONTFirmwaresSpecificsVersion_Type = DisplayString
_Ltp8xONTFirmwaresSpecificsVersion_Object = MibTableColumn
ltp8xONTFirmwaresSpecificsVersion = _Ltp8xONTFirmwaresSpecificsVersion_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 30, 7, 1, 2),
    _Ltp8xONTFirmwaresSpecificsVersion_Type()
)
ltp8xONTFirmwaresSpecificsVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTFirmwaresSpecificsVersion.setStatus("current")
_Ltp8xONTFirmwaresSpecificsHardware_Type = DisplayString
_Ltp8xONTFirmwaresSpecificsHardware_Object = MibTableColumn
ltp8xONTFirmwaresSpecificsHardware = _Ltp8xONTFirmwaresSpecificsHardware_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 30, 7, 1, 3),
    _Ltp8xONTFirmwaresSpecificsHardware_Type()
)
ltp8xONTFirmwaresSpecificsHardware.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTFirmwaresSpecificsHardware.setStatus("current")
_Ltp8xONTFirmwaresSpecificsVendor_Type = DisplayString
_Ltp8xONTFirmwaresSpecificsVendor_Object = MibTableColumn
ltp8xONTFirmwaresSpecificsVendor = _Ltp8xONTFirmwaresSpecificsVendor_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 30, 7, 1, 4),
    _Ltp8xONTFirmwaresSpecificsVendor_Type()
)
ltp8xONTFirmwaresSpecificsVendor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTFirmwaresSpecificsVendor.setStatus("current")
_Ltp8xONTFirmwaresSpecificsRowStatus_Type = RowStatus
_Ltp8xONTFirmwaresSpecificsRowStatus_Object = MibTableColumn
ltp8xONTFirmwaresSpecificsRowStatus = _Ltp8xONTFirmwaresSpecificsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 30, 7, 1, 10),
    _Ltp8xONTFirmwaresSpecificsRowStatus_Type()
)
ltp8xONTFirmwaresSpecificsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTFirmwaresSpecificsRowStatus.setStatus("current")
_Ltp8xONTFirmwaresVersionPriorityFile_Type = DisplayString
_Ltp8xONTFirmwaresVersionPriorityFile_Object = MibScalar
ltp8xONTFirmwaresVersionPriorityFile = _Ltp8xONTFirmwaresVersionPriorityFile_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 30, 8),
    _Ltp8xONTFirmwaresVersionPriorityFile_Type()
)
ltp8xONTFirmwaresVersionPriorityFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTFirmwaresVersionPriorityFile.setStatus("current")
_Ltp8xONTFirmwaresDownload_ObjectIdentity = ObjectIdentity
ltp8xONTFirmwaresDownload = _Ltp8xONTFirmwaresDownload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 30, 10)
)
_Ltp8xONTFirmwaresDownloadIPAddress_Type = IpAddress
_Ltp8xONTFirmwaresDownloadIPAddress_Object = MibScalar
ltp8xONTFirmwaresDownloadIPAddress = _Ltp8xONTFirmwaresDownloadIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 30, 10, 1),
    _Ltp8xONTFirmwaresDownloadIPAddress_Type()
)
ltp8xONTFirmwaresDownloadIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTFirmwaresDownloadIPAddress.setStatus("current")
_Ltp8xONTFirmwaresDownloadPath_Type = DisplayString
_Ltp8xONTFirmwaresDownloadPath_Object = MibScalar
ltp8xONTFirmwaresDownloadPath = _Ltp8xONTFirmwaresDownloadPath_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 30, 10, 2),
    _Ltp8xONTFirmwaresDownloadPath_Type()
)
ltp8xONTFirmwaresDownloadPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTFirmwaresDownloadPath.setStatus("current")
_Ltp8xONTFirmwaresDownloadAction_Type = Unsigned32
_Ltp8xONTFirmwaresDownloadAction_Object = MibScalar
ltp8xONTFirmwaresDownloadAction = _Ltp8xONTFirmwaresDownloadAction_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 30, 10, 3),
    _Ltp8xONTFirmwaresDownloadAction_Type()
)
ltp8xONTFirmwaresDownloadAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTFirmwaresDownloadAction.setStatus("current")


class _Ltp8xONTFirmwaresDownloadResult_Type(Integer32):
    """Custom type ltp8xONTFirmwaresDownloadResult based on Integer32"""
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
        *(("failed", 4),
          ("inProgess", 2),
          ("notActive", 1),
          ("success", 3))
    )


_Ltp8xONTFirmwaresDownloadResult_Type.__name__ = "Integer32"
_Ltp8xONTFirmwaresDownloadResult_Object = MibScalar
ltp8xONTFirmwaresDownloadResult = _Ltp8xONTFirmwaresDownloadResult_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 30, 10, 4),
    _Ltp8xONTFirmwaresDownloadResult_Type()
)
ltp8xONTFirmwaresDownloadResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTFirmwaresDownloadResult.setStatus("current")


class _Ltp8xONTFirmwaresDownloadProtocol_Type(Integer32):
    """Custom type ltp8xONTFirmwaresDownloadProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("http", 2),
          ("tftp", 1))
    )


_Ltp8xONTFirmwaresDownloadProtocol_Type.__name__ = "Integer32"
_Ltp8xONTFirmwaresDownloadProtocol_Object = MibScalar
ltp8xONTFirmwaresDownloadProtocol = _Ltp8xONTFirmwaresDownloadProtocol_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 30, 10, 5),
    _Ltp8xONTFirmwaresDownloadProtocol_Type()
)
ltp8xONTFirmwaresDownloadProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTFirmwaresDownloadProtocol.setStatus("current")
_Ltp8xONTFirmwaresDownloadPort_Type = Unsigned32
_Ltp8xONTFirmwaresDownloadPort_Object = MibScalar
ltp8xONTFirmwaresDownloadPort = _Ltp8xONTFirmwaresDownloadPort_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 30, 10, 6),
    _Ltp8xONTFirmwaresDownloadPort_Type()
)
ltp8xONTFirmwaresDownloadPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTFirmwaresDownloadPort.setStatus("current")
_Ltp8xONTFirmwareUpdateViaOMCI_ObjectIdentity = ObjectIdentity
ltp8xONTFirmwareUpdateViaOMCI = _Ltp8xONTFirmwareUpdateViaOMCI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 30, 11)
)
_Ltp8xONTFirmwareUpdateViaOMCISlot_Type = Unsigned32
_Ltp8xONTFirmwareUpdateViaOMCISlot_Object = MibScalar
ltp8xONTFirmwareUpdateViaOMCISlot = _Ltp8xONTFirmwareUpdateViaOMCISlot_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 30, 11, 1),
    _Ltp8xONTFirmwareUpdateViaOMCISlot_Type()
)
ltp8xONTFirmwareUpdateViaOMCISlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTFirmwareUpdateViaOMCISlot.setStatus("current")
_Ltp8xONTFirmwareUpdateViaOMCISerial_Type = ONTSerial
_Ltp8xONTFirmwareUpdateViaOMCISerial_Object = MibScalar
ltp8xONTFirmwareUpdateViaOMCISerial = _Ltp8xONTFirmwareUpdateViaOMCISerial_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 30, 11, 2),
    _Ltp8xONTFirmwareUpdateViaOMCISerial_Type()
)
ltp8xONTFirmwareUpdateViaOMCISerial.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTFirmwareUpdateViaOMCISerial.setStatus("current")
_Ltp8xONTFirmwareUpdateViaOMCIFilename_Type = DisplayString
_Ltp8xONTFirmwareUpdateViaOMCIFilename_Object = MibScalar
ltp8xONTFirmwareUpdateViaOMCIFilename = _Ltp8xONTFirmwareUpdateViaOMCIFilename_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 30, 11, 3),
    _Ltp8xONTFirmwareUpdateViaOMCIFilename_Type()
)
ltp8xONTFirmwareUpdateViaOMCIFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTFirmwareUpdateViaOMCIFilename.setStatus("current")
_Ltp8xONTFirmwareUpdateViaOMCIAction_Type = Unsigned32
_Ltp8xONTFirmwareUpdateViaOMCIAction_Object = MibScalar
ltp8xONTFirmwareUpdateViaOMCIAction = _Ltp8xONTFirmwareUpdateViaOMCIAction_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 30, 11, 4),
    _Ltp8xONTFirmwareUpdateViaOMCIAction_Type()
)
ltp8xONTFirmwareUpdateViaOMCIAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTFirmwareUpdateViaOMCIAction.setStatus("current")
_Ltp8xONTFWUpdateSchedulerTable_Object = MibTable
ltp8xONTFWUpdateSchedulerTable = _Ltp8xONTFWUpdateSchedulerTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 30, 20)
)
if mibBuilder.loadTexts:
    ltp8xONTFWUpdateSchedulerTable.setStatus("current")
_Ltp8xONTFWUpdateSchedulerEntry_Object = MibTableRow
ltp8xONTFWUpdateSchedulerEntry = _Ltp8xONTFWUpdateSchedulerEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 30, 20, 1)
)
ltp8xONTFWUpdateSchedulerEntry.setIndexNames(
    (0, "ELTEX-LTP8X", "ltp8xONTFWUpdateSchedulerSlot"),
    (0, "ELTEX-LTP8X", "ltp8xONTFWUpdateSchedulerTaskID"),
)
if mibBuilder.loadTexts:
    ltp8xONTFWUpdateSchedulerEntry.setStatus("current")
_Ltp8xONTFWUpdateSchedulerSlot_Type = Unsigned32
_Ltp8xONTFWUpdateSchedulerSlot_Object = MibTableColumn
ltp8xONTFWUpdateSchedulerSlot = _Ltp8xONTFWUpdateSchedulerSlot_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 30, 20, 1, 1),
    _Ltp8xONTFWUpdateSchedulerSlot_Type()
)
ltp8xONTFWUpdateSchedulerSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTFWUpdateSchedulerSlot.setStatus("current")
_Ltp8xONTFWUpdateSchedulerTaskID_Type = Unsigned32
_Ltp8xONTFWUpdateSchedulerTaskID_Object = MibTableColumn
ltp8xONTFWUpdateSchedulerTaskID = _Ltp8xONTFWUpdateSchedulerTaskID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 30, 20, 1, 2),
    _Ltp8xONTFWUpdateSchedulerTaskID_Type()
)
ltp8xONTFWUpdateSchedulerTaskID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTFWUpdateSchedulerTaskID.setStatus("current")
_Ltp8xONTFWUpdateSchedulerSerial_Type = ONTSerial
_Ltp8xONTFWUpdateSchedulerSerial_Object = MibTableColumn
ltp8xONTFWUpdateSchedulerSerial = _Ltp8xONTFWUpdateSchedulerSerial_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 30, 20, 1, 3),
    _Ltp8xONTFWUpdateSchedulerSerial_Type()
)
ltp8xONTFWUpdateSchedulerSerial.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTFWUpdateSchedulerSerial.setStatus("current")


class _Ltp8xONTFWUpdateSchedulerTaskState_Type(Integer32):
    """Custom type ltp8xONTFWUpdateSchedulerTaskState based on Integer32"""
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
        *(("done", 3),
          ("failed", 2),
          ("inProgress", 1),
          ("scheduled", 0),
          ("unnecessary", 4))
    )


_Ltp8xONTFWUpdateSchedulerTaskState_Type.__name__ = "Integer32"
_Ltp8xONTFWUpdateSchedulerTaskState_Object = MibTableColumn
ltp8xONTFWUpdateSchedulerTaskState = _Ltp8xONTFWUpdateSchedulerTaskState_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 30, 20, 1, 4),
    _Ltp8xONTFWUpdateSchedulerTaskState_Type()
)
ltp8xONTFWUpdateSchedulerTaskState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTFWUpdateSchedulerTaskState.setStatus("current")
_Ltp8xONTFWUpdateSchedulerFilename_Type = DisplayString
_Ltp8xONTFWUpdateSchedulerFilename_Object = MibTableColumn
ltp8xONTFWUpdateSchedulerFilename = _Ltp8xONTFWUpdateSchedulerFilename_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 30, 20, 1, 5),
    _Ltp8xONTFWUpdateSchedulerFilename_Type()
)
ltp8xONTFWUpdateSchedulerFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTFWUpdateSchedulerFilename.setStatus("current")
_Ltp8xONTFWUpdateSchedulerTries_Type = Unsigned32
_Ltp8xONTFWUpdateSchedulerTries_Object = MibTableColumn
ltp8xONTFWUpdateSchedulerTries = _Ltp8xONTFWUpdateSchedulerTries_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 30, 20, 1, 6),
    _Ltp8xONTFWUpdateSchedulerTries_Type()
)
ltp8xONTFWUpdateSchedulerTries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTFWUpdateSchedulerTries.setStatus("current")
_Ltp8xONTFWUpdateSchedulerONTChannel_Type = Unsigned32
_Ltp8xONTFWUpdateSchedulerONTChannel_Object = MibTableColumn
ltp8xONTFWUpdateSchedulerONTChannel = _Ltp8xONTFWUpdateSchedulerONTChannel_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 30, 20, 1, 7),
    _Ltp8xONTFWUpdateSchedulerONTChannel_Type()
)
ltp8xONTFWUpdateSchedulerONTChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTFWUpdateSchedulerONTChannel.setStatus("current")
_Ltp8xONTFWUpdateSchedulerONTId_Type = Unsigned32
_Ltp8xONTFWUpdateSchedulerONTId_Object = MibTableColumn
ltp8xONTFWUpdateSchedulerONTId = _Ltp8xONTFWUpdateSchedulerONTId_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 30, 20, 1, 8),
    _Ltp8xONTFWUpdateSchedulerONTId_Type()
)
ltp8xONTFWUpdateSchedulerONTId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTFWUpdateSchedulerONTId.setStatus("current")
_Ltp8xONTFWUpdateSchedulerUseSerial_Type = TruthValue
_Ltp8xONTFWUpdateSchedulerUseSerial_Object = MibTableColumn
ltp8xONTFWUpdateSchedulerUseSerial = _Ltp8xONTFWUpdateSchedulerUseSerial_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 30, 20, 1, 9),
    _Ltp8xONTFWUpdateSchedulerUseSerial_Type()
)
ltp8xONTFWUpdateSchedulerUseSerial.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTFWUpdateSchedulerUseSerial.setStatus("current")
_Ltp8xONTFWUpdateSchedulerRowStatus_Type = RowStatus
_Ltp8xONTFWUpdateSchedulerRowStatus_Object = MibTableColumn
ltp8xONTFWUpdateSchedulerRowStatus = _Ltp8xONTFWUpdateSchedulerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 30, 20, 1, 10),
    _Ltp8xONTFWUpdateSchedulerRowStatus_Type()
)
ltp8xONTFWUpdateSchedulerRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTFWUpdateSchedulerRowStatus.setStatus("current")
_Ltp8xONTAutoUpdateTable_Object = MibTable
ltp8xONTAutoUpdateTable = _Ltp8xONTAutoUpdateTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 30, 22)
)
if mibBuilder.loadTexts:
    ltp8xONTAutoUpdateTable.setStatus("current")
_Ltp8xONTAutoUpdateEntry_Object = MibTableRow
ltp8xONTAutoUpdateEntry = _Ltp8xONTAutoUpdateEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 30, 22, 1)
)
ltp8xONTAutoUpdateEntry.setIndexNames(
    (0, "ELTEX-LTP8X", "ltp8xONTAutoUpdateDescription"),
)
if mibBuilder.loadTexts:
    ltp8xONTAutoUpdateEntry.setStatus("current")


class _Ltp8xONTAutoUpdateDescription_Type(DisplayString):
    """Custom type ltp8xONTAutoUpdateDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_Ltp8xONTAutoUpdateDescription_Type.__name__ = "DisplayString"
_Ltp8xONTAutoUpdateDescription_Object = MibTableColumn
ltp8xONTAutoUpdateDescription = _Ltp8xONTAutoUpdateDescription_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 30, 22, 1, 1),
    _Ltp8xONTAutoUpdateDescription_Type()
)
ltp8xONTAutoUpdateDescription.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ltp8xONTAutoUpdateDescription.setStatus("current")


class _Ltp8xONTAutoUpdateEquipmentID_Type(DisplayString):
    """Custom type ltp8xONTAutoUpdateEquipmentID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_Ltp8xONTAutoUpdateEquipmentID_Type.__name__ = "DisplayString"
_Ltp8xONTAutoUpdateEquipmentID_Object = MibTableColumn
ltp8xONTAutoUpdateEquipmentID = _Ltp8xONTAutoUpdateEquipmentID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 30, 22, 1, 2),
    _Ltp8xONTAutoUpdateEquipmentID_Type()
)
ltp8xONTAutoUpdateEquipmentID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTAutoUpdateEquipmentID.setStatus("current")


class _Ltp8xONTAutoUpdateFirmwareVersion_Type(DisplayString):
    """Custom type ltp8xONTAutoUpdateFirmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_Ltp8xONTAutoUpdateFirmwareVersion_Type.__name__ = "DisplayString"
_Ltp8xONTAutoUpdateFirmwareVersion_Object = MibTableColumn
ltp8xONTAutoUpdateFirmwareVersion = _Ltp8xONTAutoUpdateFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 30, 22, 1, 3),
    _Ltp8xONTAutoUpdateFirmwareVersion_Type()
)
ltp8xONTAutoUpdateFirmwareVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTAutoUpdateFirmwareVersion.setStatus("current")
_Ltp8xONTAutoUpdateFilename_Type = DisplayString
_Ltp8xONTAutoUpdateFilename_Object = MibTableColumn
ltp8xONTAutoUpdateFilename = _Ltp8xONTAutoUpdateFilename_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 30, 22, 1, 4),
    _Ltp8xONTAutoUpdateFilename_Type()
)
ltp8xONTAutoUpdateFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTAutoUpdateFilename.setStatus("current")


class _Ltp8xONTAutoUpdateMode_Type(Integer32):
    """Custom type ltp8xONTAutoUpdateMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("global", 3),
          ("immediate", 1),
          ("postpone", 2))
    )


_Ltp8xONTAutoUpdateMode_Type.__name__ = "Integer32"
_Ltp8xONTAutoUpdateMode_Object = MibTableColumn
ltp8xONTAutoUpdateMode = _Ltp8xONTAutoUpdateMode_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 30, 22, 1, 5),
    _Ltp8xONTAutoUpdateMode_Type()
)
ltp8xONTAutoUpdateMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTAutoUpdateMode.setStatus("current")
_Ltp8xONTAutoUpdateFirmwareVersionMatches_Type = TruthValue
_Ltp8xONTAutoUpdateFirmwareVersionMatches_Object = MibTableColumn
ltp8xONTAutoUpdateFirmwareVersionMatches = _Ltp8xONTAutoUpdateFirmwareVersionMatches_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 30, 22, 1, 6),
    _Ltp8xONTAutoUpdateFirmwareVersionMatches_Type()
)
ltp8xONTAutoUpdateFirmwareVersionMatches.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTAutoUpdateFirmwareVersionMatches.setStatus("current")
_Ltp8xONTAutoUpdateDowngrade_Type = TruthValue
_Ltp8xONTAutoUpdateDowngrade_Object = MibTableColumn
ltp8xONTAutoUpdateDowngrade = _Ltp8xONTAutoUpdateDowngrade_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 30, 22, 1, 7),
    _Ltp8xONTAutoUpdateDowngrade_Type()
)
ltp8xONTAutoUpdateDowngrade.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTAutoUpdateDowngrade.setStatus("current")
_Ltp8xONTAutoUpdateRowStatus_Type = RowStatus
_Ltp8xONTAutoUpdateRowStatus_Object = MibTableColumn
ltp8xONTAutoUpdateRowStatus = _Ltp8xONTAutoUpdateRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 30, 22, 1, 10),
    _Ltp8xONTAutoUpdateRowStatus_Type()
)
ltp8xONTAutoUpdateRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTAutoUpdateRowStatus.setStatus("current")


class _Ltp8xONTAutoUpdateEnabled_Type(Integer32):
    """Custom type ltp8xONTAutoUpdateEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("immediate", 1),
          ("postpone", 2))
    )


_Ltp8xONTAutoUpdateEnabled_Type.__name__ = "Integer32"
_Ltp8xONTAutoUpdateEnabled_Object = MibScalar
ltp8xONTAutoUpdateEnabled = _Ltp8xONTAutoUpdateEnabled_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 30, 23),
    _Ltp8xONTAutoUpdateEnabled_Type()
)
ltp8xONTAutoUpdateEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTAutoUpdateEnabled.setStatus("current")
_Ltp8xONTAllocProfileTable_Object = MibTable
ltp8xONTAllocProfileTable = _Ltp8xONTAllocProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 40)
)
if mibBuilder.loadTexts:
    ltp8xONTAllocProfileTable.setStatus("current")
_Ltp8xONTAllocProfileEntry_Object = MibTableRow
ltp8xONTAllocProfileEntry = _Ltp8xONTAllocProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 40, 1)
)
ltp8xONTAllocProfileEntry.setIndexNames(
    (0, "ELTEX-LTP8X", "ltp8xONTAllocID"),
)
if mibBuilder.loadTexts:
    ltp8xONTAllocProfileEntry.setStatus("current")
_Ltp8xONTAllocID_Type = Unsigned32
_Ltp8xONTAllocID_Object = MibTableColumn
ltp8xONTAllocID = _Ltp8xONTAllocID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 40, 1, 1),
    _Ltp8xONTAllocID_Type()
)
ltp8xONTAllocID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTAllocID.setStatus("current")
_Ltp8xONTAllocDescription_Type = DisplayString
_Ltp8xONTAllocDescription_Object = MibTableColumn
ltp8xONTAllocDescription = _Ltp8xONTAllocDescription_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 40, 1, 2),
    _Ltp8xONTAllocDescription_Type()
)
ltp8xONTAllocDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTAllocDescription.setStatus("current")
_Ltp8xONTAllocName_Type = DisplayString
_Ltp8xONTAllocName_Object = MibTableColumn
ltp8xONTAllocName = _Ltp8xONTAllocName_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 40, 1, 3),
    _Ltp8xONTAllocName_Type()
)
ltp8xONTAllocName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTAllocName.setStatus("current")


class _Ltp8xONTAllocServiceClass_Type(Integer32):
    """Custom type ltp8xONTAllocServiceClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("cbr", 3),
          ("data", 0),
          ("periodicAllocation", 4),
          ("type5", 5),
          ("voip", 2))
    )


_Ltp8xONTAllocServiceClass_Type.__name__ = "Integer32"
_Ltp8xONTAllocServiceClass_Object = MibTableColumn
ltp8xONTAllocServiceClass = _Ltp8xONTAllocServiceClass_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 40, 1, 4),
    _Ltp8xONTAllocServiceClass_Type()
)
ltp8xONTAllocServiceClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTAllocServiceClass.setStatus("current")


class _Ltp8xONTAllocStatusReporting_Type(Integer32):
    """Custom type ltp8xONTAllocStatusReporting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nsr", 0),
          ("type0", 1),
          ("type1", 2))
    )


_Ltp8xONTAllocStatusReporting_Type.__name__ = "Integer32"
_Ltp8xONTAllocStatusReporting_Object = MibTableColumn
ltp8xONTAllocStatusReporting = _Ltp8xONTAllocStatusReporting_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 40, 1, 5),
    _Ltp8xONTAllocStatusReporting_Type()
)
ltp8xONTAllocStatusReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTAllocStatusReporting.setStatus("current")
_Ltp8xONTAllocSize_Type = Unsigned32
_Ltp8xONTAllocSize_Object = MibTableColumn
ltp8xONTAllocSize = _Ltp8xONTAllocSize_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 40, 1, 6),
    _Ltp8xONTAllocSize_Type()
)
ltp8xONTAllocSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTAllocSize.setStatus("current")
_Ltp8xONTAllocPeriod_Type = Unsigned32
_Ltp8xONTAllocPeriod_Object = MibTableColumn
ltp8xONTAllocPeriod = _Ltp8xONTAllocPeriod_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 40, 1, 7),
    _Ltp8xONTAllocPeriod_Type()
)
ltp8xONTAllocPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTAllocPeriod.setStatus("current")
_Ltp8xONTAllocFixedBandwidth_Type = Unsigned32
_Ltp8xONTAllocFixedBandwidth_Object = MibTableColumn
ltp8xONTAllocFixedBandwidth = _Ltp8xONTAllocFixedBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 40, 1, 8),
    _Ltp8xONTAllocFixedBandwidth_Type()
)
ltp8xONTAllocFixedBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTAllocFixedBandwidth.setStatus("current")
_Ltp8xONTAllocGuaranteedBandwidth_Type = Unsigned32
_Ltp8xONTAllocGuaranteedBandwidth_Object = MibTableColumn
ltp8xONTAllocGuaranteedBandwidth = _Ltp8xONTAllocGuaranteedBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 40, 1, 9),
    _Ltp8xONTAllocGuaranteedBandwidth_Type()
)
ltp8xONTAllocGuaranteedBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTAllocGuaranteedBandwidth.setStatus("current")
_Ltp8xONTAllocBestEffortBandwidth_Type = Unsigned32
_Ltp8xONTAllocBestEffortBandwidth_Object = MibTableColumn
ltp8xONTAllocBestEffortBandwidth = _Ltp8xONTAllocBestEffortBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 40, 1, 10),
    _Ltp8xONTAllocBestEffortBandwidth_Type()
)
ltp8xONTAllocBestEffortBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTAllocBestEffortBandwidth.setStatus("current")
_Ltp8xONTAllocRowStatus_Type = RowStatus
_Ltp8xONTAllocRowStatus_Object = MibTableColumn
ltp8xONTAllocRowStatus = _Ltp8xONTAllocRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 40, 1, 20),
    _Ltp8xONTAllocRowStatus_Type()
)
ltp8xONTAllocRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTAllocRowStatus.setStatus("current")
_Ltp8xONTPortsProfileTable_Object = MibTable
ltp8xONTPortsProfileTable = _Ltp8xONTPortsProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 41)
)
if mibBuilder.loadTexts:
    ltp8xONTPortsProfileTable.setStatus("current")
_Ltp8xONTPortsProfileEntry_Object = MibTableRow
ltp8xONTPortsProfileEntry = _Ltp8xONTPortsProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 41, 1)
)
ltp8xONTPortsProfileEntry.setIndexNames(
    (0, "ELTEX-LTP8X", "ltp8xONTPortsID"),
)
if mibBuilder.loadTexts:
    ltp8xONTPortsProfileEntry.setStatus("current")
_Ltp8xONTPortsID_Type = Unsigned32
_Ltp8xONTPortsID_Object = MibTableColumn
ltp8xONTPortsID = _Ltp8xONTPortsID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 41, 1, 1),
    _Ltp8xONTPortsID_Type()
)
ltp8xONTPortsID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTPortsID.setStatus("current")
_Ltp8xONTPortsDescription_Type = DisplayString
_Ltp8xONTPortsDescription_Object = MibTableColumn
ltp8xONTPortsDescription = _Ltp8xONTPortsDescription_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 41, 1, 2),
    _Ltp8xONTPortsDescription_Type()
)
ltp8xONTPortsDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTPortsDescription.setStatus("current")
_Ltp8xONTPortsName_Type = DisplayString
_Ltp8xONTPortsName_Object = MibTableColumn
ltp8xONTPortsName = _Ltp8xONTPortsName_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 41, 1, 3),
    _Ltp8xONTPortsName_Type()
)
ltp8xONTPortsName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTPortsName.setStatus("current")
_Ltp8xONTPortsIGMPVersion_Type = Unsigned32
_Ltp8xONTPortsIGMPVersion_Object = MibTableColumn
ltp8xONTPortsIGMPVersion = _Ltp8xONTPortsIGMPVersion_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 41, 1, 4),
    _Ltp8xONTPortsIGMPVersion_Type()
)
ltp8xONTPortsIGMPVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTPortsIGMPVersion.setStatus("current")


class _Ltp8xONTPortsIGMPUpstreamMode_Type(Integer32):
    """Custom type ltp8xONTPortsIGMPUpstreamMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("proxy", 2),
          ("snooping", 0),
          ("spr", 1))
    )


_Ltp8xONTPortsIGMPUpstreamMode_Type.__name__ = "Integer32"
_Ltp8xONTPortsIGMPUpstreamMode_Object = MibTableColumn
ltp8xONTPortsIGMPUpstreamMode = _Ltp8xONTPortsIGMPUpstreamMode_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 41, 1, 5),
    _Ltp8xONTPortsIGMPUpstreamMode_Type()
)
ltp8xONTPortsIGMPUpstreamMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTPortsIGMPUpstreamMode.setStatus("current")
_Ltp8xONTPortsIGMPImmediateLeave_Type = TruthValue
_Ltp8xONTPortsIGMPImmediateLeave_Object = MibTableColumn
ltp8xONTPortsIGMPImmediateLeave = _Ltp8xONTPortsIGMPImmediateLeave_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 41, 1, 6),
    _Ltp8xONTPortsIGMPImmediateLeave_Type()
)
ltp8xONTPortsIGMPImmediateLeave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTPortsIGMPImmediateLeave.setStatus("current")
_Ltp8xONTPortsIGMPRobustness_Type = Unsigned32
_Ltp8xONTPortsIGMPRobustness_Object = MibTableColumn
ltp8xONTPortsIGMPRobustness = _Ltp8xONTPortsIGMPRobustness_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 41, 1, 7),
    _Ltp8xONTPortsIGMPRobustness_Type()
)
ltp8xONTPortsIGMPRobustness.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTPortsIGMPRobustness.setStatus("current")
_Ltp8xONTPortsIGMPQuerierIP_Type = IpAddress
_Ltp8xONTPortsIGMPQuerierIP_Object = MibTableColumn
ltp8xONTPortsIGMPQuerierIP = _Ltp8xONTPortsIGMPQuerierIP_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 41, 1, 8),
    _Ltp8xONTPortsIGMPQuerierIP_Type()
)
ltp8xONTPortsIGMPQuerierIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTPortsIGMPQuerierIP.setStatus("current")
_Ltp8xONTPortsIGMPQueryInterval_Type = Unsigned32
_Ltp8xONTPortsIGMPQueryInterval_Object = MibTableColumn
ltp8xONTPortsIGMPQueryInterval = _Ltp8xONTPortsIGMPQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 41, 1, 9),
    _Ltp8xONTPortsIGMPQueryInterval_Type()
)
ltp8xONTPortsIGMPQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTPortsIGMPQueryInterval.setStatus("current")
_Ltp8xONTPortsIGMPQueryMaxResponseTime_Type = Unsigned32
_Ltp8xONTPortsIGMPQueryMaxResponseTime_Object = MibTableColumn
ltp8xONTPortsIGMPQueryMaxResponseTime = _Ltp8xONTPortsIGMPQueryMaxResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 41, 1, 10),
    _Ltp8xONTPortsIGMPQueryMaxResponseTime_Type()
)
ltp8xONTPortsIGMPQueryMaxResponseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTPortsIGMPQueryMaxResponseTime.setStatus("current")
_Ltp8xONTPortsIGMPLastMemberQueryInterval_Type = Unsigned32
_Ltp8xONTPortsIGMPLastMemberQueryInterval_Object = MibTableColumn
ltp8xONTPortsIGMPLastMemberQueryInterval = _Ltp8xONTPortsIGMPLastMemberQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 41, 1, 11),
    _Ltp8xONTPortsIGMPLastMemberQueryInterval_Type()
)
ltp8xONTPortsIGMPLastMemberQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTPortsIGMPLastMemberQueryInterval.setStatus("current")
_Ltp8xONTPortsVEIPMulticastEnable_Type = TruthValue
_Ltp8xONTPortsVEIPMulticastEnable_Object = MibTableColumn
ltp8xONTPortsVEIPMulticastEnable = _Ltp8xONTPortsVEIPMulticastEnable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 41, 1, 12),
    _Ltp8xONTPortsVEIPMulticastEnable_Type()
)
ltp8xONTPortsVEIPMulticastEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTPortsVEIPMulticastEnable.setStatus("current")
_Ltp8xONTPortsVEIPIGMPUpstreamVID_Type = Unsigned32
_Ltp8xONTPortsVEIPIGMPUpstreamVID_Object = MibTableColumn
ltp8xONTPortsVEIPIGMPUpstreamVID = _Ltp8xONTPortsVEIPIGMPUpstreamVID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 41, 1, 13),
    _Ltp8xONTPortsVEIPIGMPUpstreamVID_Type()
)
ltp8xONTPortsVEIPIGMPUpstreamVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTPortsVEIPIGMPUpstreamVID.setStatus("current")
_Ltp8xONTPortsVEIPIGMPUpstreamPriority_Type = Unsigned32
_Ltp8xONTPortsVEIPIGMPUpstreamPriority_Object = MibTableColumn
ltp8xONTPortsVEIPIGMPUpstreamPriority = _Ltp8xONTPortsVEIPIGMPUpstreamPriority_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 41, 1, 14),
    _Ltp8xONTPortsVEIPIGMPUpstreamPriority_Type()
)
ltp8xONTPortsVEIPIGMPUpstreamPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTPortsVEIPIGMPUpstreamPriority.setStatus("current")


class _Ltp8xONTPortsVEIPIGMPUpstreamTagControl_Type(Integer32):
    """Custom type ltp8xONTPortsVEIPIGMPUpstreamTagControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("addTag", 1),
          ("pass", 0),
          ("replaceTag", 2),
          ("replaceVid", 3))
    )


_Ltp8xONTPortsVEIPIGMPUpstreamTagControl_Type.__name__ = "Integer32"
_Ltp8xONTPortsVEIPIGMPUpstreamTagControl_Object = MibTableColumn
ltp8xONTPortsVEIPIGMPUpstreamTagControl = _Ltp8xONTPortsVEIPIGMPUpstreamTagControl_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 41, 1, 15),
    _Ltp8xONTPortsVEIPIGMPUpstreamTagControl_Type()
)
ltp8xONTPortsVEIPIGMPUpstreamTagControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTPortsVEIPIGMPUpstreamTagControl.setStatus("current")
_Ltp8xONTPortsVEIPMaxGroups_Type = Unsigned32
_Ltp8xONTPortsVEIPMaxGroups_Object = MibTableColumn
ltp8xONTPortsVEIPMaxGroups = _Ltp8xONTPortsVEIPMaxGroups_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 41, 1, 16),
    _Ltp8xONTPortsVEIPMaxGroups_Type()
)
ltp8xONTPortsVEIPMaxGroups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTPortsVEIPMaxGroups.setStatus("current")
_Ltp8xONTPortsVEIPMaxMulticastBandwidth_Type = Unsigned32
_Ltp8xONTPortsVEIPMaxMulticastBandwidth_Object = MibTableColumn
ltp8xONTPortsVEIPMaxMulticastBandwidth = _Ltp8xONTPortsVEIPMaxMulticastBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 41, 1, 17),
    _Ltp8xONTPortsVEIPMaxMulticastBandwidth_Type()
)
ltp8xONTPortsVEIPMaxMulticastBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTPortsVEIPMaxMulticastBandwidth.setStatus("current")
_Ltp8xONTPortsRowStatus_Type = RowStatus
_Ltp8xONTPortsRowStatus_Object = MibTableColumn
ltp8xONTPortsRowStatus = _Ltp8xONTPortsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 41, 1, 20),
    _Ltp8xONTPortsRowStatus_Type()
)
ltp8xONTPortsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTPortsRowStatus.setStatus("current")
_Ltp8xONTPortsVEIPIGMPDownstreamVID_Type = Unsigned32
_Ltp8xONTPortsVEIPIGMPDownstreamVID_Object = MibTableColumn
ltp8xONTPortsVEIPIGMPDownstreamVID = _Ltp8xONTPortsVEIPIGMPDownstreamVID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 41, 1, 21),
    _Ltp8xONTPortsVEIPIGMPDownstreamVID_Type()
)
ltp8xONTPortsVEIPIGMPDownstreamVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTPortsVEIPIGMPDownstreamVID.setStatus("current")
_Ltp8xONTPortsVEIPIGMPDownstreamPriority_Type = Unsigned32
_Ltp8xONTPortsVEIPIGMPDownstreamPriority_Object = MibTableColumn
ltp8xONTPortsVEIPIGMPDownstreamPriority = _Ltp8xONTPortsVEIPIGMPDownstreamPriority_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 41, 1, 22),
    _Ltp8xONTPortsVEIPIGMPDownstreamPriority_Type()
)
ltp8xONTPortsVEIPIGMPDownstreamPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTPortsVEIPIGMPDownstreamPriority.setStatus("current")


class _Ltp8xONTPortsVEIPIGMPDownstreamTagControl_Type(Integer32):
    """Custom type ltp8xONTPortsVEIPIGMPDownstreamTagControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("addTag", 2),
          ("addTagSubscriberInfo", 5),
          ("pass", 0),
          ("removeTag", 1),
          ("replaceTag", 3),
          ("replaceTagSubscriberInfo", 6),
          ("replaceVid", 4),
          ("replaceVidSubscriberInfo", 7))
    )


_Ltp8xONTPortsVEIPIGMPDownstreamTagControl_Type.__name__ = "Integer32"
_Ltp8xONTPortsVEIPIGMPDownstreamTagControl_Object = MibTableColumn
ltp8xONTPortsVEIPIGMPDownstreamTagControl = _Ltp8xONTPortsVEIPIGMPDownstreamTagControl_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 41, 1, 23),
    _Ltp8xONTPortsVEIPIGMPDownstreamTagControl_Type()
)
ltp8xONTPortsVEIPIGMPDownstreamTagControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTPortsVEIPIGMPDownstreamTagControl.setStatus("current")


class _Ltp8xONTPortsMulticastIPVersion_Type(Integer32):
    """Custom type ltp8xONTPortsMulticastIPVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 0),
          ("ipv6", 1))
    )


_Ltp8xONTPortsMulticastIPVersion_Type.__name__ = "Integer32"
_Ltp8xONTPortsMulticastIPVersion_Object = MibTableColumn
ltp8xONTPortsMulticastIPVersion = _Ltp8xONTPortsMulticastIPVersion_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 41, 1, 30),
    _Ltp8xONTPortsMulticastIPVersion_Type()
)
ltp8xONTPortsMulticastIPVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTPortsMulticastIPVersion.setStatus("current")
_Ltp8xONTPortsMLDVersion_Type = Unsigned32
_Ltp8xONTPortsMLDVersion_Object = MibTableColumn
ltp8xONTPortsMLDVersion = _Ltp8xONTPortsMLDVersion_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 41, 1, 31),
    _Ltp8xONTPortsMLDVersion_Type()
)
ltp8xONTPortsMLDVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTPortsMLDVersion.setStatus("current")


class _Ltp8xONTPortsMLDUpstreamMode_Type(Integer32):
    """Custom type ltp8xONTPortsMLDUpstreamMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("proxy", 2),
          ("snooping", 0),
          ("spr", 1))
    )


_Ltp8xONTPortsMLDUpstreamMode_Type.__name__ = "Integer32"
_Ltp8xONTPortsMLDUpstreamMode_Object = MibTableColumn
ltp8xONTPortsMLDUpstreamMode = _Ltp8xONTPortsMLDUpstreamMode_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 41, 1, 32),
    _Ltp8xONTPortsMLDUpstreamMode_Type()
)
ltp8xONTPortsMLDUpstreamMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTPortsMLDUpstreamMode.setStatus("current")
_Ltp8xONTPortsMLDImmediateLeave_Type = TruthValue
_Ltp8xONTPortsMLDImmediateLeave_Object = MibTableColumn
ltp8xONTPortsMLDImmediateLeave = _Ltp8xONTPortsMLDImmediateLeave_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 41, 1, 33),
    _Ltp8xONTPortsMLDImmediateLeave_Type()
)
ltp8xONTPortsMLDImmediateLeave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTPortsMLDImmediateLeave.setStatus("current")
_Ltp8xONTPortsMLDRobustness_Type = Unsigned32
_Ltp8xONTPortsMLDRobustness_Object = MibTableColumn
ltp8xONTPortsMLDRobustness = _Ltp8xONTPortsMLDRobustness_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 41, 1, 34),
    _Ltp8xONTPortsMLDRobustness_Type()
)
ltp8xONTPortsMLDRobustness.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTPortsMLDRobustness.setStatus("current")
_Ltp8xONTPortsMLDQuerierIP_Type = Ipv6Address
_Ltp8xONTPortsMLDQuerierIP_Object = MibTableColumn
ltp8xONTPortsMLDQuerierIP = _Ltp8xONTPortsMLDQuerierIP_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 41, 1, 35),
    _Ltp8xONTPortsMLDQuerierIP_Type()
)
ltp8xONTPortsMLDQuerierIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTPortsMLDQuerierIP.setStatus("current")
_Ltp8xONTPortsMLDQueryInterval_Type = Unsigned32
_Ltp8xONTPortsMLDQueryInterval_Object = MibTableColumn
ltp8xONTPortsMLDQueryInterval = _Ltp8xONTPortsMLDQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 41, 1, 36),
    _Ltp8xONTPortsMLDQueryInterval_Type()
)
ltp8xONTPortsMLDQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTPortsMLDQueryInterval.setStatus("current")
_Ltp8xONTPortsMLDQueryMaxResponseTime_Type = Unsigned32
_Ltp8xONTPortsMLDQueryMaxResponseTime_Object = MibTableColumn
ltp8xONTPortsMLDQueryMaxResponseTime = _Ltp8xONTPortsMLDQueryMaxResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 41, 1, 37),
    _Ltp8xONTPortsMLDQueryMaxResponseTime_Type()
)
ltp8xONTPortsMLDQueryMaxResponseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTPortsMLDQueryMaxResponseTime.setStatus("current")
_Ltp8xONTPortsMLDLastMemberQueryInterval_Type = Unsigned32
_Ltp8xONTPortsMLDLastMemberQueryInterval_Object = MibTableColumn
ltp8xONTPortsMLDLastMemberQueryInterval = _Ltp8xONTPortsMLDLastMemberQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 41, 1, 38),
    _Ltp8xONTPortsMLDLastMemberQueryInterval_Type()
)
ltp8xONTPortsMLDLastMemberQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTPortsMLDLastMemberQueryInterval.setStatus("current")
_Ltp8xONTPortsProfileUNITable_Object = MibTable
ltp8xONTPortsProfileUNITable = _Ltp8xONTPortsProfileUNITable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 42)
)
if mibBuilder.loadTexts:
    ltp8xONTPortsProfileUNITable.setStatus("current")
_Ltp8xONTPortsProfileUNIEntry_Object = MibTableRow
ltp8xONTPortsProfileUNIEntry = _Ltp8xONTPortsProfileUNIEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 42, 1)
)
ltp8xONTPortsProfileUNIEntry.setIndexNames(
    (0, "ELTEX-LTP8X", "ltp8xONTPortsID"),
    (0, "ELTEX-LTP8X", "ltp8xONTPortsUNIPort"),
)
if mibBuilder.loadTexts:
    ltp8xONTPortsProfileUNIEntry.setStatus("current")
_Ltp8xONTPortsUNIPort_Type = Unsigned32
_Ltp8xONTPortsUNIPort_Object = MibTableColumn
ltp8xONTPortsUNIPort = _Ltp8xONTPortsUNIPort_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 42, 1, 1),
    _Ltp8xONTPortsUNIPort_Type()
)
ltp8xONTPortsUNIPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTPortsUNIPort.setStatus("current")


class _Ltp8xONTPortsUNIBridgeGroup_Type(Integer32):
    """Custom type ltp8xONTPortsUNIBridgeGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("routed", 0)
    )


_Ltp8xONTPortsUNIBridgeGroup_Type.__name__ = "Integer32"
_Ltp8xONTPortsUNIBridgeGroup_Object = MibTableColumn
ltp8xONTPortsUNIBridgeGroup = _Ltp8xONTPortsUNIBridgeGroup_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 42, 1, 2),
    _Ltp8xONTPortsUNIBridgeGroup_Type()
)
ltp8xONTPortsUNIBridgeGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTPortsUNIBridgeGroup.setStatus("current")
_Ltp8xONTPortsUNIMulticastEnabled_Type = TruthValue
_Ltp8xONTPortsUNIMulticastEnabled_Object = MibTableColumn
ltp8xONTPortsUNIMulticastEnabled = _Ltp8xONTPortsUNIMulticastEnabled_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 42, 1, 3),
    _Ltp8xONTPortsUNIMulticastEnabled_Type()
)
ltp8xONTPortsUNIMulticastEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTPortsUNIMulticastEnabled.setStatus("current")
_Ltp8xONTPortsUNIIGMPUpstreamVID_Type = Unsigned32
_Ltp8xONTPortsUNIIGMPUpstreamVID_Object = MibTableColumn
ltp8xONTPortsUNIIGMPUpstreamVID = _Ltp8xONTPortsUNIIGMPUpstreamVID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 42, 1, 4),
    _Ltp8xONTPortsUNIIGMPUpstreamVID_Type()
)
ltp8xONTPortsUNIIGMPUpstreamVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTPortsUNIIGMPUpstreamVID.setStatus("current")
_Ltp8xONTPortsUNIIGMPUpstreamPriority_Type = Unsigned32
_Ltp8xONTPortsUNIIGMPUpstreamPriority_Object = MibTableColumn
ltp8xONTPortsUNIIGMPUpstreamPriority = _Ltp8xONTPortsUNIIGMPUpstreamPriority_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 42, 1, 5),
    _Ltp8xONTPortsUNIIGMPUpstreamPriority_Type()
)
ltp8xONTPortsUNIIGMPUpstreamPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTPortsUNIIGMPUpstreamPriority.setStatus("current")


class _Ltp8xONTPortsUNIIGMPUpstreamTagControl_Type(Integer32):
    """Custom type ltp8xONTPortsUNIIGMPUpstreamTagControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("addTag", 1),
          ("pass", 0),
          ("replaceTag", 2),
          ("replaceVid", 3))
    )


_Ltp8xONTPortsUNIIGMPUpstreamTagControl_Type.__name__ = "Integer32"
_Ltp8xONTPortsUNIIGMPUpstreamTagControl_Object = MibTableColumn
ltp8xONTPortsUNIIGMPUpstreamTagControl = _Ltp8xONTPortsUNIIGMPUpstreamTagControl_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 42, 1, 6),
    _Ltp8xONTPortsUNIIGMPUpstreamTagControl_Type()
)
ltp8xONTPortsUNIIGMPUpstreamTagControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTPortsUNIIGMPUpstreamTagControl.setStatus("current")
_Ltp8xONTPortsUNIMaxGroups_Type = Unsigned32
_Ltp8xONTPortsUNIMaxGroups_Object = MibTableColumn
ltp8xONTPortsUNIMaxGroups = _Ltp8xONTPortsUNIMaxGroups_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 42, 1, 7),
    _Ltp8xONTPortsUNIMaxGroups_Type()
)
ltp8xONTPortsUNIMaxGroups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTPortsUNIMaxGroups.setStatus("current")
_Ltp8xONTPortsUNIMaxMulticastBandwidth_Type = Unsigned32
_Ltp8xONTPortsUNIMaxMulticastBandwidth_Object = MibTableColumn
ltp8xONTPortsUNIMaxMulticastBandwidth = _Ltp8xONTPortsUNIMaxMulticastBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 42, 1, 8),
    _Ltp8xONTPortsUNIMaxMulticastBandwidth_Type()
)
ltp8xONTPortsUNIMaxMulticastBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTPortsUNIMaxMulticastBandwidth.setStatus("current")
_Ltp8xONTPortsUNIShapingDownstreamEnabled_Type = TruthValue
_Ltp8xONTPortsUNIShapingDownstreamEnabled_Object = MibTableColumn
ltp8xONTPortsUNIShapingDownstreamEnabled = _Ltp8xONTPortsUNIShapingDownstreamEnabled_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 42, 1, 9),
    _Ltp8xONTPortsUNIShapingDownstreamEnabled_Type()
)
ltp8xONTPortsUNIShapingDownstreamEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTPortsUNIShapingDownstreamEnabled.setStatus("current")
_Ltp8xONTPortsUNIShapingDownstreamCommitedRate_Type = Unsigned32
_Ltp8xONTPortsUNIShapingDownstreamCommitedRate_Object = MibTableColumn
ltp8xONTPortsUNIShapingDownstreamCommitedRate = _Ltp8xONTPortsUNIShapingDownstreamCommitedRate_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 42, 1, 10),
    _Ltp8xONTPortsUNIShapingDownstreamCommitedRate_Type()
)
ltp8xONTPortsUNIShapingDownstreamCommitedRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTPortsUNIShapingDownstreamCommitedRate.setStatus("current")
_Ltp8xONTPortsUNIShapingDownstreamPeakRate_Type = Unsigned32
_Ltp8xONTPortsUNIShapingDownstreamPeakRate_Object = MibTableColumn
ltp8xONTPortsUNIShapingDownstreamPeakRate = _Ltp8xONTPortsUNIShapingDownstreamPeakRate_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 42, 1, 11),
    _Ltp8xONTPortsUNIShapingDownstreamPeakRate_Type()
)
ltp8xONTPortsUNIShapingDownstreamPeakRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTPortsUNIShapingDownstreamPeakRate.setStatus("current")
_Ltp8xONTPortsUNIShapingUpstreamEnabled_Type = TruthValue
_Ltp8xONTPortsUNIShapingUpstreamEnabled_Object = MibTableColumn
ltp8xONTPortsUNIShapingUpstreamEnabled = _Ltp8xONTPortsUNIShapingUpstreamEnabled_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 42, 1, 12),
    _Ltp8xONTPortsUNIShapingUpstreamEnabled_Type()
)
ltp8xONTPortsUNIShapingUpstreamEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTPortsUNIShapingUpstreamEnabled.setStatus("current")
_Ltp8xONTPortsUNIShapingUpstreamCommitedRate_Type = Unsigned32
_Ltp8xONTPortsUNIShapingUpstreamCommitedRate_Object = MibTableColumn
ltp8xONTPortsUNIShapingUpstreamCommitedRate = _Ltp8xONTPortsUNIShapingUpstreamCommitedRate_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 42, 1, 13),
    _Ltp8xONTPortsUNIShapingUpstreamCommitedRate_Type()
)
ltp8xONTPortsUNIShapingUpstreamCommitedRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTPortsUNIShapingUpstreamCommitedRate.setStatus("current")
_Ltp8xONTPortsUNIShapingUpstreamPeakRate_Type = Unsigned32
_Ltp8xONTPortsUNIShapingUpstreamPeakRate_Object = MibTableColumn
ltp8xONTPortsUNIShapingUpstreamPeakRate = _Ltp8xONTPortsUNIShapingUpstreamPeakRate_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 42, 1, 14),
    _Ltp8xONTPortsUNIShapingUpstreamPeakRate_Type()
)
ltp8xONTPortsUNIShapingUpstreamPeakRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTPortsUNIShapingUpstreamPeakRate.setStatus("current")
_Ltp8xONTPortsUNIIGMPDownstreamVID_Type = Unsigned32
_Ltp8xONTPortsUNIIGMPDownstreamVID_Object = MibTableColumn
ltp8xONTPortsUNIIGMPDownstreamVID = _Ltp8xONTPortsUNIIGMPDownstreamVID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 42, 1, 15),
    _Ltp8xONTPortsUNIIGMPDownstreamVID_Type()
)
ltp8xONTPortsUNIIGMPDownstreamVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTPortsUNIIGMPDownstreamVID.setStatus("current")
_Ltp8xONTPortsUNIIGMPDownstreamPriority_Type = Unsigned32
_Ltp8xONTPortsUNIIGMPDownstreamPriority_Object = MibTableColumn
ltp8xONTPortsUNIIGMPDownstreamPriority = _Ltp8xONTPortsUNIIGMPDownstreamPriority_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 42, 1, 16),
    _Ltp8xONTPortsUNIIGMPDownstreamPriority_Type()
)
ltp8xONTPortsUNIIGMPDownstreamPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTPortsUNIIGMPDownstreamPriority.setStatus("current")


class _Ltp8xONTPortsUNIIGMPDownstreamTagControl_Type(Integer32):
    """Custom type ltp8xONTPortsUNIIGMPDownstreamTagControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("addTag", 2),
          ("addTagSubscriberInfo", 5),
          ("pass", 0),
          ("removeTag", 1),
          ("replaceTag", 3),
          ("replaceTagSubscriberInfo", 6),
          ("replaceVid", 4),
          ("replaceVidSubscriberInfo", 7))
    )


_Ltp8xONTPortsUNIIGMPDownstreamTagControl_Type.__name__ = "Integer32"
_Ltp8xONTPortsUNIIGMPDownstreamTagControl_Object = MibTableColumn
ltp8xONTPortsUNIIGMPDownstreamTagControl = _Ltp8xONTPortsUNIIGMPDownstreamTagControl_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 42, 1, 17),
    _Ltp8xONTPortsUNIIGMPDownstreamTagControl_Type()
)
ltp8xONTPortsUNIIGMPDownstreamTagControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTPortsUNIIGMPDownstreamTagControl.setStatus("current")
_Ltp8xONTVoiceProfileTable_Object = MibTable
ltp8xONTVoiceProfileTable = _Ltp8xONTVoiceProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 43)
)
if mibBuilder.loadTexts:
    ltp8xONTVoiceProfileTable.setStatus("current")
_Ltp8xONTVoiceProfileEntry_Object = MibTableRow
ltp8xONTVoiceProfileEntry = _Ltp8xONTVoiceProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 43, 1)
)
ltp8xONTVoiceProfileEntry.setIndexNames(
    (0, "ELTEX-LTP8X", "ltp8xONTVoiceID"),
)
if mibBuilder.loadTexts:
    ltp8xONTVoiceProfileEntry.setStatus("current")
_Ltp8xONTVoiceID_Type = Unsigned32
_Ltp8xONTVoiceID_Object = MibTableColumn
ltp8xONTVoiceID = _Ltp8xONTVoiceID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 43, 1, 1),
    _Ltp8xONTVoiceID_Type()
)
ltp8xONTVoiceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTVoiceID.setStatus("current")
_Ltp8xONTVoiceDescription_Type = DisplayString
_Ltp8xONTVoiceDescription_Object = MibTableColumn
ltp8xONTVoiceDescription = _Ltp8xONTVoiceDescription_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 43, 1, 2),
    _Ltp8xONTVoiceDescription_Type()
)
ltp8xONTVoiceDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTVoiceDescription.setStatus("current")
_Ltp8xONTVoiceName_Type = DisplayString
_Ltp8xONTVoiceName_Object = MibTableColumn
ltp8xONTVoiceName = _Ltp8xONTVoiceName_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 43, 1, 3),
    _Ltp8xONTVoiceName_Type()
)
ltp8xONTVoiceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTVoiceName.setStatus("current")
_Ltp8xONTVoiceCrossConnect_Type = Unsigned32
_Ltp8xONTVoiceCrossConnect_Object = MibTableColumn
ltp8xONTVoiceCrossConnect = _Ltp8xONTVoiceCrossConnect_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 43, 1, 4),
    _Ltp8xONTVoiceCrossConnect_Type()
)
ltp8xONTVoiceCrossConnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTVoiceCrossConnect.setStatus("current")
_Ltp8xONTVoiceRowStatus_Type = RowStatus
_Ltp8xONTVoiceRowStatus_Object = MibTableColumn
ltp8xONTVoiceRowStatus = _Ltp8xONTVoiceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 43, 1, 10),
    _Ltp8xONTVoiceRowStatus_Type()
)
ltp8xONTVoiceRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTVoiceRowStatus.setStatus("current")
_Ltp8xONTScriptingProfiles_ObjectIdentity = ObjectIdentity
ltp8xONTScriptingProfiles = _Ltp8xONTScriptingProfiles_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 44)
)
_Ltp8xONTScriptingProfileTable_Object = MibTable
ltp8xONTScriptingProfileTable = _Ltp8xONTScriptingProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 44, 1)
)
if mibBuilder.loadTexts:
    ltp8xONTScriptingProfileTable.setStatus("current")
_Ltp8xONTScriptingProfileEntry_Object = MibTableRow
ltp8xONTScriptingProfileEntry = _Ltp8xONTScriptingProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 44, 1, 1)
)
ltp8xONTScriptingProfileEntry.setIndexNames(
    (0, "ELTEX-LTP8X", "ltp8xONTScriptingID"),
)
if mibBuilder.loadTexts:
    ltp8xONTScriptingProfileEntry.setStatus("current")
_Ltp8xONTScriptingID_Type = Unsigned32
_Ltp8xONTScriptingID_Object = MibTableColumn
ltp8xONTScriptingID = _Ltp8xONTScriptingID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 44, 1, 1, 1),
    _Ltp8xONTScriptingID_Type()
)
ltp8xONTScriptingID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTScriptingID.setStatus("current")
_Ltp8xONTScriptingDescription_Type = DisplayString
_Ltp8xONTScriptingDescription_Object = MibTableColumn
ltp8xONTScriptingDescription = _Ltp8xONTScriptingDescription_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 44, 1, 1, 2),
    _Ltp8xONTScriptingDescription_Type()
)
ltp8xONTScriptingDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTScriptingDescription.setStatus("current")
_Ltp8xONTScriptingName_Type = DisplayString
_Ltp8xONTScriptingName_Object = MibTableColumn
ltp8xONTScriptingName = _Ltp8xONTScriptingName_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 44, 1, 1, 3),
    _Ltp8xONTScriptingName_Type()
)
ltp8xONTScriptingName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTScriptingName.setStatus("current")
_Ltp8xONTScriptingRowStatus_Type = RowStatus
_Ltp8xONTScriptingRowStatus_Object = MibTableColumn
ltp8xONTScriptingRowStatus = _Ltp8xONTScriptingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 44, 1, 1, 10),
    _Ltp8xONTScriptingRowStatus_Type()
)
ltp8xONTScriptingRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTScriptingRowStatus.setStatus("current")
_Ltp8xONTScriptingProfileScriptsTable_Object = MibTable
ltp8xONTScriptingProfileScriptsTable = _Ltp8xONTScriptingProfileScriptsTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 44, 2)
)
if mibBuilder.loadTexts:
    ltp8xONTScriptingProfileScriptsTable.setStatus("current")
_Ltp8xONTScriptingProfileScriptsEntry_Object = MibTableRow
ltp8xONTScriptingProfileScriptsEntry = _Ltp8xONTScriptingProfileScriptsEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 44, 2, 1)
)
ltp8xONTScriptingProfileScriptsEntry.setIndexNames(
    (0, "ELTEX-LTP8X", "ltp8xONTScriptingID"),
    (0, "ELTEX-LTP8X", "ltp8xONTScriptingChunkID"),
)
if mibBuilder.loadTexts:
    ltp8xONTScriptingProfileScriptsEntry.setStatus("current")
_Ltp8xONTScriptingChunkID_Type = Unsigned32
_Ltp8xONTScriptingChunkID_Object = MibTableColumn
ltp8xONTScriptingChunkID = _Ltp8xONTScriptingChunkID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 44, 2, 1, 1),
    _Ltp8xONTScriptingChunkID_Type()
)
ltp8xONTScriptingChunkID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ltp8xONTScriptingChunkID.setStatus("current")


class _Ltp8xONTScriptingText_Type(OctetString):
    """Custom type ltp8xONTScriptingText based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Ltp8xONTScriptingText_Type.__name__ = "OctetString"
_Ltp8xONTScriptingText_Object = MibTableColumn
ltp8xONTScriptingText = _Ltp8xONTScriptingText_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 44, 2, 1, 2),
    _Ltp8xONTScriptingText_Type()
)
ltp8xONTScriptingText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTScriptingText.setStatus("current")
_Ltp8xONTPortsProfileMCDynamicEntriesTable_Object = MibTable
ltp8xONTPortsProfileMCDynamicEntriesTable = _Ltp8xONTPortsProfileMCDynamicEntriesTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 46)
)
if mibBuilder.loadTexts:
    ltp8xONTPortsProfileMCDynamicEntriesTable.setStatus("current")
_Ltp8xONTPortsProfileMCDynamicEntriesEntry_Object = MibTableRow
ltp8xONTPortsProfileMCDynamicEntriesEntry = _Ltp8xONTPortsProfileMCDynamicEntriesEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 46, 1)
)
ltp8xONTPortsProfileMCDynamicEntriesEntry.setIndexNames(
    (0, "ELTEX-LTP8X", "ltp8xONTPortsID"),
    (0, "ELTEX-LTP8X", "ltp8xONTPortsMCEntryID"),
)
if mibBuilder.loadTexts:
    ltp8xONTPortsProfileMCDynamicEntriesEntry.setStatus("current")
_Ltp8xONTPortsMCEntryID_Type = Unsigned32
_Ltp8xONTPortsMCEntryID_Object = MibTableColumn
ltp8xONTPortsMCEntryID = _Ltp8xONTPortsMCEntryID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 46, 1, 1),
    _Ltp8xONTPortsMCEntryID_Type()
)
ltp8xONTPortsMCEntryID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ltp8xONTPortsMCEntryID.setStatus("current")
_Ltp8xONTPortsMCVLANID_Type = Unsigned32
_Ltp8xONTPortsMCVLANID_Object = MibTableColumn
ltp8xONTPortsMCVLANID = _Ltp8xONTPortsMCVLANID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 46, 1, 2),
    _Ltp8xONTPortsMCVLANID_Type()
)
ltp8xONTPortsMCVLANID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTPortsMCVLANID.setStatus("current")
_Ltp8xONTPortsMCFirstGroupIP_Type = IpAddress
_Ltp8xONTPortsMCFirstGroupIP_Object = MibTableColumn
ltp8xONTPortsMCFirstGroupIP = _Ltp8xONTPortsMCFirstGroupIP_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 46, 1, 3),
    _Ltp8xONTPortsMCFirstGroupIP_Type()
)
ltp8xONTPortsMCFirstGroupIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTPortsMCFirstGroupIP.setStatus("current")
_Ltp8xONTPortsMCLastGroupIP_Type = IpAddress
_Ltp8xONTPortsMCLastGroupIP_Object = MibTableColumn
ltp8xONTPortsMCLastGroupIP = _Ltp8xONTPortsMCLastGroupIP_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 46, 1, 4),
    _Ltp8xONTPortsMCLastGroupIP_Type()
)
ltp8xONTPortsMCLastGroupIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTPortsMCLastGroupIP.setStatus("current")
_Ltp8xONTPortsProfileMLDDynamicEntriesTable_Object = MibTable
ltp8xONTPortsProfileMLDDynamicEntriesTable = _Ltp8xONTPortsProfileMLDDynamicEntriesTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 47)
)
if mibBuilder.loadTexts:
    ltp8xONTPortsProfileMLDDynamicEntriesTable.setStatus("current")
_Ltp8xONTPortsProfileMLDDynamicEntriesEntry_Object = MibTableRow
ltp8xONTPortsProfileMLDDynamicEntriesEntry = _Ltp8xONTPortsProfileMLDDynamicEntriesEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 47, 1)
)
ltp8xONTPortsProfileMLDDynamicEntriesEntry.setIndexNames(
    (0, "ELTEX-LTP8X", "ltp8xONTPortsID"),
    (0, "ELTEX-LTP8X", "ltp8xONTPortsMLDEntryID"),
)
if mibBuilder.loadTexts:
    ltp8xONTPortsProfileMLDDynamicEntriesEntry.setStatus("current")
_Ltp8xONTPortsMLDEntryID_Type = Unsigned32
_Ltp8xONTPortsMLDEntryID_Object = MibTableColumn
ltp8xONTPortsMLDEntryID = _Ltp8xONTPortsMLDEntryID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 47, 1, 1),
    _Ltp8xONTPortsMLDEntryID_Type()
)
ltp8xONTPortsMLDEntryID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ltp8xONTPortsMLDEntryID.setStatus("current")
_Ltp8xONTPortsMLDVLANID_Type = Unsigned32
_Ltp8xONTPortsMLDVLANID_Object = MibTableColumn
ltp8xONTPortsMLDVLANID = _Ltp8xONTPortsMLDVLANID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 47, 1, 2),
    _Ltp8xONTPortsMLDVLANID_Type()
)
ltp8xONTPortsMLDVLANID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTPortsMLDVLANID.setStatus("current")
_Ltp8xONTPortsMLDMCFirstGroupIP_Type = Ipv6Address
_Ltp8xONTPortsMLDMCFirstGroupIP_Object = MibTableColumn
ltp8xONTPortsMLDMCFirstGroupIP = _Ltp8xONTPortsMLDMCFirstGroupIP_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 47, 1, 5),
    _Ltp8xONTPortsMLDMCFirstGroupIP_Type()
)
ltp8xONTPortsMLDMCFirstGroupIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTPortsMLDMCFirstGroupIP.setStatus("current")
_Ltp8xONTPortsMLDMCLastGroupIP_Type = Ipv6Address
_Ltp8xONTPortsMLDMCLastGroupIP_Object = MibTableColumn
ltp8xONTPortsMLDMCLastGroupIP = _Ltp8xONTPortsMLDMCLastGroupIP_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 47, 1, 6),
    _Ltp8xONTPortsMLDMCLastGroupIP_Type()
)
ltp8xONTPortsMLDMCLastGroupIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTPortsMLDMCLastGroupIP.setStatus("current")
_Ltp8xONTPortsMLDMCPreviewLength_Type = Unsigned32
_Ltp8xONTPortsMLDMCPreviewLength_Object = MibTableColumn
ltp8xONTPortsMLDMCPreviewLength = _Ltp8xONTPortsMLDMCPreviewLength_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 47, 1, 7),
    _Ltp8xONTPortsMLDMCPreviewLength_Type()
)
ltp8xONTPortsMLDMCPreviewLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTPortsMLDMCPreviewLength.setStatus("current")
_Ltp8xONTPortsMLDMCPreviewRepeatTime_Type = Unsigned32
_Ltp8xONTPortsMLDMCPreviewRepeatTime_Object = MibTableColumn
ltp8xONTPortsMLDMCPreviewRepeatTime = _Ltp8xONTPortsMLDMCPreviewRepeatTime_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 47, 1, 8),
    _Ltp8xONTPortsMLDMCPreviewRepeatTime_Type()
)
ltp8xONTPortsMLDMCPreviewRepeatTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTPortsMLDMCPreviewRepeatTime.setStatus("current")
_Ltp8xONTPortsMLDMCPreviewRepeatCount_Type = Unsigned32
_Ltp8xONTPortsMLDMCPreviewRepeatCount_Object = MibTableColumn
ltp8xONTPortsMLDMCPreviewRepeatCount = _Ltp8xONTPortsMLDMCPreviewRepeatCount_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 47, 1, 9),
    _Ltp8xONTPortsMLDMCPreviewRepeatCount_Type()
)
ltp8xONTPortsMLDMCPreviewRepeatCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTPortsMLDMCPreviewRepeatCount.setStatus("current")
_Ltp8xONTPortsMLDMCPreviewResetTime_Type = Unsigned32
_Ltp8xONTPortsMLDMCPreviewResetTime_Object = MibTableColumn
ltp8xONTPortsMLDMCPreviewResetTime = _Ltp8xONTPortsMLDMCPreviewResetTime_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 47, 1, 10),
    _Ltp8xONTPortsMLDMCPreviewResetTime_Type()
)
ltp8xONTPortsMLDMCPreviewResetTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTPortsMLDMCPreviewResetTime.setStatus("current")
_Ltp8xONTMulticastStatsTable_Object = MibTable
ltp8xONTMulticastStatsTable = _Ltp8xONTMulticastStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 50)
)
if mibBuilder.loadTexts:
    ltp8xONTMulticastStatsTable.setStatus("current")
_Ltp8xONTMulticastStatsEntry_Object = MibTableRow
ltp8xONTMulticastStatsEntry = _Ltp8xONTMulticastStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 50, 1)
)
ltp8xONTMulticastStatsEntry.setIndexNames(
    (0, "ELTEX-LTP8X", "ltp8xONTMulticastStatsSlot"),
    (0, "ELTEX-LTP8X", "ltp8xONTMulticastStatsONTSerial"),
    (0, "ELTEX-LTP8X", "ltp8xONTMulticastStatsRecordID"),
)
if mibBuilder.loadTexts:
    ltp8xONTMulticastStatsEntry.setStatus("current")
_Ltp8xONTMulticastStatsSlot_Type = Unsigned32
_Ltp8xONTMulticastStatsSlot_Object = MibTableColumn
ltp8xONTMulticastStatsSlot = _Ltp8xONTMulticastStatsSlot_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 50, 1, 1),
    _Ltp8xONTMulticastStatsSlot_Type()
)
ltp8xONTMulticastStatsSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTMulticastStatsSlot.setStatus("current")
_Ltp8xONTMulticastStatsONTSerial_Type = ONTSerial
_Ltp8xONTMulticastStatsONTSerial_Object = MibTableColumn
ltp8xONTMulticastStatsONTSerial = _Ltp8xONTMulticastStatsONTSerial_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 50, 1, 2),
    _Ltp8xONTMulticastStatsONTSerial_Type()
)
ltp8xONTMulticastStatsONTSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTMulticastStatsONTSerial.setStatus("current")
_Ltp8xONTMulticastStatsRecordID_Type = Unsigned32
_Ltp8xONTMulticastStatsRecordID_Object = MibTableColumn
ltp8xONTMulticastStatsRecordID = _Ltp8xONTMulticastStatsRecordID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 50, 1, 3),
    _Ltp8xONTMulticastStatsRecordID_Type()
)
ltp8xONTMulticastStatsRecordID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTMulticastStatsRecordID.setStatus("current")
_Ltp8xONTMulticastStatsMulticastAddress_Type = IpAddress
_Ltp8xONTMulticastStatsMulticastAddress_Object = MibTableColumn
ltp8xONTMulticastStatsMulticastAddress = _Ltp8xONTMulticastStatsMulticastAddress_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 50, 1, 4),
    _Ltp8xONTMulticastStatsMulticastAddress_Type()
)
ltp8xONTMulticastStatsMulticastAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTMulticastStatsMulticastAddress.setStatus("current")
_Ltp8xONTMulticastStatsStart_Type = DisplayString
_Ltp8xONTMulticastStatsStart_Object = MibTableColumn
ltp8xONTMulticastStatsStart = _Ltp8xONTMulticastStatsStart_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 50, 1, 5),
    _Ltp8xONTMulticastStatsStart_Type()
)
ltp8xONTMulticastStatsStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTMulticastStatsStart.setStatus("current")
_Ltp8xONTMulticastStatsStop_Type = DisplayString
_Ltp8xONTMulticastStatsStop_Object = MibTableColumn
ltp8xONTMulticastStatsStop = _Ltp8xONTMulticastStatsStop_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 50, 1, 6),
    _Ltp8xONTMulticastStatsStop_Type()
)
ltp8xONTMulticastStatsStop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTMulticastStatsStop.setStatus("current")
_Ltp8xONTACSPropertiesTable_Object = MibTable
ltp8xONTACSPropertiesTable = _Ltp8xONTACSPropertiesTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 60)
)
if mibBuilder.loadTexts:
    ltp8xONTACSPropertiesTable.setStatus("current")
_Ltp8xONTACSPropertiesEntry_Object = MibTableRow
ltp8xONTACSPropertiesEntry = _Ltp8xONTACSPropertiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 60, 1)
)
ltp8xONTACSPropertiesEntry.setIndexNames(
    (0, "ELTEX-LTP8X", "ltp8xONTACSPropertiesONTSerial"),
    (0, "ELTEX-LTP8X", "ltp8xONTACSPropertiesPropertyID"),
)
if mibBuilder.loadTexts:
    ltp8xONTACSPropertiesEntry.setStatus("current")
_Ltp8xONTACSPropertiesONTSerial_Type = ONTSerial
_Ltp8xONTACSPropertiesONTSerial_Object = MibTableColumn
ltp8xONTACSPropertiesONTSerial = _Ltp8xONTACSPropertiesONTSerial_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 60, 1, 1),
    _Ltp8xONTACSPropertiesONTSerial_Type()
)
ltp8xONTACSPropertiesONTSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTACSPropertiesONTSerial.setStatus("current")
_Ltp8xONTACSPropertiesPropertyID_Type = Unsigned32
_Ltp8xONTACSPropertiesPropertyID_Object = MibTableColumn
ltp8xONTACSPropertiesPropertyID = _Ltp8xONTACSPropertiesPropertyID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 60, 1, 2),
    _Ltp8xONTACSPropertiesPropertyID_Type()
)
ltp8xONTACSPropertiesPropertyID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTACSPropertiesPropertyID.setStatus("current")
_Ltp8xONTACSPropertiesPropertyName_Type = DisplayString
_Ltp8xONTACSPropertiesPropertyName_Object = MibTableColumn
ltp8xONTACSPropertiesPropertyName = _Ltp8xONTACSPropertiesPropertyName_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 60, 1, 3),
    _Ltp8xONTACSPropertiesPropertyName_Type()
)
ltp8xONTACSPropertiesPropertyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTACSPropertiesPropertyName.setStatus("current")
_Ltp8xONTACSPropertiesPropertyValue_Type = DisplayString
_Ltp8xONTACSPropertiesPropertyValue_Object = MibTableColumn
ltp8xONTACSPropertiesPropertyValue = _Ltp8xONTACSPropertiesPropertyValue_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 60, 1, 4),
    _Ltp8xONTACSPropertiesPropertyValue_Type()
)
ltp8xONTACSPropertiesPropertyValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTACSPropertiesPropertyValue.setStatus("current")
_Ltp8xONTACSPropertiesRowStatus_Type = RowStatus
_Ltp8xONTACSPropertiesRowStatus_Object = MibTableColumn
ltp8xONTACSPropertiesRowStatus = _Ltp8xONTACSPropertiesRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 60, 1, 5),
    _Ltp8xONTACSPropertiesRowStatus_Type()
)
ltp8xONTACSPropertiesRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTACSPropertiesRowStatus.setStatus("current")
_Ltp8xONTACSPropertiesTableSupported_Type = TruthValue
_Ltp8xONTACSPropertiesTableSupported_Object = MibScalar
ltp8xONTACSPropertiesTableSupported = _Ltp8xONTACSPropertiesTableSupported_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 61),
    _Ltp8xONTACSPropertiesTableSupported_Type()
)
ltp8xONTACSPropertiesTableSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTACSPropertiesTableSupported.setStatus("current")
_Ltp8xONTACSPrivatesConfigTable_Object = MibTable
ltp8xONTACSPrivatesConfigTable = _Ltp8xONTACSPrivatesConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 62)
)
if mibBuilder.loadTexts:
    ltp8xONTACSPrivatesConfigTable.setStatus("current")
_Ltp8xONTACSPrivatesConfigEntry_Object = MibTableRow
ltp8xONTACSPrivatesConfigEntry = _Ltp8xONTACSPrivatesConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 62, 1)
)
ltp8xONTACSPrivatesConfigEntry.setIndexNames(
    (0, "ELTEX-LTP8X", "ltp8xONTACSPrivatesPropertyName"),
    (0, "ELTEX-LTP8X", "ltp8xONTACSPrivatesPrivateIndex"),
)
if mibBuilder.loadTexts:
    ltp8xONTACSPrivatesConfigEntry.setStatus("current")


class _Ltp8xONTACSPrivatesPropertyName_Type(DisplayString):
    """Custom type ltp8xONTACSPrivatesPropertyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Ltp8xONTACSPrivatesPropertyName_Type.__name__ = "DisplayString"
_Ltp8xONTACSPrivatesPropertyName_Object = MibTableColumn
ltp8xONTACSPrivatesPropertyName = _Ltp8xONTACSPrivatesPropertyName_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 62, 1, 1),
    _Ltp8xONTACSPrivatesPropertyName_Type()
)
ltp8xONTACSPrivatesPropertyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ltp8xONTACSPrivatesPropertyName.setStatus("current")
_Ltp8xONTACSPrivatesPrivateIndex_Type = Unsigned32
_Ltp8xONTACSPrivatesPrivateIndex_Object = MibTableColumn
ltp8xONTACSPrivatesPrivateIndex = _Ltp8xONTACSPrivatesPrivateIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 62, 1, 2),
    _Ltp8xONTACSPrivatesPrivateIndex_Type()
)
ltp8xONTACSPrivatesPrivateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ltp8xONTACSPrivatesPrivateIndex.setStatus("current")


class _Ltp8xONTACSPrivatesPrivateName_Type(DisplayString):
    """Custom type ltp8xONTACSPrivatesPrivateName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Ltp8xONTACSPrivatesPrivateName_Type.__name__ = "DisplayString"
_Ltp8xONTACSPrivatesPrivateName_Object = MibTableColumn
ltp8xONTACSPrivatesPrivateName = _Ltp8xONTACSPrivatesPrivateName_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 62, 1, 3),
    _Ltp8xONTACSPrivatesPrivateName_Type()
)
ltp8xONTACSPrivatesPrivateName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTACSPrivatesPrivateName.setStatus("current")
_Ltp8xONTACSPrivatesRowStatus_Type = RowStatus
_Ltp8xONTACSPrivatesRowStatus_Object = MibTableColumn
ltp8xONTACSPrivatesRowStatus = _Ltp8xONTACSPrivatesRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 62, 1, 4),
    _Ltp8xONTACSPrivatesRowStatus_Type()
)
ltp8xONTACSPrivatesRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTACSPrivatesRowStatus.setStatus("current")
_Ltp8xONTACSUserPropertiesTable_Object = MibTable
ltp8xONTACSUserPropertiesTable = _Ltp8xONTACSUserPropertiesTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 63)
)
if mibBuilder.loadTexts:
    ltp8xONTACSUserPropertiesTable.setStatus("current")
_Ltp8xONTACSUserPropertiesEntry_Object = MibTableRow
ltp8xONTACSUserPropertiesEntry = _Ltp8xONTACSUserPropertiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 63, 1)
)
ltp8xONTACSUserPropertiesEntry.setIndexNames(
    (0, "ELTEX-LTP8X", "ltp8xONTACSUserPropertiesName"),
    (0, "ELTEX-LTP8X", "ltp8xONTACSUserPropertiesSerial"),
)
if mibBuilder.loadTexts:
    ltp8xONTACSUserPropertiesEntry.setStatus("current")


class _Ltp8xONTACSUserPropertiesName_Type(DisplayString):
    """Custom type ltp8xONTACSUserPropertiesName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Ltp8xONTACSUserPropertiesName_Type.__name__ = "DisplayString"
_Ltp8xONTACSUserPropertiesName_Object = MibTableColumn
ltp8xONTACSUserPropertiesName = _Ltp8xONTACSUserPropertiesName_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 63, 1, 1),
    _Ltp8xONTACSUserPropertiesName_Type()
)
ltp8xONTACSUserPropertiesName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ltp8xONTACSUserPropertiesName.setStatus("current")
_Ltp8xONTACSUserPropertiesSerial_Type = ONTSerial
_Ltp8xONTACSUserPropertiesSerial_Object = MibTableColumn
ltp8xONTACSUserPropertiesSerial = _Ltp8xONTACSUserPropertiesSerial_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 63, 1, 2),
    _Ltp8xONTACSUserPropertiesSerial_Type()
)
ltp8xONTACSUserPropertiesSerial.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ltp8xONTACSUserPropertiesSerial.setStatus("current")
_Ltp8xONTACSUserPropertiesValue_Type = DisplayString
_Ltp8xONTACSUserPropertiesValue_Object = MibTableColumn
ltp8xONTACSUserPropertiesValue = _Ltp8xONTACSUserPropertiesValue_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 63, 1, 3),
    _Ltp8xONTACSUserPropertiesValue_Type()
)
ltp8xONTACSUserPropertiesValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTACSUserPropertiesValue.setStatus("current")
_Ltp8xONTConnectionLogTable_Object = MibTable
ltp8xONTConnectionLogTable = _Ltp8xONTConnectionLogTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 70)
)
if mibBuilder.loadTexts:
    ltp8xONTConnectionLogTable.setStatus("current")
_Ltp8xONTConnectionLogEntry_Object = MibTableRow
ltp8xONTConnectionLogEntry = _Ltp8xONTConnectionLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 70, 1)
)
ltp8xONTConnectionLogEntry.setIndexNames(
    (0, "ELTEX-LTP8X", "ltp8xONTConnectionLogSlot"),
    (0, "ELTEX-LTP8X", "ltp8xONTConnectionLogONTSerial"),
)
if mibBuilder.loadTexts:
    ltp8xONTConnectionLogEntry.setStatus("current")
_Ltp8xONTConnectionLogSlot_Type = Unsigned32
_Ltp8xONTConnectionLogSlot_Object = MibTableColumn
ltp8xONTConnectionLogSlot = _Ltp8xONTConnectionLogSlot_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 70, 1, 1),
    _Ltp8xONTConnectionLogSlot_Type()
)
ltp8xONTConnectionLogSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ltp8xONTConnectionLogSlot.setStatus("current")
_Ltp8xONTConnectionLogONTSerial_Type = ONTSerial
_Ltp8xONTConnectionLogONTSerial_Object = MibTableColumn
ltp8xONTConnectionLogONTSerial = _Ltp8xONTConnectionLogONTSerial_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 70, 1, 2),
    _Ltp8xONTConnectionLogONTSerial_Type()
)
ltp8xONTConnectionLogONTSerial.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ltp8xONTConnectionLogONTSerial.setStatus("current")
_Ltp8xONTConnectionLogText_Type = DisplayString
_Ltp8xONTConnectionLogText_Object = MibTableColumn
ltp8xONTConnectionLogText = _Ltp8xONTConnectionLogText_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 70, 1, 3),
    _Ltp8xONTConnectionLogText_Type()
)
ltp8xONTConnectionLogText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTConnectionLogText.setStatus("current")
_Ltp8xONTConfigFreenessTable_Object = MibTable
ltp8xONTConfigFreenessTable = _Ltp8xONTConfigFreenessTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 80)
)
if mibBuilder.loadTexts:
    ltp8xONTConfigFreenessTable.setStatus("current")
_Ltp8xONTConfigFreenessEntry_Object = MibTableRow
ltp8xONTConfigFreenessEntry = _Ltp8xONTConfigFreenessEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 80, 1)
)
ltp8xONTConfigFreenessEntry.setIndexNames(
    (0, "ELTEX-LTP8X", "ltp8xONTConfigFreenessSlot"),
    (0, "ELTEX-LTP8X", "ltp8xONTConfigFreenessChannel"),
    (0, "ELTEX-LTP8X", "ltp8xONTConfigFreenessID"),
)
if mibBuilder.loadTexts:
    ltp8xONTConfigFreenessEntry.setStatus("current")
_Ltp8xONTConfigFreenessSlot_Type = Unsigned32
_Ltp8xONTConfigFreenessSlot_Object = MibTableColumn
ltp8xONTConfigFreenessSlot = _Ltp8xONTConfigFreenessSlot_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 80, 1, 1),
    _Ltp8xONTConfigFreenessSlot_Type()
)
ltp8xONTConfigFreenessSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ltp8xONTConfigFreenessSlot.setStatus("current")
_Ltp8xONTConfigFreenessChannel_Type = Unsigned32
_Ltp8xONTConfigFreenessChannel_Object = MibTableColumn
ltp8xONTConfigFreenessChannel = _Ltp8xONTConfigFreenessChannel_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 80, 1, 2),
    _Ltp8xONTConfigFreenessChannel_Type()
)
ltp8xONTConfigFreenessChannel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ltp8xONTConfigFreenessChannel.setStatus("current")
_Ltp8xONTConfigFreenessID_Type = Unsigned32
_Ltp8xONTConfigFreenessID_Object = MibTableColumn
ltp8xONTConfigFreenessID = _Ltp8xONTConfigFreenessID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 80, 1, 3),
    _Ltp8xONTConfigFreenessID_Type()
)
ltp8xONTConfigFreenessID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ltp8xONTConfigFreenessID.setStatus("current")
_Ltp8xONTConfigFreenessSerial_Type = ONTSerial
_Ltp8xONTConfigFreenessSerial_Object = MibTableColumn
ltp8xONTConfigFreenessSerial = _Ltp8xONTConfigFreenessSerial_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 80, 1, 4),
    _Ltp8xONTConfigFreenessSerial_Type()
)
ltp8xONTConfigFreenessSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xONTConfigFreenessSerial.setStatus("current")
_Ltp8xONTDisable_ObjectIdentity = ObjectIdentity
ltp8xONTDisable = _Ltp8xONTDisable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 30000)
)
_Ltp8xONTDisableSlot_Type = Unsigned32
_Ltp8xONTDisableSlot_Object = MibScalar
ltp8xONTDisableSlot = _Ltp8xONTDisableSlot_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 30000, 1),
    _Ltp8xONTDisableSlot_Type()
)
ltp8xONTDisableSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTDisableSlot.setStatus("current")
_Ltp8xONTDisableONTSerial_Type = ONTSerial
_Ltp8xONTDisableONTSerial_Object = MibScalar
ltp8xONTDisableONTSerial = _Ltp8xONTDisableONTSerial_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 30000, 2),
    _Ltp8xONTDisableONTSerial_Type()
)
ltp8xONTDisableONTSerial.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTDisableONTSerial.setStatus("current")
_Ltp8xONTDisableChannel_Type = Unsigned32
_Ltp8xONTDisableChannel_Object = MibScalar
ltp8xONTDisableChannel = _Ltp8xONTDisableChannel_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 30000, 3),
    _Ltp8xONTDisableChannel_Type()
)
ltp8xONTDisableChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTDisableChannel.setStatus("current")
_Ltp8xONTDisableActionDisable_Type = Unsigned32
_Ltp8xONTDisableActionDisable_Object = MibScalar
ltp8xONTDisableActionDisable = _Ltp8xONTDisableActionDisable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 30000, 4),
    _Ltp8xONTDisableActionDisable_Type()
)
ltp8xONTDisableActionDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTDisableActionDisable.setStatus("current")
_Ltp8xONTDisableActionEnable_Type = Unsigned32
_Ltp8xONTDisableActionEnable_Object = MibScalar
ltp8xONTDisableActionEnable = _Ltp8xONTDisableActionEnable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 3, 30000, 5),
    _Ltp8xONTDisableActionEnable_Type()
)
ltp8xONTDisableActionEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTDisableActionEnable.setStatus("current")
_Ltp8xOLT_ObjectIdentity = ObjectIdentity
ltp8xOLT = _Ltp8xOLT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5)
)
_Ltp8xOLTStateTable_Object = MibTable
ltp8xOLTStateTable = _Ltp8xOLTStateTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 1)
)
if mibBuilder.loadTexts:
    ltp8xOLTStateTable.setStatus("current")
_Ltp8xOLTStateEntry_Object = MibTableRow
ltp8xOLTStateEntry = _Ltp8xOLTStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 1, 1)
)
ltp8xOLTStateEntry.setIndexNames(
    (0, "ELTEX-LTP8X", "ltp8xOLTStateSlot"),
)
if mibBuilder.loadTexts:
    ltp8xOLTStateEntry.setStatus("current")
_Ltp8xOLTStateSlot_Type = Unsigned32
_Ltp8xOLTStateSlot_Object = MibTableColumn
ltp8xOLTStateSlot = _Ltp8xOLTStateSlot_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 1, 1, 1),
    _Ltp8xOLTStateSlot_Type()
)
ltp8xOLTStateSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xOLTStateSlot.setStatus("current")
_Ltp8xOLTStateDriverVersion_Type = DisplayString
_Ltp8xOLTStateDriverVersion_Object = MibTableColumn
ltp8xOLTStateDriverVersion = _Ltp8xOLTStateDriverVersion_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 1, 1, 2),
    _Ltp8xOLTStateDriverVersion_Type()
)
ltp8xOLTStateDriverVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xOLTStateDriverVersion.setStatus("current")
_Ltp8xOLTStateFirmwareVersion_Type = DisplayString
_Ltp8xOLTStateFirmwareVersion_Object = MibTableColumn
ltp8xOLTStateFirmwareVersion = _Ltp8xOLTStateFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 1, 1, 3),
    _Ltp8xOLTStateFirmwareVersion_Type()
)
ltp8xOLTStateFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xOLTStateFirmwareVersion.setStatus("current")
_Ltp8xOLTStateHardwareVersion_Type = DisplayString
_Ltp8xOLTStateHardwareVersion_Object = MibTableColumn
ltp8xOLTStateHardwareVersion = _Ltp8xOLTStateHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 1, 1, 4),
    _Ltp8xOLTStateHardwareVersion_Type()
)
ltp8xOLTStateHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xOLTStateHardwareVersion.setStatus("current")
_Ltp8xOLTStateFirmwareVersionChip2_Type = DisplayString
_Ltp8xOLTStateFirmwareVersionChip2_Object = MibTableColumn
ltp8xOLTStateFirmwareVersionChip2 = _Ltp8xOLTStateFirmwareVersionChip2_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 1, 1, 5),
    _Ltp8xOLTStateFirmwareVersionChip2_Type()
)
ltp8xOLTStateFirmwareVersionChip2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xOLTStateFirmwareVersionChip2.setStatus("current")
_Ltp8xOLTStateHardwareVersionChip2_Type = DisplayString
_Ltp8xOLTStateHardwareVersionChip2_Object = MibTableColumn
ltp8xOLTStateHardwareVersionChip2 = _Ltp8xOLTStateHardwareVersionChip2_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 1, 1, 6),
    _Ltp8xOLTStateHardwareVersionChip2_Type()
)
ltp8xOLTStateHardwareVersionChip2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xOLTStateHardwareVersionChip2.setStatus("current")
_Ltp8xOLTStateReconfigure_Type = Unsigned32
_Ltp8xOLTStateReconfigure_Object = MibTableColumn
ltp8xOLTStateReconfigure = _Ltp8xOLTStateReconfigure_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 1, 1, 10),
    _Ltp8xOLTStateReconfigure_Type()
)
ltp8xOLTStateReconfigure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xOLTStateReconfigure.setStatus("current")
_Ltp8xOLTMIBBoundary1_Type = Unsigned32
_Ltp8xOLTMIBBoundary1_Object = MibScalar
ltp8xOLTMIBBoundary1 = _Ltp8xOLTMIBBoundary1_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 2),
    _Ltp8xOLTMIBBoundary1_Type()
)
ltp8xOLTMIBBoundary1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xOLTMIBBoundary1.setStatus("current")
_Ltp8xOLTDhcpRATable_Object = MibTable
ltp8xOLTDhcpRATable = _Ltp8xOLTDhcpRATable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 3)
)
if mibBuilder.loadTexts:
    ltp8xOLTDhcpRATable.setStatus("current")
_Ltp8xOLTDhcpRAEntry_Object = MibTableRow
ltp8xOLTDhcpRAEntry = _Ltp8xOLTDhcpRAEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 3, 1)
)
ltp8xOLTDhcpRAEntry.setIndexNames(
    (0, "ELTEX-LTP8X", "ltp8xOLTDhcpRASlot"),
)
if mibBuilder.loadTexts:
    ltp8xOLTDhcpRAEntry.setStatus("current")
_Ltp8xOLTDhcpRASlot_Type = Unsigned32
_Ltp8xOLTDhcpRASlot_Object = MibTableColumn
ltp8xOLTDhcpRASlot = _Ltp8xOLTDhcpRASlot_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 3, 1, 1),
    _Ltp8xOLTDhcpRASlot_Type()
)
ltp8xOLTDhcpRASlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xOLTDhcpRASlot.setStatus("current")
_Ltp8xOLTMIBBoundary2_Type = Unsigned32
_Ltp8xOLTMIBBoundary2_Object = MibScalar
ltp8xOLTMIBBoundary2 = _Ltp8xOLTMIBBoundary2_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 4),
    _Ltp8xOLTMIBBoundary2_Type()
)
ltp8xOLTMIBBoundary2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xOLTMIBBoundary2.setStatus("current")
_Ltp8xOLTConfigActivationTable_Object = MibTable
ltp8xOLTConfigActivationTable = _Ltp8xOLTConfigActivationTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 5)
)
if mibBuilder.loadTexts:
    ltp8xOLTConfigActivationTable.setStatus("current")
_Ltp8xOLTConfigActivationEntry_Object = MibTableRow
ltp8xOLTConfigActivationEntry = _Ltp8xOLTConfigActivationEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 5, 1)
)
ltp8xOLTConfigActivationEntry.setIndexNames(
    (0, "ELTEX-LTP8X", "ltp8xOLTConfigActivationSlot"),
)
if mibBuilder.loadTexts:
    ltp8xOLTConfigActivationEntry.setStatus("current")
_Ltp8xOLTConfigActivationSlot_Type = Unsigned32
_Ltp8xOLTConfigActivationSlot_Object = MibTableColumn
ltp8xOLTConfigActivationSlot = _Ltp8xOLTConfigActivationSlot_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 5, 1, 1),
    _Ltp8xOLTConfigActivationSlot_Type()
)
ltp8xOLTConfigActivationSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xOLTConfigActivationSlot.setStatus("current")
_Ltp8xOLTConfigActivationPeriod_Type = Unsigned32
_Ltp8xOLTConfigActivationPeriod_Object = MibTableColumn
ltp8xOLTConfigActivationPeriod = _Ltp8xOLTConfigActivationPeriod_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 5, 1, 2),
    _Ltp8xOLTConfigActivationPeriod_Type()
)
ltp8xOLTConfigActivationPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xOLTConfigActivationPeriod.setStatus("current")
_Ltp8xOLTConfigActivationCheckPassword_Type = TruthValue
_Ltp8xOLTConfigActivationCheckPassword_Object = MibTableColumn
ltp8xOLTConfigActivationCheckPassword = _Ltp8xOLTConfigActivationCheckPassword_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 5, 1, 3),
    _Ltp8xOLTConfigActivationCheckPassword_Type()
)
ltp8xOLTConfigActivationCheckPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xOLTConfigActivationCheckPassword.setStatus("current")
_Ltp8xOLTMIBBoundary3_Type = Unsigned32
_Ltp8xOLTMIBBoundary3_Object = MibScalar
ltp8xOLTMIBBoundary3 = _Ltp8xOLTMIBBoundary3_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 6),
    _Ltp8xOLTMIBBoundary3_Type()
)
ltp8xOLTMIBBoundary3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xOLTMIBBoundary3.setStatus("current")
_Ltp8xOLTConfigDhcpTable_Object = MibTable
ltp8xOLTConfigDhcpTable = _Ltp8xOLTConfigDhcpTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 7)
)
if mibBuilder.loadTexts:
    ltp8xOLTConfigDhcpTable.setStatus("current")
_Ltp8xOLTConfigDhcpEntry_Object = MibTableRow
ltp8xOLTConfigDhcpEntry = _Ltp8xOLTConfigDhcpEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 7, 1)
)
ltp8xOLTConfigDhcpEntry.setIndexNames(
    (0, "ELTEX-LTP8X", "ltp8xOLTConfigDhcpSlot"),
)
if mibBuilder.loadTexts:
    ltp8xOLTConfigDhcpEntry.setStatus("current")
_Ltp8xOLTConfigDhcpSlot_Type = Unsigned32
_Ltp8xOLTConfigDhcpSlot_Object = MibTableColumn
ltp8xOLTConfigDhcpSlot = _Ltp8xOLTConfigDhcpSlot_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 7, 1, 1),
    _Ltp8xOLTConfigDhcpSlot_Type()
)
ltp8xOLTConfigDhcpSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xOLTConfigDhcpSlot.setStatus("current")
_Ltp8xOLTConfigDhcpRelayAgentEnabled_Type = TruthValue
_Ltp8xOLTConfigDhcpRelayAgentEnabled_Object = MibTableColumn
ltp8xOLTConfigDhcpRelayAgentEnabled = _Ltp8xOLTConfigDhcpRelayAgentEnabled_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 7, 1, 2),
    _Ltp8xOLTConfigDhcpRelayAgentEnabled_Type()
)
ltp8xOLTConfigDhcpRelayAgentEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xOLTConfigDhcpRelayAgentEnabled.setStatus("current")
_Ltp8xOLTConfigDhcpCircuitIDFormat_Type = DisplayString
_Ltp8xOLTConfigDhcpCircuitIDFormat_Object = MibTableColumn
ltp8xOLTConfigDhcpCircuitIDFormat = _Ltp8xOLTConfigDhcpCircuitIDFormat_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 7, 1, 3),
    _Ltp8xOLTConfigDhcpCircuitIDFormat_Type()
)
ltp8xOLTConfigDhcpCircuitIDFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xOLTConfigDhcpCircuitIDFormat.setStatus("current")
_Ltp8xOLTConfigDhcpRemoteIDFormat_Type = DisplayString
_Ltp8xOLTConfigDhcpRemoteIDFormat_Object = MibTableColumn
ltp8xOLTConfigDhcpRemoteIDFormat = _Ltp8xOLTConfigDhcpRemoteIDFormat_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 7, 1, 4),
    _Ltp8xOLTConfigDhcpRemoteIDFormat_Type()
)
ltp8xOLTConfigDhcpRemoteIDFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xOLTConfigDhcpRemoteIDFormat.setStatus("current")
_Ltp8xOLTConfigDhcpOverwrtOption82_Type = TruthValue
_Ltp8xOLTConfigDhcpOverwrtOption82_Object = MibTableColumn
ltp8xOLTConfigDhcpOverwrtOption82 = _Ltp8xOLTConfigDhcpOverwrtOption82_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 7, 1, 5),
    _Ltp8xOLTConfigDhcpOverwrtOption82_Type()
)
ltp8xOLTConfigDhcpOverwrtOption82.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xOLTConfigDhcpOverwrtOption82.setStatus("current")
_Ltp8xOLTConfigDhcpDosBlockEnabled_Type = TruthValue
_Ltp8xOLTConfigDhcpDosBlockEnabled_Object = MibTableColumn
ltp8xOLTConfigDhcpDosBlockEnabled = _Ltp8xOLTConfigDhcpDosBlockEnabled_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 7, 1, 6),
    _Ltp8xOLTConfigDhcpDosBlockEnabled_Type()
)
ltp8xOLTConfigDhcpDosBlockEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xOLTConfigDhcpDosBlockEnabled.setStatus("current")
_Ltp8xOLTConfigDhcpBcPacketPerSecond_Type = Unsigned32
_Ltp8xOLTConfigDhcpBcPacketPerSecond_Object = MibTableColumn
ltp8xOLTConfigDhcpBcPacketPerSecond = _Ltp8xOLTConfigDhcpBcPacketPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 7, 1, 7),
    _Ltp8xOLTConfigDhcpBcPacketPerSecond_Type()
)
ltp8xOLTConfigDhcpBcPacketPerSecond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xOLTConfigDhcpBcPacketPerSecond.setStatus("current")
_Ltp8xOLTConfigDhcpPortBlockTime_Type = Unsigned32
_Ltp8xOLTConfigDhcpPortBlockTime_Object = MibTableColumn
ltp8xOLTConfigDhcpPortBlockTime = _Ltp8xOLTConfigDhcpPortBlockTime_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 7, 1, 8),
    _Ltp8xOLTConfigDhcpPortBlockTime_Type()
)
ltp8xOLTConfigDhcpPortBlockTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xOLTConfigDhcpPortBlockTime.setStatus("current")
_Ltp8xOLTConfigDhcpTrustedServerEnabled_Type = TruthValue
_Ltp8xOLTConfigDhcpTrustedServerEnabled_Object = MibTableColumn
ltp8xOLTConfigDhcpTrustedServerEnabled = _Ltp8xOLTConfigDhcpTrustedServerEnabled_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 7, 1, 9),
    _Ltp8xOLTConfigDhcpTrustedServerEnabled_Type()
)
ltp8xOLTConfigDhcpTrustedServerEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xOLTConfigDhcpTrustedServerEnabled.setStatus("current")
_Ltp8xOLTConfigDhcpTrustedPrimary_Type = IpAddress
_Ltp8xOLTConfigDhcpTrustedPrimary_Object = MibTableColumn
ltp8xOLTConfigDhcpTrustedPrimary = _Ltp8xOLTConfigDhcpTrustedPrimary_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 7, 1, 10),
    _Ltp8xOLTConfigDhcpTrustedPrimary_Type()
)
ltp8xOLTConfigDhcpTrustedPrimary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xOLTConfigDhcpTrustedPrimary.setStatus("current")
_Ltp8xOLTConfigDhcpTrustedSecondary_Type = IpAddress
_Ltp8xOLTConfigDhcpTrustedSecondary_Object = MibTableColumn
ltp8xOLTConfigDhcpTrustedSecondary = _Ltp8xOLTConfigDhcpTrustedSecondary_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 7, 1, 11),
    _Ltp8xOLTConfigDhcpTrustedSecondary_Type()
)
ltp8xOLTConfigDhcpTrustedSecondary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xOLTConfigDhcpTrustedSecondary.setStatus("current")
_Ltp8xOLTConfigDhcpTrustedServerTimeout_Type = Unsigned32
_Ltp8xOLTConfigDhcpTrustedServerTimeout_Object = MibTableColumn
ltp8xOLTConfigDhcpTrustedServerTimeout = _Ltp8xOLTConfigDhcpTrustedServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 7, 1, 12),
    _Ltp8xOLTConfigDhcpTrustedServerTimeout_Type()
)
ltp8xOLTConfigDhcpTrustedServerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xOLTConfigDhcpTrustedServerTimeout.setStatus("current")
_Ltp8xOLTMIBBoundary4_Type = Unsigned32
_Ltp8xOLTMIBBoundary4_Object = MibScalar
ltp8xOLTMIBBoundary4 = _Ltp8xOLTMIBBoundary4_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 8),
    _Ltp8xOLTMIBBoundary4_Type()
)
ltp8xOLTMIBBoundary4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xOLTMIBBoundary4.setStatus("current")
_Ltp8xOLTConfigPPPoETable_Object = MibTable
ltp8xOLTConfigPPPoETable = _Ltp8xOLTConfigPPPoETable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 9)
)
if mibBuilder.loadTexts:
    ltp8xOLTConfigPPPoETable.setStatus("current")
_Ltp8xOLTConfigPPPoEEntry_Object = MibTableRow
ltp8xOLTConfigPPPoEEntry = _Ltp8xOLTConfigPPPoEEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 9, 1)
)
ltp8xOLTConfigPPPoEEntry.setIndexNames(
    (0, "ELTEX-LTP8X", "ltp8xOLTConfigPPPoESlot"),
)
if mibBuilder.loadTexts:
    ltp8xOLTConfigPPPoEEntry.setStatus("current")
_Ltp8xOLTConfigPPPoESlot_Type = Unsigned32
_Ltp8xOLTConfigPPPoESlot_Object = MibTableColumn
ltp8xOLTConfigPPPoESlot = _Ltp8xOLTConfigPPPoESlot_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 9, 1, 1),
    _Ltp8xOLTConfigPPPoESlot_Type()
)
ltp8xOLTConfigPPPoESlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xOLTConfigPPPoESlot.setStatus("current")
_Ltp8xOLTConfigPPPoEPlusEnabled_Type = TruthValue
_Ltp8xOLTConfigPPPoEPlusEnabled_Object = MibTableColumn
ltp8xOLTConfigPPPoEPlusEnabled = _Ltp8xOLTConfigPPPoEPlusEnabled_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 9, 1, 2),
    _Ltp8xOLTConfigPPPoEPlusEnabled_Type()
)
ltp8xOLTConfigPPPoEPlusEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xOLTConfigPPPoEPlusEnabled.setStatus("current")
_Ltp8xOLTConfigPPPoECircuitIDFormat_Type = DisplayString
_Ltp8xOLTConfigPPPoECircuitIDFormat_Object = MibTableColumn
ltp8xOLTConfigPPPoECircuitIDFormat = _Ltp8xOLTConfigPPPoECircuitIDFormat_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 9, 1, 3),
    _Ltp8xOLTConfigPPPoECircuitIDFormat_Type()
)
ltp8xOLTConfigPPPoECircuitIDFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xOLTConfigPPPoECircuitIDFormat.setStatus("current")
_Ltp8xOLTConfigPPPoERemoteIDFormat_Type = DisplayString
_Ltp8xOLTConfigPPPoERemoteIDFormat_Object = MibTableColumn
ltp8xOLTConfigPPPoERemoteIDFormat = _Ltp8xOLTConfigPPPoERemoteIDFormat_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 9, 1, 4),
    _Ltp8xOLTConfigPPPoERemoteIDFormat_Type()
)
ltp8xOLTConfigPPPoERemoteIDFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xOLTConfigPPPoERemoteIDFormat.setStatus("current")
_Ltp8xOLTConfigPPPoEVendorID_Type = Unsigned32
_Ltp8xOLTConfigPPPoEVendorID_Object = MibTableColumn
ltp8xOLTConfigPPPoEVendorID = _Ltp8xOLTConfigPPPoEVendorID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 9, 1, 5),
    _Ltp8xOLTConfigPPPoEVendorID_Type()
)
ltp8xOLTConfigPPPoEVendorID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xOLTConfigPPPoEVendorID.setStatus("current")
_Ltp8xOLTConfigPPPoEMaxSessions_Type = Unsigned32
_Ltp8xOLTConfigPPPoEMaxSessions_Object = MibTableColumn
ltp8xOLTConfigPPPoEMaxSessions = _Ltp8xOLTConfigPPPoEMaxSessions_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 9, 1, 6),
    _Ltp8xOLTConfigPPPoEMaxSessions_Type()
)
ltp8xOLTConfigPPPoEMaxSessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xOLTConfigPPPoEMaxSessions.setStatus("current")
_Ltp8xOLTConfigPPPoEMaxSessionsPerUser_Type = Unsigned32
_Ltp8xOLTConfigPPPoEMaxSessionsPerUser_Object = MibTableColumn
ltp8xOLTConfigPPPoEMaxSessionsPerUser = _Ltp8xOLTConfigPPPoEMaxSessionsPerUser_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 9, 1, 7),
    _Ltp8xOLTConfigPPPoEMaxSessionsPerUser_Type()
)
ltp8xOLTConfigPPPoEMaxSessionsPerUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xOLTConfigPPPoEMaxSessionsPerUser.setStatus("current")
_Ltp8xOLTConfigPPPoEDosBlockEnabled_Type = TruthValue
_Ltp8xOLTConfigPPPoEDosBlockEnabled_Object = MibTableColumn
ltp8xOLTConfigPPPoEDosBlockEnabled = _Ltp8xOLTConfigPPPoEDosBlockEnabled_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 9, 1, 8),
    _Ltp8xOLTConfigPPPoEDosBlockEnabled_Type()
)
ltp8xOLTConfigPPPoEDosBlockEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xOLTConfigPPPoEDosBlockEnabled.setStatus("current")
_Ltp8xOLTConfigPPPoEBcPacketPerSecond_Type = Unsigned32
_Ltp8xOLTConfigPPPoEBcPacketPerSecond_Object = MibTableColumn
ltp8xOLTConfigPPPoEBcPacketPerSecond = _Ltp8xOLTConfigPPPoEBcPacketPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 9, 1, 9),
    _Ltp8xOLTConfigPPPoEBcPacketPerSecond_Type()
)
ltp8xOLTConfigPPPoEBcPacketPerSecond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xOLTConfigPPPoEBcPacketPerSecond.setStatus("current")
_Ltp8xOLTConfigPPPoEPortBlockTime_Type = Unsigned32
_Ltp8xOLTConfigPPPoEPortBlockTime_Object = MibTableColumn
ltp8xOLTConfigPPPoEPortBlockTime = _Ltp8xOLTConfigPPPoEPortBlockTime_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 9, 1, 10),
    _Ltp8xOLTConfigPPPoEPortBlockTime_Type()
)
ltp8xOLTConfigPPPoEPortBlockTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xOLTConfigPPPoEPortBlockTime.setStatus("current")
_Ltp8xOLTMIBBoundary5_Type = Unsigned32
_Ltp8xOLTMIBBoundary5_Object = MibScalar
ltp8xOLTMIBBoundary5 = _Ltp8xOLTMIBBoundary5_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 10),
    _Ltp8xOLTMIBBoundary5_Type()
)
ltp8xOLTMIBBoundary5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xOLTMIBBoundary5.setStatus("current")
_Ltp8xOLTPPPoESessionsTable_Object = MibTable
ltp8xOLTPPPoESessionsTable = _Ltp8xOLTPPPoESessionsTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 11)
)
if mibBuilder.loadTexts:
    ltp8xOLTPPPoESessionsTable.setStatus("current")
_Ltp8xOLTPPPoESessionsEntry_Object = MibTableRow
ltp8xOLTPPPoESessionsEntry = _Ltp8xOLTPPPoESessionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 11, 1)
)
ltp8xOLTPPPoESessionsEntry.setIndexNames(
    (0, "ELTEX-LTP8X", "ltp8xOLTPPPoESessionsSlot"),
    (0, "ELTEX-LTP8X", "ltp8xOLTPPPoESessionsChannel"),
    (0, "ELTEX-LTP8X", "ltp8xOLTPPPoESessionsOntID"),
    (0, "ELTEX-LTP8X", "ltp8xOLTPPPoESessionsClientMac"),
)
if mibBuilder.loadTexts:
    ltp8xOLTPPPoESessionsEntry.setStatus("current")
_Ltp8xOLTPPPoESessionsSlot_Type = Unsigned32
_Ltp8xOLTPPPoESessionsSlot_Object = MibTableColumn
ltp8xOLTPPPoESessionsSlot = _Ltp8xOLTPPPoESessionsSlot_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 11, 1, 1),
    _Ltp8xOLTPPPoESessionsSlot_Type()
)
ltp8xOLTPPPoESessionsSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xOLTPPPoESessionsSlot.setStatus("current")
_Ltp8xOLTPPPoESessionsChannel_Type = Unsigned32
_Ltp8xOLTPPPoESessionsChannel_Object = MibTableColumn
ltp8xOLTPPPoESessionsChannel = _Ltp8xOLTPPPoESessionsChannel_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 11, 1, 2),
    _Ltp8xOLTPPPoESessionsChannel_Type()
)
ltp8xOLTPPPoESessionsChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xOLTPPPoESessionsChannel.setStatus("current")
_Ltp8xOLTPPPoESessionsOntID_Type = Unsigned32
_Ltp8xOLTPPPoESessionsOntID_Object = MibTableColumn
ltp8xOLTPPPoESessionsOntID = _Ltp8xOLTPPPoESessionsOntID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 11, 1, 3),
    _Ltp8xOLTPPPoESessionsOntID_Type()
)
ltp8xOLTPPPoESessionsOntID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xOLTPPPoESessionsOntID.setStatus("current")
_Ltp8xOLTPPPoESessionsClientMac_Type = MacAddress
_Ltp8xOLTPPPoESessionsClientMac_Object = MibTableColumn
ltp8xOLTPPPoESessionsClientMac = _Ltp8xOLTPPPoESessionsClientMac_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 11, 1, 4),
    _Ltp8xOLTPPPoESessionsClientMac_Type()
)
ltp8xOLTPPPoESessionsClientMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xOLTPPPoESessionsClientMac.setStatus("current")
_Ltp8xOLTPPPoESessionsPort_Type = Unsigned32
_Ltp8xOLTPPPoESessionsPort_Object = MibTableColumn
ltp8xOLTPPPoESessionsPort = _Ltp8xOLTPPPoESessionsPort_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 11, 1, 5),
    _Ltp8xOLTPPPoESessionsPort_Type()
)
ltp8xOLTPPPoESessionsPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xOLTPPPoESessionsPort.setStatus("current")
_Ltp8xOLTPPPoESessionsSessionID_Type = Unsigned32
_Ltp8xOLTPPPoESessionsSessionID_Object = MibTableColumn
ltp8xOLTPPPoESessionsSessionID = _Ltp8xOLTPPPoESessionsSessionID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 11, 1, 6),
    _Ltp8xOLTPPPoESessionsSessionID_Type()
)
ltp8xOLTPPPoESessionsSessionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xOLTPPPoESessionsSessionID.setStatus("current")
_Ltp8xOLTPPPoESessionsDuration_Type = TimeTicks
_Ltp8xOLTPPPoESessionsDuration_Object = MibTableColumn
ltp8xOLTPPPoESessionsDuration = _Ltp8xOLTPPPoESessionsDuration_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 11, 1, 7),
    _Ltp8xOLTPPPoESessionsDuration_Type()
)
ltp8xOLTPPPoESessionsDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xOLTPPPoESessionsDuration.setStatus("current")
_Ltp8xOLTPPPoESessionsUnblock_Type = TimeTicks
_Ltp8xOLTPPPoESessionsUnblock_Object = MibTableColumn
ltp8xOLTPPPoESessionsUnblock = _Ltp8xOLTPPPoESessionsUnblock_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 11, 1, 8),
    _Ltp8xOLTPPPoESessionsUnblock_Type()
)
ltp8xOLTPPPoESessionsUnblock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xOLTPPPoESessionsUnblock.setStatus("current")
_Ltp8xOLTPPPoESessionsSerial_Type = ONTSerial
_Ltp8xOLTPPPoESessionsSerial_Object = MibTableColumn
ltp8xOLTPPPoESessionsSerial = _Ltp8xOLTPPPoESessionsSerial_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 11, 1, 9),
    _Ltp8xOLTPPPoESessionsSerial_Type()
)
ltp8xOLTPPPoESessionsSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xOLTPPPoESessionsSerial.setStatus("current")
_Ltp8xOLTMIBBoundary6_Type = Unsigned32
_Ltp8xOLTMIBBoundary6_Object = MibScalar
ltp8xOLTMIBBoundary6 = _Ltp8xOLTMIBBoundary6_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 12),
    _Ltp8xOLTMIBBoundary6_Type()
)
ltp8xOLTMIBBoundary6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xOLTMIBBoundary6.setStatus("current")
_Ltp8xOLTMulticastStatsTable_Object = MibTable
ltp8xOLTMulticastStatsTable = _Ltp8xOLTMulticastStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 13)
)
if mibBuilder.loadTexts:
    ltp8xOLTMulticastStatsTable.setStatus("current")
_Ltp8xOLTMulticastStatsEntry_Object = MibTableRow
ltp8xOLTMulticastStatsEntry = _Ltp8xOLTMulticastStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 13, 1)
)
ltp8xOLTMulticastStatsEntry.setIndexNames(
    (0, "ELTEX-LTP8X", "ltp8xOLTMulticastStatsSlot"),
    (0, "ELTEX-LTP8X", "ltp8xOLTMulticastStatsChannel"),
    (0, "ELTEX-LTP8X", "ltp8xOLTMulticastStatsRecordID"),
)
if mibBuilder.loadTexts:
    ltp8xOLTMulticastStatsEntry.setStatus("current")
_Ltp8xOLTMulticastStatsSlot_Type = Unsigned32
_Ltp8xOLTMulticastStatsSlot_Object = MibTableColumn
ltp8xOLTMulticastStatsSlot = _Ltp8xOLTMulticastStatsSlot_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 13, 1, 1),
    _Ltp8xOLTMulticastStatsSlot_Type()
)
ltp8xOLTMulticastStatsSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xOLTMulticastStatsSlot.setStatus("current")
_Ltp8xOLTMulticastStatsChannel_Type = Unsigned32
_Ltp8xOLTMulticastStatsChannel_Object = MibTableColumn
ltp8xOLTMulticastStatsChannel = _Ltp8xOLTMulticastStatsChannel_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 13, 1, 2),
    _Ltp8xOLTMulticastStatsChannel_Type()
)
ltp8xOLTMulticastStatsChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xOLTMulticastStatsChannel.setStatus("current")
_Ltp8xOLTMulticastStatsRecordID_Type = Unsigned32
_Ltp8xOLTMulticastStatsRecordID_Object = MibTableColumn
ltp8xOLTMulticastStatsRecordID = _Ltp8xOLTMulticastStatsRecordID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 13, 1, 3),
    _Ltp8xOLTMulticastStatsRecordID_Type()
)
ltp8xOLTMulticastStatsRecordID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xOLTMulticastStatsRecordID.setStatus("current")
_Ltp8xOLTMulticastStatsONTSerial_Type = ONTSerial
_Ltp8xOLTMulticastStatsONTSerial_Object = MibTableColumn
ltp8xOLTMulticastStatsONTSerial = _Ltp8xOLTMulticastStatsONTSerial_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 13, 1, 4),
    _Ltp8xOLTMulticastStatsONTSerial_Type()
)
ltp8xOLTMulticastStatsONTSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xOLTMulticastStatsONTSerial.setStatus("current")
_Ltp8xOLTMulticastStatsMulticastAddress_Type = IpAddress
_Ltp8xOLTMulticastStatsMulticastAddress_Object = MibTableColumn
ltp8xOLTMulticastStatsMulticastAddress = _Ltp8xOLTMulticastStatsMulticastAddress_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 13, 1, 5),
    _Ltp8xOLTMulticastStatsMulticastAddress_Type()
)
ltp8xOLTMulticastStatsMulticastAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xOLTMulticastStatsMulticastAddress.setStatus("current")
_Ltp8xOLTMulticastStatsStart_Type = DisplayString
_Ltp8xOLTMulticastStatsStart_Object = MibTableColumn
ltp8xOLTMulticastStatsStart = _Ltp8xOLTMulticastStatsStart_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 13, 1, 6),
    _Ltp8xOLTMulticastStatsStart_Type()
)
ltp8xOLTMulticastStatsStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xOLTMulticastStatsStart.setStatus("current")
_Ltp8xOLTMulticastStatsStop_Type = DisplayString
_Ltp8xOLTMulticastStatsStop_Object = MibTableColumn
ltp8xOLTMulticastStatsStop = _Ltp8xOLTMulticastStatsStop_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 13, 1, 7),
    _Ltp8xOLTMulticastStatsStop_Type()
)
ltp8xOLTMulticastStatsStop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xOLTMulticastStatsStop.setStatus("current")
_Ltp8xOLTMIBBoundary7_Type = Unsigned32
_Ltp8xOLTMIBBoundary7_Object = MibScalar
ltp8xOLTMIBBoundary7 = _Ltp8xOLTMIBBoundary7_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 14),
    _Ltp8xOLTMIBBoundary7_Type()
)
ltp8xOLTMIBBoundary7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xOLTMIBBoundary7.setStatus("current")
_Ltp8xOLTAddressTableProfilesTable_Object = MibTable
ltp8xOLTAddressTableProfilesTable = _Ltp8xOLTAddressTableProfilesTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 15)
)
if mibBuilder.loadTexts:
    ltp8xOLTAddressTableProfilesTable.setStatus("current")
_Ltp8xOLTAddressTableProfilesEntry_Object = MibTableRow
ltp8xOLTAddressTableProfilesEntry = _Ltp8xOLTAddressTableProfilesEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 15, 1)
)
ltp8xOLTAddressTableProfilesEntry.setIndexNames(
    (0, "ELTEX-LTP8X", "ltp8xOLTAddressTableProfilesID"),
)
if mibBuilder.loadTexts:
    ltp8xOLTAddressTableProfilesEntry.setStatus("current")
_Ltp8xOLTAddressTableProfilesID_Type = Unsigned32
_Ltp8xOLTAddressTableProfilesID_Object = MibTableColumn
ltp8xOLTAddressTableProfilesID = _Ltp8xOLTAddressTableProfilesID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 15, 1, 1),
    _Ltp8xOLTAddressTableProfilesID_Type()
)
ltp8xOLTAddressTableProfilesID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xOLTAddressTableProfilesID.setStatus("current")
_Ltp8xOLTAddressTableProfilesDescription_Type = DisplayString
_Ltp8xOLTAddressTableProfilesDescription_Object = MibTableColumn
ltp8xOLTAddressTableProfilesDescription = _Ltp8xOLTAddressTableProfilesDescription_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 15, 1, 2),
    _Ltp8xOLTAddressTableProfilesDescription_Type()
)
ltp8xOLTAddressTableProfilesDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xOLTAddressTableProfilesDescription.setStatus("current")
_Ltp8xOLTMIBBoundary8_Type = Unsigned32
_Ltp8xOLTMIBBoundary8_Object = MibScalar
ltp8xOLTMIBBoundary8 = _Ltp8xOLTMIBBoundary8_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 16),
    _Ltp8xOLTMIBBoundary8_Type()
)
ltp8xOLTMIBBoundary8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xOLTMIBBoundary8.setStatus("current")
_Ltp8xOLTVlanProfilesTable_Object = MibTable
ltp8xOLTVlanProfilesTable = _Ltp8xOLTVlanProfilesTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 17)
)
if mibBuilder.loadTexts:
    ltp8xOLTVlanProfilesTable.setStatus("current")
_Ltp8xOLTVlanProfilesEntry_Object = MibTableRow
ltp8xOLTVlanProfilesEntry = _Ltp8xOLTVlanProfilesEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 17, 1)
)
ltp8xOLTVlanProfilesEntry.setIndexNames(
    (0, "ELTEX-LTP8X", "ltp8xOLTVlanProfilesID"),
)
if mibBuilder.loadTexts:
    ltp8xOLTVlanProfilesEntry.setStatus("current")
_Ltp8xOLTVlanProfilesID_Type = Unsigned32
_Ltp8xOLTVlanProfilesID_Object = MibTableColumn
ltp8xOLTVlanProfilesID = _Ltp8xOLTVlanProfilesID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 17, 1, 1),
    _Ltp8xOLTVlanProfilesID_Type()
)
ltp8xOLTVlanProfilesID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xOLTVlanProfilesID.setStatus("current")
_Ltp8xOLTVlanProfilesDescription_Type = DisplayString
_Ltp8xOLTVlanProfilesDescription_Object = MibTableColumn
ltp8xOLTVlanProfilesDescription = _Ltp8xOLTVlanProfilesDescription_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 17, 1, 2),
    _Ltp8xOLTVlanProfilesDescription_Type()
)
ltp8xOLTVlanProfilesDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xOLTVlanProfilesDescription.setStatus("current")
_Ltp8xOLTUpdateFirmwareTable_Object = MibTable
ltp8xOLTUpdateFirmwareTable = _Ltp8xOLTUpdateFirmwareTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 18)
)
if mibBuilder.loadTexts:
    ltp8xOLTUpdateFirmwareTable.setStatus("current")
_Ltp8xOLTUpdateFirmwareEntry_Object = MibTableRow
ltp8xOLTUpdateFirmwareEntry = _Ltp8xOLTUpdateFirmwareEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 18, 1)
)
ltp8xOLTUpdateFirmwareEntry.setIndexNames(
    (0, "ELTEX-LTP8X", "ltp8xOLTUpdateFirmwareSlot"),
)
if mibBuilder.loadTexts:
    ltp8xOLTUpdateFirmwareEntry.setStatus("current")
_Ltp8xOLTUpdateFirmwareSlot_Type = Unsigned32
_Ltp8xOLTUpdateFirmwareSlot_Object = MibTableColumn
ltp8xOLTUpdateFirmwareSlot = _Ltp8xOLTUpdateFirmwareSlot_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 18, 1, 1),
    _Ltp8xOLTUpdateFirmwareSlot_Type()
)
ltp8xOLTUpdateFirmwareSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xOLTUpdateFirmwareSlot.setStatus("current")
_Ltp8xOLTUpdateFirmwareAction_Type = Unsigned32
_Ltp8xOLTUpdateFirmwareAction_Object = MibTableColumn
ltp8xOLTUpdateFirmwareAction = _Ltp8xOLTUpdateFirmwareAction_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 18, 1, 2),
    _Ltp8xOLTUpdateFirmwareAction_Type()
)
ltp8xOLTUpdateFirmwareAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xOLTUpdateFirmwareAction.setStatus("current")
_Ltp8xOLTMulticastStatsBackwardsTable_Object = MibTable
ltp8xOLTMulticastStatsBackwardsTable = _Ltp8xOLTMulticastStatsBackwardsTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 19)
)
if mibBuilder.loadTexts:
    ltp8xOLTMulticastStatsBackwardsTable.setStatus("current")
_Ltp8xOLTMulticastStatsBackwardsEntry_Object = MibTableRow
ltp8xOLTMulticastStatsBackwardsEntry = _Ltp8xOLTMulticastStatsBackwardsEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 19, 1)
)
ltp8xOLTMulticastStatsBackwardsEntry.setIndexNames(
    (0, "ELTEX-LTP8X", "ltp8xOLTMulticastStatsBackwardsSlot"),
    (0, "ELTEX-LTP8X", "ltp8xOLTMulticastStatsBackwardsONTSerial"),
    (0, "ELTEX-LTP8X", "ltp8xOLTMulticastStatsBackwardsRecordID"),
)
if mibBuilder.loadTexts:
    ltp8xOLTMulticastStatsBackwardsEntry.setStatus("current")
_Ltp8xOLTMulticastStatsBackwardsSlot_Type = Unsigned32
_Ltp8xOLTMulticastStatsBackwardsSlot_Object = MibTableColumn
ltp8xOLTMulticastStatsBackwardsSlot = _Ltp8xOLTMulticastStatsBackwardsSlot_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 19, 1, 1),
    _Ltp8xOLTMulticastStatsBackwardsSlot_Type()
)
ltp8xOLTMulticastStatsBackwardsSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xOLTMulticastStatsBackwardsSlot.setStatus("current")
_Ltp8xOLTMulticastStatsBackwardsONTSerial_Type = ONTSerial
_Ltp8xOLTMulticastStatsBackwardsONTSerial_Object = MibTableColumn
ltp8xOLTMulticastStatsBackwardsONTSerial = _Ltp8xOLTMulticastStatsBackwardsONTSerial_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 19, 1, 2),
    _Ltp8xOLTMulticastStatsBackwardsONTSerial_Type()
)
ltp8xOLTMulticastStatsBackwardsONTSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xOLTMulticastStatsBackwardsONTSerial.setStatus("current")
_Ltp8xOLTMulticastStatsBackwardsRecordID_Type = Unsigned32
_Ltp8xOLTMulticastStatsBackwardsRecordID_Object = MibTableColumn
ltp8xOLTMulticastStatsBackwardsRecordID = _Ltp8xOLTMulticastStatsBackwardsRecordID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 19, 1, 3),
    _Ltp8xOLTMulticastStatsBackwardsRecordID_Type()
)
ltp8xOLTMulticastStatsBackwardsRecordID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xOLTMulticastStatsBackwardsRecordID.setStatus("current")
_Ltp8xOLTMulticastStatsBackwardsMulticastAddress_Type = IpAddress
_Ltp8xOLTMulticastStatsBackwardsMulticastAddress_Object = MibTableColumn
ltp8xOLTMulticastStatsBackwardsMulticastAddress = _Ltp8xOLTMulticastStatsBackwardsMulticastAddress_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 19, 1, 4),
    _Ltp8xOLTMulticastStatsBackwardsMulticastAddress_Type()
)
ltp8xOLTMulticastStatsBackwardsMulticastAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xOLTMulticastStatsBackwardsMulticastAddress.setStatus("current")
_Ltp8xOLTMulticastStatsBackwardsStart_Type = DisplayString
_Ltp8xOLTMulticastStatsBackwardsStart_Object = MibTableColumn
ltp8xOLTMulticastStatsBackwardsStart = _Ltp8xOLTMulticastStatsBackwardsStart_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 19, 1, 5),
    _Ltp8xOLTMulticastStatsBackwardsStart_Type()
)
ltp8xOLTMulticastStatsBackwardsStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xOLTMulticastStatsBackwardsStart.setStatus("current")
_Ltp8xOLTMulticastStatsBackwardsStop_Type = DisplayString
_Ltp8xOLTMulticastStatsBackwardsStop_Object = MibTableColumn
ltp8xOLTMulticastStatsBackwardsStop = _Ltp8xOLTMulticastStatsBackwardsStop_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 19, 1, 6),
    _Ltp8xOLTMulticastStatsBackwardsStop_Type()
)
ltp8xOLTMulticastStatsBackwardsStop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xOLTMulticastStatsBackwardsStop.setStatus("current")
_Ltp8xOLTONTAutoFirmwareUpdateTable_Object = MibTable
ltp8xOLTONTAutoFirmwareUpdateTable = _Ltp8xOLTONTAutoFirmwareUpdateTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 20)
)
if mibBuilder.loadTexts:
    ltp8xOLTONTAutoFirmwareUpdateTable.setStatus("current")
_Ltp8xOLTONTAutoFirmwareUpdateEntry_Object = MibTableRow
ltp8xOLTONTAutoFirmwareUpdateEntry = _Ltp8xOLTONTAutoFirmwareUpdateEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 20, 1)
)
ltp8xOLTONTAutoFirmwareUpdateEntry.setIndexNames(
    (0, "ELTEX-LTP8X", "ltp8xOLTONTAutoFirmwareUpdateSlot"),
)
if mibBuilder.loadTexts:
    ltp8xOLTONTAutoFirmwareUpdateEntry.setStatus("current")
_Ltp8xOLTONTAutoFirmwareUpdateSlot_Type = Unsigned32
_Ltp8xOLTONTAutoFirmwareUpdateSlot_Object = MibTableColumn
ltp8xOLTONTAutoFirmwareUpdateSlot = _Ltp8xOLTONTAutoFirmwareUpdateSlot_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 20, 1, 1),
    _Ltp8xOLTONTAutoFirmwareUpdateSlot_Type()
)
ltp8xOLTONTAutoFirmwareUpdateSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xOLTONTAutoFirmwareUpdateSlot.setStatus("current")
_Ltp8xOLTONTAutoFirmwareUpdateEnabled_Type = TruthValue
_Ltp8xOLTONTAutoFirmwareUpdateEnabled_Object = MibTableColumn
ltp8xOLTONTAutoFirmwareUpdateEnabled = _Ltp8xOLTONTAutoFirmwareUpdateEnabled_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 20, 1, 2),
    _Ltp8xOLTONTAutoFirmwareUpdateEnabled_Type()
)
ltp8xOLTONTAutoFirmwareUpdateEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xOLTONTAutoFirmwareUpdateEnabled.setStatus("current")
_Ltp8xOLTVInterfaceMonitoringDSTable_Object = MibTable
ltp8xOLTVInterfaceMonitoringDSTable = _Ltp8xOLTVInterfaceMonitoringDSTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 30)
)
if mibBuilder.loadTexts:
    ltp8xOLTVInterfaceMonitoringDSTable.setStatus("current")
_Ltp8xOLTVInterfaceMonitoringDSEntry_Object = MibTableRow
ltp8xOLTVInterfaceMonitoringDSEntry = _Ltp8xOLTVInterfaceMonitoringDSEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 30, 1)
)
ltp8xOLTVInterfaceMonitoringDSEntry.setIndexNames(
    (0, "ELTEX-LTP8X", "ltp8xOLTVInterfaceMonitoringDSSlot"),
    (0, "ELTEX-LTP8X", "ltp8xOLTVInterfaceMonitoringDSChannelRange"),
    (0, "ELTEX-LTP8X", "ltp8xOLTVInterfaceMonitoringDSCounterID"),
)
if mibBuilder.loadTexts:
    ltp8xOLTVInterfaceMonitoringDSEntry.setStatus("current")
_Ltp8xOLTVInterfaceMonitoringDSSlot_Type = Unsigned32
_Ltp8xOLTVInterfaceMonitoringDSSlot_Object = MibTableColumn
ltp8xOLTVInterfaceMonitoringDSSlot = _Ltp8xOLTVInterfaceMonitoringDSSlot_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 30, 1, 1),
    _Ltp8xOLTVInterfaceMonitoringDSSlot_Type()
)
ltp8xOLTVInterfaceMonitoringDSSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xOLTVInterfaceMonitoringDSSlot.setStatus("current")


class _Ltp8xOLTVInterfaceMonitoringDSChannelRange_Type(Integer32):
    """Custom type ltp8xOLTVInterfaceMonitoringDSChannelRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("range0-3", 1),
          ("range4-7", 2))
    )


_Ltp8xOLTVInterfaceMonitoringDSChannelRange_Type.__name__ = "Integer32"
_Ltp8xOLTVInterfaceMonitoringDSChannelRange_Object = MibTableColumn
ltp8xOLTVInterfaceMonitoringDSChannelRange = _Ltp8xOLTVInterfaceMonitoringDSChannelRange_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 30, 1, 2),
    _Ltp8xOLTVInterfaceMonitoringDSChannelRange_Type()
)
ltp8xOLTVInterfaceMonitoringDSChannelRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xOLTVInterfaceMonitoringDSChannelRange.setStatus("current")
_Ltp8xOLTVInterfaceMonitoringDSCounterID_Type = Unsigned32
_Ltp8xOLTVInterfaceMonitoringDSCounterID_Object = MibTableColumn
ltp8xOLTVInterfaceMonitoringDSCounterID = _Ltp8xOLTVInterfaceMonitoringDSCounterID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 30, 1, 3),
    _Ltp8xOLTVInterfaceMonitoringDSCounterID_Type()
)
ltp8xOLTVInterfaceMonitoringDSCounterID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xOLTVInterfaceMonitoringDSCounterID.setStatus("current")
_Ltp8xOLTVInterfaceMonitoringDSCounterName_Type = DisplayString
_Ltp8xOLTVInterfaceMonitoringDSCounterName_Object = MibTableColumn
ltp8xOLTVInterfaceMonitoringDSCounterName = _Ltp8xOLTVInterfaceMonitoringDSCounterName_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 30, 1, 4),
    _Ltp8xOLTVInterfaceMonitoringDSCounterName_Type()
)
ltp8xOLTVInterfaceMonitoringDSCounterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xOLTVInterfaceMonitoringDSCounterName.setStatus("current")
_Ltp8xOLTVInterfaceMonitoringDSCounterValue_Type = Unsigned32
_Ltp8xOLTVInterfaceMonitoringDSCounterValue_Object = MibTableColumn
ltp8xOLTVInterfaceMonitoringDSCounterValue = _Ltp8xOLTVInterfaceMonitoringDSCounterValue_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 30, 1, 5),
    _Ltp8xOLTVInterfaceMonitoringDSCounterValue_Type()
)
ltp8xOLTVInterfaceMonitoringDSCounterValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xOLTVInterfaceMonitoringDSCounterValue.setStatus("current")
_Ltp8xOLTVInterfaceMonitoringUSTable_Object = MibTable
ltp8xOLTVInterfaceMonitoringUSTable = _Ltp8xOLTVInterfaceMonitoringUSTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 31)
)
if mibBuilder.loadTexts:
    ltp8xOLTVInterfaceMonitoringUSTable.setStatus("current")
_Ltp8xOLTVInterfaceMonitoringUSEntry_Object = MibTableRow
ltp8xOLTVInterfaceMonitoringUSEntry = _Ltp8xOLTVInterfaceMonitoringUSEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 31, 1)
)
ltp8xOLTVInterfaceMonitoringUSEntry.setIndexNames(
    (0, "ELTEX-LTP8X", "ltp8xOLTVInterfaceMonitoringUSSlot"),
    (0, "ELTEX-LTP8X", "ltp8xOLTVInterfaceMonitoringUSChannelRange"),
    (0, "ELTEX-LTP8X", "ltp8xOLTVInterfaceMonitoringUSCounterID"),
)
if mibBuilder.loadTexts:
    ltp8xOLTVInterfaceMonitoringUSEntry.setStatus("current")
_Ltp8xOLTVInterfaceMonitoringUSSlot_Type = Unsigned32
_Ltp8xOLTVInterfaceMonitoringUSSlot_Object = MibTableColumn
ltp8xOLTVInterfaceMonitoringUSSlot = _Ltp8xOLTVInterfaceMonitoringUSSlot_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 31, 1, 1),
    _Ltp8xOLTVInterfaceMonitoringUSSlot_Type()
)
ltp8xOLTVInterfaceMonitoringUSSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xOLTVInterfaceMonitoringUSSlot.setStatus("current")


class _Ltp8xOLTVInterfaceMonitoringUSChannelRange_Type(Integer32):
    """Custom type ltp8xOLTVInterfaceMonitoringUSChannelRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("range0-3", 1),
          ("range4-7", 2))
    )


_Ltp8xOLTVInterfaceMonitoringUSChannelRange_Type.__name__ = "Integer32"
_Ltp8xOLTVInterfaceMonitoringUSChannelRange_Object = MibTableColumn
ltp8xOLTVInterfaceMonitoringUSChannelRange = _Ltp8xOLTVInterfaceMonitoringUSChannelRange_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 31, 1, 2),
    _Ltp8xOLTVInterfaceMonitoringUSChannelRange_Type()
)
ltp8xOLTVInterfaceMonitoringUSChannelRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xOLTVInterfaceMonitoringUSChannelRange.setStatus("current")
_Ltp8xOLTVInterfaceMonitoringUSCounterID_Type = Unsigned32
_Ltp8xOLTVInterfaceMonitoringUSCounterID_Object = MibTableColumn
ltp8xOLTVInterfaceMonitoringUSCounterID = _Ltp8xOLTVInterfaceMonitoringUSCounterID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 31, 1, 3),
    _Ltp8xOLTVInterfaceMonitoringUSCounterID_Type()
)
ltp8xOLTVInterfaceMonitoringUSCounterID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xOLTVInterfaceMonitoringUSCounterID.setStatus("current")
_Ltp8xOLTVInterfaceMonitoringUSCounterName_Type = DisplayString
_Ltp8xOLTVInterfaceMonitoringUSCounterName_Object = MibTableColumn
ltp8xOLTVInterfaceMonitoringUSCounterName = _Ltp8xOLTVInterfaceMonitoringUSCounterName_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 31, 1, 4),
    _Ltp8xOLTVInterfaceMonitoringUSCounterName_Type()
)
ltp8xOLTVInterfaceMonitoringUSCounterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xOLTVInterfaceMonitoringUSCounterName.setStatus("current")
_Ltp8xOLTVInterfaceMonitoringUSCounterValue_Type = Unsigned32
_Ltp8xOLTVInterfaceMonitoringUSCounterValue_Object = MibTableColumn
ltp8xOLTVInterfaceMonitoringUSCounterValue = _Ltp8xOLTVInterfaceMonitoringUSCounterValue_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 31, 1, 5),
    _Ltp8xOLTVInterfaceMonitoringUSCounterValue_Type()
)
ltp8xOLTVInterfaceMonitoringUSCounterValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xOLTVInterfaceMonitoringUSCounterValue.setStatus("current")
_Ltp8xOLTResetCountersTable_Object = MibTable
ltp8xOLTResetCountersTable = _Ltp8xOLTResetCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 50)
)
if mibBuilder.loadTexts:
    ltp8xOLTResetCountersTable.setStatus("current")
_Ltp8xOLTResetCountersEntry_Object = MibTableRow
ltp8xOLTResetCountersEntry = _Ltp8xOLTResetCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 50, 1)
)
ltp8xOLTResetCountersEntry.setIndexNames(
    (0, "ELTEX-LTP8X", "ltp8xOLTResetCountersSlot"),
)
if mibBuilder.loadTexts:
    ltp8xOLTResetCountersEntry.setStatus("current")
_Ltp8xOLTResetCountersSlot_Type = Unsigned32
_Ltp8xOLTResetCountersSlot_Object = MibTableColumn
ltp8xOLTResetCountersSlot = _Ltp8xOLTResetCountersSlot_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 50, 1, 1),
    _Ltp8xOLTResetCountersSlot_Type()
)
ltp8xOLTResetCountersSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xOLTResetCountersSlot.setStatus("current")
_Ltp8xOLTResetCountersAction_Type = Unsigned32
_Ltp8xOLTResetCountersAction_Object = MibTableColumn
ltp8xOLTResetCountersAction = _Ltp8xOLTResetCountersAction_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 50, 1, 2),
    _Ltp8xOLTResetCountersAction_Type()
)
ltp8xOLTResetCountersAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xOLTResetCountersAction.setStatus("current")
_Ltp8xOLTTerminalVLANsTable_Object = MibTable
ltp8xOLTTerminalVLANsTable = _Ltp8xOLTTerminalVLANsTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 51)
)
if mibBuilder.loadTexts:
    ltp8xOLTTerminalVLANsTable.setStatus("current")
_Ltp8xOLTTerminalVLANsEntry_Object = MibTableRow
ltp8xOLTTerminalVLANsEntry = _Ltp8xOLTTerminalVLANsEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 51, 1)
)
ltp8xOLTTerminalVLANsEntry.setIndexNames(
    (0, "ELTEX-LTP8X", "ltp8xOLTTerminalVLANsSlot"),
    (0, "ELTEX-LTP8X", "ltp8xOLTTerminalVLANsID"),
)
if mibBuilder.loadTexts:
    ltp8xOLTTerminalVLANsEntry.setStatus("current")
_Ltp8xOLTTerminalVLANsSlot_Type = Unsigned32
_Ltp8xOLTTerminalVLANsSlot_Object = MibTableColumn
ltp8xOLTTerminalVLANsSlot = _Ltp8xOLTTerminalVLANsSlot_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 51, 1, 1),
    _Ltp8xOLTTerminalVLANsSlot_Type()
)
ltp8xOLTTerminalVLANsSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ltp8xOLTTerminalVLANsSlot.setStatus("current")
_Ltp8xOLTTerminalVLANsID_Type = Unsigned32
_Ltp8xOLTTerminalVLANsID_Object = MibTableColumn
ltp8xOLTTerminalVLANsID = _Ltp8xOLTTerminalVLANsID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 51, 1, 2),
    _Ltp8xOLTTerminalVLANsID_Type()
)
ltp8xOLTTerminalVLANsID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ltp8xOLTTerminalVLANsID.setStatus("current")
_Ltp8xOLTTerminalVLANsName_Type = DisplayString
_Ltp8xOLTTerminalVLANsName_Object = MibTableColumn
ltp8xOLTTerminalVLANsName = _Ltp8xOLTTerminalVLANsName_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 51, 1, 3),
    _Ltp8xOLTTerminalVLANsName_Type()
)
ltp8xOLTTerminalVLANsName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xOLTTerminalVLANsName.setStatus("current")
_Ltp8xOLTTerminalVLANsVID_Type = Unsigned32
_Ltp8xOLTTerminalVLANsVID_Object = MibTableColumn
ltp8xOLTTerminalVLANsVID = _Ltp8xOLTTerminalVLANsVID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 51, 1, 4),
    _Ltp8xOLTTerminalVLANsVID_Type()
)
ltp8xOLTTerminalVLANsVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xOLTTerminalVLANsVID.setStatus("current")


class _Ltp8xOLTTerminalVLANsCOS_Type(Integer32):
    """Custom type ltp8xOLTTerminalVLANsCOS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            255
        )
    )
    namedValues = NamedValues(
        ("unused", 255)
    )


_Ltp8xOLTTerminalVLANsCOS_Type.__name__ = "Integer32"
_Ltp8xOLTTerminalVLANsCOS_Object = MibTableColumn
ltp8xOLTTerminalVLANsCOS = _Ltp8xOLTTerminalVLANsCOS_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 51, 1, 5),
    _Ltp8xOLTTerminalVLANsCOS_Type()
)
ltp8xOLTTerminalVLANsCOS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xOLTTerminalVLANsCOS.setStatus("current")
_Ltp8xOLTTerminalVLANsRowStatus_Type = RowStatus
_Ltp8xOLTTerminalVLANsRowStatus_Object = MibTableColumn
ltp8xOLTTerminalVLANsRowStatus = _Ltp8xOLTTerminalVLANsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 51, 1, 10),
    _Ltp8xOLTTerminalVLANsRowStatus_Type()
)
ltp8xOLTTerminalVLANsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xOLTTerminalVLANsRowStatus.setStatus("current")
_Ltp8xOLTTerminalVLANsNamesTable_Object = MibTable
ltp8xOLTTerminalVLANsNamesTable = _Ltp8xOLTTerminalVLANsNamesTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 52)
)
if mibBuilder.loadTexts:
    ltp8xOLTTerminalVLANsNamesTable.setStatus("current")
_Ltp8xOLTTerminalVLANsNamesEntry_Object = MibTableRow
ltp8xOLTTerminalVLANsNamesEntry = _Ltp8xOLTTerminalVLANsNamesEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 52, 1)
)
ltp8xOLTTerminalVLANsNamesEntry.setIndexNames(
    (0, "ELTEX-LTP8X", "ltp8xOLTTerminalVLANsNamesID"),
)
if mibBuilder.loadTexts:
    ltp8xOLTTerminalVLANsNamesEntry.setStatus("current")
_Ltp8xOLTTerminalVLANsNamesID_Type = Unsigned32
_Ltp8xOLTTerminalVLANsNamesID_Object = MibTableColumn
ltp8xOLTTerminalVLANsNamesID = _Ltp8xOLTTerminalVLANsNamesID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 52, 1, 2),
    _Ltp8xOLTTerminalVLANsNamesID_Type()
)
ltp8xOLTTerminalVLANsNamesID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ltp8xOLTTerminalVLANsNamesID.setStatus("current")
_Ltp8xOLTTerminalVLANsNamesName_Type = DisplayString
_Ltp8xOLTTerminalVLANsNamesName_Object = MibTableColumn
ltp8xOLTTerminalVLANsNamesName = _Ltp8xOLTTerminalVLANsNamesName_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 52, 1, 3),
    _Ltp8xOLTTerminalVLANsNamesName_Type()
)
ltp8xOLTTerminalVLANsNamesName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xOLTTerminalVLANsNamesName.setStatus("current")
_Ltp8xOLTTerminalVLANsNamesRowStatus_Type = RowStatus
_Ltp8xOLTTerminalVLANsNamesRowStatus_Object = MibTableColumn
ltp8xOLTTerminalVLANsNamesRowStatus = _Ltp8xOLTTerminalVLANsNamesRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 5, 52, 1, 10),
    _Ltp8xOLTTerminalVLANsNamesRowStatus_Type()
)
ltp8xOLTTerminalVLANsNamesRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xOLTTerminalVLANsNamesRowStatus.setStatus("current")
_Ltp8xSwitch_ObjectIdentity = ObjectIdentity
ltp8xSwitch = _Ltp8xSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9)
)
_Ltp8xSwitchPortsTable_Object = MibTable
ltp8xSwitchPortsTable = _Ltp8xSwitchPortsTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 1)
)
if mibBuilder.loadTexts:
    ltp8xSwitchPortsTable.setStatus("current")
_Ltp8xSwitchPortsEntry_Object = MibTableRow
ltp8xSwitchPortsEntry = _Ltp8xSwitchPortsEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 1, 1)
)
ltp8xSwitchPortsEntry.setIndexNames(
    (0, "ELTEX-LTP8X", "ltp8xSwitchPortsID"),
)
if mibBuilder.loadTexts:
    ltp8xSwitchPortsEntry.setStatus("current")
_Ltp8xSwitchPortsID_Type = Unsigned32
_Ltp8xSwitchPortsID_Object = MibTableColumn
ltp8xSwitchPortsID = _Ltp8xSwitchPortsID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 1, 1, 1),
    _Ltp8xSwitchPortsID_Type()
)
ltp8xSwitchPortsID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xSwitchPortsID.setStatus("current")
_Ltp8xSwitchPortsName_Type = DisplayString
_Ltp8xSwitchPortsName_Object = MibTableColumn
ltp8xSwitchPortsName = _Ltp8xSwitchPortsName_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 1, 1, 2),
    _Ltp8xSwitchPortsName_Type()
)
ltp8xSwitchPortsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xSwitchPortsName.setStatus("current")
_Ltp8xSwitchVLANTable_Object = MibTable
ltp8xSwitchVLANTable = _Ltp8xSwitchVLANTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 2)
)
if mibBuilder.loadTexts:
    ltp8xSwitchVLANTable.setStatus("current")
_Ltp8xSwitchVLANEntry_Object = MibTableRow
ltp8xSwitchVLANEntry = _Ltp8xSwitchVLANEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 2, 1)
)
ltp8xSwitchVLANEntry.setIndexNames(
    (0, "ELTEX-LTP8X", "ltp8xSwitchVLANSlot"),
    (0, "ELTEX-LTP8X", "ltp8xSwitchVLANVid"),
)
if mibBuilder.loadTexts:
    ltp8xSwitchVLANEntry.setStatus("current")
_Ltp8xSwitchVLANSlot_Type = Unsigned32
_Ltp8xSwitchVLANSlot_Object = MibTableColumn
ltp8xSwitchVLANSlot = _Ltp8xSwitchVLANSlot_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 2, 1, 1),
    _Ltp8xSwitchVLANSlot_Type()
)
ltp8xSwitchVLANSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xSwitchVLANSlot.setStatus("current")
_Ltp8xSwitchVLANVid_Type = Unsigned32
_Ltp8xSwitchVLANVid_Object = MibTableColumn
ltp8xSwitchVLANVid = _Ltp8xSwitchVLANVid_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 2, 1, 2),
    _Ltp8xSwitchVLANVid_Type()
)
ltp8xSwitchVLANVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xSwitchVLANVid.setStatus("current")
_Ltp8xSwitchVLANName_Type = DisplayString
_Ltp8xSwitchVLANName_Object = MibTableColumn
ltp8xSwitchVLANName = _Ltp8xSwitchVLANName_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 2, 1, 3),
    _Ltp8xSwitchVLANName_Type()
)
ltp8xSwitchVLANName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xSwitchVLANName.setStatus("current")
_Ltp8xSwitchVLANTaggedPorts_Type = PortList
_Ltp8xSwitchVLANTaggedPorts_Object = MibTableColumn
ltp8xSwitchVLANTaggedPorts = _Ltp8xSwitchVLANTaggedPorts_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 2, 1, 4),
    _Ltp8xSwitchVLANTaggedPorts_Type()
)
ltp8xSwitchVLANTaggedPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xSwitchVLANTaggedPorts.setStatus("current")
_Ltp8xSwitchVLANUntaggedPorts_Type = PortList
_Ltp8xSwitchVLANUntaggedPorts_Object = MibTableColumn
ltp8xSwitchVLANUntaggedPorts = _Ltp8xSwitchVLANUntaggedPorts_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 2, 1, 5),
    _Ltp8xSwitchVLANUntaggedPorts_Type()
)
ltp8xSwitchVLANUntaggedPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xSwitchVLANUntaggedPorts.setStatus("current")
_Ltp8xSwitchVLANRowStatus_Type = RowStatus
_Ltp8xSwitchVLANRowStatus_Object = MibTableColumn
ltp8xSwitchVLANRowStatus = _Ltp8xSwitchVLANRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 2, 1, 6),
    _Ltp8xSwitchVLANRowStatus_Type()
)
ltp8xSwitchVLANRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xSwitchVLANRowStatus.setStatus("current")
_Ltp8xSwitchVLANIGMPSnoopingEnabled_Type = TruthValue
_Ltp8xSwitchVLANIGMPSnoopingEnabled_Object = MibTableColumn
ltp8xSwitchVLANIGMPSnoopingEnabled = _Ltp8xSwitchVLANIGMPSnoopingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 2, 1, 10),
    _Ltp8xSwitchVLANIGMPSnoopingEnabled_Type()
)
ltp8xSwitchVLANIGMPSnoopingEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xSwitchVLANIGMPSnoopingEnabled.setStatus("current")
_Ltp8xSwitchVLANIGMPSnoopingQuerierEnabled_Type = TruthValue
_Ltp8xSwitchVLANIGMPSnoopingQuerierEnabled_Object = MibTableColumn
ltp8xSwitchVLANIGMPSnoopingQuerierEnabled = _Ltp8xSwitchVLANIGMPSnoopingQuerierEnabled_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 2, 1, 11),
    _Ltp8xSwitchVLANIGMPSnoopingQuerierEnabled_Type()
)
ltp8xSwitchVLANIGMPSnoopingQuerierEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xSwitchVLANIGMPSnoopingQuerierEnabled.setStatus("current")
_Ltp8xSwitchVLANMLDSnoopingEnabled_Type = TruthValue
_Ltp8xSwitchVLANMLDSnoopingEnabled_Object = MibTableColumn
ltp8xSwitchVLANMLDSnoopingEnabled = _Ltp8xSwitchVLANMLDSnoopingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 2, 1, 20),
    _Ltp8xSwitchVLANMLDSnoopingEnabled_Type()
)
ltp8xSwitchVLANMLDSnoopingEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xSwitchVLANMLDSnoopingEnabled.setStatus("current")
_Ltp8xSwitchVLANMLDSnoopingQuerierEnabled_Type = TruthValue
_Ltp8xSwitchVLANMLDSnoopingQuerierEnabled_Object = MibTableColumn
ltp8xSwitchVLANMLDSnoopingQuerierEnabled = _Ltp8xSwitchVLANMLDSnoopingQuerierEnabled_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 2, 1, 21),
    _Ltp8xSwitchVLANMLDSnoopingQuerierEnabled_Type()
)
ltp8xSwitchVLANMLDSnoopingQuerierEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xSwitchVLANMLDSnoopingQuerierEnabled.setStatus("current")
_Ltp8xSwitchIGMPSnoopingTable_Object = MibTable
ltp8xSwitchIGMPSnoopingTable = _Ltp8xSwitchIGMPSnoopingTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 3)
)
if mibBuilder.loadTexts:
    ltp8xSwitchIGMPSnoopingTable.setStatus("current")
_Ltp8xSwitchIGMPSnoopingEntry_Object = MibTableRow
ltp8xSwitchIGMPSnoopingEntry = _Ltp8xSwitchIGMPSnoopingEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 3, 1)
)
ltp8xSwitchIGMPSnoopingEntry.setIndexNames(
    (0, "ELTEX-LTP8X", "ltp8xSwitchIGMPSnoopingSlot"),
)
if mibBuilder.loadTexts:
    ltp8xSwitchIGMPSnoopingEntry.setStatus("current")
_Ltp8xSwitchIGMPSnoopingSlot_Type = Unsigned32
_Ltp8xSwitchIGMPSnoopingSlot_Object = MibTableColumn
ltp8xSwitchIGMPSnoopingSlot = _Ltp8xSwitchIGMPSnoopingSlot_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 3, 1, 1),
    _Ltp8xSwitchIGMPSnoopingSlot_Type()
)
ltp8xSwitchIGMPSnoopingSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xSwitchIGMPSnoopingSlot.setStatus("current")
_Ltp8xSwitchIGMPSnoopingEnabled_Type = TruthValue
_Ltp8xSwitchIGMPSnoopingEnabled_Object = MibTableColumn
ltp8xSwitchIGMPSnoopingEnabled = _Ltp8xSwitchIGMPSnoopingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 3, 1, 2),
    _Ltp8xSwitchIGMPSnoopingEnabled_Type()
)
ltp8xSwitchIGMPSnoopingEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xSwitchIGMPSnoopingEnabled.setStatus("current")
_Ltp8xSwitchMLDSnoopingEnabled_Type = TruthValue
_Ltp8xSwitchMLDSnoopingEnabled_Object = MibTableColumn
ltp8xSwitchMLDSnoopingEnabled = _Ltp8xSwitchMLDSnoopingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 3, 1, 3),
    _Ltp8xSwitchMLDSnoopingEnabled_Type()
)
ltp8xSwitchMLDSnoopingEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xSwitchMLDSnoopingEnabled.setStatus("current")
_Ltp8xSwitchOperationalVLANTable_Object = MibTable
ltp8xSwitchOperationalVLANTable = _Ltp8xSwitchOperationalVLANTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 4)
)
if mibBuilder.loadTexts:
    ltp8xSwitchOperationalVLANTable.setStatus("current")
_Ltp8xSwitchOperationalVLANEntry_Object = MibTableRow
ltp8xSwitchOperationalVLANEntry = _Ltp8xSwitchOperationalVLANEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 4, 1)
)
ltp8xSwitchOperationalVLANEntry.setIndexNames(
    (0, "ELTEX-LTP8X", "ltp8xSwitchOperationalVLANSlot"),
    (0, "ELTEX-LTP8X", "ltp8xSwitchOperationalVLANVid"),
)
if mibBuilder.loadTexts:
    ltp8xSwitchOperationalVLANEntry.setStatus("current")
_Ltp8xSwitchOperationalVLANSlot_Type = Unsigned32
_Ltp8xSwitchOperationalVLANSlot_Object = MibTableColumn
ltp8xSwitchOperationalVLANSlot = _Ltp8xSwitchOperationalVLANSlot_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 4, 1, 1),
    _Ltp8xSwitchOperationalVLANSlot_Type()
)
ltp8xSwitchOperationalVLANSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xSwitchOperationalVLANSlot.setStatus("current")
_Ltp8xSwitchOperationalVLANVid_Type = Unsigned32
_Ltp8xSwitchOperationalVLANVid_Object = MibTableColumn
ltp8xSwitchOperationalVLANVid = _Ltp8xSwitchOperationalVLANVid_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 4, 1, 2),
    _Ltp8xSwitchOperationalVLANVid_Type()
)
ltp8xSwitchOperationalVLANVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xSwitchOperationalVLANVid.setStatus("current")
_Ltp8xSwitchOperationalVLANName_Type = DisplayString
_Ltp8xSwitchOperationalVLANName_Object = MibTableColumn
ltp8xSwitchOperationalVLANName = _Ltp8xSwitchOperationalVLANName_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 4, 1, 3),
    _Ltp8xSwitchOperationalVLANName_Type()
)
ltp8xSwitchOperationalVLANName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xSwitchOperationalVLANName.setStatus("current")
_Ltp8xSwitchOperationalVLANTaggedPorts_Type = PortList
_Ltp8xSwitchOperationalVLANTaggedPorts_Object = MibTableColumn
ltp8xSwitchOperationalVLANTaggedPorts = _Ltp8xSwitchOperationalVLANTaggedPorts_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 4, 1, 4),
    _Ltp8xSwitchOperationalVLANTaggedPorts_Type()
)
ltp8xSwitchOperationalVLANTaggedPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xSwitchOperationalVLANTaggedPorts.setStatus("current")
_Ltp8xSwitchOperationalVLANUntaggedPorts_Type = PortList
_Ltp8xSwitchOperationalVLANUntaggedPorts_Object = MibTableColumn
ltp8xSwitchOperationalVLANUntaggedPorts = _Ltp8xSwitchOperationalVLANUntaggedPorts_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 4, 1, 5),
    _Ltp8xSwitchOperationalVLANUntaggedPorts_Type()
)
ltp8xSwitchOperationalVLANUntaggedPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xSwitchOperationalVLANUntaggedPorts.setStatus("current")
_Ltp8xSwitchPortCountersTable_Object = MibTable
ltp8xSwitchPortCountersTable = _Ltp8xSwitchPortCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 5)
)
if mibBuilder.loadTexts:
    ltp8xSwitchPortCountersTable.setStatus("current")
_Ltp8xSwitchPortCountersEntry_Object = MibTableRow
ltp8xSwitchPortCountersEntry = _Ltp8xSwitchPortCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 5, 1)
)
ltp8xSwitchPortCountersEntry.setIndexNames(
    (0, "ELTEX-LTP8X", "ltp8xSwitchPortCountersSlot"),
    (0, "ELTEX-LTP8X", "ltp8xSwitchPortCountersPortID"),
)
if mibBuilder.loadTexts:
    ltp8xSwitchPortCountersEntry.setStatus("current")
_Ltp8xSwitchPortCountersSlot_Type = Unsigned32
_Ltp8xSwitchPortCountersSlot_Object = MibTableColumn
ltp8xSwitchPortCountersSlot = _Ltp8xSwitchPortCountersSlot_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 5, 1, 1),
    _Ltp8xSwitchPortCountersSlot_Type()
)
ltp8xSwitchPortCountersSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ltp8xSwitchPortCountersSlot.setStatus("current")
_Ltp8xSwitchPortCountersPortID_Type = Unsigned32
_Ltp8xSwitchPortCountersPortID_Object = MibTableColumn
ltp8xSwitchPortCountersPortID = _Ltp8xSwitchPortCountersPortID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 5, 1, 2),
    _Ltp8xSwitchPortCountersPortID_Type()
)
ltp8xSwitchPortCountersPortID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ltp8xSwitchPortCountersPortID.setStatus("current")
_Ltp8xSwitchPortGoodOctetsRcv_Type = Counter64
_Ltp8xSwitchPortGoodOctetsRcv_Object = MibTableColumn
ltp8xSwitchPortGoodOctetsRcv = _Ltp8xSwitchPortGoodOctetsRcv_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 5, 1, 3),
    _Ltp8xSwitchPortGoodOctetsRcv_Type()
)
ltp8xSwitchPortGoodOctetsRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xSwitchPortGoodOctetsRcv.setStatus("current")
_Ltp8xSwitchPortBadOctetsRcv_Type = Counter64
_Ltp8xSwitchPortBadOctetsRcv_Object = MibTableColumn
ltp8xSwitchPortBadOctetsRcv = _Ltp8xSwitchPortBadOctetsRcv_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 5, 1, 4),
    _Ltp8xSwitchPortBadOctetsRcv_Type()
)
ltp8xSwitchPortBadOctetsRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xSwitchPortBadOctetsRcv.setStatus("current")
_Ltp8xSwitchPortMacTransmitErr_Type = Counter64
_Ltp8xSwitchPortMacTransmitErr_Object = MibTableColumn
ltp8xSwitchPortMacTransmitErr = _Ltp8xSwitchPortMacTransmitErr_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 5, 1, 5),
    _Ltp8xSwitchPortMacTransmitErr_Type()
)
ltp8xSwitchPortMacTransmitErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xSwitchPortMacTransmitErr.setStatus("current")
_Ltp8xSwitchPortGoodPktsRcv_Type = Counter64
_Ltp8xSwitchPortGoodPktsRcv_Object = MibTableColumn
ltp8xSwitchPortGoodPktsRcv = _Ltp8xSwitchPortGoodPktsRcv_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 5, 1, 6),
    _Ltp8xSwitchPortGoodPktsRcv_Type()
)
ltp8xSwitchPortGoodPktsRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xSwitchPortGoodPktsRcv.setStatus("current")
_Ltp8xSwitchPortBadPktsRcv_Type = Counter64
_Ltp8xSwitchPortBadPktsRcv_Object = MibTableColumn
ltp8xSwitchPortBadPktsRcv = _Ltp8xSwitchPortBadPktsRcv_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 5, 1, 7),
    _Ltp8xSwitchPortBadPktsRcv_Type()
)
ltp8xSwitchPortBadPktsRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xSwitchPortBadPktsRcv.setStatus("current")
_Ltp8xSwitchPortBrdcPktsRcv_Type = Counter64
_Ltp8xSwitchPortBrdcPktsRcv_Object = MibTableColumn
ltp8xSwitchPortBrdcPktsRcv = _Ltp8xSwitchPortBrdcPktsRcv_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 5, 1, 8),
    _Ltp8xSwitchPortBrdcPktsRcv_Type()
)
ltp8xSwitchPortBrdcPktsRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xSwitchPortBrdcPktsRcv.setStatus("current")
_Ltp8xSwitchPortMcPktsRcv_Type = Counter64
_Ltp8xSwitchPortMcPktsRcv_Object = MibTableColumn
ltp8xSwitchPortMcPktsRcv = _Ltp8xSwitchPortMcPktsRcv_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 5, 1, 9),
    _Ltp8xSwitchPortMcPktsRcv_Type()
)
ltp8xSwitchPortMcPktsRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xSwitchPortMcPktsRcv.setStatus("current")
_Ltp8xSwitchPortPkts64Octets_Type = Counter64
_Ltp8xSwitchPortPkts64Octets_Object = MibTableColumn
ltp8xSwitchPortPkts64Octets = _Ltp8xSwitchPortPkts64Octets_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 5, 1, 10),
    _Ltp8xSwitchPortPkts64Octets_Type()
)
ltp8xSwitchPortPkts64Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xSwitchPortPkts64Octets.setStatus("current")
_Ltp8xSwitchPortPkts65to127Octets_Type = Counter64
_Ltp8xSwitchPortPkts65to127Octets_Object = MibTableColumn
ltp8xSwitchPortPkts65to127Octets = _Ltp8xSwitchPortPkts65to127Octets_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 5, 1, 11),
    _Ltp8xSwitchPortPkts65to127Octets_Type()
)
ltp8xSwitchPortPkts65to127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xSwitchPortPkts65to127Octets.setStatus("current")
_Ltp8xSwitchPortPkts128to255Octets_Type = Counter64
_Ltp8xSwitchPortPkts128to255Octets_Object = MibTableColumn
ltp8xSwitchPortPkts128to255Octets = _Ltp8xSwitchPortPkts128to255Octets_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 5, 1, 12),
    _Ltp8xSwitchPortPkts128to255Octets_Type()
)
ltp8xSwitchPortPkts128to255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xSwitchPortPkts128to255Octets.setStatus("current")
_Ltp8xSwitchPortPkts256to511Octets_Type = Counter64
_Ltp8xSwitchPortPkts256to511Octets_Object = MibTableColumn
ltp8xSwitchPortPkts256to511Octets = _Ltp8xSwitchPortPkts256to511Octets_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 5, 1, 13),
    _Ltp8xSwitchPortPkts256to511Octets_Type()
)
ltp8xSwitchPortPkts256to511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xSwitchPortPkts256to511Octets.setStatus("current")
_Ltp8xSwitchPortPkts512to1023Octets_Type = Counter64
_Ltp8xSwitchPortPkts512to1023Octets_Object = MibTableColumn
ltp8xSwitchPortPkts512to1023Octets = _Ltp8xSwitchPortPkts512to1023Octets_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 5, 1, 14),
    _Ltp8xSwitchPortPkts512to1023Octets_Type()
)
ltp8xSwitchPortPkts512to1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xSwitchPortPkts512to1023Octets.setStatus("current")
_Ltp8xSwitchPortPkts1024tomaxOctets_Type = Counter64
_Ltp8xSwitchPortPkts1024tomaxOctets_Object = MibTableColumn
ltp8xSwitchPortPkts1024tomaxOctets = _Ltp8xSwitchPortPkts1024tomaxOctets_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 5, 1, 15),
    _Ltp8xSwitchPortPkts1024tomaxOctets_Type()
)
ltp8xSwitchPortPkts1024tomaxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xSwitchPortPkts1024tomaxOctets.setStatus("current")
_Ltp8xSwitchPortGoodOctetsSent_Type = Counter64
_Ltp8xSwitchPortGoodOctetsSent_Object = MibTableColumn
ltp8xSwitchPortGoodOctetsSent = _Ltp8xSwitchPortGoodOctetsSent_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 5, 1, 16),
    _Ltp8xSwitchPortGoodOctetsSent_Type()
)
ltp8xSwitchPortGoodOctetsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xSwitchPortGoodOctetsSent.setStatus("current")
_Ltp8xSwitchPortGoodPktsSent_Type = Counter64
_Ltp8xSwitchPortGoodPktsSent_Object = MibTableColumn
ltp8xSwitchPortGoodPktsSent = _Ltp8xSwitchPortGoodPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 5, 1, 17),
    _Ltp8xSwitchPortGoodPktsSent_Type()
)
ltp8xSwitchPortGoodPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xSwitchPortGoodPktsSent.setStatus("current")
_Ltp8xSwitchPortExcessiveCollisions_Type = Counter64
_Ltp8xSwitchPortExcessiveCollisions_Object = MibTableColumn
ltp8xSwitchPortExcessiveCollisions = _Ltp8xSwitchPortExcessiveCollisions_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 5, 1, 18),
    _Ltp8xSwitchPortExcessiveCollisions_Type()
)
ltp8xSwitchPortExcessiveCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xSwitchPortExcessiveCollisions.setStatus("current")
_Ltp8xSwitchPortMcPktsSent_Type = Counter64
_Ltp8xSwitchPortMcPktsSent_Object = MibTableColumn
ltp8xSwitchPortMcPktsSent = _Ltp8xSwitchPortMcPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 5, 1, 19),
    _Ltp8xSwitchPortMcPktsSent_Type()
)
ltp8xSwitchPortMcPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xSwitchPortMcPktsSent.setStatus("current")
_Ltp8xSwitchPortBrdcPktsSent_Type = Counter64
_Ltp8xSwitchPortBrdcPktsSent_Object = MibTableColumn
ltp8xSwitchPortBrdcPktsSent = _Ltp8xSwitchPortBrdcPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 5, 1, 20),
    _Ltp8xSwitchPortBrdcPktsSent_Type()
)
ltp8xSwitchPortBrdcPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xSwitchPortBrdcPktsSent.setStatus("current")
_Ltp8xSwitchPortUnrecogMacCntrRcv_Type = Counter64
_Ltp8xSwitchPortUnrecogMacCntrRcv_Object = MibTableColumn
ltp8xSwitchPortUnrecogMacCntrRcv = _Ltp8xSwitchPortUnrecogMacCntrRcv_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 5, 1, 21),
    _Ltp8xSwitchPortUnrecogMacCntrRcv_Type()
)
ltp8xSwitchPortUnrecogMacCntrRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xSwitchPortUnrecogMacCntrRcv.setStatus("current")
_Ltp8xSwitchPortFcSent_Type = Counter64
_Ltp8xSwitchPortFcSent_Object = MibTableColumn
ltp8xSwitchPortFcSent = _Ltp8xSwitchPortFcSent_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 5, 1, 22),
    _Ltp8xSwitchPortFcSent_Type()
)
ltp8xSwitchPortFcSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xSwitchPortFcSent.setStatus("current")
_Ltp8xSwitchPortGoodFcRcv_Type = Counter64
_Ltp8xSwitchPortGoodFcRcv_Object = MibTableColumn
ltp8xSwitchPortGoodFcRcv = _Ltp8xSwitchPortGoodFcRcv_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 5, 1, 23),
    _Ltp8xSwitchPortGoodFcRcv_Type()
)
ltp8xSwitchPortGoodFcRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xSwitchPortGoodFcRcv.setStatus("current")
_Ltp8xSwitchPortDropEvents_Type = Counter64
_Ltp8xSwitchPortDropEvents_Object = MibTableColumn
ltp8xSwitchPortDropEvents = _Ltp8xSwitchPortDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 5, 1, 24),
    _Ltp8xSwitchPortDropEvents_Type()
)
ltp8xSwitchPortDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xSwitchPortDropEvents.setStatus("current")
_Ltp8xSwitchPortUndersizePkts_Type = Counter64
_Ltp8xSwitchPortUndersizePkts_Object = MibTableColumn
ltp8xSwitchPortUndersizePkts = _Ltp8xSwitchPortUndersizePkts_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 5, 1, 25),
    _Ltp8xSwitchPortUndersizePkts_Type()
)
ltp8xSwitchPortUndersizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xSwitchPortUndersizePkts.setStatus("current")
_Ltp8xSwitchPortFragmentsPkts_Type = Counter64
_Ltp8xSwitchPortFragmentsPkts_Object = MibTableColumn
ltp8xSwitchPortFragmentsPkts = _Ltp8xSwitchPortFragmentsPkts_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 5, 1, 26),
    _Ltp8xSwitchPortFragmentsPkts_Type()
)
ltp8xSwitchPortFragmentsPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xSwitchPortFragmentsPkts.setStatus("current")
_Ltp8xSwitchPortOversizePkts_Type = Counter64
_Ltp8xSwitchPortOversizePkts_Object = MibTableColumn
ltp8xSwitchPortOversizePkts = _Ltp8xSwitchPortOversizePkts_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 5, 1, 27),
    _Ltp8xSwitchPortOversizePkts_Type()
)
ltp8xSwitchPortOversizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xSwitchPortOversizePkts.setStatus("current")
_Ltp8xSwitchPortJabberPkts_Type = Counter64
_Ltp8xSwitchPortJabberPkts_Object = MibTableColumn
ltp8xSwitchPortJabberPkts = _Ltp8xSwitchPortJabberPkts_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 5, 1, 28),
    _Ltp8xSwitchPortJabberPkts_Type()
)
ltp8xSwitchPortJabberPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xSwitchPortJabberPkts.setStatus("current")
_Ltp8xSwitchPortMacRcvError_Type = Counter64
_Ltp8xSwitchPortMacRcvError_Object = MibTableColumn
ltp8xSwitchPortMacRcvError = _Ltp8xSwitchPortMacRcvError_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 5, 1, 29),
    _Ltp8xSwitchPortMacRcvError_Type()
)
ltp8xSwitchPortMacRcvError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xSwitchPortMacRcvError.setStatus("current")
_Ltp8xSwitchPortBadCrc_Type = Counter64
_Ltp8xSwitchPortBadCrc_Object = MibTableColumn
ltp8xSwitchPortBadCrc = _Ltp8xSwitchPortBadCrc_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 5, 1, 30),
    _Ltp8xSwitchPortBadCrc_Type()
)
ltp8xSwitchPortBadCrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xSwitchPortBadCrc.setStatus("current")
_Ltp8xSwitchPortCollisions_Type = Counter64
_Ltp8xSwitchPortCollisions_Object = MibTableColumn
ltp8xSwitchPortCollisions = _Ltp8xSwitchPortCollisions_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 5, 1, 31),
    _Ltp8xSwitchPortCollisions_Type()
)
ltp8xSwitchPortCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xSwitchPortCollisions.setStatus("current")
_Ltp8xSwitchPortLateCollisions_Type = Counter64
_Ltp8xSwitchPortLateCollisions_Object = MibTableColumn
ltp8xSwitchPortLateCollisions = _Ltp8xSwitchPortLateCollisions_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 5, 1, 32),
    _Ltp8xSwitchPortLateCollisions_Type()
)
ltp8xSwitchPortLateCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xSwitchPortLateCollisions.setStatus("current")
_Ltp8xSwitchPortBadFcRcv_Type = Counter64
_Ltp8xSwitchPortBadFcRcv_Object = MibTableColumn
ltp8xSwitchPortBadFcRcv = _Ltp8xSwitchPortBadFcRcv_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 5, 1, 33),
    _Ltp8xSwitchPortBadFcRcv_Type()
)
ltp8xSwitchPortBadFcRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xSwitchPortBadFcRcv.setStatus("current")
_Ltp8xSwitchPortCountersReset_Type = Unsigned32
_Ltp8xSwitchPortCountersReset_Object = MibTableColumn
ltp8xSwitchPortCountersReset = _Ltp8xSwitchPortCountersReset_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 5, 1, 50),
    _Ltp8xSwitchPortCountersReset_Type()
)
ltp8xSwitchPortCountersReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xSwitchPortCountersReset.setStatus("current")
_Ltp8xSwitchMacListTable_Object = MibTable
ltp8xSwitchMacListTable = _Ltp8xSwitchMacListTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 6)
)
if mibBuilder.loadTexts:
    ltp8xSwitchMacListTable.setStatus("current")
_Ltp8xSwitchMacListEntry_Object = MibTableRow
ltp8xSwitchMacListEntry = _Ltp8xSwitchMacListEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 6, 1)
)
ltp8xSwitchMacListEntry.setIndexNames(
    (0, "ELTEX-LTP8X", "ltp8xSwitchMacListSlot"),
    (0, "ELTEX-LTP8X", "ltp8xSwitchMacListVID"),
    (0, "ELTEX-LTP8X", "ltp8xSwitchMacListMacAddress"),
)
if mibBuilder.loadTexts:
    ltp8xSwitchMacListEntry.setStatus("current")
_Ltp8xSwitchMacListSlot_Type = Unsigned32
_Ltp8xSwitchMacListSlot_Object = MibTableColumn
ltp8xSwitchMacListSlot = _Ltp8xSwitchMacListSlot_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 6, 1, 1),
    _Ltp8xSwitchMacListSlot_Type()
)
ltp8xSwitchMacListSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ltp8xSwitchMacListSlot.setStatus("current")
_Ltp8xSwitchMacListVID_Type = Unsigned32
_Ltp8xSwitchMacListVID_Object = MibTableColumn
ltp8xSwitchMacListVID = _Ltp8xSwitchMacListVID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 6, 1, 2),
    _Ltp8xSwitchMacListVID_Type()
)
ltp8xSwitchMacListVID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ltp8xSwitchMacListVID.setStatus("current")
_Ltp8xSwitchMacListMacAddress_Type = MacAddress
_Ltp8xSwitchMacListMacAddress_Object = MibTableColumn
ltp8xSwitchMacListMacAddress = _Ltp8xSwitchMacListMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 6, 1, 3),
    _Ltp8xSwitchMacListMacAddress_Type()
)
ltp8xSwitchMacListMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ltp8xSwitchMacListMacAddress.setStatus("current")
_Ltp8xSwitchMacListInterface_Type = Unsigned32
_Ltp8xSwitchMacListInterface_Object = MibTableColumn
ltp8xSwitchMacListInterface = _Ltp8xSwitchMacListInterface_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 6, 1, 4),
    _Ltp8xSwitchMacListInterface_Type()
)
ltp8xSwitchMacListInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xSwitchMacListInterface.setStatus("current")
_Ltp8xSwitchMacListStatic_Type = TruthValue
_Ltp8xSwitchMacListStatic_Object = MibTableColumn
ltp8xSwitchMacListStatic = _Ltp8xSwitchMacListStatic_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 6, 1, 5),
    _Ltp8xSwitchMacListStatic_Type()
)
ltp8xSwitchMacListStatic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xSwitchMacListStatic.setStatus("current")
_Ltp8xSwitchMacListMacAddressString_Type = DisplayString
_Ltp8xSwitchMacListMacAddressString_Object = MibTableColumn
ltp8xSwitchMacListMacAddressString = _Ltp8xSwitchMacListMacAddressString_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 6, 1, 6),
    _Ltp8xSwitchMacListMacAddressString_Type()
)
ltp8xSwitchMacListMacAddressString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xSwitchMacListMacAddressString.setStatus("current")
_Ltp8xSwitchPortsUtilization_ObjectIdentity = ObjectIdentity
ltp8xSwitchPortsUtilization = _Ltp8xSwitchPortsUtilization_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 8)
)
_Ltp8xPortsUtilizationInterval_Type = Unsigned32
_Ltp8xPortsUtilizationInterval_Object = MibScalar
ltp8xPortsUtilizationInterval = _Ltp8xPortsUtilizationInterval_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 8, 1),
    _Ltp8xPortsUtilizationInterval_Type()
)
ltp8xPortsUtilizationInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xPortsUtilizationInterval.setStatus("current")
_Ltp8xPortsUtilizationTable_Object = MibTable
ltp8xPortsUtilizationTable = _Ltp8xPortsUtilizationTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 8, 2)
)
if mibBuilder.loadTexts:
    ltp8xPortsUtilizationTable.setStatus("current")
_Ltp8xPortsUtilizationEntry_Object = MibTableRow
ltp8xPortsUtilizationEntry = _Ltp8xPortsUtilizationEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 8, 2, 1)
)
ltp8xPortsUtilizationEntry.setIndexNames(
    (0, "ELTEX-LTP8X", "ltp8xPortsUtilizationSlot"),
    (0, "ELTEX-LTP8X", "ltp8xPortsUtilizationPortID"),
)
if mibBuilder.loadTexts:
    ltp8xPortsUtilizationEntry.setStatus("current")
_Ltp8xPortsUtilizationSlot_Type = Unsigned32
_Ltp8xPortsUtilizationSlot_Object = MibTableColumn
ltp8xPortsUtilizationSlot = _Ltp8xPortsUtilizationSlot_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 8, 2, 1, 1),
    _Ltp8xPortsUtilizationSlot_Type()
)
ltp8xPortsUtilizationSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ltp8xPortsUtilizationSlot.setStatus("current")
_Ltp8xPortsUtilizationPortID_Type = Unsigned32
_Ltp8xPortsUtilizationPortID_Object = MibTableColumn
ltp8xPortsUtilizationPortID = _Ltp8xPortsUtilizationPortID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 8, 2, 1, 2),
    _Ltp8xPortsUtilizationPortID_Type()
)
ltp8xPortsUtilizationPortID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ltp8xPortsUtilizationPortID.setStatus("current")
_Ltp8xPortsUtilizationLastKbitsSent_Type = Counter64
_Ltp8xPortsUtilizationLastKbitsSent_Object = MibTableColumn
ltp8xPortsUtilizationLastKbitsSent = _Ltp8xPortsUtilizationLastKbitsSent_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 8, 2, 1, 3),
    _Ltp8xPortsUtilizationLastKbitsSent_Type()
)
ltp8xPortsUtilizationLastKbitsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xPortsUtilizationLastKbitsSent.setStatus("current")
_Ltp8xPortsUtilizationLastKbitsRecv_Type = Counter64
_Ltp8xPortsUtilizationLastKbitsRecv_Object = MibTableColumn
ltp8xPortsUtilizationLastKbitsRecv = _Ltp8xPortsUtilizationLastKbitsRecv_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 8, 2, 1, 4),
    _Ltp8xPortsUtilizationLastKbitsRecv_Type()
)
ltp8xPortsUtilizationLastKbitsRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xPortsUtilizationLastKbitsRecv.setStatus("current")
_Ltp8xPortsUtilizationLastFramesSent_Type = Counter64
_Ltp8xPortsUtilizationLastFramesSent_Object = MibTableColumn
ltp8xPortsUtilizationLastFramesSent = _Ltp8xPortsUtilizationLastFramesSent_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 8, 2, 1, 5),
    _Ltp8xPortsUtilizationLastFramesSent_Type()
)
ltp8xPortsUtilizationLastFramesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xPortsUtilizationLastFramesSent.setStatus("current")
_Ltp8xPortsUtilizationLastFramesRecv_Type = Counter64
_Ltp8xPortsUtilizationLastFramesRecv_Object = MibTableColumn
ltp8xPortsUtilizationLastFramesRecv = _Ltp8xPortsUtilizationLastFramesRecv_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 8, 2, 1, 6),
    _Ltp8xPortsUtilizationLastFramesRecv_Type()
)
ltp8xPortsUtilizationLastFramesRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xPortsUtilizationLastFramesRecv.setStatus("current")
_Ltp8xPortsUtilizationAverageKbitsSent_Type = Counter64
_Ltp8xPortsUtilizationAverageKbitsSent_Object = MibTableColumn
ltp8xPortsUtilizationAverageKbitsSent = _Ltp8xPortsUtilizationAverageKbitsSent_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 8, 2, 1, 7),
    _Ltp8xPortsUtilizationAverageKbitsSent_Type()
)
ltp8xPortsUtilizationAverageKbitsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xPortsUtilizationAverageKbitsSent.setStatus("current")
_Ltp8xPortsUtilizationAverageKbitsRecv_Type = Counter64
_Ltp8xPortsUtilizationAverageKbitsRecv_Object = MibTableColumn
ltp8xPortsUtilizationAverageKbitsRecv = _Ltp8xPortsUtilizationAverageKbitsRecv_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 8, 2, 1, 8),
    _Ltp8xPortsUtilizationAverageKbitsRecv_Type()
)
ltp8xPortsUtilizationAverageKbitsRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xPortsUtilizationAverageKbitsRecv.setStatus("current")
_Ltp8xPortsUtilizationAverageFramesSent_Type = Counter64
_Ltp8xPortsUtilizationAverageFramesSent_Object = MibTableColumn
ltp8xPortsUtilizationAverageFramesSent = _Ltp8xPortsUtilizationAverageFramesSent_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 8, 2, 1, 9),
    _Ltp8xPortsUtilizationAverageFramesSent_Type()
)
ltp8xPortsUtilizationAverageFramesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xPortsUtilizationAverageFramesSent.setStatus("current")
_Ltp8xPortsUtilizationAverageFramesRecv_Type = Counter64
_Ltp8xPortsUtilizationAverageFramesRecv_Object = MibTableColumn
ltp8xPortsUtilizationAverageFramesRecv = _Ltp8xPortsUtilizationAverageFramesRecv_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 8, 2, 1, 10),
    _Ltp8xPortsUtilizationAverageFramesRecv_Type()
)
ltp8xPortsUtilizationAverageFramesRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xPortsUtilizationAverageFramesRecv.setStatus("current")
_Ltp8xQOSConfig_ObjectIdentity = ObjectIdentity
ltp8xQOSConfig = _Ltp8xQOSConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 10)
)
_Ltp8xQOSConfigTable_Object = MibTable
ltp8xQOSConfigTable = _Ltp8xQOSConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 10, 1)
)
if mibBuilder.loadTexts:
    ltp8xQOSConfigTable.setStatus("current")
_Ltp8xQOSConfigEntry_Object = MibTableRow
ltp8xQOSConfigEntry = _Ltp8xQOSConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 10, 1, 1)
)
ltp8xQOSConfigEntry.setIndexNames(
    (0, "ELTEX-LTP8X", "ltp8xQOSConfigSlot"),
)
if mibBuilder.loadTexts:
    ltp8xQOSConfigEntry.setStatus("current")
_Ltp8xQOSConfigSlot_Type = Unsigned32
_Ltp8xQOSConfigSlot_Object = MibTableColumn
ltp8xQOSConfigSlot = _Ltp8xQOSConfigSlot_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 10, 1, 1, 1),
    _Ltp8xQOSConfigSlot_Type()
)
ltp8xQOSConfigSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ltp8xQOSConfigSlot.setStatus("current")


class _Ltp8xQOSDefaultQueue_Type(Unsigned32):
    """Custom type ltp8xQOSDefaultQueue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_Ltp8xQOSDefaultQueue_Type.__name__ = "Unsigned32"
_Ltp8xQOSDefaultQueue_Object = MibTableColumn
ltp8xQOSDefaultQueue = _Ltp8xQOSDefaultQueue_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 10, 1, 1, 2),
    _Ltp8xQOSDefaultQueue_Type()
)
ltp8xQOSDefaultQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xQOSDefaultQueue.setStatus("current")


class _Ltp8xQOSType_Type(Integer32):
    """Custom type ltp8xQOSType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("type8021p", 1),
          ("typeAllEqual", 0),
          ("typeDscpTos", 2),
          ("typeDscpTos8021p", 3))
    )


_Ltp8xQOSType_Type.__name__ = "Integer32"
_Ltp8xQOSType_Object = MibTableColumn
ltp8xQOSType = _Ltp8xQOSType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 10, 1, 1, 3),
    _Ltp8xQOSType_Type()
)
ltp8xQOSType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xQOSType.setStatus("current")
_Ltp8xQOSDownstreamQinQPrioritization_Type = TruthValue
_Ltp8xQOSDownstreamQinQPrioritization_Object = MibTableColumn
ltp8xQOSDownstreamQinQPrioritization = _Ltp8xQOSDownstreamQinQPrioritization_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 10, 1, 1, 4),
    _Ltp8xQOSDownstreamQinQPrioritization_Type()
)
ltp8xQOSDownstreamQinQPrioritization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xQOSDownstreamQinQPrioritization.setStatus("current")
_Ltp8xQOS8021pMappingTable_Object = MibTable
ltp8xQOS8021pMappingTable = _Ltp8xQOS8021pMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 10, 2)
)
if mibBuilder.loadTexts:
    ltp8xQOS8021pMappingTable.setStatus("current")
_Ltp8xQOS8021pMappingEntry_Object = MibTableRow
ltp8xQOS8021pMappingEntry = _Ltp8xQOS8021pMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 10, 2, 1)
)
ltp8xQOS8021pMappingEntry.setIndexNames(
    (0, "ELTEX-LTP8X", "ltp8xQOS8021pMappingSlot"),
    (0, "ELTEX-LTP8X", "ltp8xQOS8021pMappingQueue"),
)
if mibBuilder.loadTexts:
    ltp8xQOS8021pMappingEntry.setStatus("current")
_Ltp8xQOS8021pMappingSlot_Type = Unsigned32
_Ltp8xQOS8021pMappingSlot_Object = MibTableColumn
ltp8xQOS8021pMappingSlot = _Ltp8xQOS8021pMappingSlot_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 10, 2, 1, 1),
    _Ltp8xQOS8021pMappingSlot_Type()
)
ltp8xQOS8021pMappingSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ltp8xQOS8021pMappingSlot.setStatus("current")
_Ltp8xQOS8021pMappingQueue_Type = Unsigned32
_Ltp8xQOS8021pMappingQueue_Object = MibTableColumn
ltp8xQOS8021pMappingQueue = _Ltp8xQOS8021pMappingQueue_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 10, 2, 1, 2),
    _Ltp8xQOS8021pMappingQueue_Type()
)
ltp8xQOS8021pMappingQueue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ltp8xQOS8021pMappingQueue.setStatus("current")


class _Ltp8xQOS8021pMappingFields_Type(OctetString):
    """Custom type ltp8xQOS8021pMappingFields based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_Ltp8xQOS8021pMappingFields_Type.__name__ = "OctetString"
_Ltp8xQOS8021pMappingFields_Object = MibTableColumn
ltp8xQOS8021pMappingFields = _Ltp8xQOS8021pMappingFields_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 10, 2, 1, 3),
    _Ltp8xQOS8021pMappingFields_Type()
)
ltp8xQOS8021pMappingFields.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xQOS8021pMappingFields.setStatus("current")
_Ltp8xQOSDSCPMappingTable_Object = MibTable
ltp8xQOSDSCPMappingTable = _Ltp8xQOSDSCPMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 10, 3)
)
if mibBuilder.loadTexts:
    ltp8xQOSDSCPMappingTable.setStatus("current")
_Ltp8xQOSDSCPMappingEntry_Object = MibTableRow
ltp8xQOSDSCPMappingEntry = _Ltp8xQOSDSCPMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 10, 3, 1)
)
ltp8xQOSDSCPMappingEntry.setIndexNames(
    (0, "ELTEX-LTP8X", "ltp8xQOSDSCPMappingSlot"),
    (0, "ELTEX-LTP8X", "ltp8xQOSDSCPMappingQueue"),
)
if mibBuilder.loadTexts:
    ltp8xQOSDSCPMappingEntry.setStatus("current")
_Ltp8xQOSDSCPMappingSlot_Type = Unsigned32
_Ltp8xQOSDSCPMappingSlot_Object = MibTableColumn
ltp8xQOSDSCPMappingSlot = _Ltp8xQOSDSCPMappingSlot_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 10, 3, 1, 1),
    _Ltp8xQOSDSCPMappingSlot_Type()
)
ltp8xQOSDSCPMappingSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ltp8xQOSDSCPMappingSlot.setStatus("current")
_Ltp8xQOSDSCPMappingQueue_Type = Unsigned32
_Ltp8xQOSDSCPMappingQueue_Object = MibTableColumn
ltp8xQOSDSCPMappingQueue = _Ltp8xQOSDSCPMappingQueue_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 10, 3, 1, 2),
    _Ltp8xQOSDSCPMappingQueue_Type()
)
ltp8xQOSDSCPMappingQueue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ltp8xQOSDSCPMappingQueue.setStatus("current")


class _Ltp8xQOSDSCPMappingFields_Type(OctetString):
    """Custom type ltp8xQOSDSCPMappingFields based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_Ltp8xQOSDSCPMappingFields_Type.__name__ = "OctetString"
_Ltp8xQOSDSCPMappingFields_Object = MibTableColumn
ltp8xQOSDSCPMappingFields = _Ltp8xQOSDSCPMappingFields_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 10, 3, 1, 3),
    _Ltp8xQOSDSCPMappingFields_Type()
)
ltp8xQOSDSCPMappingFields.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xQOSDSCPMappingFields.setStatus("current")
_Ltp8xACLConfig_ObjectIdentity = ObjectIdentity
ltp8xACLConfig = _Ltp8xACLConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 15)
)
_Ltp8xACLGlobalModeTable_Object = MibTable
ltp8xACLGlobalModeTable = _Ltp8xACLGlobalModeTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 15, 1)
)
if mibBuilder.loadTexts:
    ltp8xACLGlobalModeTable.setStatus("current")
_Ltp8xACLGlobalModeEntry_Object = MibTableRow
ltp8xACLGlobalModeEntry = _Ltp8xACLGlobalModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 15, 1, 1)
)
ltp8xACLGlobalModeEntry.setIndexNames(
    (0, "ELTEX-LTP8X", "ltp8xACLGlobalModeSlot"),
)
if mibBuilder.loadTexts:
    ltp8xACLGlobalModeEntry.setStatus("current")
_Ltp8xACLGlobalModeSlot_Type = Unsigned32
_Ltp8xACLGlobalModeSlot_Object = MibTableColumn
ltp8xACLGlobalModeSlot = _Ltp8xACLGlobalModeSlot_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 15, 1, 1, 1),
    _Ltp8xACLGlobalModeSlot_Type()
)
ltp8xACLGlobalModeSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ltp8xACLGlobalModeSlot.setStatus("current")


class _Ltp8xACLGlobalMode_Type(Integer32):
    """Custom type ltp8xACLGlobalMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("blackList", 0),
          ("whiteList", 1))
    )


_Ltp8xACLGlobalMode_Type.__name__ = "Integer32"
_Ltp8xACLGlobalMode_Object = MibTableColumn
ltp8xACLGlobalMode = _Ltp8xACLGlobalMode_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 15, 1, 1, 2),
    _Ltp8xACLGlobalMode_Type()
)
ltp8xACLGlobalMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xACLGlobalMode.setStatus("current")
_Ltp8xACLListsTable_Object = MibTable
ltp8xACLListsTable = _Ltp8xACLListsTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 15, 2)
)
if mibBuilder.loadTexts:
    ltp8xACLListsTable.setStatus("current")
_Ltp8xACLListsEntry_Object = MibTableRow
ltp8xACLListsEntry = _Ltp8xACLListsEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 15, 2, 1)
)
ltp8xACLListsEntry.setIndexNames(
    (0, "ELTEX-LTP8X", "ltp8xACLListsSlot"),
    (0, "ELTEX-LTP8X", "ltp8xACLListsID"),
)
if mibBuilder.loadTexts:
    ltp8xACLListsEntry.setStatus("current")
_Ltp8xACLListsSlot_Type = Unsigned32
_Ltp8xACLListsSlot_Object = MibTableColumn
ltp8xACLListsSlot = _Ltp8xACLListsSlot_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 15, 2, 1, 1),
    _Ltp8xACLListsSlot_Type()
)
ltp8xACLListsSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ltp8xACLListsSlot.setStatus("current")
_Ltp8xACLListsID_Type = Unsigned32
_Ltp8xACLListsID_Object = MibTableColumn
ltp8xACLListsID = _Ltp8xACLListsID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 15, 2, 1, 2),
    _Ltp8xACLListsID_Type()
)
ltp8xACLListsID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ltp8xACLListsID.setStatus("current")
_Ltp8xACLListsName_Type = DisplayString
_Ltp8xACLListsName_Object = MibTableColumn
ltp8xACLListsName = _Ltp8xACLListsName_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 15, 2, 1, 3),
    _Ltp8xACLListsName_Type()
)
ltp8xACLListsName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xACLListsName.setStatus("current")
_Ltp8xACLListsPorts_Type = PortList
_Ltp8xACLListsPorts_Object = MibTableColumn
ltp8xACLListsPorts = _Ltp8xACLListsPorts_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 15, 2, 1, 4),
    _Ltp8xACLListsPorts_Type()
)
ltp8xACLListsPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xACLListsPorts.setStatus("current")
_Ltp8xACLListsFiltersCount_Type = Unsigned32
_Ltp8xACLListsFiltersCount_Object = MibTableColumn
ltp8xACLListsFiltersCount = _Ltp8xACLListsFiltersCount_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 15, 2, 1, 5),
    _Ltp8xACLListsFiltersCount_Type()
)
ltp8xACLListsFiltersCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xACLListsFiltersCount.setStatus("current")
_Ltp8xACLListsRowStatus_Type = RowStatus
_Ltp8xACLListsRowStatus_Object = MibTableColumn
ltp8xACLListsRowStatus = _Ltp8xACLListsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 15, 2, 1, 10),
    _Ltp8xACLListsRowStatus_Type()
)
ltp8xACLListsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xACLListsRowStatus.setStatus("current")
_Ltp8xACLFiltersTable_Object = MibTable
ltp8xACLFiltersTable = _Ltp8xACLFiltersTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 15, 3)
)
if mibBuilder.loadTexts:
    ltp8xACLFiltersTable.setStatus("current")
_Ltp8xACLFiltersEntry_Object = MibTableRow
ltp8xACLFiltersEntry = _Ltp8xACLFiltersEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 15, 3, 1)
)
ltp8xACLFiltersEntry.setIndexNames(
    (0, "ELTEX-LTP8X", "ltp8xACLFiltersSlot"),
    (0, "ELTEX-LTP8X", "ltp8xACLFiltersListID"),
    (0, "ELTEX-LTP8X", "ltp8xACLFiltersFilterID"),
)
if mibBuilder.loadTexts:
    ltp8xACLFiltersEntry.setStatus("current")
_Ltp8xACLFiltersSlot_Type = Unsigned32
_Ltp8xACLFiltersSlot_Object = MibTableColumn
ltp8xACLFiltersSlot = _Ltp8xACLFiltersSlot_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 15, 3, 1, 1),
    _Ltp8xACLFiltersSlot_Type()
)
ltp8xACLFiltersSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ltp8xACLFiltersSlot.setStatus("current")
_Ltp8xACLFiltersListID_Type = Unsigned32
_Ltp8xACLFiltersListID_Object = MibTableColumn
ltp8xACLFiltersListID = _Ltp8xACLFiltersListID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 15, 3, 1, 2),
    _Ltp8xACLFiltersListID_Type()
)
ltp8xACLFiltersListID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ltp8xACLFiltersListID.setStatus("current")
_Ltp8xACLFiltersFilterID_Type = Unsigned32
_Ltp8xACLFiltersFilterID_Object = MibTableColumn
ltp8xACLFiltersFilterID = _Ltp8xACLFiltersFilterID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 15, 3, 1, 3),
    _Ltp8xACLFiltersFilterID_Type()
)
ltp8xACLFiltersFilterID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ltp8xACLFiltersFilterID.setStatus("current")


class _Ltp8xACLFiltersType_Type(Integer32):
    """Custom type ltp8xACLFiltersType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("ipDA", 5),
          ("ipProto", 3),
          ("ipSA", 4),
          ("l2Proto", 2),
          ("macDA", 1),
          ("macSA", 0),
          ("tcpDPort", 7),
          ("tcpSPort", 6),
          ("udpDPort", 9),
          ("updSPort", 8))
    )


_Ltp8xACLFiltersType_Type.__name__ = "Integer32"
_Ltp8xACLFiltersType_Object = MibTableColumn
ltp8xACLFiltersType = _Ltp8xACLFiltersType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 15, 3, 1, 4),
    _Ltp8xACLFiltersType_Type()
)
ltp8xACLFiltersType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xACLFiltersType.setStatus("current")
_Ltp8xACLFiltersMacAddress_Type = MacAddress
_Ltp8xACLFiltersMacAddress_Object = MibTableColumn
ltp8xACLFiltersMacAddress = _Ltp8xACLFiltersMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 15, 3, 1, 5),
    _Ltp8xACLFiltersMacAddress_Type()
)
ltp8xACLFiltersMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xACLFiltersMacAddress.setStatus("current")
_Ltp8xACLFiltersIpAddress_Type = IpAddress
_Ltp8xACLFiltersIpAddress_Object = MibTableColumn
ltp8xACLFiltersIpAddress = _Ltp8xACLFiltersIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 15, 3, 1, 6),
    _Ltp8xACLFiltersIpAddress_Type()
)
ltp8xACLFiltersIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xACLFiltersIpAddress.setStatus("current")
_Ltp8xACLFiltersProtocol_Type = Unsigned32
_Ltp8xACLFiltersProtocol_Object = MibTableColumn
ltp8xACLFiltersProtocol = _Ltp8xACLFiltersProtocol_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 15, 3, 1, 7),
    _Ltp8xACLFiltersProtocol_Type()
)
ltp8xACLFiltersProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xACLFiltersProtocol.setStatus("current")
_Ltp8xACLFiltersPort_Type = Unsigned32
_Ltp8xACLFiltersPort_Object = MibTableColumn
ltp8xACLFiltersPort = _Ltp8xACLFiltersPort_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 15, 3, 1, 8),
    _Ltp8xACLFiltersPort_Type()
)
ltp8xACLFiltersPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xACLFiltersPort.setStatus("current")
_Ltp8xACLFiltersRowStatus_Type = RowStatus
_Ltp8xACLFiltersRowStatus_Object = MibTableColumn
ltp8xACLFiltersRowStatus = _Ltp8xACLFiltersRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 15, 3, 1, 10),
    _Ltp8xACLFiltersRowStatus_Type()
)
ltp8xACLFiltersRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xACLFiltersRowStatus.setStatus("current")
_Ltp8xIGMPProxyReportTable_Object = MibTable
ltp8xIGMPProxyReportTable = _Ltp8xIGMPProxyReportTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 20)
)
if mibBuilder.loadTexts:
    ltp8xIGMPProxyReportTable.setStatus("current")
_Ltp8xIGMPProxyReportEntry_Object = MibTableRow
ltp8xIGMPProxyReportEntry = _Ltp8xIGMPProxyReportEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 20, 1)
)
ltp8xIGMPProxyReportEntry.setIndexNames(
    (0, "ELTEX-LTP8X", "ltp8xIGMPProxyReportSlot"),
)
if mibBuilder.loadTexts:
    ltp8xIGMPProxyReportEntry.setStatus("current")
_Ltp8xIGMPProxyReportSlot_Type = Unsigned32
_Ltp8xIGMPProxyReportSlot_Object = MibTableColumn
ltp8xIGMPProxyReportSlot = _Ltp8xIGMPProxyReportSlot_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 20, 1, 1),
    _Ltp8xIGMPProxyReportSlot_Type()
)
ltp8xIGMPProxyReportSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ltp8xIGMPProxyReportSlot.setStatus("current")
_Ltp8xIGMPProxyReportEnabled_Type = TruthValue
_Ltp8xIGMPProxyReportEnabled_Object = MibTableColumn
ltp8xIGMPProxyReportEnabled = _Ltp8xIGMPProxyReportEnabled_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 20, 1, 2),
    _Ltp8xIGMPProxyReportEnabled_Type()
)
ltp8xIGMPProxyReportEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xIGMPProxyReportEnabled.setStatus("current")
_Ltp8xMLDProxyReportEnabled_Type = TruthValue
_Ltp8xMLDProxyReportEnabled_Object = MibTableColumn
ltp8xMLDProxyReportEnabled = _Ltp8xMLDProxyReportEnabled_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 20, 1, 3),
    _Ltp8xMLDProxyReportEnabled_Type()
)
ltp8xMLDProxyReportEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xMLDProxyReportEnabled.setStatus("current")
_Ltp8xIGMPProxyReportRangesTable_Object = MibTable
ltp8xIGMPProxyReportRangesTable = _Ltp8xIGMPProxyReportRangesTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 21)
)
if mibBuilder.loadTexts:
    ltp8xIGMPProxyReportRangesTable.setStatus("current")
_Ltp8xIGMPProxyReportRangesEntry_Object = MibTableRow
ltp8xIGMPProxyReportRangesEntry = _Ltp8xIGMPProxyReportRangesEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 21, 1)
)
ltp8xIGMPProxyReportRangesEntry.setIndexNames(
    (0, "ELTEX-LTP8X", "ltp8xIGMPProxyReportRangesSlot"),
    (0, "ELTEX-LTP8X", "ltp8xIGMPProxyReportRangesID"),
)
if mibBuilder.loadTexts:
    ltp8xIGMPProxyReportRangesEntry.setStatus("current")
_Ltp8xIGMPProxyReportRangesSlot_Type = Unsigned32
_Ltp8xIGMPProxyReportRangesSlot_Object = MibTableColumn
ltp8xIGMPProxyReportRangesSlot = _Ltp8xIGMPProxyReportRangesSlot_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 21, 1, 1),
    _Ltp8xIGMPProxyReportRangesSlot_Type()
)
ltp8xIGMPProxyReportRangesSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ltp8xIGMPProxyReportRangesSlot.setStatus("current")
_Ltp8xIGMPProxyReportRangesID_Type = Unsigned32
_Ltp8xIGMPProxyReportRangesID_Object = MibTableColumn
ltp8xIGMPProxyReportRangesID = _Ltp8xIGMPProxyReportRangesID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 21, 1, 2),
    _Ltp8xIGMPProxyReportRangesID_Type()
)
ltp8xIGMPProxyReportRangesID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ltp8xIGMPProxyReportRangesID.setStatus("current")
_Ltp8xIGMPProxyReportRangesStart_Type = IpAddress
_Ltp8xIGMPProxyReportRangesStart_Object = MibTableColumn
ltp8xIGMPProxyReportRangesStart = _Ltp8xIGMPProxyReportRangesStart_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 21, 1, 3),
    _Ltp8xIGMPProxyReportRangesStart_Type()
)
ltp8xIGMPProxyReportRangesStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xIGMPProxyReportRangesStart.setStatus("current")
_Ltp8xIGMPProxyReportRangesEnd_Type = IpAddress
_Ltp8xIGMPProxyReportRangesEnd_Object = MibTableColumn
ltp8xIGMPProxyReportRangesEnd = _Ltp8xIGMPProxyReportRangesEnd_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 21, 1, 4),
    _Ltp8xIGMPProxyReportRangesEnd_Type()
)
ltp8xIGMPProxyReportRangesEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xIGMPProxyReportRangesEnd.setStatus("current")


class _Ltp8xIGMPProxyReportRangesFromVLAN_Type(Integer32):
    """Custom type ltp8xIGMPProxyReportRangesFromVLAN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            65535
        )
    )
    namedValues = NamedValues(
        ("all", 65535)
    )


_Ltp8xIGMPProxyReportRangesFromVLAN_Type.__name__ = "Integer32"
_Ltp8xIGMPProxyReportRangesFromVLAN_Object = MibTableColumn
ltp8xIGMPProxyReportRangesFromVLAN = _Ltp8xIGMPProxyReportRangesFromVLAN_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 21, 1, 5),
    _Ltp8xIGMPProxyReportRangesFromVLAN_Type()
)
ltp8xIGMPProxyReportRangesFromVLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xIGMPProxyReportRangesFromVLAN.setStatus("current")
_Ltp8xIGMPProxyReportRangesToVLAN_Type = Integer32
_Ltp8xIGMPProxyReportRangesToVLAN_Object = MibTableColumn
ltp8xIGMPProxyReportRangesToVLAN = _Ltp8xIGMPProxyReportRangesToVLAN_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 21, 1, 6),
    _Ltp8xIGMPProxyReportRangesToVLAN_Type()
)
ltp8xIGMPProxyReportRangesToVLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xIGMPProxyReportRangesToVLAN.setStatus("current")
_Ltp8xIGMPProxyRowStatus_Type = RowStatus
_Ltp8xIGMPProxyRowStatus_Object = MibTableColumn
ltp8xIGMPProxyRowStatus = _Ltp8xIGMPProxyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 21, 1, 10),
    _Ltp8xIGMPProxyRowStatus_Type()
)
ltp8xIGMPProxyRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xIGMPProxyRowStatus.setStatus("current")
_Ltp8xIGMPProxyReportRangesGlobalTable_Object = MibTable
ltp8xIGMPProxyReportRangesGlobalTable = _Ltp8xIGMPProxyReportRangesGlobalTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 22)
)
if mibBuilder.loadTexts:
    ltp8xIGMPProxyReportRangesGlobalTable.setStatus("current")
_Ltp8xIGMPProxyReportRangesGlobalEntry_Object = MibTableRow
ltp8xIGMPProxyReportRangesGlobalEntry = _Ltp8xIGMPProxyReportRangesGlobalEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 22, 1)
)
ltp8xIGMPProxyReportRangesGlobalEntry.setIndexNames(
    (0, "ELTEX-LTP8X", "ltp8xIGMPProxyReportRangesGlobalID"),
)
if mibBuilder.loadTexts:
    ltp8xIGMPProxyReportRangesGlobalEntry.setStatus("current")
_Ltp8xIGMPProxyReportRangesGlobalID_Type = Unsigned32
_Ltp8xIGMPProxyReportRangesGlobalID_Object = MibTableColumn
ltp8xIGMPProxyReportRangesGlobalID = _Ltp8xIGMPProxyReportRangesGlobalID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 22, 1, 1),
    _Ltp8xIGMPProxyReportRangesGlobalID_Type()
)
ltp8xIGMPProxyReportRangesGlobalID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ltp8xIGMPProxyReportRangesGlobalID.setStatus("current")
_Ltp8xIGMPProxyReportRangesGlobalStart_Type = IpAddress
_Ltp8xIGMPProxyReportRangesGlobalStart_Object = MibTableColumn
ltp8xIGMPProxyReportRangesGlobalStart = _Ltp8xIGMPProxyReportRangesGlobalStart_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 22, 1, 2),
    _Ltp8xIGMPProxyReportRangesGlobalStart_Type()
)
ltp8xIGMPProxyReportRangesGlobalStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xIGMPProxyReportRangesGlobalStart.setStatus("current")
_Ltp8xIGMPProxyReportRangesGlobalEnd_Type = IpAddress
_Ltp8xIGMPProxyReportRangesGlobalEnd_Object = MibTableColumn
ltp8xIGMPProxyReportRangesGlobalEnd = _Ltp8xIGMPProxyReportRangesGlobalEnd_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 22, 1, 3),
    _Ltp8xIGMPProxyReportRangesGlobalEnd_Type()
)
ltp8xIGMPProxyReportRangesGlobalEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xIGMPProxyReportRangesGlobalEnd.setStatus("current")


class _Ltp8xIGMPProxyReportRangesGlobalFromVLAN_Type(Integer32):
    """Custom type ltp8xIGMPProxyReportRangesGlobalFromVLAN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            65535
        )
    )
    namedValues = NamedValues(
        ("all", 65535)
    )


_Ltp8xIGMPProxyReportRangesGlobalFromVLAN_Type.__name__ = "Integer32"
_Ltp8xIGMPProxyReportRangesGlobalFromVLAN_Object = MibTableColumn
ltp8xIGMPProxyReportRangesGlobalFromVLAN = _Ltp8xIGMPProxyReportRangesGlobalFromVLAN_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 22, 1, 4),
    _Ltp8xIGMPProxyReportRangesGlobalFromVLAN_Type()
)
ltp8xIGMPProxyReportRangesGlobalFromVLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xIGMPProxyReportRangesGlobalFromVLAN.setStatus("current")
_Ltp8xIGMPProxyReportRangesGlobalToVLAN_Type = Integer32
_Ltp8xIGMPProxyReportRangesGlobalToVLAN_Object = MibTableColumn
ltp8xIGMPProxyReportRangesGlobalToVLAN = _Ltp8xIGMPProxyReportRangesGlobalToVLAN_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 22, 1, 5),
    _Ltp8xIGMPProxyReportRangesGlobalToVLAN_Type()
)
ltp8xIGMPProxyReportRangesGlobalToVLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xIGMPProxyReportRangesGlobalToVLAN.setStatus("current")
_Ltp8xIGMPProxyGlobalRowStatus_Type = RowStatus
_Ltp8xIGMPProxyGlobalRowStatus_Object = MibTableColumn
ltp8xIGMPProxyGlobalRowStatus = _Ltp8xIGMPProxyGlobalRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 22, 1, 10),
    _Ltp8xIGMPProxyGlobalRowStatus_Type()
)
ltp8xIGMPProxyGlobalRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xIGMPProxyGlobalRowStatus.setStatus("current")
_Ltp8xMLDProxyReportRangesTable_Object = MibTable
ltp8xMLDProxyReportRangesTable = _Ltp8xMLDProxyReportRangesTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 23)
)
if mibBuilder.loadTexts:
    ltp8xMLDProxyReportRangesTable.setStatus("current")
_Ltp8xMLDProxyReportRangesEntry_Object = MibTableRow
ltp8xMLDProxyReportRangesEntry = _Ltp8xMLDProxyReportRangesEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 23, 1)
)
ltp8xMLDProxyReportRangesEntry.setIndexNames(
    (0, "ELTEX-LTP8X", "ltp8xMLDProxyReportRangesSlot"),
    (0, "ELTEX-LTP8X", "ltp8xMLDProxyReportRangesID"),
)
if mibBuilder.loadTexts:
    ltp8xMLDProxyReportRangesEntry.setStatus("current")
_Ltp8xMLDProxyReportRangesSlot_Type = Unsigned32
_Ltp8xMLDProxyReportRangesSlot_Object = MibTableColumn
ltp8xMLDProxyReportRangesSlot = _Ltp8xMLDProxyReportRangesSlot_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 23, 1, 1),
    _Ltp8xMLDProxyReportRangesSlot_Type()
)
ltp8xMLDProxyReportRangesSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ltp8xMLDProxyReportRangesSlot.setStatus("current")
_Ltp8xMLDProxyReportRangesID_Type = Unsigned32
_Ltp8xMLDProxyReportRangesID_Object = MibTableColumn
ltp8xMLDProxyReportRangesID = _Ltp8xMLDProxyReportRangesID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 23, 1, 2),
    _Ltp8xMLDProxyReportRangesID_Type()
)
ltp8xMLDProxyReportRangesID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ltp8xMLDProxyReportRangesID.setStatus("current")
_Ltp8xMLDProxyReportRangesStart_Type = Ipv6Address
_Ltp8xMLDProxyReportRangesStart_Object = MibTableColumn
ltp8xMLDProxyReportRangesStart = _Ltp8xMLDProxyReportRangesStart_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 23, 1, 3),
    _Ltp8xMLDProxyReportRangesStart_Type()
)
ltp8xMLDProxyReportRangesStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xMLDProxyReportRangesStart.setStatus("current")
_Ltp8xMLDProxyReportRangesEnd_Type = Ipv6Address
_Ltp8xMLDProxyReportRangesEnd_Object = MibTableColumn
ltp8xMLDProxyReportRangesEnd = _Ltp8xMLDProxyReportRangesEnd_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 23, 1, 4),
    _Ltp8xMLDProxyReportRangesEnd_Type()
)
ltp8xMLDProxyReportRangesEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xMLDProxyReportRangesEnd.setStatus("current")


class _Ltp8xMLDProxyReportRangesFromVLAN_Type(Integer32):
    """Custom type ltp8xMLDProxyReportRangesFromVLAN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            65535
        )
    )
    namedValues = NamedValues(
        ("all", 65535)
    )


_Ltp8xMLDProxyReportRangesFromVLAN_Type.__name__ = "Integer32"
_Ltp8xMLDProxyReportRangesFromVLAN_Object = MibTableColumn
ltp8xMLDProxyReportRangesFromVLAN = _Ltp8xMLDProxyReportRangesFromVLAN_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 23, 1, 5),
    _Ltp8xMLDProxyReportRangesFromVLAN_Type()
)
ltp8xMLDProxyReportRangesFromVLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xMLDProxyReportRangesFromVLAN.setStatus("current")
_Ltp8xMLDProxyReportRangesToVLAN_Type = Integer32
_Ltp8xMLDProxyReportRangesToVLAN_Object = MibTableColumn
ltp8xMLDProxyReportRangesToVLAN = _Ltp8xMLDProxyReportRangesToVLAN_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 23, 1, 6),
    _Ltp8xMLDProxyReportRangesToVLAN_Type()
)
ltp8xMLDProxyReportRangesToVLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xMLDProxyReportRangesToVLAN.setStatus("current")
_Ltp8xMLDProxyRowStatus_Type = RowStatus
_Ltp8xMLDProxyRowStatus_Object = MibTableColumn
ltp8xMLDProxyRowStatus = _Ltp8xMLDProxyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 23, 1, 10),
    _Ltp8xMLDProxyRowStatus_Type()
)
ltp8xMLDProxyRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xMLDProxyRowStatus.setStatus("current")
_Ltp8xMLDProxyReportRangesGlobalTable_Object = MibTable
ltp8xMLDProxyReportRangesGlobalTable = _Ltp8xMLDProxyReportRangesGlobalTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 24)
)
if mibBuilder.loadTexts:
    ltp8xMLDProxyReportRangesGlobalTable.setStatus("current")
_Ltp8xMLDProxyReportRangesGlobalEntry_Object = MibTableRow
ltp8xMLDProxyReportRangesGlobalEntry = _Ltp8xMLDProxyReportRangesGlobalEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 24, 1)
)
ltp8xMLDProxyReportRangesGlobalEntry.setIndexNames(
    (0, "ELTEX-LTP8X", "ltp8xMLDProxyReportRangesGlobalID"),
)
if mibBuilder.loadTexts:
    ltp8xMLDProxyReportRangesGlobalEntry.setStatus("current")
_Ltp8xMLDProxyReportRangesGlobalID_Type = Unsigned32
_Ltp8xMLDProxyReportRangesGlobalID_Object = MibTableColumn
ltp8xMLDProxyReportRangesGlobalID = _Ltp8xMLDProxyReportRangesGlobalID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 24, 1, 1),
    _Ltp8xMLDProxyReportRangesGlobalID_Type()
)
ltp8xMLDProxyReportRangesGlobalID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ltp8xMLDProxyReportRangesGlobalID.setStatus("current")
_Ltp8xMLDProxyReportRangesGlobalStart_Type = Ipv6Address
_Ltp8xMLDProxyReportRangesGlobalStart_Object = MibTableColumn
ltp8xMLDProxyReportRangesGlobalStart = _Ltp8xMLDProxyReportRangesGlobalStart_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 24, 1, 2),
    _Ltp8xMLDProxyReportRangesGlobalStart_Type()
)
ltp8xMLDProxyReportRangesGlobalStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xMLDProxyReportRangesGlobalStart.setStatus("current")
_Ltp8xMLDProxyReportRangesGlobalEnd_Type = Ipv6Address
_Ltp8xMLDProxyReportRangesGlobalEnd_Object = MibTableColumn
ltp8xMLDProxyReportRangesGlobalEnd = _Ltp8xMLDProxyReportRangesGlobalEnd_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 24, 1, 3),
    _Ltp8xMLDProxyReportRangesGlobalEnd_Type()
)
ltp8xMLDProxyReportRangesGlobalEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xMLDProxyReportRangesGlobalEnd.setStatus("current")


class _Ltp8xMLDProxyReportRangesGlobalFromVLAN_Type(Integer32):
    """Custom type ltp8xMLDProxyReportRangesGlobalFromVLAN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            65535
        )
    )
    namedValues = NamedValues(
        ("all", 65535)
    )


_Ltp8xMLDProxyReportRangesGlobalFromVLAN_Type.__name__ = "Integer32"
_Ltp8xMLDProxyReportRangesGlobalFromVLAN_Object = MibTableColumn
ltp8xMLDProxyReportRangesGlobalFromVLAN = _Ltp8xMLDProxyReportRangesGlobalFromVLAN_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 24, 1, 4),
    _Ltp8xMLDProxyReportRangesGlobalFromVLAN_Type()
)
ltp8xMLDProxyReportRangesGlobalFromVLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xMLDProxyReportRangesGlobalFromVLAN.setStatus("current")
_Ltp8xMLDProxyReportRangesGlobalToVLAN_Type = Integer32
_Ltp8xMLDProxyReportRangesGlobalToVLAN_Object = MibTableColumn
ltp8xMLDProxyReportRangesGlobalToVLAN = _Ltp8xMLDProxyReportRangesGlobalToVLAN_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 24, 1, 5),
    _Ltp8xMLDProxyReportRangesGlobalToVLAN_Type()
)
ltp8xMLDProxyReportRangesGlobalToVLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xMLDProxyReportRangesGlobalToVLAN.setStatus("current")
_Ltp8xMLDProxyGlobalRowStatus_Type = RowStatus
_Ltp8xMLDProxyGlobalRowStatus_Object = MibTableColumn
ltp8xMLDProxyGlobalRowStatus = _Ltp8xMLDProxyGlobalRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 9, 24, 1, 10),
    _Ltp8xMLDProxyGlobalRowStatus_Type()
)
ltp8xMLDProxyGlobalRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xMLDProxyGlobalRowStatus.setStatus("current")
_Ltp8xP2PTable_Object = MibTable
ltp8xP2PTable = _Ltp8xP2PTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 10)
)
if mibBuilder.loadTexts:
    ltp8xP2PTable.setStatus("current")
_Ltp8xP2PEntry_Object = MibTableRow
ltp8xP2PEntry = _Ltp8xP2PEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 10, 1)
)
ltp8xP2PEntry.setIndexNames(
    (0, "ELTEX-LTP8X", "ltp8xP2PSlot"),
)
if mibBuilder.loadTexts:
    ltp8xP2PEntry.setStatus("current")
_Ltp8xP2PSlot_Type = Unsigned32
_Ltp8xP2PSlot_Object = MibTableColumn
ltp8xP2PSlot = _Ltp8xP2PSlot_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 10, 1, 1),
    _Ltp8xP2PSlot_Type()
)
ltp8xP2PSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xP2PSlot.setStatus("current")
_Ltp8xP2PEnabled_Type = TruthValue
_Ltp8xP2PEnabled_Object = MibTableColumn
ltp8xP2PEnabled = _Ltp8xP2PEnabled_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 10, 1, 2),
    _Ltp8xP2PEnabled_Type()
)
ltp8xP2PEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xP2PEnabled.setStatus("current")
_Ltp8xPLC_ObjectIdentity = ObjectIdentity
ltp8xPLC = _Ltp8xPLC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 11)
)
_Ltp8xPLCBoardStateTable_Object = MibTable
ltp8xPLCBoardStateTable = _Ltp8xPLCBoardStateTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 11, 1)
)
if mibBuilder.loadTexts:
    ltp8xPLCBoardStateTable.setStatus("current")
_Ltp8xPLCBoardStateEntry_Object = MibTableRow
ltp8xPLCBoardStateEntry = _Ltp8xPLCBoardStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 11, 1, 1)
)
ltp8xPLCBoardStateEntry.setIndexNames(
    (0, "ELTEX-LTP8X", "ltp8xPLCBoardStateSlot"),
)
if mibBuilder.loadTexts:
    ltp8xPLCBoardStateEntry.setStatus("current")
_Ltp8xPLCBoardStateSlot_Type = Unsigned32
_Ltp8xPLCBoardStateSlot_Object = MibTableColumn
ltp8xPLCBoardStateSlot = _Ltp8xPLCBoardStateSlot_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 11, 1, 1, 1),
    _Ltp8xPLCBoardStateSlot_Type()
)
ltp8xPLCBoardStateSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xPLCBoardStateSlot.setStatus("current")
_Ltp8xPLCBoardStateRAMFree_Type = Unsigned32
_Ltp8xPLCBoardStateRAMFree_Object = MibTableColumn
ltp8xPLCBoardStateRAMFree = _Ltp8xPLCBoardStateRAMFree_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 11, 1, 1, 2),
    _Ltp8xPLCBoardStateRAMFree_Type()
)
ltp8xPLCBoardStateRAMFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xPLCBoardStateRAMFree.setStatus("current")
_Ltp8xPLCBoardStateLoadAverage1Minute_Type = Unsigned32
_Ltp8xPLCBoardStateLoadAverage1Minute_Object = MibTableColumn
ltp8xPLCBoardStateLoadAverage1Minute = _Ltp8xPLCBoardStateLoadAverage1Minute_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 11, 1, 1, 3),
    _Ltp8xPLCBoardStateLoadAverage1Minute_Type()
)
ltp8xPLCBoardStateLoadAverage1Minute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xPLCBoardStateLoadAverage1Minute.setStatus("current")
_Ltp8xPLCBoardStateLoadAverage5Minutes_Type = Unsigned32
_Ltp8xPLCBoardStateLoadAverage5Minutes_Object = MibTableColumn
ltp8xPLCBoardStateLoadAverage5Minutes = _Ltp8xPLCBoardStateLoadAverage5Minutes_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 11, 1, 1, 4),
    _Ltp8xPLCBoardStateLoadAverage5Minutes_Type()
)
ltp8xPLCBoardStateLoadAverage5Minutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xPLCBoardStateLoadAverage5Minutes.setStatus("current")
_Ltp8xPLCBoardStateLoadAverage15Minutes_Type = Unsigned32
_Ltp8xPLCBoardStateLoadAverage15Minutes_Object = MibTableColumn
ltp8xPLCBoardStateLoadAverage15Minutes = _Ltp8xPLCBoardStateLoadAverage15Minutes_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 11, 1, 1, 5),
    _Ltp8xPLCBoardStateLoadAverage15Minutes_Type()
)
ltp8xPLCBoardStateLoadAverage15Minutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xPLCBoardStateLoadAverage15Minutes.setStatus("current")
_Ltp8xPLCBoardStateSensor1Temperature_Type = Unsigned32
_Ltp8xPLCBoardStateSensor1Temperature_Object = MibTableColumn
ltp8xPLCBoardStateSensor1Temperature = _Ltp8xPLCBoardStateSensor1Temperature_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 11, 1, 1, 6),
    _Ltp8xPLCBoardStateSensor1Temperature_Type()
)
ltp8xPLCBoardStateSensor1Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xPLCBoardStateSensor1Temperature.setStatus("current")
_Ltp8xPLCBoardStateSensor2Temperature_Type = Unsigned32
_Ltp8xPLCBoardStateSensor2Temperature_Object = MibTableColumn
ltp8xPLCBoardStateSensor2Temperature = _Ltp8xPLCBoardStateSensor2Temperature_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 11, 1, 1, 7),
    _Ltp8xPLCBoardStateSensor2Temperature_Type()
)
ltp8xPLCBoardStateSensor2Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xPLCBoardStateSensor2Temperature.setStatus("current")
_Ltp8xPLCBoardStateUptime_Type = Unsigned32
_Ltp8xPLCBoardStateUptime_Object = MibTableColumn
ltp8xPLCBoardStateUptime = _Ltp8xPLCBoardStateUptime_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 11, 1, 1, 8),
    _Ltp8xPLCBoardStateUptime_Type()
)
ltp8xPLCBoardStateUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xPLCBoardStateUptime.setStatus("current")
_Ltp8xPLCBoardStateSerialNumber_Type = DisplayString
_Ltp8xPLCBoardStateSerialNumber_Object = MibTableColumn
ltp8xPLCBoardStateSerialNumber = _Ltp8xPLCBoardStateSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 11, 1, 1, 9),
    _Ltp8xPLCBoardStateSerialNumber_Type()
)
ltp8xPLCBoardStateSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xPLCBoardStateSerialNumber.setStatus("current")
_Ltp8xPLCBoardStateFirmwareRevision_Type = DisplayString
_Ltp8xPLCBoardStateFirmwareRevision_Object = MibTableColumn
ltp8xPLCBoardStateFirmwareRevision = _Ltp8xPLCBoardStateFirmwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 11, 1, 1, 10),
    _Ltp8xPLCBoardStateFirmwareRevision_Type()
)
ltp8xPLCBoardStateFirmwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xPLCBoardStateFirmwareRevision.setStatus("current")
_Ltp8xPLCBoardStateDiskFreeSpace_Type = Unsigned32
_Ltp8xPLCBoardStateDiskFreeSpace_Object = MibTableColumn
ltp8xPLCBoardStateDiskFreeSpace = _Ltp8xPLCBoardStateDiskFreeSpace_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 11, 1, 1, 11),
    _Ltp8xPLCBoardStateDiskFreeSpace_Type()
)
ltp8xPLCBoardStateDiskFreeSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xPLCBoardStateDiskFreeSpace.setStatus("current")
_Ltp8xPLCBoardStateModuleVersion_Type = DisplayString
_Ltp8xPLCBoardStateModuleVersion_Object = MibTableColumn
ltp8xPLCBoardStateModuleVersion = _Ltp8xPLCBoardStateModuleVersion_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 11, 1, 1, 12),
    _Ltp8xPLCBoardStateModuleVersion_Type()
)
ltp8xPLCBoardStateModuleVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xPLCBoardStateModuleVersion.setStatus("current")
_Ltp8xPLCBoardStateBuildTime_Type = DisplayString
_Ltp8xPLCBoardStateBuildTime_Object = MibTableColumn
ltp8xPLCBoardStateBuildTime = _Ltp8xPLCBoardStateBuildTime_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 11, 1, 1, 13),
    _Ltp8xPLCBoardStateBuildTime_Type()
)
ltp8xPLCBoardStateBuildTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xPLCBoardStateBuildTime.setStatus("current")
_Ltp8xPLCBoardStateBuildRevision_Type = Unsigned32
_Ltp8xPLCBoardStateBuildRevision_Object = MibTableColumn
ltp8xPLCBoardStateBuildRevision = _Ltp8xPLCBoardStateBuildRevision_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 11, 1, 1, 14),
    _Ltp8xPLCBoardStateBuildRevision_Type()
)
ltp8xPLCBoardStateBuildRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xPLCBoardStateBuildRevision.setStatus("current")
_Ltp8xPLCBoardStateHardwareVesion_Type = Unsigned32
_Ltp8xPLCBoardStateHardwareVesion_Object = MibTableColumn
ltp8xPLCBoardStateHardwareVesion = _Ltp8xPLCBoardStateHardwareVesion_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 11, 1, 1, 15),
    _Ltp8xPLCBoardStateHardwareVesion_Type()
)
ltp8xPLCBoardStateHardwareVesion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xPLCBoardStateHardwareVesion.setStatus("current")


class _Ltp8xPLCBoardStateSensor1TemperatureExt_Type(Integer32):
    """Custom type ltp8xPLCBoardStateSensor1TemperatureExt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            65535
        )
    )
    namedValues = NamedValues(
        ("notValid", 65535)
    )


_Ltp8xPLCBoardStateSensor1TemperatureExt_Type.__name__ = "Integer32"
_Ltp8xPLCBoardStateSensor1TemperatureExt_Object = MibTableColumn
ltp8xPLCBoardStateSensor1TemperatureExt = _Ltp8xPLCBoardStateSensor1TemperatureExt_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 11, 1, 1, 16),
    _Ltp8xPLCBoardStateSensor1TemperatureExt_Type()
)
ltp8xPLCBoardStateSensor1TemperatureExt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xPLCBoardStateSensor1TemperatureExt.setStatus("current")


class _Ltp8xPLCBoardStateSensor2TemperatureExt_Type(Integer32):
    """Custom type ltp8xPLCBoardStateSensor2TemperatureExt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            65535
        )
    )
    namedValues = NamedValues(
        ("notValid", 65535)
    )


_Ltp8xPLCBoardStateSensor2TemperatureExt_Type.__name__ = "Integer32"
_Ltp8xPLCBoardStateSensor2TemperatureExt_Object = MibTableColumn
ltp8xPLCBoardStateSensor2TemperatureExt = _Ltp8xPLCBoardStateSensor2TemperatureExt_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 11, 1, 1, 17),
    _Ltp8xPLCBoardStateSensor2TemperatureExt_Type()
)
ltp8xPLCBoardStateSensor2TemperatureExt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xPLCBoardStateSensor2TemperatureExt.setStatus("current")
_Ltp8xSyncCounters_ObjectIdentity = ObjectIdentity
ltp8xSyncCounters = _Ltp8xSyncCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 15)
)
_Ltp8xSyncCountersTable_Object = MibTable
ltp8xSyncCountersTable = _Ltp8xSyncCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 15, 1)
)
if mibBuilder.loadTexts:
    ltp8xSyncCountersTable.setStatus("current")
_Ltp8xSyncCountersEntry_Object = MibTableRow
ltp8xSyncCountersEntry = _Ltp8xSyncCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 15, 1, 1)
)
ltp8xSyncCountersEntry.setIndexNames(
    (0, "ELTEX-LTP8X", "ltp8xSyncCountersSlot"),
)
if mibBuilder.loadTexts:
    ltp8xSyncCountersEntry.setStatus("current")
_Ltp8xSyncCountersSlot_Type = Unsigned32
_Ltp8xSyncCountersSlot_Object = MibTableColumn
ltp8xSyncCountersSlot = _Ltp8xSyncCountersSlot_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 15, 1, 1, 1),
    _Ltp8xSyncCountersSlot_Type()
)
ltp8xSyncCountersSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xSyncCountersSlot.setStatus("current")
_Ltp8xSyncCountersConfig_Type = Unsigned32
_Ltp8xSyncCountersConfig_Object = MibTableColumn
ltp8xSyncCountersConfig = _Ltp8xSyncCountersConfig_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 15, 1, 1, 2),
    _Ltp8xSyncCountersConfig_Type()
)
ltp8xSyncCountersConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xSyncCountersConfig.setStatus("current")
_Ltp8xSyncCountersState_Type = Unsigned32
_Ltp8xSyncCountersState_Object = MibTableColumn
ltp8xSyncCountersState = _Ltp8xSyncCountersState_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 15, 1, 1, 3),
    _Ltp8xSyncCountersState_Type()
)
ltp8xSyncCountersState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xSyncCountersState.setStatus("current")
_Ltp8xRawData_ObjectIdentity = ObjectIdentity
ltp8xRawData = _Ltp8xRawData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 90)
)
_Ltp8xRawMacTable_Object = MibTable
ltp8xRawMacTable = _Ltp8xRawMacTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 90, 1)
)
if mibBuilder.loadTexts:
    ltp8xRawMacTable.setStatus("current")
_Ltp8xRawMacEntry_Object = MibTableRow
ltp8xRawMacEntry = _Ltp8xRawMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 90, 1, 1)
)
ltp8xRawMacEntry.setIndexNames(
    (0, "ELTEX-LTP8X", "ltp8xRawMacSlot"),
    (0, "ELTEX-LTP8X", "ltp8xRawMacChunkID"),
)
if mibBuilder.loadTexts:
    ltp8xRawMacEntry.setStatus("current")
_Ltp8xRawMacSlot_Type = Unsigned32
_Ltp8xRawMacSlot_Object = MibTableColumn
ltp8xRawMacSlot = _Ltp8xRawMacSlot_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 90, 1, 1, 1),
    _Ltp8xRawMacSlot_Type()
)
ltp8xRawMacSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ltp8xRawMacSlot.setStatus("current")
_Ltp8xRawMacChunkID_Type = Unsigned32
_Ltp8xRawMacChunkID_Object = MibTableColumn
ltp8xRawMacChunkID = _Ltp8xRawMacChunkID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 90, 1, 1, 2),
    _Ltp8xRawMacChunkID_Type()
)
ltp8xRawMacChunkID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ltp8xRawMacChunkID.setStatus("current")


class _Ltp8xRawMacText_Type(OctetString):
    """Custom type ltp8xRawMacText based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Ltp8xRawMacText_Type.__name__ = "OctetString"
_Ltp8xRawMacText_Object = MibTableColumn
ltp8xRawMacText = _Ltp8xRawMacText_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 90, 1, 1, 3),
    _Ltp8xRawMacText_Type()
)
ltp8xRawMacText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xRawMacText.setStatus("current")
_Ltp8xRawSwitchMacTable_Object = MibTable
ltp8xRawSwitchMacTable = _Ltp8xRawSwitchMacTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 90, 2)
)
if mibBuilder.loadTexts:
    ltp8xRawSwitchMacTable.setStatus("current")
_Ltp8xRawSwitchMacEntry_Object = MibTableRow
ltp8xRawSwitchMacEntry = _Ltp8xRawSwitchMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 90, 2, 1)
)
ltp8xRawSwitchMacEntry.setIndexNames(
    (0, "ELTEX-LTP8X", "ltp8xRawSwitchMacSlot"),
    (0, "ELTEX-LTP8X", "ltp8xRawSwitchMacChunkID"),
)
if mibBuilder.loadTexts:
    ltp8xRawSwitchMacEntry.setStatus("current")
_Ltp8xRawSwitchMacSlot_Type = Unsigned32
_Ltp8xRawSwitchMacSlot_Object = MibTableColumn
ltp8xRawSwitchMacSlot = _Ltp8xRawSwitchMacSlot_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 90, 2, 1, 1),
    _Ltp8xRawSwitchMacSlot_Type()
)
ltp8xRawSwitchMacSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ltp8xRawSwitchMacSlot.setStatus("current")
_Ltp8xRawSwitchMacChunkID_Type = Unsigned32
_Ltp8xRawSwitchMacChunkID_Object = MibTableColumn
ltp8xRawSwitchMacChunkID = _Ltp8xRawSwitchMacChunkID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 90, 2, 1, 2),
    _Ltp8xRawSwitchMacChunkID_Type()
)
ltp8xRawSwitchMacChunkID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ltp8xRawSwitchMacChunkID.setStatus("current")


class _Ltp8xRawSwitchMacText_Type(OctetString):
    """Custom type ltp8xRawSwitchMacText based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Ltp8xRawSwitchMacText_Type.__name__ = "OctetString"
_Ltp8xRawSwitchMacText_Object = MibTableColumn
ltp8xRawSwitchMacText = _Ltp8xRawSwitchMacText_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 90, 2, 1, 3),
    _Ltp8xRawSwitchMacText_Type()
)
ltp8xRawSwitchMacText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xRawSwitchMacText.setStatus("current")
_Ltp8xMIBBoundary_Type = Unsigned32
_Ltp8xMIBBoundary_Object = MibScalar
ltp8xMIBBoundary = _Ltp8xMIBBoundary_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 99),
    _Ltp8xMIBBoundary_Type()
)
ltp8xMIBBoundary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xMIBBoundary.setStatus("current")
_Ltp8xTraps_ObjectIdentity = ObjectIdentity
ltp8xTraps = _Ltp8xTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100)
)
_Ltp8xAlarmTraps_ObjectIdentity = ObjectIdentity
ltp8xAlarmTraps = _Ltp8xAlarmTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 1)
)
_Ltp8xOkTraps_ObjectIdentity = ObjectIdentity
ltp8xOkTraps = _Ltp8xOkTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 2)
)
_Plc8AlarmTraps_ObjectIdentity = ObjectIdentity
plc8AlarmTraps = _Plc8AlarmTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 3)
)
_Plc8OkTraps_ObjectIdentity = ObjectIdentity
plc8OkTraps = _Plc8OkTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 4)
)
_Ltp4x_ObjectIdentity = ObjectIdentity
ltp4x = _Ltp4x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 70)
)

# Managed Objects groups

ltp8xObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 200)
)
ltp8xObjectGroup.setObjects(
      *(("ELTEX-LTP8X", "ltp8xPONChannelSlot"),
        ("ELTEX-LTP8X", "ltp8xPONChannelID"),
        ("ELTEX-LTP8X", "ltp8xPONChannelState"),
        ("ELTEX-LTP8X", "ltp8xPONChannelONTCount"),
        ("ELTEX-LTP8X", "ltp8xPONChannelEnabled"),
        ("ELTEX-LTP8X", "ltp8xONTSlot"),
        ("ELTEX-LTP8X", "ltp8xONTSerial"),
        ("ELTEX-LTP8X", "ltp8xONTStateChannel"),
        ("ELTEX-LTP8X", "ltp8xONTStateID"),
        ("ELTEX-LTP8X", "ltp8xONTStateState"),
        ("ELTEX-LTP8X", "ltp8xONTStateEqualizationDelay"),
        ("ELTEX-LTP8X", "ltp8xONTStateFecState"),
        ("ELTEX-LTP8X", "ltp8xONTStateEncryptionKey"),
        ("ELTEX-LTP8X", "ltp8xONTStateOMCIPortId"),
        ("ELTEX-LTP8X", "ltp8xONTStateDistance"),
        ("ELTEX-LTP8X", "ltp8xONTStateReconfigure"),
        ("ELTEX-LTP8X", "ltp8xONTStateUpdateFirmware"),
        ("ELTEX-LTP8X", "ltp8xONTConfigSlot"),
        ("ELTEX-LTP8X", "ltp8xONTConfigSerial"),
        ("ELTEX-LTP8X", "ltp8xONTConfigChannel"),
        ("ELTEX-LTP8X", "ltp8xONTConfigID"),
        ("ELTEX-LTP8X", "ltp8xONTConfigServicesProfile"),
        ("ELTEX-LTP8X", "ltp8xONTConfigPassword"),
        ("ELTEX-LTP8X", "ltp8xONTConfigFecUp"),
        ("ELTEX-LTP8X", "ltp8xONTConfigRowStatus"),
        ("ELTEX-LTP8X", "ltp8xONTServiceOverrideID"),
        ("ELTEX-LTP8X", "ltp8xONTServiceOverrideSlot"),
        ("ELTEX-LTP8X", "ltp8xONTServiceOverrideSerial"),
        ("ELTEX-LTP8X", "ltp8xONTServiceOverrideEnabled"),
        ("ELTEX-LTP8X", "ltp8xONTServiceOverrideCustomerVID"),
        ("ELTEX-LTP8X", "ltp8xONTServiceOverrideCustomerCOS"),
        ("ELTEX-LTP8X", "ltp8xONTServicesID"),
        ("ELTEX-LTP8X", "ltp8xONTServicesDescription"),
        ("ELTEX-LTP8X", "ltp8xOLTStateSlot"),
        ("ELTEX-LTP8X", "ltp8xOLTStateDriverVersion"),
        ("ELTEX-LTP8X", "ltp8xOLTStateFirmwareVersion"),
        ("ELTEX-LTP8X", "ltp8xOLTStateHardwareVersion"),
        ("ELTEX-LTP8X", "ltp8xOLTDhcpRASlot"),
        ("ELTEX-LTP8X", "ltp8xOLTConfigActivationSlot"),
        ("ELTEX-LTP8X", "ltp8xOLTConfigActivationPeriod"),
        ("ELTEX-LTP8X", "ltp8xOLTConfigActivationCheckPassword"),
        ("ELTEX-LTP8X", "ltp8xOLTMulticastStatsSlot"),
        ("ELTEX-LTP8X", "ltp8xOLTMulticastStatsChannel"),
        ("ELTEX-LTP8X", "ltp8xOLTMulticastStatsRecordID"),
        ("ELTEX-LTP8X", "ltp8xOLTMulticastStatsONTSerial"),
        ("ELTEX-LTP8X", "ltp8xOLTMulticastStatsMulticastAddress"),
        ("ELTEX-LTP8X", "ltp8xOLTMulticastStatsStart"),
        ("ELTEX-LTP8X", "ltp8xOLTMulticastStatsStop"),
        ("ELTEX-LTP8X", "ltp8xP2PSlot"),
        ("ELTEX-LTP8X", "ltp8xP2PEnabled"),
        ("ELTEX-LTP8X", "ltp8xMIBBoundary"))
)
if mibBuilder.loadTexts:
    ltp8xObjectGroup.setStatus("current")


# Notification objects

ltp8xLoadAverageAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 1, 1)
)
ltp8xLoadAverageAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ltp8xLoadAverageAlarmTrap.setStatus(
        "current"
    )

ltp8xRAMAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 1, 2)
)
ltp8xRAMAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ltp8xRAMAlarmTrap.setStatus(
        "current"
    )

ltp8xLoginAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 1, 3)
)
ltp8xLoginAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ltp8xLoginAlarmTrap.setStatus(
        "current"
    )

ltp8xConfigSaveAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 1, 4)
)
ltp8xConfigSaveAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ltp8xConfigSaveAlarmTrap.setStatus(
        "current"
    )

ltp8xFirmwareUpdateAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 1, 5)
)
ltp8xFirmwareUpdateAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ltp8xFirmwareUpdateAlarmTrap.setStatus(
        "current"
    )

ltp8xDuplicateMacAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 1, 6)
)
ltp8xDuplicateMacAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ltp8xDuplicateMacAlarmTrap.setStatus(
        "current"
    )

ltp8xDataLinkLayerAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 1, 7)
)
ltp8xDataLinkLayerAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ltp8xDataLinkLayerAlarmTrap.setStatus(
        "current"
    )

ltp8xPhysicalLayerFlappingAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 1, 8)
)
ltp8xPhysicalLayerFlappingAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ltp8xPhysicalLayerFlappingAlarmTrap.setStatus(
        "current"
    )

ltp8xDataLinkLayerFlappingAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 1, 9)
)
ltp8xDataLinkLayerFlappingAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ltp8xDataLinkLayerFlappingAlarmTrap.setStatus(
        "current"
    )

ltp8xInterfaceCriticalLoadAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 1, 10)
)
ltp8xInterfaceCriticalLoadAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ltp8xInterfaceCriticalLoadAlarmTrap.setStatus(
        "current"
    )

ltp8xFreeSpaceAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 1, 11)
)
ltp8xFreeSpaceAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ltp8xFreeSpaceAlarmTrap.setStatus(
        "current"
    )

ltp8xTemperatureAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 1, 12)
)
ltp8xTemperatureAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ltp8xTemperatureAlarmTrap.setStatus(
        "current"
    )

ltp8xFanAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 1, 13)
)
ltp8xFanAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ltp8xFanAlarmTrap.setStatus(
        "current"
    )

ltp8xOntAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 1, 14)
)
ltp8xOntAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ltp8xOntAlarmTrap.setStatus(
        "current"
    )

ltp8xOntPhysicalAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 1, 15)
)
ltp8xOntPhysicalAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ltp8xOntPhysicalAlarmTrap.setStatus(
        "current"
    )

ltp8xOltUpdateAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 1, 16)
)
ltp8xOltUpdateAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ltp8xOltUpdateAlarmTrap.setStatus(
        "current"
    )

ltp8xOntUpdateAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 1, 17)
)
ltp8xOntUpdateAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ltp8xOntUpdateAlarmTrap.setStatus(
        "current"
    )

ltp8xChannelFlappingAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 1, 18)
)
ltp8xChannelFlappingAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ltp8xChannelFlappingAlarmTrap.setStatus(
        "current"
    )

ltp8xOntFlappingAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 1, 19)
)
ltp8xOntFlappingAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ltp8xOntFlappingAlarmTrap.setStatus(
        "current"
    )

ltp8xFileDownloadAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 1, 20)
)
ltp8xFileDownloadAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ltp8xFileDownloadAlarmTrap.setStatus(
        "current"
    )

ltp8xBatteryPowerAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 1, 21)
)
ltp8xBatteryPowerAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ltp8xBatteryPowerAlarmTrap.setStatus(
        "current"
    )

ltp8xBatteryLowAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 1, 22)
)
ltp8xBatteryLowAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ltp8xBatteryLowAlarmTrap.setStatus(
        "current"
    )

ltp8xLanLosAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 1, 23)
)
ltp8xLanLosAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ltp8xLanLosAlarmTrap.setStatus(
        "current"
    )

ltp8xOntConfigAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 1, 24)
)
ltp8xOntConfigAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ltp8xOntConfigAlarmTrap.setStatus(
        "current"
    )

ltp8xOntFirmwareDeleteAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 1, 25)
)
ltp8xOntFirmwareDeleteAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ltp8xOntFirmwareDeleteAlarmTrap.setStatus(
        "current"
    )

ltp8xLowRxPowerAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 1, 28)
)
ltp8xLowRxPowerAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ltp8xLowRxPowerAlarmTrap.setStatus(
        "current"
    )

ltp8xPowerSupplyAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 1, 30)
)
ltp8xPowerSupplyAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ltp8xPowerSupplyAlarmTrap.setStatus(
        "current"
    )

ltp8xRedundancyMasterChannelFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 1, 105)
)
ltp8xRedundancyMasterChannelFailTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ltp8xRedundancyMasterChannelFailTrap.setStatus(
        "current"
    )

ltp8xPonAlarmChannelTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 1, 213)
)
ltp8xPonAlarmChannelTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ltp8xPonAlarmChannelTrap.setStatus(
        "current"
    )

ltp8xPonAlarmONUiTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 1, 214)
)
ltp8xPonAlarmONUiTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ltp8xPonAlarmONUiTrap.setStatus(
        "current"
    )

ltp8xONTSignalDegradeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 1, 217)
)
ltp8xONTSignalDegradeTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ltp8xONTSignalDegradeTrap.setStatus(
        "current"
    )

ltp8xONTHighRecvOpticalPwrTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 1, 218)
)
ltp8xONTHighRecvOpticalPwrTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ltp8xONTHighRecvOpticalPwrTrap.setStatus(
        "current"
    )

ltp8xOLTDeviceNotWorkingTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 1, 219)
)
ltp8xOLTDeviceNotWorkingTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ltp8xOLTDeviceNotWorkingTrap.setStatus(
        "current"
    )

ltp8xChannelOntCntOverflowTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 1, 220)
)
ltp8xChannelOntCntOverflowTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ltp8xChannelOntCntOverflowTrap.setStatus(
        "current"
    )

ltp8xConfigRereadAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 1, 225)
)
ltp8xConfigRereadAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ltp8xConfigRereadAlarmTrap.setStatus(
        "current"
    )

ltp8xConfigBrokenAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 1, 227)
)
ltp8xConfigBrokenAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ltp8xConfigBrokenAlarmTrap.setStatus(
        "current"
    )

ltp8xLoadAverageOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 2, 1)
)
ltp8xLoadAverageOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ltp8xLoadAverageOkTrap.setStatus(
        "current"
    )

ltp8xRAMOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 2, 2)
)
ltp8xRAMOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ltp8xRAMOkTrap.setStatus(
        "current"
    )

ltp8xLoginOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 2, 3)
)
ltp8xLoginOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ltp8xLoginOkTrap.setStatus(
        "current"
    )

ltp8xConfigSaveOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 2, 4)
)
ltp8xConfigSaveOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ltp8xConfigSaveOkTrap.setStatus(
        "current"
    )

ltp8xFirmwareUpdateOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 2, 5)
)
ltp8xFirmwareUpdateOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ltp8xFirmwareUpdateOkTrap.setStatus(
        "current"
    )

ltp8xDuplicateMacOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 2, 6)
)
ltp8xDuplicateMacOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ltp8xDuplicateMacOkTrap.setStatus(
        "current"
    )

ltp8xDataLinkLayerOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 2, 7)
)
ltp8xDataLinkLayerOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ltp8xDataLinkLayerOkTrap.setStatus(
        "current"
    )

ltp8xPhysicalLayerFlappingOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 2, 8)
)
ltp8xPhysicalLayerFlappingOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ltp8xPhysicalLayerFlappingOkTrap.setStatus(
        "current"
    )

ltp8xDataLinkLayerFlappingOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 2, 9)
)
ltp8xDataLinkLayerFlappingOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ltp8xDataLinkLayerFlappingOkTrap.setStatus(
        "current"
    )

ltp8xInterfaceCriticalLoadOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 2, 10)
)
ltp8xInterfaceCriticalLoadOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ltp8xInterfaceCriticalLoadOkTrap.setStatus(
        "current"
    )

ltp8xFreeSpaceOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 2, 11)
)
ltp8xFreeSpaceOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ltp8xFreeSpaceOkTrap.setStatus(
        "current"
    )

ltp8xTemperatureOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 2, 12)
)
ltp8xTemperatureOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ltp8xTemperatureOkTrap.setStatus(
        "current"
    )

ltp8xFanOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 2, 13)
)
ltp8xFanOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ltp8xFanOkTrap.setStatus(
        "current"
    )

ltp8xOntOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 2, 14)
)
ltp8xOntOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ltp8xOntOkTrap.setStatus(
        "current"
    )

ltp8xOntPhysicalOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 2, 15)
)
ltp8xOntPhysicalOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ltp8xOntPhysicalOkTrap.setStatus(
        "current"
    )

ltp8xOltUpdateOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 2, 16)
)
ltp8xOltUpdateOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ltp8xOltUpdateOkTrap.setStatus(
        "current"
    )

ltp8xOntUpdateOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 2, 17)
)
ltp8xOntUpdateOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ltp8xOntUpdateOkTrap.setStatus(
        "current"
    )

ltp8xChannelFlappingOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 2, 18)
)
ltp8xChannelFlappingOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ltp8xChannelFlappingOkTrap.setStatus(
        "current"
    )

ltp8xOntFlappingOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 2, 19)
)
ltp8xOntFlappingOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ltp8xOntFlappingOkTrap.setStatus(
        "current"
    )

ltp8xFileDownloadOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 2, 20)
)
ltp8xFileDownloadOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ltp8xFileDownloadOkTrap.setStatus(
        "current"
    )

ltp8xBatteryPowerOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 2, 21)
)
ltp8xBatteryPowerOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ltp8xBatteryPowerOkTrap.setStatus(
        "current"
    )

ltp8xBatteryLowOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 2, 22)
)
ltp8xBatteryLowOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ltp8xBatteryLowOkTrap.setStatus(
        "current"
    )

ltp8xLanLosOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 2, 23)
)
ltp8xLanLosOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ltp8xLanLosOkTrap.setStatus(
        "current"
    )

ltp8xOntConfigOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 2, 24)
)
ltp8xOntConfigOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ltp8xOntConfigOkTrap.setStatus(
        "current"
    )

ltp8xOntFirmwareDeleteOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 2, 25)
)
ltp8xOntFirmwareDeleteOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ltp8xOntFirmwareDeleteOkTrap.setStatus(
        "current"
    )

ltp8xLowRxPowerOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 2, 28)
)
ltp8xLowRxPowerOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ltp8xLowRxPowerOkTrap.setStatus(
        "current"
    )

ltp8xPowerSupplyOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 2, 30)
)
ltp8xPowerSupplyOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ltp8xPowerSupplyOkTrap.setStatus(
        "current"
    )

ltp8xLogoutTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 2, 102)
)
ltp8xLogoutTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ltp8xLogoutTrap.setStatus(
        "current"
    )

ltp8xOntDyingGaspTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 2, 103)
)
ltp8xOntDyingGaspTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ltp8xOntDyingGaspTrap.setStatus(
        "current"
    )

ltp8xRedundantChannelSwitchTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 2, 104)
)
ltp8xRedundantChannelSwitchTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ltp8xRedundantChannelSwitchTrap.setStatus(
        "current"
    )

ltp8xONTREITrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 2, 106)
)
ltp8xONTREITrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ltp8xONTREITrap.setStatus(
        "current"
    )

ltp8xONTPowerOffTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 2, 107)
)
ltp8xONTPowerOffTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ltp8xONTPowerOffTrap.setStatus(
        "current"
    )

ltp8xConfigChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 2, 200)
)
ltp8xConfigChangeTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ltp8xConfigChangeTrap.setStatus(
        "current"
    )

ltp8xONTStateChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 2, 210)
)
ltp8xONTStateChangeTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ltp8xONTStateChangeTrap.setStatus(
        "current"
    )

ltp8xONTConfigChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 2, 211)
)
ltp8xONTConfigChangeTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ltp8xONTConfigChangeTrap.setStatus(
        "current"
    )

ltp8xChannelStateChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 2, 212)
)
ltp8xChannelStateChangeTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ltp8xChannelStateChangeTrap.setStatus(
        "current"
    )

ltp8xOLTDeviceResetTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 2, 216)
)
ltp8xOLTDeviceResetTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ltp8xOLTDeviceResetTrap.setStatus(
        "current"
    )

ltp8xOLTDeviceWorkingTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 2, 219)
)
ltp8xOLTDeviceWorkingTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ltp8xOLTDeviceWorkingTrap.setStatus(
        "current"
    )

ltp8xChannelOntCntOverflowOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 2, 220)
)
ltp8xChannelOntCntOverflowOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ltp8xChannelOntCntOverflowOkTrap.setStatus(
        "current"
    )

ltp8xConfigRereadOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 2, 225)
)
ltp8xConfigRereadOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ltp8xConfigRereadOkTrap.setStatus(
        "current"
    )

ltp8xRSSIUpdateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 2, 226)
)
ltp8xRSSIUpdateTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ltp8xRSSIUpdateTrap.setStatus(
        "current"
    )

plc8LoadAverageAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 3, 1)
)
plc8LoadAverageAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    plc8LoadAverageAlarmTrap.setStatus(
        "current"
    )

plc8RAMAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 3, 2)
)
plc8RAMAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    plc8RAMAlarmTrap.setStatus(
        "current"
    )

plc8LoginAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 3, 3)
)
plc8LoginAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    plc8LoginAlarmTrap.setStatus(
        "current"
    )

plc8ConfigSaveAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 3, 4)
)
plc8ConfigSaveAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    plc8ConfigSaveAlarmTrap.setStatus(
        "current"
    )

plc8FirmwareUpdateAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 3, 5)
)
plc8FirmwareUpdateAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    plc8FirmwareUpdateAlarmTrap.setStatus(
        "current"
    )

plc8DuplicateMacAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 3, 6)
)
plc8DuplicateMacAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    plc8DuplicateMacAlarmTrap.setStatus(
        "current"
    )

plc8DataLinkLayerAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 3, 7)
)
plc8DataLinkLayerAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    plc8DataLinkLayerAlarmTrap.setStatus(
        "current"
    )

plc8PhysicalLayerFlappingAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 3, 8)
)
plc8PhysicalLayerFlappingAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    plc8PhysicalLayerFlappingAlarmTrap.setStatus(
        "current"
    )

plc8DataLinkLayerFlappingAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 3, 9)
)
plc8DataLinkLayerFlappingAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    plc8DataLinkLayerFlappingAlarmTrap.setStatus(
        "current"
    )

plc8InterfaceCriticalLoadAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 3, 10)
)
plc8InterfaceCriticalLoadAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    plc8InterfaceCriticalLoadAlarmTrap.setStatus(
        "current"
    )

plc8FreeSpaceAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 3, 11)
)
plc8FreeSpaceAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    plc8FreeSpaceAlarmTrap.setStatus(
        "current"
    )

plc8TemperatureAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 3, 12)
)
plc8TemperatureAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    plc8TemperatureAlarmTrap.setStatus(
        "current"
    )

plc8FanAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 3, 13)
)
plc8FanAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    plc8FanAlarmTrap.setStatus(
        "current"
    )

plc8OntAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 3, 14)
)
plc8OntAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    plc8OntAlarmTrap.setStatus(
        "current"
    )

plc8OntPhysicalAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 3, 15)
)
plc8OntPhysicalAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    plc8OntPhysicalAlarmTrap.setStatus(
        "current"
    )

plc8FileDownloadAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 3, 20)
)
plc8FileDownloadAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    plc8FileDownloadAlarmTrap.setStatus(
        "current"
    )

plc8BatteryPowerAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 3, 21)
)
plc8BatteryPowerAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    plc8BatteryPowerAlarmTrap.setStatus(
        "current"
    )

plc8BatteryLowAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 3, 22)
)
plc8BatteryLowAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    plc8BatteryLowAlarmTrap.setStatus(
        "current"
    )

plc8LanLosAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 3, 23)
)
plc8LanLosAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    plc8LanLosAlarmTrap.setStatus(
        "current"
    )

plc8OntConfigAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 3, 24)
)
plc8OntConfigAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    plc8OntConfigAlarmTrap.setStatus(
        "current"
    )

plc8LowRxPowerAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 3, 28)
)
plc8LowRxPowerAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    plc8LowRxPowerAlarmTrap.setStatus(
        "current"
    )

plc8RedundancyMasterChannelFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 3, 105)
)
plc8RedundancyMasterChannelFailTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    plc8RedundancyMasterChannelFailTrap.setStatus(
        "current"
    )

plc8PonAlarmChannelTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 3, 213)
)
plc8PonAlarmChannelTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    plc8PonAlarmChannelTrap.setStatus(
        "current"
    )

plc8PonAlarmONUiTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 3, 214)
)
plc8PonAlarmONUiTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    plc8PonAlarmONUiTrap.setStatus(
        "current"
    )

plc8ONTSignalDegradeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 3, 217)
)
plc8ONTSignalDegradeTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    plc8ONTSignalDegradeTrap.setStatus(
        "current"
    )

plc8ONTHighRecvOpticalPwrTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 3, 218)
)
plc8ONTHighRecvOpticalPwrTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    plc8ONTHighRecvOpticalPwrTrap.setStatus(
        "current"
    )

plc8OLTDeviceNotWorkingTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 3, 219)
)
plc8OLTDeviceNotWorkingTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    plc8OLTDeviceNotWorkingTrap.setStatus(
        "current"
    )

plc8ChannelOntCntOverflowTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 3, 220)
)
plc8ChannelOntCntOverflowTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    plc8ChannelOntCntOverflowTrap.setStatus(
        "current"
    )

plc8LoadAverageOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 4, 1)
)
plc8LoadAverageOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    plc8LoadAverageOkTrap.setStatus(
        "current"
    )

plc8RAMOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 4, 2)
)
plc8RAMOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    plc8RAMOkTrap.setStatus(
        "current"
    )

plc8LoginOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 4, 3)
)
plc8LoginOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    plc8LoginOkTrap.setStatus(
        "current"
    )

plc8ConfigSaveOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 4, 4)
)
plc8ConfigSaveOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    plc8ConfigSaveOkTrap.setStatus(
        "current"
    )

plc8FirmwareUpdateOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 4, 5)
)
plc8FirmwareUpdateOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    plc8FirmwareUpdateOkTrap.setStatus(
        "current"
    )

plc8DuplicateMacOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 4, 6)
)
plc8DuplicateMacOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    plc8DuplicateMacOkTrap.setStatus(
        "current"
    )

plc8DataLinkLayerOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 4, 7)
)
plc8DataLinkLayerOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    plc8DataLinkLayerOkTrap.setStatus(
        "current"
    )

plc8PhysicalLayerFlappingOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 4, 8)
)
plc8PhysicalLayerFlappingOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    plc8PhysicalLayerFlappingOkTrap.setStatus(
        "current"
    )

plc8DataLinkLayerFlappingOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 4, 9)
)
plc8DataLinkLayerFlappingOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    plc8DataLinkLayerFlappingOkTrap.setStatus(
        "current"
    )

plc8InterfaceCriticalLoadOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 4, 10)
)
plc8InterfaceCriticalLoadOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    plc8InterfaceCriticalLoadOkTrap.setStatus(
        "current"
    )

plc8FreeSpaceOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 4, 11)
)
plc8FreeSpaceOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    plc8FreeSpaceOkTrap.setStatus(
        "current"
    )

plc8TemperatureOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 4, 12)
)
plc8TemperatureOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    plc8TemperatureOkTrap.setStatus(
        "current"
    )

plc8FanOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 4, 13)
)
plc8FanOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    plc8FanOkTrap.setStatus(
        "current"
    )

plc8OntOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 4, 14)
)
plc8OntOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    plc8OntOkTrap.setStatus(
        "current"
    )

plc8OntPhysicalOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 4, 15)
)
plc8OntPhysicalOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    plc8OntPhysicalOkTrap.setStatus(
        "current"
    )

plc8FileDownloadOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 4, 20)
)
plc8FileDownloadOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    plc8FileDownloadOkTrap.setStatus(
        "current"
    )

plc8BatteryPowerOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 4, 21)
)
plc8BatteryPowerOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    plc8BatteryPowerOkTrap.setStatus(
        "current"
    )

plc8BatteryLowOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 4, 22)
)
plc8BatteryLowOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    plc8BatteryLowOkTrap.setStatus(
        "current"
    )

plc8LanLosOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 4, 23)
)
plc8LanLosOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    plc8LanLosOkTrap.setStatus(
        "current"
    )

plc8OntConfigOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 4, 24)
)
plc8OntConfigOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    plc8OntConfigOkTrap.setStatus(
        "current"
    )

plc8LowRxPowerOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 4, 28)
)
plc8LowRxPowerOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    plc8LowRxPowerOkTrap.setStatus(
        "current"
    )

plc8OntDyingGaspTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 4, 103)
)
plc8OntDyingGaspTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    plc8OntDyingGaspTrap.setStatus(
        "current"
    )

plc8RedundantChannelSwitchTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 4, 104)
)
plc8RedundantChannelSwitchTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    plc8RedundantChannelSwitchTrap.setStatus(
        "current"
    )

plc8ONTREITrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 4, 106)
)
plc8ONTREITrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    plc8ONTREITrap.setStatus(
        "current"
    )

plc8ONTPowerOffTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 4, 107)
)
plc8ONTPowerOffTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    plc8ONTPowerOffTrap.setStatus(
        "current"
    )

plc8ConfigChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 4, 200)
)
plc8ConfigChangeTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    plc8ConfigChangeTrap.setStatus(
        "current"
    )

plc8ONTStateChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 4, 210)
)
plc8ONTStateChangeTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    plc8ONTStateChangeTrap.setStatus(
        "current"
    )

plc8ONTConfigChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 4, 211)
)
plc8ONTConfigChangeTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    plc8ONTConfigChangeTrap.setStatus(
        "current"
    )

plc8ChannelStateChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 4, 212)
)
plc8ChannelStateChangeTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    plc8ChannelStateChangeTrap.setStatus(
        "current"
    )

plc8OLTDeviceResetTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 4, 216)
)
plc8OLTDeviceResetTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    plc8OLTDeviceResetTrap.setStatus(
        "current"
    )

plc8OLTDeviceWorkingTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 4, 219)
)
plc8OLTDeviceWorkingTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    plc8OLTDeviceWorkingTrap.setStatus(
        "current"
    )

plc8ChannelOntCntOverflowOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 4, 220)
)
plc8ChannelOntCntOverflowOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    plc8ChannelOntCntOverflowOkTrap.setStatus(
        "current"
    )

plc8RSSIUpdateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 100, 4, 226)
)
plc8RSSIUpdateTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    plc8RSSIUpdateTrap.setStatus(
        "current"
    )


# Notifications groups

ltp8xTrapsObjectGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 201)
)
ltp8xTrapsObjectGroup.setObjects(
      *(("ELTEX-LTP8X", "ltp8xLoadAverageAlarmTrap"),
        ("ELTEX-LTP8X", "ltp8xRAMAlarmTrap"),
        ("ELTEX-LTP8X", "ltp8xLoginAlarmTrap"),
        ("ELTEX-LTP8X", "ltp8xConfigSaveAlarmTrap"),
        ("ELTEX-LTP8X", "ltp8xFirmwareUpdateAlarmTrap"),
        ("ELTEX-LTP8X", "ltp8xDuplicateMacAlarmTrap"),
        ("ELTEX-LTP8X", "ltp8xDataLinkLayerAlarmTrap"),
        ("ELTEX-LTP8X", "ltp8xPhysicalLayerFlappingAlarmTrap"),
        ("ELTEX-LTP8X", "ltp8xDataLinkLayerFlappingAlarmTrap"),
        ("ELTEX-LTP8X", "ltp8xInterfaceCriticalLoadAlarmTrap"),
        ("ELTEX-LTP8X", "ltp8xFreeSpaceAlarmTrap"),
        ("ELTEX-LTP8X", "ltp8xTemperatureAlarmTrap"),
        ("ELTEX-LTP8X", "ltp8xFanAlarmTrap"),
        ("ELTEX-LTP8X", "ltp8xOntAlarmTrap"),
        ("ELTEX-LTP8X", "ltp8xOntPhysicalAlarmTrap"),
        ("ELTEX-LTP8X", "ltp8xOltUpdateAlarmTrap"),
        ("ELTEX-LTP8X", "ltp8xOntUpdateAlarmTrap"),
        ("ELTEX-LTP8X", "ltp8xOntFlappingAlarmTrap"),
        ("ELTEX-LTP8X", "ltp8xLoadAverageOkTrap"),
        ("ELTEX-LTP8X", "ltp8xRAMOkTrap"),
        ("ELTEX-LTP8X", "ltp8xLoginOkTrap"),
        ("ELTEX-LTP8X", "ltp8xConfigSaveOkTrap"),
        ("ELTEX-LTP8X", "ltp8xFirmwareUpdateOkTrap"),
        ("ELTEX-LTP8X", "ltp8xDuplicateMacOkTrap"),
        ("ELTEX-LTP8X", "ltp8xDataLinkLayerOkTrap"),
        ("ELTEX-LTP8X", "ltp8xPhysicalLayerFlappingOkTrap"),
        ("ELTEX-LTP8X", "ltp8xDataLinkLayerFlappingOkTrap"),
        ("ELTEX-LTP8X", "ltp8xInterfaceCriticalLoadOkTrap"),
        ("ELTEX-LTP8X", "ltp8xFreeSpaceOkTrap"),
        ("ELTEX-LTP8X", "ltp8xTemperatureOkTrap"),
        ("ELTEX-LTP8X", "ltp8xFanOkTrap"),
        ("ELTEX-LTP8X", "ltp8xOntOkTrap"),
        ("ELTEX-LTP8X", "ltp8xOntPhysicalOkTrap"),
        ("ELTEX-LTP8X", "ltp8xOltUpdateOkTrap"),
        ("ELTEX-LTP8X", "ltp8xOntUpdateOkTrap"),
        ("ELTEX-LTP8X", "ltp8xOntFlappingOkTrap"),
        ("ELTEX-LTP8X", "ltp8xConfigChangeTrap"),
        ("ELTEX-LTP8X", "plc8LoadAverageAlarmTrap"),
        ("ELTEX-LTP8X", "plc8RAMAlarmTrap"),
        ("ELTEX-LTP8X", "plc8LoginAlarmTrap"),
        ("ELTEX-LTP8X", "plc8ConfigSaveAlarmTrap"),
        ("ELTEX-LTP8X", "plc8FirmwareUpdateAlarmTrap"),
        ("ELTEX-LTP8X", "plc8DuplicateMacAlarmTrap"),
        ("ELTEX-LTP8X", "plc8DataLinkLayerAlarmTrap"),
        ("ELTEX-LTP8X", "plc8PhysicalLayerFlappingAlarmTrap"),
        ("ELTEX-LTP8X", "plc8DataLinkLayerFlappingAlarmTrap"),
        ("ELTEX-LTP8X", "plc8InterfaceCriticalLoadAlarmTrap"),
        ("ELTEX-LTP8X", "plc8FreeSpaceAlarmTrap"),
        ("ELTEX-LTP8X", "plc8TemperatureAlarmTrap"),
        ("ELTEX-LTP8X", "plc8FanAlarmTrap"),
        ("ELTEX-LTP8X", "plc8OntAlarmTrap"),
        ("ELTEX-LTP8X", "plc8OntPhysicalAlarmTrap"),
        ("ELTEX-LTP8X", "plc8LoadAverageOkTrap"),
        ("ELTEX-LTP8X", "plc8RAMOkTrap"),
        ("ELTEX-LTP8X", "plc8LoginOkTrap"),
        ("ELTEX-LTP8X", "plc8ConfigSaveOkTrap"),
        ("ELTEX-LTP8X", "plc8FirmwareUpdateOkTrap"),
        ("ELTEX-LTP8X", "plc8DuplicateMacOkTrap"),
        ("ELTEX-LTP8X", "plc8DataLinkLayerOkTrap"),
        ("ELTEX-LTP8X", "plc8PhysicalLayerFlappingOkTrap"),
        ("ELTEX-LTP8X", "plc8DataLinkLayerFlappingOkTrap"),
        ("ELTEX-LTP8X", "plc8InterfaceCriticalLoadOkTrap"),
        ("ELTEX-LTP8X", "plc8FreeSpaceOkTrap"),
        ("ELTEX-LTP8X", "plc8TemperatureOkTrap"),
        ("ELTEX-LTP8X", "plc8FanOkTrap"),
        ("ELTEX-LTP8X", "plc8OntAlarmTrap"),
        ("ELTEX-LTP8X", "plc8OntPhysicalAlarmTrap"),
        ("ELTEX-LTP8X", "plc8ConfigChangeTrap"))
)
if mibBuilder.loadTexts:
    ltp8xTrapsObjectGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-LTP8X",
    **{"ONTSerial": ONTSerial,
       "LTPONTState": LTPONTState,
       "DBAServiceClass": DBAServiceClass,
       "DBAStatusReport": DBAStatusReport,
       "AddressEntryType": AddressEntryType,
       "VideoRxPowerConv": VideoRxPowerConv,
       "ltp8x": ltp8x,
       "ltp8xPONChannels": ltp8xPONChannels,
       "ltp8xPONChannelStateTable": ltp8xPONChannelStateTable,
       "ltp8xPONChannelStateEntry": ltp8xPONChannelStateEntry,
       "ltp8xPONChannelSlot": ltp8xPONChannelSlot,
       "ltp8xPONChannelID": ltp8xPONChannelID,
       "ltp8xPONChannelState": ltp8xPONChannelState,
       "ltp8xPONChannelONTCount": ltp8xPONChannelONTCount,
       "ltp8xPONChannelEnabled": ltp8xPONChannelEnabled,
       "ltp8xPONChannelSFPVendor": ltp8xPONChannelSFPVendor,
       "ltp8xPONChannelSFPProductNumber": ltp8xPONChannelSFPProductNumber,
       "ltp8xPONChannelSFPRevision": ltp8xPONChannelSFPRevision,
       "ltp8xPONChannelTxPower": ltp8xPONChannelTxPower,
       "ltp8xPONChannelSFPTemperature": ltp8xPONChannelSFPTemperature,
       "ltp8xPONChannelSFPVoltage": ltp8xPONChannelSFPVoltage,
       "ltp8xPONChannelSFPTxBiasCurrent": ltp8xPONChannelSFPTxBiasCurrent,
       "ltp8xPONChannelReconfigure": ltp8xPONChannelReconfigure,
       "ltp8xPONChannelResetCounters": ltp8xPONChannelResetCounters,
       "ltp8xPONChannelActModeTable": ltp8xPONChannelActModeTable,
       "ltp8xPONChannelActModeEntry": ltp8xPONChannelActModeEntry,
       "ltp8xPONChannelActModeSlot": ltp8xPONChannelActModeSlot,
       "ltp8xPONChannelActModeChannel": ltp8xPONChannelActModeChannel,
       "ltp8xPONChannelActModeHostControlledLumpedSN": ltp8xPONChannelActModeHostControlledLumpedSN,
       "ltp8xPONChannelAddressTable": ltp8xPONChannelAddressTable,
       "ltp8xPONChannelAddressEntry": ltp8xPONChannelAddressEntry,
       "ltp8xPONChannelAddressSlot": ltp8xPONChannelAddressSlot,
       "ltp8xPONChannelAddressChannel": ltp8xPONChannelAddressChannel,
       "ltp8xPONChannelAddressEntryID": ltp8xPONChannelAddressEntryID,
       "ltp8xPONChannelAddressONTSerial": ltp8xPONChannelAddressONTSerial,
       "ltp8xPONChannelAddressONTID": ltp8xPONChannelAddressONTID,
       "ltp8xPONChannelAddressPriority": ltp8xPONChannelAddressPriority,
       "ltp8xPONChannelAddressCVID": ltp8xPONChannelAddressCVID,
       "ltp8xPONChannelAddressSVID": ltp8xPONChannelAddressSVID,
       "ltp8xPONChannelAddressMacAddress": ltp8xPONChannelAddressMacAddress,
       "ltp8xPONChannelAddressCPUDestined": ltp8xPONChannelAddressCPUDestined,
       "ltp8xPONChannelAddressDatapathForwarding": ltp8xPONChannelAddressDatapathForwarding,
       "ltp8xPONChannelAddressUniPort": ltp8xPONChannelAddressUniPort,
       "ltp8xPONChannelAddressEntryType": ltp8xPONChannelAddressEntryType,
       "ltp8xPONChannelAddressAge": ltp8xPONChannelAddressAge,
       "ltp8xPONChannelAddressGEMPortId": ltp8xPONChannelAddressGEMPortId,
       "ltp8xPONChannelAddressUVID": ltp8xPONChannelAddressUVID,
       "ltp8xONT": ltp8xONT,
       "ltp8xONTStateTable": ltp8xONTStateTable,
       "ltp8xONTStateEntry": ltp8xONTStateEntry,
       "ltp8xONTSlot": ltp8xONTSlot,
       "ltp8xONTSerial": ltp8xONTSerial,
       "ltp8xONTStateChannel": ltp8xONTStateChannel,
       "ltp8xONTStateID": ltp8xONTStateID,
       "ltp8xONTStateState": ltp8xONTStateState,
       "ltp8xONTStateEqualizationDelay": ltp8xONTStateEqualizationDelay,
       "ltp8xONTStateFecState": ltp8xONTStateFecState,
       "ltp8xONTStateEncryptionKey": ltp8xONTStateEncryptionKey,
       "ltp8xONTStateOMCIPortId": ltp8xONTStateOMCIPortId,
       "ltp8xONTStateDistance": ltp8xONTStateDistance,
       "ltp8xONTStateRSSI": ltp8xONTStateRSSI,
       "ltp8xONTStateEquipmentID": ltp8xONTStateEquipmentID,
       "ltp8xONTStateTxPower": ltp8xONTStateTxPower,
       "ltp8xONTStateRxPower": ltp8xONTStateRxPower,
       "ltp8xONTStateTemperature": ltp8xONTStateTemperature,
       "ltp8xONTStateVideoRxPower": ltp8xONTStateVideoRxPower,
       "ltp8xONTStateVersion": ltp8xONTStateVersion,
       "ltp8xONTStateHWVersion": ltp8xONTStateHWVersion,
       "ltp8xONTStateReconfigure": ltp8xONTStateReconfigure,
       "ltp8xONTStateUpdateFirmware": ltp8xONTStateUpdateFirmware,
       "ltp8xONTStateReset": ltp8xONTStateReset,
       "ltp8xONTStateResetToDefaults": ltp8xONTStateResetToDefaults,
       "ltp8xONTStateRFPortOn": ltp8xONTStateRFPortOn,
       "ltp8xONTStateLaserVoltage": ltp8xONTStateLaserVoltage,
       "ltp8xONTStateLaserBiasCurrent": ltp8xONTStateLaserBiasCurrent,
       "ltp8xONTUNIPortsStateTable": ltp8xONTUNIPortsStateTable,
       "ltp8xONTUNIPortsStateEntry": ltp8xONTUNIPortsStateEntry,
       "ltp8xONTUNIPortsStateSlot": ltp8xONTUNIPortsStateSlot,
       "ltp8xONTUNIPortsStateSerial": ltp8xONTUNIPortsStateSerial,
       "ltp8xONTUNIPortsStatePort": ltp8xONTUNIPortsStatePort,
       "ltp8xONTUNIPortsStateAvailable": ltp8xONTUNIPortsStateAvailable,
       "ltp8xONTUNIPortsStateLinkUp": ltp8xONTUNIPortsStateLinkUp,
       "ltp8xONTUNIPortsStateSpeed": ltp8xONTUNIPortsStateSpeed,
       "ltp8xONTUNIPortsStateDuplex": ltp8xONTUNIPortsStateDuplex,
       "ltp8xONTStatistics": ltp8xONTStatistics,
       "ltp8xONTWANCountersTable": ltp8xONTWANCountersTable,
       "ltp8xONTWANCountersEntry": ltp8xONTWANCountersEntry,
       "ltp8xONTWANCountersSlot": ltp8xONTWANCountersSlot,
       "ltp8xONTWANCountersSerial": ltp8xONTWANCountersSerial,
       "ltp8xONTWANCountersCrossConnect": ltp8xONTWANCountersCrossConnect,
       "ltp8xONTWANCountersRXDrops": ltp8xONTWANCountersRXDrops,
       "ltp8xONTWANCountersRXErrors": ltp8xONTWANCountersRXErrors,
       "ltp8xONTWANCountersRecvBytes": ltp8xONTWANCountersRecvBytes,
       "ltp8xONTWANCountersRecvFrames": ltp8xONTWANCountersRecvFrames,
       "ltp8xONTWANCountersTXDrops": ltp8xONTWANCountersTXDrops,
       "ltp8xONTWANCountersTXErrors": ltp8xONTWANCountersTXErrors,
       "ltp8xONTWANCountersTrmtBytes": ltp8xONTWANCountersTrmtBytes,
       "ltp8xONTWANCountersTrmtFrames": ltp8xONTWANCountersTrmtFrames,
       "ltp8xONTGEMPortCountersTable": ltp8xONTGEMPortCountersTable,
       "ltp8xONTGEMPortCountersEntry": ltp8xONTGEMPortCountersEntry,
       "ltp8xONTGEMPortCountersSlot": ltp8xONTGEMPortCountersSlot,
       "ltp8xONTGEMPortCountersSerial": ltp8xONTGEMPortCountersSerial,
       "ltp8xONTGEMPortCountersCrossConnect": ltp8xONTGEMPortCountersCrossConnect,
       "ltp8xONTGEMPortCountersDSFinishedIntervals": ltp8xONTGEMPortCountersDSFinishedIntervals,
       "ltp8xONTGEMPortCountersDSGEMFrames": ltp8xONTGEMPortCountersDSGEMFrames,
       "ltp8xONTGEMPortCountersDSPayloadBytesLOW": ltp8xONTGEMPortCountersDSPayloadBytesLOW,
       "ltp8xONTGEMPortCountersDSPayloadBytesHIGH": ltp8xONTGEMPortCountersDSPayloadBytesHIGH,
       "ltp8xONTGEMPortCountersUSFinishedIntervals": ltp8xONTGEMPortCountersUSFinishedIntervals,
       "ltp8xONTGEMPortCountersUSGEMFrames": ltp8xONTGEMPortCountersUSGEMFrames,
       "ltp8xONTGEMPortCountersUSPayloadBytesLOW": ltp8xONTGEMPortCountersUSPayloadBytesLOW,
       "ltp8xONTGEMPortCountersUSPayloadBytesHIGH": ltp8xONTGEMPortCountersUSPayloadBytesHIGH,
       "ltp8xONTEthPerformMonitoringHistDataTable": ltp8xONTEthPerformMonitoringHistDataTable,
       "ltp8xONTEthPerformMonitoringHistDataEntry": ltp8xONTEthPerformMonitoringHistDataEntry,
       "ltp8xONTEthPerformMonitoringHistDataSlot": ltp8xONTEthPerformMonitoringHistDataSlot,
       "ltp8xONTEthPerformMonitoringHistDataSerial": ltp8xONTEthPerformMonitoringHistDataSerial,
       "ltp8xONTEthPerformMonitoringHistDataPort": ltp8xONTEthPerformMonitoringHistDataPort,
       "ltp8xONTEthPerformMonitoringHistDataCounterID": ltp8xONTEthPerformMonitoringHistDataCounterID,
       "ltp8xONTEthPerformMonitoringHistDataCounterName": ltp8xONTEthPerformMonitoringHistDataCounterName,
       "ltp8xONTEthPerformMonitoringHistDataCounterValue": ltp8xONTEthPerformMonitoringHistDataCounterValue,
       "ltp8xONTGalEthPerformMonitoringHistDataTable": ltp8xONTGalEthPerformMonitoringHistDataTable,
       "ltp8xONTGalEthPerformMonitoringHistDataEntry": ltp8xONTGalEthPerformMonitoringHistDataEntry,
       "ltp8xONTGalEthPerformMonitoringHistDataSlot": ltp8xONTGalEthPerformMonitoringHistDataSlot,
       "ltp8xONTGalEthPerformMonitoringHistDataSerial": ltp8xONTGalEthPerformMonitoringHistDataSerial,
       "ltp8xONTGalEthPerformMonitoringHistDataCrossConnect": ltp8xONTGalEthPerformMonitoringHistDataCrossConnect,
       "ltp8xONTGalEthPerformMonitoringHistDataCounterID": ltp8xONTGalEthPerformMonitoringHistDataCounterID,
       "ltp8xONTGalEthPerformMonitoringHistDataCounterName": ltp8xONTGalEthPerformMonitoringHistDataCounterName,
       "ltp8xONTGalEthPerformMonitoringHistDataCounterValue": ltp8xONTGalEthPerformMonitoringHistDataCounterValue,
       "ltp8xONTFecPerformMonitoringHistDataTable": ltp8xONTFecPerformMonitoringHistDataTable,
       "ltp8xONTFecPerformMonitoringHistDataEntry": ltp8xONTFecPerformMonitoringHistDataEntry,
       "ltp8xONTFecPerformMonitoringHistDataSlot": ltp8xONTFecPerformMonitoringHistDataSlot,
       "ltp8xONTFecPerformMonitoringHistDataSerial": ltp8xONTFecPerformMonitoringHistDataSerial,
       "ltp8xONTFecPerformMonitoringHistDataDummyIndex": ltp8xONTFecPerformMonitoringHistDataDummyIndex,
       "ltp8xONTFecPerformMonitoringHistDataCounterID": ltp8xONTFecPerformMonitoringHistDataCounterID,
       "ltp8xONTFecPerformMonitoringHistDataCounterName": ltp8xONTFecPerformMonitoringHistDataCounterName,
       "ltp8xONTFecPerformMonitoringHistDataCounterValue": ltp8xONTFecPerformMonitoringHistDataCounterValue,
       "ltp8xONTEthFrameDSPerformMonitoringHistDataTable": ltp8xONTEthFrameDSPerformMonitoringHistDataTable,
       "ltp8xONTEthFrameDSPerformMonitoringHistDataEntry": ltp8xONTEthFrameDSPerformMonitoringHistDataEntry,
       "ltp8xONTEthFrameDSPerformMonitoringHistDataSlot": ltp8xONTEthFrameDSPerformMonitoringHistDataSlot,
       "ltp8xONTEthFrameDSPerformMonitoringHistDataSerial": ltp8xONTEthFrameDSPerformMonitoringHistDataSerial,
       "ltp8xONTEthFrameDSPerformMonitoringHistDataPort": ltp8xONTEthFrameDSPerformMonitoringHistDataPort,
       "ltp8xONTEthFrameDSPerformMonitoringHistDataCounterID": ltp8xONTEthFrameDSPerformMonitoringHistDataCounterID,
       "ltp8xONTEthFrameDSPerformMonitoringHistDataCounterName": ltp8xONTEthFrameDSPerformMonitoringHistDataCounterName,
       "ltp8xONTEthFrameDSPerformMonitoringHistDataCounterValue": ltp8xONTEthFrameDSPerformMonitoringHistDataCounterValue,
       "ltp8xONTEthFrameUSPerformMonitoringHistDataTable": ltp8xONTEthFrameUSPerformMonitoringHistDataTable,
       "ltp8xONTEthFrameUSPerformMonitoringHistDataEntry": ltp8xONTEthFrameUSPerformMonitoringHistDataEntry,
       "ltp8xONTEthFrameUSPerformMonitoringHistDataSlot": ltp8xONTEthFrameUSPerformMonitoringHistDataSlot,
       "ltp8xONTEthFrameUSPerformMonitoringHistDataSerial": ltp8xONTEthFrameUSPerformMonitoringHistDataSerial,
       "ltp8xONTEthFrameUSPerformMonitoringHistDataPort": ltp8xONTEthFrameUSPerformMonitoringHistDataPort,
       "ltp8xONTEthFrameUSPerformMonitoringHistDataCounterID": ltp8xONTEthFrameUSPerformMonitoringHistDataCounterID,
       "ltp8xONTEthFrameUSPerformMonitoringHistDataCounterName": ltp8xONTEthFrameUSPerformMonitoringHistDataCounterName,
       "ltp8xONTEthFrameUSPerformMonitoringHistDataCounterValue": ltp8xONTEthFrameUSPerformMonitoringHistDataCounterValue,
       "ltp8xONTGEMPortPerformMonitoringDSTable": ltp8xONTGEMPortPerformMonitoringDSTable,
       "ltp8xONTGEMPortPerformMonitoringDSEntry": ltp8xONTGEMPortPerformMonitoringDSEntry,
       "ltp8xONTGEMPortPerformMonitoringDSSlot": ltp8xONTGEMPortPerformMonitoringDSSlot,
       "ltp8xONTGEMPortPerformMonitoringDSSerial": ltp8xONTGEMPortPerformMonitoringDSSerial,
       "ltp8xONTGEMPortPerformMonitoringDSCrossConnect": ltp8xONTGEMPortPerformMonitoringDSCrossConnect,
       "ltp8xONTGEMPortPerformMonitoringDSCounterID": ltp8xONTGEMPortPerformMonitoringDSCounterID,
       "ltp8xONTGEMPortPerformMonitoringDSCounterName": ltp8xONTGEMPortPerformMonitoringDSCounterName,
       "ltp8xONTGEMPortPerformMonitoringDSCounterValue": ltp8xONTGEMPortPerformMonitoringDSCounterValue,
       "ltp8xONTGEMPortPerformMonitoringUSTable": ltp8xONTGEMPortPerformMonitoringUSTable,
       "ltp8xONTGEMPortPerformMonitoringUSEntry": ltp8xONTGEMPortPerformMonitoringUSEntry,
       "ltp8xONTGEMPortPerformMonitoringUSSlot": ltp8xONTGEMPortPerformMonitoringUSSlot,
       "ltp8xONTGEMPortPerformMonitoringUSSerial": ltp8xONTGEMPortPerformMonitoringUSSerial,
       "ltp8xONTGEMPortPerformMonitoringUSCrossConnect": ltp8xONTGEMPortPerformMonitoringUSCrossConnect,
       "ltp8xONTGEMPortPerformMonitoringUSCounterID": ltp8xONTGEMPortPerformMonitoringUSCounterID,
       "ltp8xONTGEMPortPerformMonitoringUSCounterName": ltp8xONTGEMPortPerformMonitoringUSCounterName,
       "ltp8xONTGEMPortPerformMonitoringUSCounterValue": ltp8xONTGEMPortPerformMonitoringUSCounterValue,
       "ltp8xONTCrossConnectDSTable": ltp8xONTCrossConnectDSTable,
       "ltp8xONTCrossConnectDSEntry": ltp8xONTCrossConnectDSEntry,
       "ltp8xONTCrossConnectDSSlot": ltp8xONTCrossConnectDSSlot,
       "ltp8xONTCrossConnectDSSerial": ltp8xONTCrossConnectDSSerial,
       "ltp8xONTCrossConnectDSCrossConnect": ltp8xONTCrossConnectDSCrossConnect,
       "ltp8xONTCrossConnectDSCounterID": ltp8xONTCrossConnectDSCounterID,
       "ltp8xONTCrossConnectDSCounterName": ltp8xONTCrossConnectDSCounterName,
       "ltp8xONTCrossConnectDSCounterValue": ltp8xONTCrossConnectDSCounterValue,
       "ltp8xONTCrossConnectUSTable": ltp8xONTCrossConnectUSTable,
       "ltp8xONTCrossConnectUSEntry": ltp8xONTCrossConnectUSEntry,
       "ltp8xONTCrossConnectUSSlot": ltp8xONTCrossConnectUSSlot,
       "ltp8xONTCrossConnectUSSerial": ltp8xONTCrossConnectUSSerial,
       "ltp8xONTCrossConnectUSCrossConnect": ltp8xONTCrossConnectUSCrossConnect,
       "ltp8xONTCrossConnectUSCounterID": ltp8xONTCrossConnectUSCounterID,
       "ltp8xONTCrossConnectUSCounterName": ltp8xONTCrossConnectUSCounterName,
       "ltp8xONTCrossConnectUSCounterValue": ltp8xONTCrossConnectUSCounterValue,
       "ltp8xONTServiceDSTable": ltp8xONTServiceDSTable,
       "ltp8xONTServiceDSEntry": ltp8xONTServiceDSEntry,
       "ltp8xONTServiceDSSlot": ltp8xONTServiceDSSlot,
       "ltp8xONTServiceDSSerial": ltp8xONTServiceDSSerial,
       "ltp8xONTServiceDSService": ltp8xONTServiceDSService,
       "ltp8xONTServiceDSCounterID": ltp8xONTServiceDSCounterID,
       "ltp8xONTServiceDSCounterName": ltp8xONTServiceDSCounterName,
       "ltp8xONTServiceDSCounterValue": ltp8xONTServiceDSCounterValue,
       "ltp8xONTServiceUSTable": ltp8xONTServiceUSTable,
       "ltp8xONTServiceUSEntry": ltp8xONTServiceUSEntry,
       "ltp8xONTServiceUSSlot": ltp8xONTServiceUSSlot,
       "ltp8xONTServiceUSSerial": ltp8xONTServiceUSSerial,
       "ltp8xONTServiceUSService": ltp8xONTServiceUSService,
       "ltp8xONTServiceUSCounterID": ltp8xONTServiceUSCounterID,
       "ltp8xONTServiceUSCounterName": ltp8xONTServiceUSCounterName,
       "ltp8xONTServiceUSCounterValue": ltp8xONTServiceUSCounterValue,
       "ltp8xONTEthFrameExtendedPerformMonitoringDSTable": ltp8xONTEthFrameExtendedPerformMonitoringDSTable,
       "ltp8xONTEthFrameExtendedPerformMonitoringDSEntry": ltp8xONTEthFrameExtendedPerformMonitoringDSEntry,
       "ltp8xONTEthFrameExtendedPerformMonitoringDSSlot": ltp8xONTEthFrameExtendedPerformMonitoringDSSlot,
       "ltp8xONTEthFrameExtendedPerformMonitoringDSSerial": ltp8xONTEthFrameExtendedPerformMonitoringDSSerial,
       "ltp8xONTEthFrameExtendedPerformMonitoringDSPort": ltp8xONTEthFrameExtendedPerformMonitoringDSPort,
       "ltp8xONTEthFrameExtendedPerformMonitoringDSCounterID": ltp8xONTEthFrameExtendedPerformMonitoringDSCounterID,
       "ltp8xONTEthFrameExtendedPerformMonitoringDSCounterName": ltp8xONTEthFrameExtendedPerformMonitoringDSCounterName,
       "ltp8xONTEthFrameExtendedPerformMonitoringDSCounterValue": ltp8xONTEthFrameExtendedPerformMonitoringDSCounterValue,
       "ltp8xONTEthFrameExtendedPerformMonitoringUSTable": ltp8xONTEthFrameExtendedPerformMonitoringUSTable,
       "ltp8xONTEthFrameExtendedPerformMonitoringUSEntry": ltp8xONTEthFrameExtendedPerformMonitoringUSEntry,
       "ltp8xONTEthFrameExtendedPerformMonitoringUSSlot": ltp8xONTEthFrameExtendedPerformMonitoringUSSlot,
       "ltp8xONTEthFrameExtendedPerformMonitoringUSSerial": ltp8xONTEthFrameExtendedPerformMonitoringUSSerial,
       "ltp8xONTEthFrameExtendedPerformMonitoringUSPort": ltp8xONTEthFrameExtendedPerformMonitoringUSPort,
       "ltp8xONTEthFrameExtendedPerformMonitoringUSCounterID": ltp8xONTEthFrameExtendedPerformMonitoringUSCounterID,
       "ltp8xONTEthFrameExtendedPerformMonitoringUSCounterName": ltp8xONTEthFrameExtendedPerformMonitoringUSCounterName,
       "ltp8xONTEthFrameExtendedPerformMonitoringUSCounterValue": ltp8xONTEthFrameExtendedPerformMonitoringUSCounterValue,
       "ltp8xONTResetCountersTable": ltp8xONTResetCountersTable,
       "ltp8xONTResetCountersEntry": ltp8xONTResetCountersEntry,
       "ltp8xONTResetCountersSlot": ltp8xONTResetCountersSlot,
       "ltp8xONTResetCountersSerial": ltp8xONTResetCountersSerial,
       "ltp8xONTResetCountersAction": ltp8xONTResetCountersAction,
       "ltp8xONTConfigTable": ltp8xONTConfigTable,
       "ltp8xONTConfigEntry": ltp8xONTConfigEntry,
       "ltp8xONTConfigSlot": ltp8xONTConfigSlot,
       "ltp8xONTConfigSerial": ltp8xONTConfigSerial,
       "ltp8xONTConfigChannel": ltp8xONTConfigChannel,
       "ltp8xONTConfigID": ltp8xONTConfigID,
       "ltp8xONTConfigServicesProfile": ltp8xONTConfigServicesProfile,
       "ltp8xONTConfigPassword": ltp8xONTConfigPassword,
       "ltp8xONTConfigFecUp": ltp8xONTConfigFecUp,
       "ltp8xONTConfigDescription": ltp8xONTConfigDescription,
       "ltp8xONTConfigManagementProfile": ltp8xONTConfigManagementProfile,
       "ltp8xONTConfigMulticastProfile": ltp8xONTConfigMulticastProfile,
       "ltp8xONTConfigCrossConnectProfile0": ltp8xONTConfigCrossConnectProfile0,
       "ltp8xONTConfigCrossConnectProfile1": ltp8xONTConfigCrossConnectProfile1,
       "ltp8xONTConfigCrossConnectProfile2": ltp8xONTConfigCrossConnectProfile2,
       "ltp8xONTConfigCrossConnectProfile3": ltp8xONTConfigCrossConnectProfile3,
       "ltp8xONTConfigCrossConnectProfile4": ltp8xONTConfigCrossConnectProfile4,
       "ltp8xONTConfigCrossConnectProfile5": ltp8xONTConfigCrossConnectProfile5,
       "ltp8xONTConfigCrossConnectProfile6": ltp8xONTConfigCrossConnectProfile6,
       "ltp8xONTConfigCrossConnectProfile7": ltp8xONTConfigCrossConnectProfile7,
       "ltp8xONTConfigShapingProfile": ltp8xONTConfigShapingProfile,
       "ltp8xONTConfigRowStatus": ltp8xONTConfigRowStatus,
       "ltp8xONTConfigEncryptionEnabled": ltp8xONTConfigEncryptionEnabled,
       "ltp8xONTConfigDownstreamBroadcastEnabled": ltp8xONTConfigDownstreamBroadcastEnabled,
       "ltp8xONTConfigAllocProfile0": ltp8xONTConfigAllocProfile0,
       "ltp8xONTConfigAllocProfile1": ltp8xONTConfigAllocProfile1,
       "ltp8xONTConfigAllocProfile2": ltp8xONTConfigAllocProfile2,
       "ltp8xONTConfigAllocProfile3": ltp8xONTConfigAllocProfile3,
       "ltp8xONTConfigAllocProfile4": ltp8xONTConfigAllocProfile4,
       "ltp8xONTConfigAllocProfile5": ltp8xONTConfigAllocProfile5,
       "ltp8xONTConfigAllocProfile6": ltp8xONTConfigAllocProfile6,
       "ltp8xONTConfigAllocProfile7": ltp8xONTConfigAllocProfile7,
       "ltp8xONTConfigPortsProfile": ltp8xONTConfigPortsProfile,
       "ltp8xONTConfigRFPortEnabled": ltp8xONTConfigRFPortEnabled,
       "ltp8xONTConfigHostControlledOMCI": ltp8xONTConfigHostControlledOMCI,
       "ltp8xONTConfigVoiceProfile": ltp8xONTConfigVoiceProfile,
       "ltp8xONTConfigEnabled": ltp8xONTConfigEnabled,
       "ltp8xONTConfigScriptingProfile": ltp8xONTConfigScriptingProfile,
       "ltp8xONTConfigBerInterval": ltp8xONTConfigBerInterval,
       "ltp8xONTConfigBerUpdatePeriod": ltp8xONTConfigBerUpdatePeriod,
       "ltp8xONTConfigOMCIErrorTolerant": ltp8xONTConfigOMCIErrorTolerant,
       "ltp8xONTConfigCustomModel": ltp8xONTConfigCustomModel,
       "ltp8xONTConfigEMSProfile": ltp8xONTConfigEMSProfile,
       "ltp8xONTConfigBandwidthManagementACSProfile": ltp8xONTConfigBandwidthManagementACSProfile,
       "ltp8xONTConfigTemplate": ltp8xONTConfigTemplate,
       "ltp8xONTServiceOverrideTable": ltp8xONTServiceOverrideTable,
       "ltp8xONTServiceOverrideEntry": ltp8xONTServiceOverrideEntry,
       "ltp8xONTServiceOverrideID": ltp8xONTServiceOverrideID,
       "ltp8xONTServiceOverrideSlot": ltp8xONTServiceOverrideSlot,
       "ltp8xONTServiceOverrideSerial": ltp8xONTServiceOverrideSerial,
       "ltp8xONTServiceOverrideEnabled": ltp8xONTServiceOverrideEnabled,
       "ltp8xONTServiceOverrideCustomerVID": ltp8xONTServiceOverrideCustomerVID,
       "ltp8xONTServiceOverrideCustomerCOS": ltp8xONTServiceOverrideCustomerCOS,
       "ltp8xONTManagementProfileTable": ltp8xONTManagementProfileTable,
       "ltp8xONTManagementProfileEntry": ltp8xONTManagementProfileEntry,
       "ltp8xONTManagementID": ltp8xONTManagementID,
       "ltp8xONTManagementDescription": ltp8xONTManagementDescription,
       "ltp8xONTManagementName": ltp8xONTManagementName,
       "ltp8xONTManagementCrossConnect": ltp8xONTManagementCrossConnect,
       "ltp8xONTManagementURL": ltp8xONTManagementURL,
       "ltp8xONTManagementUsername": ltp8xONTManagementUsername,
       "ltp8xONTManagementPassword": ltp8xONTManagementPassword,
       "ltp8xONTManagementOMCIConfiguration": ltp8xONTManagementOMCIConfiguration,
       "ltp8xONTManagementRowStatus": ltp8xONTManagementRowStatus,
       "ltp8xONTMulticastProfileTable": ltp8xONTMulticastProfileTable,
       "ltp8xONTMulticastProfileEntry": ltp8xONTMulticastProfileEntry,
       "ltp8xONTMulticastID": ltp8xONTMulticastID,
       "ltp8xONTMulticastDescription": ltp8xONTMulticastDescription,
       "ltp8xONTMulticastName": ltp8xONTMulticastName,
       "ltp8xONTServicesProfileTable": ltp8xONTServicesProfileTable,
       "ltp8xONTServicesProfileEntry": ltp8xONTServicesProfileEntry,
       "ltp8xONTServicesID": ltp8xONTServicesID,
       "ltp8xONTServicesDescription": ltp8xONTServicesDescription,
       "ltp8xONTServicesName": ltp8xONTServicesName,
       "ltp8xONTCrossConnectProfileTable": ltp8xONTCrossConnectProfileTable,
       "ltp8xONTCrossConnectProfileEntry": ltp8xONTCrossConnectProfileEntry,
       "ltp8xONTCrossConnectID": ltp8xONTCrossConnectID,
       "ltp8xONTCrossConnectDescription": ltp8xONTCrossConnectDescription,
       "ltp8xONTCrossConnectName": ltp8xONTCrossConnectName,
       "ltp8xONTCrossConnectModel": ltp8xONTCrossConnectModel,
       "ltp8xONTCrossConnectBridgeGroup": ltp8xONTCrossConnectBridgeGroup,
       "ltp8xONTCrossConnectTagMode": ltp8xONTCrossConnectTagMode,
       "ltp8xONTCrossConnectOuterVID": ltp8xONTCrossConnectOuterVID,
       "ltp8xONTCrossConnectOuterCOS": ltp8xONTCrossConnectOuterCOS,
       "ltp8xONTCrossConnectInnerVID": ltp8xONTCrossConnectInnerVID,
       "ltp8xONTCrossConnectUVID": ltp8xONTCrossConnectUVID,
       "ltp8xONTCrossConnectUCOS": ltp8xONTCrossConnectUCOS,
       "ltp8xONTCrossConnectMacTableEntryLimit": ltp8xONTCrossConnectMacTableEntryLimit,
       "ltp8xONTCrossConnectType": ltp8xONTCrossConnectType,
       "ltp8xONTCrossConnectIphostEid": ltp8xONTCrossConnectIphostEid,
       "ltp8xONTCrossConnectPriorityQueue": ltp8xONTCrossConnectPriorityQueue,
       "ltp8xONTCrossConnectRowStatus": ltp8xONTCrossConnectRowStatus,
       "ltp8xONTMulticastGroupsTable": ltp8xONTMulticastGroupsTable,
       "ltp8xONTMulticastGroupsEntry": ltp8xONTMulticastGroupsEntry,
       "ltp8xONTMulticastGroupsSlot": ltp8xONTMulticastGroupsSlot,
       "ltp8xONTMulticastGroupsSerial": ltp8xONTMulticastGroupsSerial,
       "ltp8xONTMulticastGroupsEntryID": ltp8xONTMulticastGroupsEntryID,
       "ltp8xONTMulticastGroupsVLAN": ltp8xONTMulticastGroupsVLAN,
       "ltp8xONTMulticastGroupsSourceIP": ltp8xONTMulticastGroupsSourceIP,
       "ltp8xONTMulticastGroupsDestIP": ltp8xONTMulticastGroupsDestIP,
       "ltp8xONTMulticastGroupsBEBandwidth": ltp8xONTMulticastGroupsBEBandwidth,
       "ltp8xONTMulticastGroupsClientIP": ltp8xONTMulticastGroupsClientIP,
       "ltp8xONTMulticastGroupsRecentJoinTime": ltp8xONTMulticastGroupsRecentJoinTime,
       "ltp8xONTBufferZoneTable": ltp8xONTBufferZoneTable,
       "ltp8xONTBufferZoneEntry": ltp8xONTBufferZoneEntry,
       "ltp8xONTBufferZoneValue": ltp8xONTBufferZoneValue,
       "ltp8xONTAddressTable": ltp8xONTAddressTable,
       "ltp8xONTAddressEntry": ltp8xONTAddressEntry,
       "ltp8xONTAddressSlot": ltp8xONTAddressSlot,
       "ltp8xONTAddressSerial": ltp8xONTAddressSerial,
       "ltp8xONTAddressEntryID": ltp8xONTAddressEntryID,
       "ltp8xONTAddressPriority": ltp8xONTAddressPriority,
       "ltp8xONTAddressCVID": ltp8xONTAddressCVID,
       "ltp8xONTAddressSVID": ltp8xONTAddressSVID,
       "ltp8xONTAddressMacAddress": ltp8xONTAddressMacAddress,
       "ltp8xONTAddressCPUDestined": ltp8xONTAddressCPUDestined,
       "ltp8xONTAddressDatapathForwarding": ltp8xONTAddressDatapathForwarding,
       "ltp8xONTAddressUniPort": ltp8xONTAddressUniPort,
       "ltp8xONTAddressEntryType": ltp8xONTAddressEntryType,
       "ltp8xONTAddressAge": ltp8xONTAddressAge,
       "ltp8xONTAddressGEMPortId": ltp8xONTAddressGEMPortId,
       "ltp8xONTAddressUVID": ltp8xONTAddressUVID,
       "ltp8xONTMassUpdateFirmwareTable": ltp8xONTMassUpdateFirmwareTable,
       "ltp8xONTMassUpdateFirmwareEntry": ltp8xONTMassUpdateFirmwareEntry,
       "ltp8xONTMassUpdateFirmwareSlot": ltp8xONTMassUpdateFirmwareSlot,
       "ltp8xONTMassUpdateFirmwareAction": ltp8xONTMassUpdateFirmwareAction,
       "ltp8xONTCustomCrossConnectTable": ltp8xONTCustomCrossConnectTable,
       "ltp8xONTCustomCrossConnectEntry": ltp8xONTCustomCrossConnectEntry,
       "ltp8xONTCustomCrossConnectSlot": ltp8xONTCustomCrossConnectSlot,
       "ltp8xONTCustomCrossConnectSerial": ltp8xONTCustomCrossConnectSerial,
       "ltp8xONTCustomCrossConnectID": ltp8xONTCustomCrossConnectID,
       "ltp8xONTCustomCrossConnectEnabled": ltp8xONTCustomCrossConnectEnabled,
       "ltp8xONTCustomCrossConnectVID": ltp8xONTCustomCrossConnectVID,
       "ltp8xONTCustomCrossConnectCOS": ltp8xONTCustomCrossConnectCOS,
       "ltp8xONTCustomCrossConnectSVID": ltp8xONTCustomCrossConnectSVID,
       "ltp8xONTACSConfigTable": ltp8xONTACSConfigTable,
       "ltp8xONTACSConfigEntry": ltp8xONTACSConfigEntry,
       "ltp8xONTACSConfigSerial": ltp8xONTACSConfigSerial,
       "ltp8xONTACSUserID": ltp8xONTACSUserID,
       "ltp8xONTACSConfigProfile": ltp8xONTACSConfigProfile,
       "ltp8xONTACSConfigVoice1Enable": ltp8xONTACSConfigVoice1Enable,
       "ltp8xONTACSConfigVoice1Number": ltp8xONTACSConfigVoice1Number,
       "ltp8xONTACSConfigVoice1Password": ltp8xONTACSConfigVoice1Password,
       "ltp8xONTACSConfigVoice2Enable": ltp8xONTACSConfigVoice2Enable,
       "ltp8xONTACSConfigVoice2Number": ltp8xONTACSConfigVoice2Number,
       "ltp8xONTACSConfigVoice2Password": ltp8xONTACSConfigVoice2Password,
       "ltp8xONTACSConfigSIPProxy": ltp8xONTACSConfigSIPProxy,
       "ltp8xONTACSConfigPPPLogin": ltp8xONTACSConfigPPPLogin,
       "ltp8xONTACSConfigPPPPassword": ltp8xONTACSConfigPPPPassword,
       "ltp8xONTACSConfigInternetVlan": ltp8xONTACSConfigInternetVlan,
       "ltp8xONTACSConfigResetToDefaults": ltp8xONTACSConfigResetToDefaults,
       "ltp8xONTACSConfigReboot": ltp8xONTACSConfigReboot,
       "ltp8xONTACSConfigReconfigure": ltp8xONTACSConfigReconfigure,
       "ltp8xONTACSConfigDelete": ltp8xONTACSConfigDelete,
       "ltp8xONTACSProfilesTable": ltp8xONTACSProfilesTable,
       "ltp8xONTACSProfilesEntry": ltp8xONTACSProfilesEntry,
       "ltp8xONTACSProfilesName": ltp8xONTACSProfilesName,
       "ltp8xONTACSProfilesDescription": ltp8xONTACSProfilesDescription,
       "ltp8xONTACSConfigAltTable": ltp8xONTACSConfigAltTable,
       "ltp8xONTACSConfigAltEntry": ltp8xONTACSConfigAltEntry,
       "ltp8xONTACSConfigAltSerial": ltp8xONTACSConfigAltSerial,
       "ltp8xONTACSConfigAltSubscriberID": ltp8xONTACSConfigAltSubscriberID,
       "ltp8xONTACSConfigAltProfile": ltp8xONTACSConfigAltProfile,
       "ltp8xONTACSConfigAltVoice1Enable": ltp8xONTACSConfigAltVoice1Enable,
       "ltp8xONTACSConfigAltVoice1Number": ltp8xONTACSConfigAltVoice1Number,
       "ltp8xONTACSConfigAltVoice1Password": ltp8xONTACSConfigAltVoice1Password,
       "ltp8xONTACSConfigAltVoice2Enable": ltp8xONTACSConfigAltVoice2Enable,
       "ltp8xONTACSConfigAltVoice2Number": ltp8xONTACSConfigAltVoice2Number,
       "ltp8xONTACSConfigAltVoice2Password": ltp8xONTACSConfigAltVoice2Password,
       "ltp8xONTACSConfigAltSIPProxy": ltp8xONTACSConfigAltSIPProxy,
       "ltp8xONTACSConfigAltPPPLogin": ltp8xONTACSConfigAltPPPLogin,
       "ltp8xONTACSConfigAltPPPPassword": ltp8xONTACSConfigAltPPPPassword,
       "ltp8xONTACSConfigAltInternetVlan": ltp8xONTACSConfigAltInternetVlan,
       "ltp8xONTACSConfigAltResetToDefaults": ltp8xONTACSConfigAltResetToDefaults,
       "ltp8xONTACSConfigAltRowStatus": ltp8xONTACSConfigAltRowStatus,
       "ltp8xONTShapingProfileTable": ltp8xONTShapingProfileTable,
       "ltp8xONTShapingProfileEntry": ltp8xONTShapingProfileEntry,
       "ltp8xONTShapingID": ltp8xONTShapingID,
       "ltp8xONTShapingDescription": ltp8xONTShapingDescription,
       "ltp8xONTShapingName": ltp8xONTShapingName,
       "ltp8xONTShapingDownstreamOnePolicer": ltp8xONTShapingDownstreamOnePolicer,
       "ltp8xONTShapingRowStatus": ltp8xONTShapingRowStatus,
       "ltp8xONTShapingProfileServicesTable": ltp8xONTShapingProfileServicesTable,
       "ltp8xONTShapingProfileServicesEntry": ltp8xONTShapingProfileServicesEntry,
       "ltp8xONTShapingCrossConnect": ltp8xONTShapingCrossConnect,
       "ltp8xONTShapingUpstreamEnable": ltp8xONTShapingUpstreamEnable,
       "ltp8xONTShapingUpstreamCommitedRate": ltp8xONTShapingUpstreamCommitedRate,
       "ltp8xONTShapingUpstreamPeakRate": ltp8xONTShapingUpstreamPeakRate,
       "ltp8xONTShapingDownstreamEnable": ltp8xONTShapingDownstreamEnable,
       "ltp8xONTShapingDownstreamPeakRate": ltp8xONTShapingDownstreamPeakRate,
       "ltp8xONTACSState": ltp8xONTACSState,
       "ltp8xONTACSStateTable": ltp8xONTACSStateTable,
       "ltp8xONTACSStateEntry": ltp8xONTACSStateEntry,
       "ltp8xONTACSStateBindingID": ltp8xONTACSStateBindingID,
       "ltp8xONTACSStateSerial": ltp8xONTACSStateSerial,
       "ltp8xONTACSStateBindingName": ltp8xONTACSStateBindingName,
       "ltp8xONTACSStateBindingValue": ltp8xONTACSStateBindingValue,
       "ltp8xONTACSStateDeleteRow": ltp8xONTACSStateDeleteRow,
       "ltp8xONTACSStateCommitRequest": ltp8xONTACSStateCommitRequest,
       "ltp8xONTACSStateClear": ltp8xONTACSStateClear,
       "ltp8xONTACSStateMaxIndex": ltp8xONTACSStateMaxIndex,
       "ltp8xONTACSStateLastSetIndex": ltp8xONTACSStateLastSetIndex,
       "ltp8xONTACSStateLock": ltp8xONTACSStateLock,
       "ltp8xONTStaticWANConfigTable": ltp8xONTStaticWANConfigTable,
       "ltp8xONTStaticWANConfigEntry": ltp8xONTStaticWANConfigEntry,
       "ltp8xONTStaticWANConfigSerial": ltp8xONTStaticWANConfigSerial,
       "ltp8xONTStaticWANConfigConnection": ltp8xONTStaticWANConfigConnection,
       "ltp8xONTStaticWANConfigDefaultGateway": ltp8xONTStaticWANConfigDefaultGateway,
       "ltp8xONTStaticWANConfigExternalIPAddress": ltp8xONTStaticWANConfigExternalIPAddress,
       "ltp8xONTStaticWANConfigSubnetMask": ltp8xONTStaticWANConfigSubnetMask,
       "ltp8xONTBandwidthManagementProfileTable": ltp8xONTBandwidthManagementProfileTable,
       "ltp8xONTBandwidthManagementProfileEntry": ltp8xONTBandwidthManagementProfileEntry,
       "ltp8xONTBandwidthManagementID": ltp8xONTBandwidthManagementID,
       "ltp8xONTBandwidthManagementDescription": ltp8xONTBandwidthManagementDescription,
       "ltp8xONTBandwidthManagementName": ltp8xONTBandwidthManagementName,
       "ltp8xONTServiceBandwidthManagementTable": ltp8xONTServiceBandwidthManagementTable,
       "ltp8xONTServiceBandwidthManagementEntry": ltp8xONTServiceBandwidthManagementEntry,
       "ltp8xONTServiceBandwidthManagementServiceID": ltp8xONTServiceBandwidthManagementServiceID,
       "ltp8xONTServiceBandwidthManagementSlot": ltp8xONTServiceBandwidthManagementSlot,
       "ltp8xONTServiceBandwidthManagementSerial": ltp8xONTServiceBandwidthManagementSerial,
       "ltp8xONTServiceBandwidthManagementProfile": ltp8xONTServiceBandwidthManagementProfile,
       "ltp8xONTTemplates": ltp8xONTTemplates,
       "ltp8xONTTemplateValuesTable": ltp8xONTTemplateValuesTable,
       "ltp8xONTTemplateValuesEntry": ltp8xONTTemplateValuesEntry,
       "ltp8xONTTemplateValuesID": ltp8xONTTemplateValuesID,
       "ltp8xONTTemplateValuesName": ltp8xONTTemplateValuesName,
       "ltp8xONTTemplateValuesDescription": ltp8xONTTemplateValuesDescription,
       "ltp8xONTTemplateValuesSerial": ltp8xONTTemplateValuesSerial,
       "ltp8xONTTemplateValuesPassword": ltp8xONTTemplateValuesPassword,
       "ltp8xONTTemplateValuesFecUp": ltp8xONTTemplateValuesFecUp,
       "ltp8xONTTemplateValuesManagementProfile": ltp8xONTTemplateValuesManagementProfile,
       "ltp8xONTTemplateValuesCrossConnectProfile0": ltp8xONTTemplateValuesCrossConnectProfile0,
       "ltp8xONTTemplateValuesCrossConnectProfile1": ltp8xONTTemplateValuesCrossConnectProfile1,
       "ltp8xONTTemplateValuesCrossConnectProfile2": ltp8xONTTemplateValuesCrossConnectProfile2,
       "ltp8xONTTemplateValuesCrossConnectProfile3": ltp8xONTTemplateValuesCrossConnectProfile3,
       "ltp8xONTTemplateValuesCrossConnectProfile4": ltp8xONTTemplateValuesCrossConnectProfile4,
       "ltp8xONTTemplateValuesCrossConnectProfile5": ltp8xONTTemplateValuesCrossConnectProfile5,
       "ltp8xONTTemplateValuesCrossConnectProfile6": ltp8xONTTemplateValuesCrossConnectProfile6,
       "ltp8xONTTemplateValuesCrossConnectProfile7": ltp8xONTTemplateValuesCrossConnectProfile7,
       "ltp8xONTTemplateValuesShapingProfile": ltp8xONTTemplateValuesShapingProfile,
       "ltp8xONTTemplateValuesDownstreamBroadcastEnabled": ltp8xONTTemplateValuesDownstreamBroadcastEnabled,
       "ltp8xONTTemplateValuesAllocProfile0": ltp8xONTTemplateValuesAllocProfile0,
       "ltp8xONTTemplateValuesAllocProfile1": ltp8xONTTemplateValuesAllocProfile1,
       "ltp8xONTTemplateValuesAllocProfile2": ltp8xONTTemplateValuesAllocProfile2,
       "ltp8xONTTemplateValuesAllocProfile3": ltp8xONTTemplateValuesAllocProfile3,
       "ltp8xONTTemplateValuesAllocProfile4": ltp8xONTTemplateValuesAllocProfile4,
       "ltp8xONTTemplateValuesAllocProfile5": ltp8xONTTemplateValuesAllocProfile5,
       "ltp8xONTTemplateValuesAllocProfile6": ltp8xONTTemplateValuesAllocProfile6,
       "ltp8xONTTemplateValuesAllocProfile7": ltp8xONTTemplateValuesAllocProfile7,
       "ltp8xONTTemplateValuesPortsProfile": ltp8xONTTemplateValuesPortsProfile,
       "ltp8xONTTemplateValuesRFPortEnabled": ltp8xONTTemplateValuesRFPortEnabled,
       "ltp8xONTTemplateValuesScriptingProfile": ltp8xONTTemplateValuesScriptingProfile,
       "ltp8xONTTemplateValuesBerInterval": ltp8xONTTemplateValuesBerInterval,
       "ltp8xONTTemplateValuesBerUpdatePeriod": ltp8xONTTemplateValuesBerUpdatePeriod,
       "ltp8xONTTemplateValuesOMCIErrorTolerant": ltp8xONTTemplateValuesOMCIErrorTolerant,
       "ltp8xONTTemplateValuesRowStatus": ltp8xONTTemplateValuesRowStatus,
       "ltp8xONTTemplateOverridesTable": ltp8xONTTemplateOverridesTable,
       "ltp8xONTTemplateOverridesEntry": ltp8xONTTemplateOverridesEntry,
       "ltp8xONTTemplateOverridesSerial": ltp8xONTTemplateOverridesSerial,
       "ltp8xONTTemplateOverridesPassword": ltp8xONTTemplateOverridesPassword,
       "ltp8xONTTemplateOverridesFecUp": ltp8xONTTemplateOverridesFecUp,
       "ltp8xONTTemplateOverridesManagementProfile": ltp8xONTTemplateOverridesManagementProfile,
       "ltp8xONTTemplateOverridesCrossConnectProfile0": ltp8xONTTemplateOverridesCrossConnectProfile0,
       "ltp8xONTTemplateOverridesCrossConnectProfile1": ltp8xONTTemplateOverridesCrossConnectProfile1,
       "ltp8xONTTemplateOverridesCrossConnectProfile2": ltp8xONTTemplateOverridesCrossConnectProfile2,
       "ltp8xONTTemplateOverridesCrossConnectProfile3": ltp8xONTTemplateOverridesCrossConnectProfile3,
       "ltp8xONTTemplateOverridesCrossConnectProfile4": ltp8xONTTemplateOverridesCrossConnectProfile4,
       "ltp8xONTTemplateOverridesCrossConnectProfile5": ltp8xONTTemplateOverridesCrossConnectProfile5,
       "ltp8xONTTemplateOverridesCrossConnectProfile6": ltp8xONTTemplateOverridesCrossConnectProfile6,
       "ltp8xONTTemplateOverridesCrossConnectProfile7": ltp8xONTTemplateOverridesCrossConnectProfile7,
       "ltp8xONTTemplateOverridesShapingProfile": ltp8xONTTemplateOverridesShapingProfile,
       "ltp8xONTTemplateOverridesDownstreamBroadcastEnabled": ltp8xONTTemplateOverridesDownstreamBroadcastEnabled,
       "ltp8xONTTemplateOverridesAllocProfile0": ltp8xONTTemplateOverridesAllocProfile0,
       "ltp8xONTTemplateOverridesAllocProfile1": ltp8xONTTemplateOverridesAllocProfile1,
       "ltp8xONTTemplateOverridesAllocProfile2": ltp8xONTTemplateOverridesAllocProfile2,
       "ltp8xONTTemplateOverridesAllocProfile3": ltp8xONTTemplateOverridesAllocProfile3,
       "ltp8xONTTemplateOverridesAllocProfile4": ltp8xONTTemplateOverridesAllocProfile4,
       "ltp8xONTTemplateOverridesAllocProfile5": ltp8xONTTemplateOverridesAllocProfile5,
       "ltp8xONTTemplateOverridesAllocProfile6": ltp8xONTTemplateOverridesAllocProfile6,
       "ltp8xONTTemplateOverridesAllocProfile7": ltp8xONTTemplateOverridesAllocProfile7,
       "ltp8xONTTemplateOverridesPortsProfile": ltp8xONTTemplateOverridesPortsProfile,
       "ltp8xONTTemplateOverridesRFPortEnabled": ltp8xONTTemplateOverridesRFPortEnabled,
       "ltp8xONTTemplateOverridesScriptingProfile": ltp8xONTTemplateOverridesScriptingProfile,
       "ltp8xONTTemplateOverridesBerInterval": ltp8xONTTemplateOverridesBerInterval,
       "ltp8xONTTemplateOverridesBerUpdatePeriod": ltp8xONTTemplateOverridesBerUpdatePeriod,
       "ltp8xONTTemplateOverridesOMCIErrorTolerant": ltp8xONTTemplateOverridesOMCIErrorTolerant,
       "ltp8xONTTemplateServicesValuesTable": ltp8xONTTemplateServicesValuesTable,
       "ltp8xONTTemplateServicesValuesEntry": ltp8xONTTemplateServicesValuesEntry,
       "ltp8xONTTemplateServicesValuesServiceID": ltp8xONTTemplateServicesValuesServiceID,
       "ltp8xONTTemplateServicesValuesCrossConnectProfile": ltp8xONTTemplateServicesValuesCrossConnectProfile,
       "ltp8xONTTemplateServicesValuesDBAProfile": ltp8xONTTemplateServicesValuesDBAProfile,
       "ltp8xONTTemplateServicesOverridesTable": ltp8xONTTemplateServicesOverridesTable,
       "ltp8xONTTemplateServicesOverridesEntry": ltp8xONTTemplateServicesOverridesEntry,
       "ltp8xONTTemplateServicesOverridesServiceID": ltp8xONTTemplateServicesOverridesServiceID,
       "ltp8xONTTemplateServicesOverridesCrossConnectProfile": ltp8xONTTemplateServicesOverridesCrossConnectProfile,
       "ltp8xONTTemplateServicesOverridesDBAProfile": ltp8xONTTemplateServicesOverridesDBAProfile,
       "ltp8xONTFullServicesConfigTable": ltp8xONTFullServicesConfigTable,
       "ltp8xONTFullServicesConfigEntry": ltp8xONTFullServicesConfigEntry,
       "ltp8xONTFullServicesConfigSlot": ltp8xONTFullServicesConfigSlot,
       "ltp8xONTFullServicesConfigSerial": ltp8xONTFullServicesConfigSerial,
       "ltp8xONTFullServicesConfigServiceID": ltp8xONTFullServicesConfigServiceID,
       "ltp8xONTFullServicesConfigCrossConnectProfile": ltp8xONTFullServicesConfigCrossConnectProfile,
       "ltp8xONTFullServicesConfigDBAProfile": ltp8xONTFullServicesConfigDBAProfile,
       "ltp8xONTSelectiveTunnelTable": ltp8xONTSelectiveTunnelTable,
       "ltp8xONTSelectiveTunnelEntry": ltp8xONTSelectiveTunnelEntry,
       "ltp8xONTSelectiveTunnelSlot": ltp8xONTSelectiveTunnelSlot,
       "ltp8xONTSelectiveTunnelSerial": ltp8xONTSelectiveTunnelSerial,
       "ltp8xONTSelectiveTunnelServiceID": ltp8xONTSelectiveTunnelServiceID,
       "ltp8xONTSelectiveTunnelUVIDIndex": ltp8xONTSelectiveTunnelUVIDIndex,
       "ltp8xONTSelectiveTunnelUVID": ltp8xONTSelectiveTunnelUVID,
       "ltp8xONTFirmwares": ltp8xONTFirmwares,
       "ltp8xONTFirmwaresFilesTable": ltp8xONTFirmwaresFilesTable,
       "ltp8xONTFirmwaresFilesEntry": ltp8xONTFirmwaresFilesEntry,
       "ltp8xONTFirmwaresFilesEntryID": ltp8xONTFirmwaresFilesEntryID,
       "ltp8xONTFirmwaresFilesName": ltp8xONTFirmwaresFilesName,
       "ltp8xONTFirmwaresFilesVersion": ltp8xONTFirmwaresFilesVersion,
       "ltp8xONTFirmwaresFilesHardware": ltp8xONTFirmwaresFilesHardware,
       "ltp8xONTFirmwaresFilesDelete": ltp8xONTFirmwaresFilesDelete,
       "ltp8xONTFirmwaresTable": ltp8xONTFirmwaresTable,
       "ltp8xONTFirmwaresEntry": ltp8xONTFirmwaresEntry,
       "ltp8xONTFirmwaresEntryID": ltp8xONTFirmwaresEntryID,
       "ltp8xONTFirmwaresName": ltp8xONTFirmwaresName,
       "ltp8xONTFirmwaresVersion": ltp8xONTFirmwaresVersion,
       "ltp8xONTFirmwaresHardware": ltp8xONTFirmwaresHardware,
       "ltp8xONTFirmwaresURL": ltp8xONTFirmwaresURL,
       "ltp8xONTFirmwaresScheduler": ltp8xONTFirmwaresScheduler,
       "ltp8xONTFirmwaresSafeMode": ltp8xONTFirmwaresSafeMode,
       "ltp8xONTFirmwaresDowngrade": ltp8xONTFirmwaresDowngrade,
       "ltp8xONTFirmwaresRowStatus": ltp8xONTFirmwaresRowStatus,
       "ltp8xONTFirmwaresProfilesTable": ltp8xONTFirmwaresProfilesTable,
       "ltp8xONTFirmwaresProfilesEntry": ltp8xONTFirmwaresProfilesEntry,
       "ltp8xONTFirmwaresProfilesFWID": ltp8xONTFirmwaresProfilesFWID,
       "ltp8xONTFirmwaresProfilesName": ltp8xONTFirmwaresProfilesName,
       "ltp8xONTFirmwaresProfilesRowStatus": ltp8xONTFirmwaresProfilesRowStatus,
       "ltp8xONTFirmwaresSchedulerConfig": ltp8xONTFirmwaresSchedulerConfig,
       "ltp8xONTFirmwaresSchedulerDailyFrom": ltp8xONTFirmwaresSchedulerDailyFrom,
       "ltp8xONTFirmwaresSchedulerDailyTo": ltp8xONTFirmwaresSchedulerDailyTo,
       "ltp8xONTFirmwaresSchedulerPeriodFrom": ltp8xONTFirmwaresSchedulerPeriodFrom,
       "ltp8xONTFirmwaresSchedulerPeriodTo": ltp8xONTFirmwaresSchedulerPeriodTo,
       "ltp8xONTFirmwaresSchedulerWeeklyFrom": ltp8xONTFirmwaresSchedulerWeeklyFrom,
       "ltp8xONTFirmwaresSchedulerWeeklyTo": ltp8xONTFirmwaresSchedulerWeeklyTo,
       "ltp8xONTFirmwaresSpecificsTable": ltp8xONTFirmwaresSpecificsTable,
       "ltp8xONTFirmwaresSpecificsEntry": ltp8xONTFirmwaresSpecificsEntry,
       "ltp8xONTFirmwaresSpecificsName": ltp8xONTFirmwaresSpecificsName,
       "ltp8xONTFirmwaresSpecificsVersion": ltp8xONTFirmwaresSpecificsVersion,
       "ltp8xONTFirmwaresSpecificsHardware": ltp8xONTFirmwaresSpecificsHardware,
       "ltp8xONTFirmwaresSpecificsVendor": ltp8xONTFirmwaresSpecificsVendor,
       "ltp8xONTFirmwaresSpecificsRowStatus": ltp8xONTFirmwaresSpecificsRowStatus,
       "ltp8xONTFirmwaresVersionPriorityFile": ltp8xONTFirmwaresVersionPriorityFile,
       "ltp8xONTFirmwaresDownload": ltp8xONTFirmwaresDownload,
       "ltp8xONTFirmwaresDownloadIPAddress": ltp8xONTFirmwaresDownloadIPAddress,
       "ltp8xONTFirmwaresDownloadPath": ltp8xONTFirmwaresDownloadPath,
       "ltp8xONTFirmwaresDownloadAction": ltp8xONTFirmwaresDownloadAction,
       "ltp8xONTFirmwaresDownloadResult": ltp8xONTFirmwaresDownloadResult,
       "ltp8xONTFirmwaresDownloadProtocol": ltp8xONTFirmwaresDownloadProtocol,
       "ltp8xONTFirmwaresDownloadPort": ltp8xONTFirmwaresDownloadPort,
       "ltp8xONTFirmwareUpdateViaOMCI": ltp8xONTFirmwareUpdateViaOMCI,
       "ltp8xONTFirmwareUpdateViaOMCISlot": ltp8xONTFirmwareUpdateViaOMCISlot,
       "ltp8xONTFirmwareUpdateViaOMCISerial": ltp8xONTFirmwareUpdateViaOMCISerial,
       "ltp8xONTFirmwareUpdateViaOMCIFilename": ltp8xONTFirmwareUpdateViaOMCIFilename,
       "ltp8xONTFirmwareUpdateViaOMCIAction": ltp8xONTFirmwareUpdateViaOMCIAction,
       "ltp8xONTFWUpdateSchedulerTable": ltp8xONTFWUpdateSchedulerTable,
       "ltp8xONTFWUpdateSchedulerEntry": ltp8xONTFWUpdateSchedulerEntry,
       "ltp8xONTFWUpdateSchedulerSlot": ltp8xONTFWUpdateSchedulerSlot,
       "ltp8xONTFWUpdateSchedulerTaskID": ltp8xONTFWUpdateSchedulerTaskID,
       "ltp8xONTFWUpdateSchedulerSerial": ltp8xONTFWUpdateSchedulerSerial,
       "ltp8xONTFWUpdateSchedulerTaskState": ltp8xONTFWUpdateSchedulerTaskState,
       "ltp8xONTFWUpdateSchedulerFilename": ltp8xONTFWUpdateSchedulerFilename,
       "ltp8xONTFWUpdateSchedulerTries": ltp8xONTFWUpdateSchedulerTries,
       "ltp8xONTFWUpdateSchedulerONTChannel": ltp8xONTFWUpdateSchedulerONTChannel,
       "ltp8xONTFWUpdateSchedulerONTId": ltp8xONTFWUpdateSchedulerONTId,
       "ltp8xONTFWUpdateSchedulerUseSerial": ltp8xONTFWUpdateSchedulerUseSerial,
       "ltp8xONTFWUpdateSchedulerRowStatus": ltp8xONTFWUpdateSchedulerRowStatus,
       "ltp8xONTAutoUpdateTable": ltp8xONTAutoUpdateTable,
       "ltp8xONTAutoUpdateEntry": ltp8xONTAutoUpdateEntry,
       "ltp8xONTAutoUpdateDescription": ltp8xONTAutoUpdateDescription,
       "ltp8xONTAutoUpdateEquipmentID": ltp8xONTAutoUpdateEquipmentID,
       "ltp8xONTAutoUpdateFirmwareVersion": ltp8xONTAutoUpdateFirmwareVersion,
       "ltp8xONTAutoUpdateFilename": ltp8xONTAutoUpdateFilename,
       "ltp8xONTAutoUpdateMode": ltp8xONTAutoUpdateMode,
       "ltp8xONTAutoUpdateFirmwareVersionMatches": ltp8xONTAutoUpdateFirmwareVersionMatches,
       "ltp8xONTAutoUpdateDowngrade": ltp8xONTAutoUpdateDowngrade,
       "ltp8xONTAutoUpdateRowStatus": ltp8xONTAutoUpdateRowStatus,
       "ltp8xONTAutoUpdateEnabled": ltp8xONTAutoUpdateEnabled,
       "ltp8xONTAllocProfileTable": ltp8xONTAllocProfileTable,
       "ltp8xONTAllocProfileEntry": ltp8xONTAllocProfileEntry,
       "ltp8xONTAllocID": ltp8xONTAllocID,
       "ltp8xONTAllocDescription": ltp8xONTAllocDescription,
       "ltp8xONTAllocName": ltp8xONTAllocName,
       "ltp8xONTAllocServiceClass": ltp8xONTAllocServiceClass,
       "ltp8xONTAllocStatusReporting": ltp8xONTAllocStatusReporting,
       "ltp8xONTAllocSize": ltp8xONTAllocSize,
       "ltp8xONTAllocPeriod": ltp8xONTAllocPeriod,
       "ltp8xONTAllocFixedBandwidth": ltp8xONTAllocFixedBandwidth,
       "ltp8xONTAllocGuaranteedBandwidth": ltp8xONTAllocGuaranteedBandwidth,
       "ltp8xONTAllocBestEffortBandwidth": ltp8xONTAllocBestEffortBandwidth,
       "ltp8xONTAllocRowStatus": ltp8xONTAllocRowStatus,
       "ltp8xONTPortsProfileTable": ltp8xONTPortsProfileTable,
       "ltp8xONTPortsProfileEntry": ltp8xONTPortsProfileEntry,
       "ltp8xONTPortsID": ltp8xONTPortsID,
       "ltp8xONTPortsDescription": ltp8xONTPortsDescription,
       "ltp8xONTPortsName": ltp8xONTPortsName,
       "ltp8xONTPortsIGMPVersion": ltp8xONTPortsIGMPVersion,
       "ltp8xONTPortsIGMPUpstreamMode": ltp8xONTPortsIGMPUpstreamMode,
       "ltp8xONTPortsIGMPImmediateLeave": ltp8xONTPortsIGMPImmediateLeave,
       "ltp8xONTPortsIGMPRobustness": ltp8xONTPortsIGMPRobustness,
       "ltp8xONTPortsIGMPQuerierIP": ltp8xONTPortsIGMPQuerierIP,
       "ltp8xONTPortsIGMPQueryInterval": ltp8xONTPortsIGMPQueryInterval,
       "ltp8xONTPortsIGMPQueryMaxResponseTime": ltp8xONTPortsIGMPQueryMaxResponseTime,
       "ltp8xONTPortsIGMPLastMemberQueryInterval": ltp8xONTPortsIGMPLastMemberQueryInterval,
       "ltp8xONTPortsVEIPMulticastEnable": ltp8xONTPortsVEIPMulticastEnable,
       "ltp8xONTPortsVEIPIGMPUpstreamVID": ltp8xONTPortsVEIPIGMPUpstreamVID,
       "ltp8xONTPortsVEIPIGMPUpstreamPriority": ltp8xONTPortsVEIPIGMPUpstreamPriority,
       "ltp8xONTPortsVEIPIGMPUpstreamTagControl": ltp8xONTPortsVEIPIGMPUpstreamTagControl,
       "ltp8xONTPortsVEIPMaxGroups": ltp8xONTPortsVEIPMaxGroups,
       "ltp8xONTPortsVEIPMaxMulticastBandwidth": ltp8xONTPortsVEIPMaxMulticastBandwidth,
       "ltp8xONTPortsRowStatus": ltp8xONTPortsRowStatus,
       "ltp8xONTPortsVEIPIGMPDownstreamVID": ltp8xONTPortsVEIPIGMPDownstreamVID,
       "ltp8xONTPortsVEIPIGMPDownstreamPriority": ltp8xONTPortsVEIPIGMPDownstreamPriority,
       "ltp8xONTPortsVEIPIGMPDownstreamTagControl": ltp8xONTPortsVEIPIGMPDownstreamTagControl,
       "ltp8xONTPortsMulticastIPVersion": ltp8xONTPortsMulticastIPVersion,
       "ltp8xONTPortsMLDVersion": ltp8xONTPortsMLDVersion,
       "ltp8xONTPortsMLDUpstreamMode": ltp8xONTPortsMLDUpstreamMode,
       "ltp8xONTPortsMLDImmediateLeave": ltp8xONTPortsMLDImmediateLeave,
       "ltp8xONTPortsMLDRobustness": ltp8xONTPortsMLDRobustness,
       "ltp8xONTPortsMLDQuerierIP": ltp8xONTPortsMLDQuerierIP,
       "ltp8xONTPortsMLDQueryInterval": ltp8xONTPortsMLDQueryInterval,
       "ltp8xONTPortsMLDQueryMaxResponseTime": ltp8xONTPortsMLDQueryMaxResponseTime,
       "ltp8xONTPortsMLDLastMemberQueryInterval": ltp8xONTPortsMLDLastMemberQueryInterval,
       "ltp8xONTPortsProfileUNITable": ltp8xONTPortsProfileUNITable,
       "ltp8xONTPortsProfileUNIEntry": ltp8xONTPortsProfileUNIEntry,
       "ltp8xONTPortsUNIPort": ltp8xONTPortsUNIPort,
       "ltp8xONTPortsUNIBridgeGroup": ltp8xONTPortsUNIBridgeGroup,
       "ltp8xONTPortsUNIMulticastEnabled": ltp8xONTPortsUNIMulticastEnabled,
       "ltp8xONTPortsUNIIGMPUpstreamVID": ltp8xONTPortsUNIIGMPUpstreamVID,
       "ltp8xONTPortsUNIIGMPUpstreamPriority": ltp8xONTPortsUNIIGMPUpstreamPriority,
       "ltp8xONTPortsUNIIGMPUpstreamTagControl": ltp8xONTPortsUNIIGMPUpstreamTagControl,
       "ltp8xONTPortsUNIMaxGroups": ltp8xONTPortsUNIMaxGroups,
       "ltp8xONTPortsUNIMaxMulticastBandwidth": ltp8xONTPortsUNIMaxMulticastBandwidth,
       "ltp8xONTPortsUNIShapingDownstreamEnabled": ltp8xONTPortsUNIShapingDownstreamEnabled,
       "ltp8xONTPortsUNIShapingDownstreamCommitedRate": ltp8xONTPortsUNIShapingDownstreamCommitedRate,
       "ltp8xONTPortsUNIShapingDownstreamPeakRate": ltp8xONTPortsUNIShapingDownstreamPeakRate,
       "ltp8xONTPortsUNIShapingUpstreamEnabled": ltp8xONTPortsUNIShapingUpstreamEnabled,
       "ltp8xONTPortsUNIShapingUpstreamCommitedRate": ltp8xONTPortsUNIShapingUpstreamCommitedRate,
       "ltp8xONTPortsUNIShapingUpstreamPeakRate": ltp8xONTPortsUNIShapingUpstreamPeakRate,
       "ltp8xONTPortsUNIIGMPDownstreamVID": ltp8xONTPortsUNIIGMPDownstreamVID,
       "ltp8xONTPortsUNIIGMPDownstreamPriority": ltp8xONTPortsUNIIGMPDownstreamPriority,
       "ltp8xONTPortsUNIIGMPDownstreamTagControl": ltp8xONTPortsUNIIGMPDownstreamTagControl,
       "ltp8xONTVoiceProfileTable": ltp8xONTVoiceProfileTable,
       "ltp8xONTVoiceProfileEntry": ltp8xONTVoiceProfileEntry,
       "ltp8xONTVoiceID": ltp8xONTVoiceID,
       "ltp8xONTVoiceDescription": ltp8xONTVoiceDescription,
       "ltp8xONTVoiceName": ltp8xONTVoiceName,
       "ltp8xONTVoiceCrossConnect": ltp8xONTVoiceCrossConnect,
       "ltp8xONTVoiceRowStatus": ltp8xONTVoiceRowStatus,
       "ltp8xONTScriptingProfiles": ltp8xONTScriptingProfiles,
       "ltp8xONTScriptingProfileTable": ltp8xONTScriptingProfileTable,
       "ltp8xONTScriptingProfileEntry": ltp8xONTScriptingProfileEntry,
       "ltp8xONTScriptingID": ltp8xONTScriptingID,
       "ltp8xONTScriptingDescription": ltp8xONTScriptingDescription,
       "ltp8xONTScriptingName": ltp8xONTScriptingName,
       "ltp8xONTScriptingRowStatus": ltp8xONTScriptingRowStatus,
       "ltp8xONTScriptingProfileScriptsTable": ltp8xONTScriptingProfileScriptsTable,
       "ltp8xONTScriptingProfileScriptsEntry": ltp8xONTScriptingProfileScriptsEntry,
       "ltp8xONTScriptingChunkID": ltp8xONTScriptingChunkID,
       "ltp8xONTScriptingText": ltp8xONTScriptingText,
       "ltp8xONTPortsProfileMCDynamicEntriesTable": ltp8xONTPortsProfileMCDynamicEntriesTable,
       "ltp8xONTPortsProfileMCDynamicEntriesEntry": ltp8xONTPortsProfileMCDynamicEntriesEntry,
       "ltp8xONTPortsMCEntryID": ltp8xONTPortsMCEntryID,
       "ltp8xONTPortsMCVLANID": ltp8xONTPortsMCVLANID,
       "ltp8xONTPortsMCFirstGroupIP": ltp8xONTPortsMCFirstGroupIP,
       "ltp8xONTPortsMCLastGroupIP": ltp8xONTPortsMCLastGroupIP,
       "ltp8xONTPortsProfileMLDDynamicEntriesTable": ltp8xONTPortsProfileMLDDynamicEntriesTable,
       "ltp8xONTPortsProfileMLDDynamicEntriesEntry": ltp8xONTPortsProfileMLDDynamicEntriesEntry,
       "ltp8xONTPortsMLDEntryID": ltp8xONTPortsMLDEntryID,
       "ltp8xONTPortsMLDVLANID": ltp8xONTPortsMLDVLANID,
       "ltp8xONTPortsMLDMCFirstGroupIP": ltp8xONTPortsMLDMCFirstGroupIP,
       "ltp8xONTPortsMLDMCLastGroupIP": ltp8xONTPortsMLDMCLastGroupIP,
       "ltp8xONTPortsMLDMCPreviewLength": ltp8xONTPortsMLDMCPreviewLength,
       "ltp8xONTPortsMLDMCPreviewRepeatTime": ltp8xONTPortsMLDMCPreviewRepeatTime,
       "ltp8xONTPortsMLDMCPreviewRepeatCount": ltp8xONTPortsMLDMCPreviewRepeatCount,
       "ltp8xONTPortsMLDMCPreviewResetTime": ltp8xONTPortsMLDMCPreviewResetTime,
       "ltp8xONTMulticastStatsTable": ltp8xONTMulticastStatsTable,
       "ltp8xONTMulticastStatsEntry": ltp8xONTMulticastStatsEntry,
       "ltp8xONTMulticastStatsSlot": ltp8xONTMulticastStatsSlot,
       "ltp8xONTMulticastStatsONTSerial": ltp8xONTMulticastStatsONTSerial,
       "ltp8xONTMulticastStatsRecordID": ltp8xONTMulticastStatsRecordID,
       "ltp8xONTMulticastStatsMulticastAddress": ltp8xONTMulticastStatsMulticastAddress,
       "ltp8xONTMulticastStatsStart": ltp8xONTMulticastStatsStart,
       "ltp8xONTMulticastStatsStop": ltp8xONTMulticastStatsStop,
       "ltp8xONTACSPropertiesTable": ltp8xONTACSPropertiesTable,
       "ltp8xONTACSPropertiesEntry": ltp8xONTACSPropertiesEntry,
       "ltp8xONTACSPropertiesONTSerial": ltp8xONTACSPropertiesONTSerial,
       "ltp8xONTACSPropertiesPropertyID": ltp8xONTACSPropertiesPropertyID,
       "ltp8xONTACSPropertiesPropertyName": ltp8xONTACSPropertiesPropertyName,
       "ltp8xONTACSPropertiesPropertyValue": ltp8xONTACSPropertiesPropertyValue,
       "ltp8xONTACSPropertiesRowStatus": ltp8xONTACSPropertiesRowStatus,
       "ltp8xONTACSPropertiesTableSupported": ltp8xONTACSPropertiesTableSupported,
       "ltp8xONTACSPrivatesConfigTable": ltp8xONTACSPrivatesConfigTable,
       "ltp8xONTACSPrivatesConfigEntry": ltp8xONTACSPrivatesConfigEntry,
       "ltp8xONTACSPrivatesPropertyName": ltp8xONTACSPrivatesPropertyName,
       "ltp8xONTACSPrivatesPrivateIndex": ltp8xONTACSPrivatesPrivateIndex,
       "ltp8xONTACSPrivatesPrivateName": ltp8xONTACSPrivatesPrivateName,
       "ltp8xONTACSPrivatesRowStatus": ltp8xONTACSPrivatesRowStatus,
       "ltp8xONTACSUserPropertiesTable": ltp8xONTACSUserPropertiesTable,
       "ltp8xONTACSUserPropertiesEntry": ltp8xONTACSUserPropertiesEntry,
       "ltp8xONTACSUserPropertiesName": ltp8xONTACSUserPropertiesName,
       "ltp8xONTACSUserPropertiesSerial": ltp8xONTACSUserPropertiesSerial,
       "ltp8xONTACSUserPropertiesValue": ltp8xONTACSUserPropertiesValue,
       "ltp8xONTConnectionLogTable": ltp8xONTConnectionLogTable,
       "ltp8xONTConnectionLogEntry": ltp8xONTConnectionLogEntry,
       "ltp8xONTConnectionLogSlot": ltp8xONTConnectionLogSlot,
       "ltp8xONTConnectionLogONTSerial": ltp8xONTConnectionLogONTSerial,
       "ltp8xONTConnectionLogText": ltp8xONTConnectionLogText,
       "ltp8xONTConfigFreenessTable": ltp8xONTConfigFreenessTable,
       "ltp8xONTConfigFreenessEntry": ltp8xONTConfigFreenessEntry,
       "ltp8xONTConfigFreenessSlot": ltp8xONTConfigFreenessSlot,
       "ltp8xONTConfigFreenessChannel": ltp8xONTConfigFreenessChannel,
       "ltp8xONTConfigFreenessID": ltp8xONTConfigFreenessID,
       "ltp8xONTConfigFreenessSerial": ltp8xONTConfigFreenessSerial,
       "ltp8xONTDisable": ltp8xONTDisable,
       "ltp8xONTDisableSlot": ltp8xONTDisableSlot,
       "ltp8xONTDisableONTSerial": ltp8xONTDisableONTSerial,
       "ltp8xONTDisableChannel": ltp8xONTDisableChannel,
       "ltp8xONTDisableActionDisable": ltp8xONTDisableActionDisable,
       "ltp8xONTDisableActionEnable": ltp8xONTDisableActionEnable,
       "ltp8xOLT": ltp8xOLT,
       "ltp8xOLTStateTable": ltp8xOLTStateTable,
       "ltp8xOLTStateEntry": ltp8xOLTStateEntry,
       "ltp8xOLTStateSlot": ltp8xOLTStateSlot,
       "ltp8xOLTStateDriverVersion": ltp8xOLTStateDriverVersion,
       "ltp8xOLTStateFirmwareVersion": ltp8xOLTStateFirmwareVersion,
       "ltp8xOLTStateHardwareVersion": ltp8xOLTStateHardwareVersion,
       "ltp8xOLTStateFirmwareVersionChip2": ltp8xOLTStateFirmwareVersionChip2,
       "ltp8xOLTStateHardwareVersionChip2": ltp8xOLTStateHardwareVersionChip2,
       "ltp8xOLTStateReconfigure": ltp8xOLTStateReconfigure,
       "ltp8xOLTMIBBoundary1": ltp8xOLTMIBBoundary1,
       "ltp8xOLTDhcpRATable": ltp8xOLTDhcpRATable,
       "ltp8xOLTDhcpRAEntry": ltp8xOLTDhcpRAEntry,
       "ltp8xOLTDhcpRASlot": ltp8xOLTDhcpRASlot,
       "ltp8xOLTMIBBoundary2": ltp8xOLTMIBBoundary2,
       "ltp8xOLTConfigActivationTable": ltp8xOLTConfigActivationTable,
       "ltp8xOLTConfigActivationEntry": ltp8xOLTConfigActivationEntry,
       "ltp8xOLTConfigActivationSlot": ltp8xOLTConfigActivationSlot,
       "ltp8xOLTConfigActivationPeriod": ltp8xOLTConfigActivationPeriod,
       "ltp8xOLTConfigActivationCheckPassword": ltp8xOLTConfigActivationCheckPassword,
       "ltp8xOLTMIBBoundary3": ltp8xOLTMIBBoundary3,
       "ltp8xOLTConfigDhcpTable": ltp8xOLTConfigDhcpTable,
       "ltp8xOLTConfigDhcpEntry": ltp8xOLTConfigDhcpEntry,
       "ltp8xOLTConfigDhcpSlot": ltp8xOLTConfigDhcpSlot,
       "ltp8xOLTConfigDhcpRelayAgentEnabled": ltp8xOLTConfigDhcpRelayAgentEnabled,
       "ltp8xOLTConfigDhcpCircuitIDFormat": ltp8xOLTConfigDhcpCircuitIDFormat,
       "ltp8xOLTConfigDhcpRemoteIDFormat": ltp8xOLTConfigDhcpRemoteIDFormat,
       "ltp8xOLTConfigDhcpOverwrtOption82": ltp8xOLTConfigDhcpOverwrtOption82,
       "ltp8xOLTConfigDhcpDosBlockEnabled": ltp8xOLTConfigDhcpDosBlockEnabled,
       "ltp8xOLTConfigDhcpBcPacketPerSecond": ltp8xOLTConfigDhcpBcPacketPerSecond,
       "ltp8xOLTConfigDhcpPortBlockTime": ltp8xOLTConfigDhcpPortBlockTime,
       "ltp8xOLTConfigDhcpTrustedServerEnabled": ltp8xOLTConfigDhcpTrustedServerEnabled,
       "ltp8xOLTConfigDhcpTrustedPrimary": ltp8xOLTConfigDhcpTrustedPrimary,
       "ltp8xOLTConfigDhcpTrustedSecondary": ltp8xOLTConfigDhcpTrustedSecondary,
       "ltp8xOLTConfigDhcpTrustedServerTimeout": ltp8xOLTConfigDhcpTrustedServerTimeout,
       "ltp8xOLTMIBBoundary4": ltp8xOLTMIBBoundary4,
       "ltp8xOLTConfigPPPoETable": ltp8xOLTConfigPPPoETable,
       "ltp8xOLTConfigPPPoEEntry": ltp8xOLTConfigPPPoEEntry,
       "ltp8xOLTConfigPPPoESlot": ltp8xOLTConfigPPPoESlot,
       "ltp8xOLTConfigPPPoEPlusEnabled": ltp8xOLTConfigPPPoEPlusEnabled,
       "ltp8xOLTConfigPPPoECircuitIDFormat": ltp8xOLTConfigPPPoECircuitIDFormat,
       "ltp8xOLTConfigPPPoERemoteIDFormat": ltp8xOLTConfigPPPoERemoteIDFormat,
       "ltp8xOLTConfigPPPoEVendorID": ltp8xOLTConfigPPPoEVendorID,
       "ltp8xOLTConfigPPPoEMaxSessions": ltp8xOLTConfigPPPoEMaxSessions,
       "ltp8xOLTConfigPPPoEMaxSessionsPerUser": ltp8xOLTConfigPPPoEMaxSessionsPerUser,
       "ltp8xOLTConfigPPPoEDosBlockEnabled": ltp8xOLTConfigPPPoEDosBlockEnabled,
       "ltp8xOLTConfigPPPoEBcPacketPerSecond": ltp8xOLTConfigPPPoEBcPacketPerSecond,
       "ltp8xOLTConfigPPPoEPortBlockTime": ltp8xOLTConfigPPPoEPortBlockTime,
       "ltp8xOLTMIBBoundary5": ltp8xOLTMIBBoundary5,
       "ltp8xOLTPPPoESessionsTable": ltp8xOLTPPPoESessionsTable,
       "ltp8xOLTPPPoESessionsEntry": ltp8xOLTPPPoESessionsEntry,
       "ltp8xOLTPPPoESessionsSlot": ltp8xOLTPPPoESessionsSlot,
       "ltp8xOLTPPPoESessionsChannel": ltp8xOLTPPPoESessionsChannel,
       "ltp8xOLTPPPoESessionsOntID": ltp8xOLTPPPoESessionsOntID,
       "ltp8xOLTPPPoESessionsClientMac": ltp8xOLTPPPoESessionsClientMac,
       "ltp8xOLTPPPoESessionsPort": ltp8xOLTPPPoESessionsPort,
       "ltp8xOLTPPPoESessionsSessionID": ltp8xOLTPPPoESessionsSessionID,
       "ltp8xOLTPPPoESessionsDuration": ltp8xOLTPPPoESessionsDuration,
       "ltp8xOLTPPPoESessionsUnblock": ltp8xOLTPPPoESessionsUnblock,
       "ltp8xOLTPPPoESessionsSerial": ltp8xOLTPPPoESessionsSerial,
       "ltp8xOLTMIBBoundary6": ltp8xOLTMIBBoundary6,
       "ltp8xOLTMulticastStatsTable": ltp8xOLTMulticastStatsTable,
       "ltp8xOLTMulticastStatsEntry": ltp8xOLTMulticastStatsEntry,
       "ltp8xOLTMulticastStatsSlot": ltp8xOLTMulticastStatsSlot,
       "ltp8xOLTMulticastStatsChannel": ltp8xOLTMulticastStatsChannel,
       "ltp8xOLTMulticastStatsRecordID": ltp8xOLTMulticastStatsRecordID,
       "ltp8xOLTMulticastStatsONTSerial": ltp8xOLTMulticastStatsONTSerial,
       "ltp8xOLTMulticastStatsMulticastAddress": ltp8xOLTMulticastStatsMulticastAddress,
       "ltp8xOLTMulticastStatsStart": ltp8xOLTMulticastStatsStart,
       "ltp8xOLTMulticastStatsStop": ltp8xOLTMulticastStatsStop,
       "ltp8xOLTMIBBoundary7": ltp8xOLTMIBBoundary7,
       "ltp8xOLTAddressTableProfilesTable": ltp8xOLTAddressTableProfilesTable,
       "ltp8xOLTAddressTableProfilesEntry": ltp8xOLTAddressTableProfilesEntry,
       "ltp8xOLTAddressTableProfilesID": ltp8xOLTAddressTableProfilesID,
       "ltp8xOLTAddressTableProfilesDescription": ltp8xOLTAddressTableProfilesDescription,
       "ltp8xOLTMIBBoundary8": ltp8xOLTMIBBoundary8,
       "ltp8xOLTVlanProfilesTable": ltp8xOLTVlanProfilesTable,
       "ltp8xOLTVlanProfilesEntry": ltp8xOLTVlanProfilesEntry,
       "ltp8xOLTVlanProfilesID": ltp8xOLTVlanProfilesID,
       "ltp8xOLTVlanProfilesDescription": ltp8xOLTVlanProfilesDescription,
       "ltp8xOLTUpdateFirmwareTable": ltp8xOLTUpdateFirmwareTable,
       "ltp8xOLTUpdateFirmwareEntry": ltp8xOLTUpdateFirmwareEntry,
       "ltp8xOLTUpdateFirmwareSlot": ltp8xOLTUpdateFirmwareSlot,
       "ltp8xOLTUpdateFirmwareAction": ltp8xOLTUpdateFirmwareAction,
       "ltp8xOLTMulticastStatsBackwardsTable": ltp8xOLTMulticastStatsBackwardsTable,
       "ltp8xOLTMulticastStatsBackwardsEntry": ltp8xOLTMulticastStatsBackwardsEntry,
       "ltp8xOLTMulticastStatsBackwardsSlot": ltp8xOLTMulticastStatsBackwardsSlot,
       "ltp8xOLTMulticastStatsBackwardsONTSerial": ltp8xOLTMulticastStatsBackwardsONTSerial,
       "ltp8xOLTMulticastStatsBackwardsRecordID": ltp8xOLTMulticastStatsBackwardsRecordID,
       "ltp8xOLTMulticastStatsBackwardsMulticastAddress": ltp8xOLTMulticastStatsBackwardsMulticastAddress,
       "ltp8xOLTMulticastStatsBackwardsStart": ltp8xOLTMulticastStatsBackwardsStart,
       "ltp8xOLTMulticastStatsBackwardsStop": ltp8xOLTMulticastStatsBackwardsStop,
       "ltp8xOLTONTAutoFirmwareUpdateTable": ltp8xOLTONTAutoFirmwareUpdateTable,
       "ltp8xOLTONTAutoFirmwareUpdateEntry": ltp8xOLTONTAutoFirmwareUpdateEntry,
       "ltp8xOLTONTAutoFirmwareUpdateSlot": ltp8xOLTONTAutoFirmwareUpdateSlot,
       "ltp8xOLTONTAutoFirmwareUpdateEnabled": ltp8xOLTONTAutoFirmwareUpdateEnabled,
       "ltp8xOLTVInterfaceMonitoringDSTable": ltp8xOLTVInterfaceMonitoringDSTable,
       "ltp8xOLTVInterfaceMonitoringDSEntry": ltp8xOLTVInterfaceMonitoringDSEntry,
       "ltp8xOLTVInterfaceMonitoringDSSlot": ltp8xOLTVInterfaceMonitoringDSSlot,
       "ltp8xOLTVInterfaceMonitoringDSChannelRange": ltp8xOLTVInterfaceMonitoringDSChannelRange,
       "ltp8xOLTVInterfaceMonitoringDSCounterID": ltp8xOLTVInterfaceMonitoringDSCounterID,
       "ltp8xOLTVInterfaceMonitoringDSCounterName": ltp8xOLTVInterfaceMonitoringDSCounterName,
       "ltp8xOLTVInterfaceMonitoringDSCounterValue": ltp8xOLTVInterfaceMonitoringDSCounterValue,
       "ltp8xOLTVInterfaceMonitoringUSTable": ltp8xOLTVInterfaceMonitoringUSTable,
       "ltp8xOLTVInterfaceMonitoringUSEntry": ltp8xOLTVInterfaceMonitoringUSEntry,
       "ltp8xOLTVInterfaceMonitoringUSSlot": ltp8xOLTVInterfaceMonitoringUSSlot,
       "ltp8xOLTVInterfaceMonitoringUSChannelRange": ltp8xOLTVInterfaceMonitoringUSChannelRange,
       "ltp8xOLTVInterfaceMonitoringUSCounterID": ltp8xOLTVInterfaceMonitoringUSCounterID,
       "ltp8xOLTVInterfaceMonitoringUSCounterName": ltp8xOLTVInterfaceMonitoringUSCounterName,
       "ltp8xOLTVInterfaceMonitoringUSCounterValue": ltp8xOLTVInterfaceMonitoringUSCounterValue,
       "ltp8xOLTResetCountersTable": ltp8xOLTResetCountersTable,
       "ltp8xOLTResetCountersEntry": ltp8xOLTResetCountersEntry,
       "ltp8xOLTResetCountersSlot": ltp8xOLTResetCountersSlot,
       "ltp8xOLTResetCountersAction": ltp8xOLTResetCountersAction,
       "ltp8xOLTTerminalVLANsTable": ltp8xOLTTerminalVLANsTable,
       "ltp8xOLTTerminalVLANsEntry": ltp8xOLTTerminalVLANsEntry,
       "ltp8xOLTTerminalVLANsSlot": ltp8xOLTTerminalVLANsSlot,
       "ltp8xOLTTerminalVLANsID": ltp8xOLTTerminalVLANsID,
       "ltp8xOLTTerminalVLANsName": ltp8xOLTTerminalVLANsName,
       "ltp8xOLTTerminalVLANsVID": ltp8xOLTTerminalVLANsVID,
       "ltp8xOLTTerminalVLANsCOS": ltp8xOLTTerminalVLANsCOS,
       "ltp8xOLTTerminalVLANsRowStatus": ltp8xOLTTerminalVLANsRowStatus,
       "ltp8xOLTTerminalVLANsNamesTable": ltp8xOLTTerminalVLANsNamesTable,
       "ltp8xOLTTerminalVLANsNamesEntry": ltp8xOLTTerminalVLANsNamesEntry,
       "ltp8xOLTTerminalVLANsNamesID": ltp8xOLTTerminalVLANsNamesID,
       "ltp8xOLTTerminalVLANsNamesName": ltp8xOLTTerminalVLANsNamesName,
       "ltp8xOLTTerminalVLANsNamesRowStatus": ltp8xOLTTerminalVLANsNamesRowStatus,
       "ltp8xSwitch": ltp8xSwitch,
       "ltp8xSwitchPortsTable": ltp8xSwitchPortsTable,
       "ltp8xSwitchPortsEntry": ltp8xSwitchPortsEntry,
       "ltp8xSwitchPortsID": ltp8xSwitchPortsID,
       "ltp8xSwitchPortsName": ltp8xSwitchPortsName,
       "ltp8xSwitchVLANTable": ltp8xSwitchVLANTable,
       "ltp8xSwitchVLANEntry": ltp8xSwitchVLANEntry,
       "ltp8xSwitchVLANSlot": ltp8xSwitchVLANSlot,
       "ltp8xSwitchVLANVid": ltp8xSwitchVLANVid,
       "ltp8xSwitchVLANName": ltp8xSwitchVLANName,
       "ltp8xSwitchVLANTaggedPorts": ltp8xSwitchVLANTaggedPorts,
       "ltp8xSwitchVLANUntaggedPorts": ltp8xSwitchVLANUntaggedPorts,
       "ltp8xSwitchVLANRowStatus": ltp8xSwitchVLANRowStatus,
       "ltp8xSwitchVLANIGMPSnoopingEnabled": ltp8xSwitchVLANIGMPSnoopingEnabled,
       "ltp8xSwitchVLANIGMPSnoopingQuerierEnabled": ltp8xSwitchVLANIGMPSnoopingQuerierEnabled,
       "ltp8xSwitchVLANMLDSnoopingEnabled": ltp8xSwitchVLANMLDSnoopingEnabled,
       "ltp8xSwitchVLANMLDSnoopingQuerierEnabled": ltp8xSwitchVLANMLDSnoopingQuerierEnabled,
       "ltp8xSwitchIGMPSnoopingTable": ltp8xSwitchIGMPSnoopingTable,
       "ltp8xSwitchIGMPSnoopingEntry": ltp8xSwitchIGMPSnoopingEntry,
       "ltp8xSwitchIGMPSnoopingSlot": ltp8xSwitchIGMPSnoopingSlot,
       "ltp8xSwitchIGMPSnoopingEnabled": ltp8xSwitchIGMPSnoopingEnabled,
       "ltp8xSwitchMLDSnoopingEnabled": ltp8xSwitchMLDSnoopingEnabled,
       "ltp8xSwitchOperationalVLANTable": ltp8xSwitchOperationalVLANTable,
       "ltp8xSwitchOperationalVLANEntry": ltp8xSwitchOperationalVLANEntry,
       "ltp8xSwitchOperationalVLANSlot": ltp8xSwitchOperationalVLANSlot,
       "ltp8xSwitchOperationalVLANVid": ltp8xSwitchOperationalVLANVid,
       "ltp8xSwitchOperationalVLANName": ltp8xSwitchOperationalVLANName,
       "ltp8xSwitchOperationalVLANTaggedPorts": ltp8xSwitchOperationalVLANTaggedPorts,
       "ltp8xSwitchOperationalVLANUntaggedPorts": ltp8xSwitchOperationalVLANUntaggedPorts,
       "ltp8xSwitchPortCountersTable": ltp8xSwitchPortCountersTable,
       "ltp8xSwitchPortCountersEntry": ltp8xSwitchPortCountersEntry,
       "ltp8xSwitchPortCountersSlot": ltp8xSwitchPortCountersSlot,
       "ltp8xSwitchPortCountersPortID": ltp8xSwitchPortCountersPortID,
       "ltp8xSwitchPortGoodOctetsRcv": ltp8xSwitchPortGoodOctetsRcv,
       "ltp8xSwitchPortBadOctetsRcv": ltp8xSwitchPortBadOctetsRcv,
       "ltp8xSwitchPortMacTransmitErr": ltp8xSwitchPortMacTransmitErr,
       "ltp8xSwitchPortGoodPktsRcv": ltp8xSwitchPortGoodPktsRcv,
       "ltp8xSwitchPortBadPktsRcv": ltp8xSwitchPortBadPktsRcv,
       "ltp8xSwitchPortBrdcPktsRcv": ltp8xSwitchPortBrdcPktsRcv,
       "ltp8xSwitchPortMcPktsRcv": ltp8xSwitchPortMcPktsRcv,
       "ltp8xSwitchPortPkts64Octets": ltp8xSwitchPortPkts64Octets,
       "ltp8xSwitchPortPkts65to127Octets": ltp8xSwitchPortPkts65to127Octets,
       "ltp8xSwitchPortPkts128to255Octets": ltp8xSwitchPortPkts128to255Octets,
       "ltp8xSwitchPortPkts256to511Octets": ltp8xSwitchPortPkts256to511Octets,
       "ltp8xSwitchPortPkts512to1023Octets": ltp8xSwitchPortPkts512to1023Octets,
       "ltp8xSwitchPortPkts1024tomaxOctets": ltp8xSwitchPortPkts1024tomaxOctets,
       "ltp8xSwitchPortGoodOctetsSent": ltp8xSwitchPortGoodOctetsSent,
       "ltp8xSwitchPortGoodPktsSent": ltp8xSwitchPortGoodPktsSent,
       "ltp8xSwitchPortExcessiveCollisions": ltp8xSwitchPortExcessiveCollisions,
       "ltp8xSwitchPortMcPktsSent": ltp8xSwitchPortMcPktsSent,
       "ltp8xSwitchPortBrdcPktsSent": ltp8xSwitchPortBrdcPktsSent,
       "ltp8xSwitchPortUnrecogMacCntrRcv": ltp8xSwitchPortUnrecogMacCntrRcv,
       "ltp8xSwitchPortFcSent": ltp8xSwitchPortFcSent,
       "ltp8xSwitchPortGoodFcRcv": ltp8xSwitchPortGoodFcRcv,
       "ltp8xSwitchPortDropEvents": ltp8xSwitchPortDropEvents,
       "ltp8xSwitchPortUndersizePkts": ltp8xSwitchPortUndersizePkts,
       "ltp8xSwitchPortFragmentsPkts": ltp8xSwitchPortFragmentsPkts,
       "ltp8xSwitchPortOversizePkts": ltp8xSwitchPortOversizePkts,
       "ltp8xSwitchPortJabberPkts": ltp8xSwitchPortJabberPkts,
       "ltp8xSwitchPortMacRcvError": ltp8xSwitchPortMacRcvError,
       "ltp8xSwitchPortBadCrc": ltp8xSwitchPortBadCrc,
       "ltp8xSwitchPortCollisions": ltp8xSwitchPortCollisions,
       "ltp8xSwitchPortLateCollisions": ltp8xSwitchPortLateCollisions,
       "ltp8xSwitchPortBadFcRcv": ltp8xSwitchPortBadFcRcv,
       "ltp8xSwitchPortCountersReset": ltp8xSwitchPortCountersReset,
       "ltp8xSwitchMacListTable": ltp8xSwitchMacListTable,
       "ltp8xSwitchMacListEntry": ltp8xSwitchMacListEntry,
       "ltp8xSwitchMacListSlot": ltp8xSwitchMacListSlot,
       "ltp8xSwitchMacListVID": ltp8xSwitchMacListVID,
       "ltp8xSwitchMacListMacAddress": ltp8xSwitchMacListMacAddress,
       "ltp8xSwitchMacListInterface": ltp8xSwitchMacListInterface,
       "ltp8xSwitchMacListStatic": ltp8xSwitchMacListStatic,
       "ltp8xSwitchMacListMacAddressString": ltp8xSwitchMacListMacAddressString,
       "ltp8xSwitchPortsUtilization": ltp8xSwitchPortsUtilization,
       "ltp8xPortsUtilizationInterval": ltp8xPortsUtilizationInterval,
       "ltp8xPortsUtilizationTable": ltp8xPortsUtilizationTable,
       "ltp8xPortsUtilizationEntry": ltp8xPortsUtilizationEntry,
       "ltp8xPortsUtilizationSlot": ltp8xPortsUtilizationSlot,
       "ltp8xPortsUtilizationPortID": ltp8xPortsUtilizationPortID,
       "ltp8xPortsUtilizationLastKbitsSent": ltp8xPortsUtilizationLastKbitsSent,
       "ltp8xPortsUtilizationLastKbitsRecv": ltp8xPortsUtilizationLastKbitsRecv,
       "ltp8xPortsUtilizationLastFramesSent": ltp8xPortsUtilizationLastFramesSent,
       "ltp8xPortsUtilizationLastFramesRecv": ltp8xPortsUtilizationLastFramesRecv,
       "ltp8xPortsUtilizationAverageKbitsSent": ltp8xPortsUtilizationAverageKbitsSent,
       "ltp8xPortsUtilizationAverageKbitsRecv": ltp8xPortsUtilizationAverageKbitsRecv,
       "ltp8xPortsUtilizationAverageFramesSent": ltp8xPortsUtilizationAverageFramesSent,
       "ltp8xPortsUtilizationAverageFramesRecv": ltp8xPortsUtilizationAverageFramesRecv,
       "ltp8xQOSConfig": ltp8xQOSConfig,
       "ltp8xQOSConfigTable": ltp8xQOSConfigTable,
       "ltp8xQOSConfigEntry": ltp8xQOSConfigEntry,
       "ltp8xQOSConfigSlot": ltp8xQOSConfigSlot,
       "ltp8xQOSDefaultQueue": ltp8xQOSDefaultQueue,
       "ltp8xQOSType": ltp8xQOSType,
       "ltp8xQOSDownstreamQinQPrioritization": ltp8xQOSDownstreamQinQPrioritization,
       "ltp8xQOS8021pMappingTable": ltp8xQOS8021pMappingTable,
       "ltp8xQOS8021pMappingEntry": ltp8xQOS8021pMappingEntry,
       "ltp8xQOS8021pMappingSlot": ltp8xQOS8021pMappingSlot,
       "ltp8xQOS8021pMappingQueue": ltp8xQOS8021pMappingQueue,
       "ltp8xQOS8021pMappingFields": ltp8xQOS8021pMappingFields,
       "ltp8xQOSDSCPMappingTable": ltp8xQOSDSCPMappingTable,
       "ltp8xQOSDSCPMappingEntry": ltp8xQOSDSCPMappingEntry,
       "ltp8xQOSDSCPMappingSlot": ltp8xQOSDSCPMappingSlot,
       "ltp8xQOSDSCPMappingQueue": ltp8xQOSDSCPMappingQueue,
       "ltp8xQOSDSCPMappingFields": ltp8xQOSDSCPMappingFields,
       "ltp8xACLConfig": ltp8xACLConfig,
       "ltp8xACLGlobalModeTable": ltp8xACLGlobalModeTable,
       "ltp8xACLGlobalModeEntry": ltp8xACLGlobalModeEntry,
       "ltp8xACLGlobalModeSlot": ltp8xACLGlobalModeSlot,
       "ltp8xACLGlobalMode": ltp8xACLGlobalMode,
       "ltp8xACLListsTable": ltp8xACLListsTable,
       "ltp8xACLListsEntry": ltp8xACLListsEntry,
       "ltp8xACLListsSlot": ltp8xACLListsSlot,
       "ltp8xACLListsID": ltp8xACLListsID,
       "ltp8xACLListsName": ltp8xACLListsName,
       "ltp8xACLListsPorts": ltp8xACLListsPorts,
       "ltp8xACLListsFiltersCount": ltp8xACLListsFiltersCount,
       "ltp8xACLListsRowStatus": ltp8xACLListsRowStatus,
       "ltp8xACLFiltersTable": ltp8xACLFiltersTable,
       "ltp8xACLFiltersEntry": ltp8xACLFiltersEntry,
       "ltp8xACLFiltersSlot": ltp8xACLFiltersSlot,
       "ltp8xACLFiltersListID": ltp8xACLFiltersListID,
       "ltp8xACLFiltersFilterID": ltp8xACLFiltersFilterID,
       "ltp8xACLFiltersType": ltp8xACLFiltersType,
       "ltp8xACLFiltersMacAddress": ltp8xACLFiltersMacAddress,
       "ltp8xACLFiltersIpAddress": ltp8xACLFiltersIpAddress,
       "ltp8xACLFiltersProtocol": ltp8xACLFiltersProtocol,
       "ltp8xACLFiltersPort": ltp8xACLFiltersPort,
       "ltp8xACLFiltersRowStatus": ltp8xACLFiltersRowStatus,
       "ltp8xIGMPProxyReportTable": ltp8xIGMPProxyReportTable,
       "ltp8xIGMPProxyReportEntry": ltp8xIGMPProxyReportEntry,
       "ltp8xIGMPProxyReportSlot": ltp8xIGMPProxyReportSlot,
       "ltp8xIGMPProxyReportEnabled": ltp8xIGMPProxyReportEnabled,
       "ltp8xMLDProxyReportEnabled": ltp8xMLDProxyReportEnabled,
       "ltp8xIGMPProxyReportRangesTable": ltp8xIGMPProxyReportRangesTable,
       "ltp8xIGMPProxyReportRangesEntry": ltp8xIGMPProxyReportRangesEntry,
       "ltp8xIGMPProxyReportRangesSlot": ltp8xIGMPProxyReportRangesSlot,
       "ltp8xIGMPProxyReportRangesID": ltp8xIGMPProxyReportRangesID,
       "ltp8xIGMPProxyReportRangesStart": ltp8xIGMPProxyReportRangesStart,
       "ltp8xIGMPProxyReportRangesEnd": ltp8xIGMPProxyReportRangesEnd,
       "ltp8xIGMPProxyReportRangesFromVLAN": ltp8xIGMPProxyReportRangesFromVLAN,
       "ltp8xIGMPProxyReportRangesToVLAN": ltp8xIGMPProxyReportRangesToVLAN,
       "ltp8xIGMPProxyRowStatus": ltp8xIGMPProxyRowStatus,
       "ltp8xIGMPProxyReportRangesGlobalTable": ltp8xIGMPProxyReportRangesGlobalTable,
       "ltp8xIGMPProxyReportRangesGlobalEntry": ltp8xIGMPProxyReportRangesGlobalEntry,
       "ltp8xIGMPProxyReportRangesGlobalID": ltp8xIGMPProxyReportRangesGlobalID,
       "ltp8xIGMPProxyReportRangesGlobalStart": ltp8xIGMPProxyReportRangesGlobalStart,
       "ltp8xIGMPProxyReportRangesGlobalEnd": ltp8xIGMPProxyReportRangesGlobalEnd,
       "ltp8xIGMPProxyReportRangesGlobalFromVLAN": ltp8xIGMPProxyReportRangesGlobalFromVLAN,
       "ltp8xIGMPProxyReportRangesGlobalToVLAN": ltp8xIGMPProxyReportRangesGlobalToVLAN,
       "ltp8xIGMPProxyGlobalRowStatus": ltp8xIGMPProxyGlobalRowStatus,
       "ltp8xMLDProxyReportRangesTable": ltp8xMLDProxyReportRangesTable,
       "ltp8xMLDProxyReportRangesEntry": ltp8xMLDProxyReportRangesEntry,
       "ltp8xMLDProxyReportRangesSlot": ltp8xMLDProxyReportRangesSlot,
       "ltp8xMLDProxyReportRangesID": ltp8xMLDProxyReportRangesID,
       "ltp8xMLDProxyReportRangesStart": ltp8xMLDProxyReportRangesStart,
       "ltp8xMLDProxyReportRangesEnd": ltp8xMLDProxyReportRangesEnd,
       "ltp8xMLDProxyReportRangesFromVLAN": ltp8xMLDProxyReportRangesFromVLAN,
       "ltp8xMLDProxyReportRangesToVLAN": ltp8xMLDProxyReportRangesToVLAN,
       "ltp8xMLDProxyRowStatus": ltp8xMLDProxyRowStatus,
       "ltp8xMLDProxyReportRangesGlobalTable": ltp8xMLDProxyReportRangesGlobalTable,
       "ltp8xMLDProxyReportRangesGlobalEntry": ltp8xMLDProxyReportRangesGlobalEntry,
       "ltp8xMLDProxyReportRangesGlobalID": ltp8xMLDProxyReportRangesGlobalID,
       "ltp8xMLDProxyReportRangesGlobalStart": ltp8xMLDProxyReportRangesGlobalStart,
       "ltp8xMLDProxyReportRangesGlobalEnd": ltp8xMLDProxyReportRangesGlobalEnd,
       "ltp8xMLDProxyReportRangesGlobalFromVLAN": ltp8xMLDProxyReportRangesGlobalFromVLAN,
       "ltp8xMLDProxyReportRangesGlobalToVLAN": ltp8xMLDProxyReportRangesGlobalToVLAN,
       "ltp8xMLDProxyGlobalRowStatus": ltp8xMLDProxyGlobalRowStatus,
       "ltp8xP2PTable": ltp8xP2PTable,
       "ltp8xP2PEntry": ltp8xP2PEntry,
       "ltp8xP2PSlot": ltp8xP2PSlot,
       "ltp8xP2PEnabled": ltp8xP2PEnabled,
       "ltp8xPLC": ltp8xPLC,
       "ltp8xPLCBoardStateTable": ltp8xPLCBoardStateTable,
       "ltp8xPLCBoardStateEntry": ltp8xPLCBoardStateEntry,
       "ltp8xPLCBoardStateSlot": ltp8xPLCBoardStateSlot,
       "ltp8xPLCBoardStateRAMFree": ltp8xPLCBoardStateRAMFree,
       "ltp8xPLCBoardStateLoadAverage1Minute": ltp8xPLCBoardStateLoadAverage1Minute,
       "ltp8xPLCBoardStateLoadAverage5Minutes": ltp8xPLCBoardStateLoadAverage5Minutes,
       "ltp8xPLCBoardStateLoadAverage15Minutes": ltp8xPLCBoardStateLoadAverage15Minutes,
       "ltp8xPLCBoardStateSensor1Temperature": ltp8xPLCBoardStateSensor1Temperature,
       "ltp8xPLCBoardStateSensor2Temperature": ltp8xPLCBoardStateSensor2Temperature,
       "ltp8xPLCBoardStateUptime": ltp8xPLCBoardStateUptime,
       "ltp8xPLCBoardStateSerialNumber": ltp8xPLCBoardStateSerialNumber,
       "ltp8xPLCBoardStateFirmwareRevision": ltp8xPLCBoardStateFirmwareRevision,
       "ltp8xPLCBoardStateDiskFreeSpace": ltp8xPLCBoardStateDiskFreeSpace,
       "ltp8xPLCBoardStateModuleVersion": ltp8xPLCBoardStateModuleVersion,
       "ltp8xPLCBoardStateBuildTime": ltp8xPLCBoardStateBuildTime,
       "ltp8xPLCBoardStateBuildRevision": ltp8xPLCBoardStateBuildRevision,
       "ltp8xPLCBoardStateHardwareVesion": ltp8xPLCBoardStateHardwareVesion,
       "ltp8xPLCBoardStateSensor1TemperatureExt": ltp8xPLCBoardStateSensor1TemperatureExt,
       "ltp8xPLCBoardStateSensor2TemperatureExt": ltp8xPLCBoardStateSensor2TemperatureExt,
       "ltp8xSyncCounters": ltp8xSyncCounters,
       "ltp8xSyncCountersTable": ltp8xSyncCountersTable,
       "ltp8xSyncCountersEntry": ltp8xSyncCountersEntry,
       "ltp8xSyncCountersSlot": ltp8xSyncCountersSlot,
       "ltp8xSyncCountersConfig": ltp8xSyncCountersConfig,
       "ltp8xSyncCountersState": ltp8xSyncCountersState,
       "ltp8xRawData": ltp8xRawData,
       "ltp8xRawMacTable": ltp8xRawMacTable,
       "ltp8xRawMacEntry": ltp8xRawMacEntry,
       "ltp8xRawMacSlot": ltp8xRawMacSlot,
       "ltp8xRawMacChunkID": ltp8xRawMacChunkID,
       "ltp8xRawMacText": ltp8xRawMacText,
       "ltp8xRawSwitchMacTable": ltp8xRawSwitchMacTable,
       "ltp8xRawSwitchMacEntry": ltp8xRawSwitchMacEntry,
       "ltp8xRawSwitchMacSlot": ltp8xRawSwitchMacSlot,
       "ltp8xRawSwitchMacChunkID": ltp8xRawSwitchMacChunkID,
       "ltp8xRawSwitchMacText": ltp8xRawSwitchMacText,
       "ltp8xMIBBoundary": ltp8xMIBBoundary,
       "ltp8xTraps": ltp8xTraps,
       "ltp8xAlarmTraps": ltp8xAlarmTraps,
       "ltp8xLoadAverageAlarmTrap": ltp8xLoadAverageAlarmTrap,
       "ltp8xRAMAlarmTrap": ltp8xRAMAlarmTrap,
       "ltp8xLoginAlarmTrap": ltp8xLoginAlarmTrap,
       "ltp8xConfigSaveAlarmTrap": ltp8xConfigSaveAlarmTrap,
       "ltp8xFirmwareUpdateAlarmTrap": ltp8xFirmwareUpdateAlarmTrap,
       "ltp8xDuplicateMacAlarmTrap": ltp8xDuplicateMacAlarmTrap,
       "ltp8xDataLinkLayerAlarmTrap": ltp8xDataLinkLayerAlarmTrap,
       "ltp8xPhysicalLayerFlappingAlarmTrap": ltp8xPhysicalLayerFlappingAlarmTrap,
       "ltp8xDataLinkLayerFlappingAlarmTrap": ltp8xDataLinkLayerFlappingAlarmTrap,
       "ltp8xInterfaceCriticalLoadAlarmTrap": ltp8xInterfaceCriticalLoadAlarmTrap,
       "ltp8xFreeSpaceAlarmTrap": ltp8xFreeSpaceAlarmTrap,
       "ltp8xTemperatureAlarmTrap": ltp8xTemperatureAlarmTrap,
       "ltp8xFanAlarmTrap": ltp8xFanAlarmTrap,
       "ltp8xOntAlarmTrap": ltp8xOntAlarmTrap,
       "ltp8xOntPhysicalAlarmTrap": ltp8xOntPhysicalAlarmTrap,
       "ltp8xOltUpdateAlarmTrap": ltp8xOltUpdateAlarmTrap,
       "ltp8xOntUpdateAlarmTrap": ltp8xOntUpdateAlarmTrap,
       "ltp8xChannelFlappingAlarmTrap": ltp8xChannelFlappingAlarmTrap,
       "ltp8xOntFlappingAlarmTrap": ltp8xOntFlappingAlarmTrap,
       "ltp8xFileDownloadAlarmTrap": ltp8xFileDownloadAlarmTrap,
       "ltp8xBatteryPowerAlarmTrap": ltp8xBatteryPowerAlarmTrap,
       "ltp8xBatteryLowAlarmTrap": ltp8xBatteryLowAlarmTrap,
       "ltp8xLanLosAlarmTrap": ltp8xLanLosAlarmTrap,
       "ltp8xOntConfigAlarmTrap": ltp8xOntConfigAlarmTrap,
       "ltp8xOntFirmwareDeleteAlarmTrap": ltp8xOntFirmwareDeleteAlarmTrap,
       "ltp8xLowRxPowerAlarmTrap": ltp8xLowRxPowerAlarmTrap,
       "ltp8xPowerSupplyAlarmTrap": ltp8xPowerSupplyAlarmTrap,
       "ltp8xRedundancyMasterChannelFailTrap": ltp8xRedundancyMasterChannelFailTrap,
       "ltp8xPonAlarmChannelTrap": ltp8xPonAlarmChannelTrap,
       "ltp8xPonAlarmONUiTrap": ltp8xPonAlarmONUiTrap,
       "ltp8xONTSignalDegradeTrap": ltp8xONTSignalDegradeTrap,
       "ltp8xONTHighRecvOpticalPwrTrap": ltp8xONTHighRecvOpticalPwrTrap,
       "ltp8xOLTDeviceNotWorkingTrap": ltp8xOLTDeviceNotWorkingTrap,
       "ltp8xChannelOntCntOverflowTrap": ltp8xChannelOntCntOverflowTrap,
       "ltp8xConfigRereadAlarmTrap": ltp8xConfigRereadAlarmTrap,
       "ltp8xConfigBrokenAlarmTrap": ltp8xConfigBrokenAlarmTrap,
       "ltp8xOkTraps": ltp8xOkTraps,
       "ltp8xLoadAverageOkTrap": ltp8xLoadAverageOkTrap,
       "ltp8xRAMOkTrap": ltp8xRAMOkTrap,
       "ltp8xLoginOkTrap": ltp8xLoginOkTrap,
       "ltp8xConfigSaveOkTrap": ltp8xConfigSaveOkTrap,
       "ltp8xFirmwareUpdateOkTrap": ltp8xFirmwareUpdateOkTrap,
       "ltp8xDuplicateMacOkTrap": ltp8xDuplicateMacOkTrap,
       "ltp8xDataLinkLayerOkTrap": ltp8xDataLinkLayerOkTrap,
       "ltp8xPhysicalLayerFlappingOkTrap": ltp8xPhysicalLayerFlappingOkTrap,
       "ltp8xDataLinkLayerFlappingOkTrap": ltp8xDataLinkLayerFlappingOkTrap,
       "ltp8xInterfaceCriticalLoadOkTrap": ltp8xInterfaceCriticalLoadOkTrap,
       "ltp8xFreeSpaceOkTrap": ltp8xFreeSpaceOkTrap,
       "ltp8xTemperatureOkTrap": ltp8xTemperatureOkTrap,
       "ltp8xFanOkTrap": ltp8xFanOkTrap,
       "ltp8xOntOkTrap": ltp8xOntOkTrap,
       "ltp8xOntPhysicalOkTrap": ltp8xOntPhysicalOkTrap,
       "ltp8xOltUpdateOkTrap": ltp8xOltUpdateOkTrap,
       "ltp8xOntUpdateOkTrap": ltp8xOntUpdateOkTrap,
       "ltp8xChannelFlappingOkTrap": ltp8xChannelFlappingOkTrap,
       "ltp8xOntFlappingOkTrap": ltp8xOntFlappingOkTrap,
       "ltp8xFileDownloadOkTrap": ltp8xFileDownloadOkTrap,
       "ltp8xBatteryPowerOkTrap": ltp8xBatteryPowerOkTrap,
       "ltp8xBatteryLowOkTrap": ltp8xBatteryLowOkTrap,
       "ltp8xLanLosOkTrap": ltp8xLanLosOkTrap,
       "ltp8xOntConfigOkTrap": ltp8xOntConfigOkTrap,
       "ltp8xOntFirmwareDeleteOkTrap": ltp8xOntFirmwareDeleteOkTrap,
       "ltp8xLowRxPowerOkTrap": ltp8xLowRxPowerOkTrap,
       "ltp8xPowerSupplyOkTrap": ltp8xPowerSupplyOkTrap,
       "ltp8xLogoutTrap": ltp8xLogoutTrap,
       "ltp8xOntDyingGaspTrap": ltp8xOntDyingGaspTrap,
       "ltp8xRedundantChannelSwitchTrap": ltp8xRedundantChannelSwitchTrap,
       "ltp8xONTREITrap": ltp8xONTREITrap,
       "ltp8xONTPowerOffTrap": ltp8xONTPowerOffTrap,
       "ltp8xConfigChangeTrap": ltp8xConfigChangeTrap,
       "ltp8xONTStateChangeTrap": ltp8xONTStateChangeTrap,
       "ltp8xONTConfigChangeTrap": ltp8xONTConfigChangeTrap,
       "ltp8xChannelStateChangeTrap": ltp8xChannelStateChangeTrap,
       "ltp8xOLTDeviceResetTrap": ltp8xOLTDeviceResetTrap,
       "ltp8xOLTDeviceWorkingTrap": ltp8xOLTDeviceWorkingTrap,
       "ltp8xChannelOntCntOverflowOkTrap": ltp8xChannelOntCntOverflowOkTrap,
       "ltp8xConfigRereadOkTrap": ltp8xConfigRereadOkTrap,
       "ltp8xRSSIUpdateTrap": ltp8xRSSIUpdateTrap,
       "plc8AlarmTraps": plc8AlarmTraps,
       "plc8LoadAverageAlarmTrap": plc8LoadAverageAlarmTrap,
       "plc8RAMAlarmTrap": plc8RAMAlarmTrap,
       "plc8LoginAlarmTrap": plc8LoginAlarmTrap,
       "plc8ConfigSaveAlarmTrap": plc8ConfigSaveAlarmTrap,
       "plc8FirmwareUpdateAlarmTrap": plc8FirmwareUpdateAlarmTrap,
       "plc8DuplicateMacAlarmTrap": plc8DuplicateMacAlarmTrap,
       "plc8DataLinkLayerAlarmTrap": plc8DataLinkLayerAlarmTrap,
       "plc8PhysicalLayerFlappingAlarmTrap": plc8PhysicalLayerFlappingAlarmTrap,
       "plc8DataLinkLayerFlappingAlarmTrap": plc8DataLinkLayerFlappingAlarmTrap,
       "plc8InterfaceCriticalLoadAlarmTrap": plc8InterfaceCriticalLoadAlarmTrap,
       "plc8FreeSpaceAlarmTrap": plc8FreeSpaceAlarmTrap,
       "plc8TemperatureAlarmTrap": plc8TemperatureAlarmTrap,
       "plc8FanAlarmTrap": plc8FanAlarmTrap,
       "plc8OntAlarmTrap": plc8OntAlarmTrap,
       "plc8OntPhysicalAlarmTrap": plc8OntPhysicalAlarmTrap,
       "plc8FileDownloadAlarmTrap": plc8FileDownloadAlarmTrap,
       "plc8BatteryPowerAlarmTrap": plc8BatteryPowerAlarmTrap,
       "plc8BatteryLowAlarmTrap": plc8BatteryLowAlarmTrap,
       "plc8LanLosAlarmTrap": plc8LanLosAlarmTrap,
       "plc8OntConfigAlarmTrap": plc8OntConfigAlarmTrap,
       "plc8LowRxPowerAlarmTrap": plc8LowRxPowerAlarmTrap,
       "plc8RedundancyMasterChannelFailTrap": plc8RedundancyMasterChannelFailTrap,
       "plc8PonAlarmChannelTrap": plc8PonAlarmChannelTrap,
       "plc8PonAlarmONUiTrap": plc8PonAlarmONUiTrap,
       "plc8ONTSignalDegradeTrap": plc8ONTSignalDegradeTrap,
       "plc8ONTHighRecvOpticalPwrTrap": plc8ONTHighRecvOpticalPwrTrap,
       "plc8OLTDeviceNotWorkingTrap": plc8OLTDeviceNotWorkingTrap,
       "plc8ChannelOntCntOverflowTrap": plc8ChannelOntCntOverflowTrap,
       "plc8OkTraps": plc8OkTraps,
       "plc8LoadAverageOkTrap": plc8LoadAverageOkTrap,
       "plc8RAMOkTrap": plc8RAMOkTrap,
       "plc8LoginOkTrap": plc8LoginOkTrap,
       "plc8ConfigSaveOkTrap": plc8ConfigSaveOkTrap,
       "plc8FirmwareUpdateOkTrap": plc8FirmwareUpdateOkTrap,
       "plc8DuplicateMacOkTrap": plc8DuplicateMacOkTrap,
       "plc8DataLinkLayerOkTrap": plc8DataLinkLayerOkTrap,
       "plc8PhysicalLayerFlappingOkTrap": plc8PhysicalLayerFlappingOkTrap,
       "plc8DataLinkLayerFlappingOkTrap": plc8DataLinkLayerFlappingOkTrap,
       "plc8InterfaceCriticalLoadOkTrap": plc8InterfaceCriticalLoadOkTrap,
       "plc8FreeSpaceOkTrap": plc8FreeSpaceOkTrap,
       "plc8TemperatureOkTrap": plc8TemperatureOkTrap,
       "plc8FanOkTrap": plc8FanOkTrap,
       "plc8OntOkTrap": plc8OntOkTrap,
       "plc8OntPhysicalOkTrap": plc8OntPhysicalOkTrap,
       "plc8FileDownloadOkTrap": plc8FileDownloadOkTrap,
       "plc8BatteryPowerOkTrap": plc8BatteryPowerOkTrap,
       "plc8BatteryLowOkTrap": plc8BatteryLowOkTrap,
       "plc8LanLosOkTrap": plc8LanLosOkTrap,
       "plc8OntConfigOkTrap": plc8OntConfigOkTrap,
       "plc8LowRxPowerOkTrap": plc8LowRxPowerOkTrap,
       "plc8OntDyingGaspTrap": plc8OntDyingGaspTrap,
       "plc8RedundantChannelSwitchTrap": plc8RedundantChannelSwitchTrap,
       "plc8ONTREITrap": plc8ONTREITrap,
       "plc8ONTPowerOffTrap": plc8ONTPowerOffTrap,
       "plc8ConfigChangeTrap": plc8ConfigChangeTrap,
       "plc8ONTStateChangeTrap": plc8ONTStateChangeTrap,
       "plc8ONTConfigChangeTrap": plc8ONTConfigChangeTrap,
       "plc8ChannelStateChangeTrap": plc8ChannelStateChangeTrap,
       "plc8OLTDeviceResetTrap": plc8OLTDeviceResetTrap,
       "plc8OLTDeviceWorkingTrap": plc8OLTDeviceWorkingTrap,
       "plc8ChannelOntCntOverflowOkTrap": plc8ChannelOntCntOverflowOkTrap,
       "plc8RSSIUpdateTrap": plc8RSSIUpdateTrap,
       "ltp8xObjectGroup": ltp8xObjectGroup,
       "ltp8xTrapsObjectGroup": ltp8xTrapsObjectGroup,
       "ltp4x": ltp4x}
)
