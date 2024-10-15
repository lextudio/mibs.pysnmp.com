# SNMP MIB module (KBRIDGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/KBRIDGE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:16:37 2024
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

karlnet = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 762)
)
karlnet.setRevisions(
        ("2002-01-28 12:00",
         "2001-07-17 12:00",
         "2001-05-09 12:00",
         "2000-09-18 12:00",
         "2000-07-25 12:00",
         "2000-07-11 12:00")
)


# Types definitions



class MacAddress(OctetString):
    """Custom type MacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Kbridge_mib_ObjectIdentity = ObjectIdentity
kbridge_mib = _Kbridge_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 762, 2)
)
_KarlNetKBControl_ObjectIdentity = ObjectIdentity
karlNetKBControl = _KarlNetKBControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 762, 2, 1)
)


class _KbControlReboot_Type(Integer32):
    """Custom type kbControlReboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_KbControlReboot_Type.__name__ = "Integer32"
_KbControlReboot_Object = MibScalar
kbControlReboot = _KbControlReboot_Object(
    (1, 3, 6, 1, 4, 1, 762, 2, 1, 6),
    _KbControlReboot_Type()
)
kbControlReboot.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    kbControlReboot.setStatus("current")


class _KbControlTestSNMPWrite_Type(Integer32):
    """Custom type kbControlTestSNMPWrite based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_KbControlTestSNMPWrite_Type.__name__ = "Integer32"
_KbControlTestSNMPWrite_Object = MibScalar
kbControlTestSNMPWrite = _KbControlTestSNMPWrite_Object(
    (1, 3, 6, 1, 4, 1, 762, 2, 1, 9),
    _KbControlTestSNMPWrite_Type()
)
kbControlTestSNMPWrite.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    kbControlTestSNMPWrite.setStatus("current")


class _KbControlShutdown_Type(Integer32):
    """Custom type kbControlShutdown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_KbControlShutdown_Type.__name__ = "Integer32"
_KbControlShutdown_Object = MibScalar
kbControlShutdown = _KbControlShutdown_Object(
    (1, 3, 6, 1, 4, 1, 762, 2, 1, 11),
    _KbControlShutdown_Type()
)
kbControlShutdown.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    kbControlShutdown.setStatus("current")
_KbControlTemperature_Type = Integer32
_KbControlTemperature_Object = MibScalar
kbControlTemperature = _KbControlTemperature_Object(
    (1, 3, 6, 1, 4, 1, 762, 2, 1, 12),
    _KbControlTemperature_Type()
)
kbControlTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kbControlTemperature.setStatus("current")
_KbWireless_ObjectIdentity = ObjectIdentity
kbWireless = _KbWireless_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 762, 2, 5)
)
_KbWirelessStationNumber_Type = Integer32
_KbWirelessStationNumber_Object = MibScalar
kbWirelessStationNumber = _KbWirelessStationNumber_Object(
    (1, 3, 6, 1, 4, 1, 762, 2, 5, 1),
    _KbWirelessStationNumber_Type()
)
kbWirelessStationNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kbWirelessStationNumber.setStatus("current")
_KbWirelessStationTable_Object = MibTable
kbWirelessStationTable = _KbWirelessStationTable_Object(
    (1, 3, 6, 1, 4, 1, 762, 2, 5, 2)
)
if mibBuilder.loadTexts:
    kbWirelessStationTable.setStatus("current")
_KbWirelessStationEntry_Object = MibTableRow
kbWirelessStationEntry = _KbWirelessStationEntry_Object(
    (1, 3, 6, 1, 4, 1, 762, 2, 5, 2, 1)
)
kbWirelessStationEntry.setIndexNames(
    (0, "KBRIDGE-MIB", "kbWirelessStationIndex"),
)
if mibBuilder.loadTexts:
    kbWirelessStationEntry.setStatus("current")


class _KbWirelessStationIndex_Type(Unsigned32):
    """Custom type kbWirelessStationIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_KbWirelessStationIndex_Type.__name__ = "Unsigned32"
_KbWirelessStationIndex_Object = MibTableColumn
kbWirelessStationIndex = _KbWirelessStationIndex_Object(
    (1, 3, 6, 1, 4, 1, 762, 2, 5, 2, 1, 1),
    _KbWirelessStationIndex_Type()
)
kbWirelessStationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kbWirelessStationIndex.setStatus("current")


class _KbWirelessStationInterfaceNumber_Type(Unsigned32):
    """Custom type kbWirelessStationInterfaceNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_KbWirelessStationInterfaceNumber_Type.__name__ = "Unsigned32"
_KbWirelessStationInterfaceNumber_Object = MibTableColumn
kbWirelessStationInterfaceNumber = _KbWirelessStationInterfaceNumber_Object(
    (1, 3, 6, 1, 4, 1, 762, 2, 5, 2, 1, 2),
    _KbWirelessStationInterfaceNumber_Type()
)
kbWirelessStationInterfaceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kbWirelessStationInterfaceNumber.setStatus("current")
_KbWirelessStationName_Type = OctetString
_KbWirelessStationName_Object = MibTableColumn
kbWirelessStationName = _KbWirelessStationName_Object(
    (1, 3, 6, 1, 4, 1, 762, 2, 5, 2, 1, 3),
    _KbWirelessStationName_Type()
)
kbWirelessStationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kbWirelessStationName.setStatus("current")
_KbWirelessStationExclHellos_Type = Counter32
_KbWirelessStationExclHellos_Object = MibTableColumn
kbWirelessStationExclHellos = _KbWirelessStationExclHellos_Object(
    (1, 3, 6, 1, 4, 1, 762, 2, 5, 2, 1, 4),
    _KbWirelessStationExclHellos_Type()
)
kbWirelessStationExclHellos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kbWirelessStationExclHellos.setStatus("current")
_KbWirelessStationGoodHellos_Type = Counter32
_KbWirelessStationGoodHellos_Object = MibTableColumn
kbWirelessStationGoodHellos = _KbWirelessStationGoodHellos_Object(
    (1, 3, 6, 1, 4, 1, 762, 2, 5, 2, 1, 5),
    _KbWirelessStationGoodHellos_Type()
)
kbWirelessStationGoodHellos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kbWirelessStationGoodHellos.setStatus("current")
_KbWirelessStationLowHellos_Type = Counter32
_KbWirelessStationLowHellos_Object = MibTableColumn
kbWirelessStationLowHellos = _KbWirelessStationLowHellos_Object(
    (1, 3, 6, 1, 4, 1, 762, 2, 5, 2, 1, 6),
    _KbWirelessStationLowHellos_Type()
)
kbWirelessStationLowHellos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kbWirelessStationLowHellos.setStatus("current")
_KbWirelessStationSignalLevel_Type = Gauge32
_KbWirelessStationSignalLevel_Object = MibTableColumn
kbWirelessStationSignalLevel = _KbWirelessStationSignalLevel_Object(
    (1, 3, 6, 1, 4, 1, 762, 2, 5, 2, 1, 7),
    _KbWirelessStationSignalLevel_Type()
)
kbWirelessStationSignalLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kbWirelessStationSignalLevel.setStatus("current")
_KbWirelessStationNoiseLevel_Type = Gauge32
_KbWirelessStationNoiseLevel_Object = MibTableColumn
kbWirelessStationNoiseLevel = _KbWirelessStationNoiseLevel_Object(
    (1, 3, 6, 1, 4, 1, 762, 2, 5, 2, 1, 8),
    _KbWirelessStationNoiseLevel_Type()
)
kbWirelessStationNoiseLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kbWirelessStationNoiseLevel.setStatus("current")
_KbWirelessStationSignalQuality_Type = Gauge32
_KbWirelessStationSignalQuality_Object = MibTableColumn
kbWirelessStationSignalQuality = _KbWirelessStationSignalQuality_Object(
    (1, 3, 6, 1, 4, 1, 762, 2, 5, 2, 1, 9),
    _KbWirelessStationSignalQuality_Type()
)
kbWirelessStationSignalQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kbWirelessStationSignalQuality.setStatus("current")
_KbWirelessStationPktTransmits_Type = Counter32
_KbWirelessStationPktTransmits_Object = MibTableColumn
kbWirelessStationPktTransmits = _KbWirelessStationPktTransmits_Object(
    (1, 3, 6, 1, 4, 1, 762, 2, 5, 2, 1, 10),
    _KbWirelessStationPktTransmits_Type()
)
kbWirelessStationPktTransmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kbWirelessStationPktTransmits.setStatus("current")
_KbWirelessStationMACAddress_Type = OctetString
_KbWirelessStationMACAddress_Object = MibTableColumn
kbWirelessStationMACAddress = _KbWirelessStationMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 762, 2, 5, 2, 1, 11),
    _KbWirelessStationMACAddress_Type()
)
kbWirelessStationMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kbWirelessStationMACAddress.setStatus("current")
_KbWirelessStationTransmits_Type = Counter32
_KbWirelessStationTransmits_Object = MibTableColumn
kbWirelessStationTransmits = _KbWirelessStationTransmits_Object(
    (1, 3, 6, 1, 4, 1, 762, 2, 5, 2, 1, 12),
    _KbWirelessStationTransmits_Type()
)
kbWirelessStationTransmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kbWirelessStationTransmits.setStatus("current")
_KbWirelessStationBadTransmits_Type = Counter32
_KbWirelessStationBadTransmits_Object = MibTableColumn
kbWirelessStationBadTransmits = _KbWirelessStationBadTransmits_Object(
    (1, 3, 6, 1, 4, 1, 762, 2, 5, 2, 1, 13),
    _KbWirelessStationBadTransmits_Type()
)
kbWirelessStationBadTransmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kbWirelessStationBadTransmits.setStatus("current")
_KbWirelessStationReTransmits_Type = Counter32
_KbWirelessStationReTransmits_Object = MibTableColumn
kbWirelessStationReTransmits = _KbWirelessStationReTransmits_Object(
    (1, 3, 6, 1, 4, 1, 762, 2, 5, 2, 1, 14),
    _KbWirelessStationReTransmits_Type()
)
kbWirelessStationReTransmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kbWirelessStationReTransmits.setStatus("current")
_KbWirelessStationIPAddress_Type = IpAddress
_KbWirelessStationIPAddress_Object = MibTableColumn
kbWirelessStationIPAddress = _KbWirelessStationIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 762, 2, 5, 2, 1, 15),
    _KbWirelessStationIPAddress_Type()
)
kbWirelessStationIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kbWirelessStationIPAddress.setStatus("current")


class _KbWirelessStationType_Type(Integer32):
    """Custom type kbWirelessStationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("compatibility-Mode", 1),
          ("tc-Base-Station", 3),
          ("tc-Peer-to-Peer", 2),
          ("tc-Polling-Base-Station", 5),
          ("tc-PtP-Controller", 6),
          ("tc-Satellite-Station", 4))
    )


_KbWirelessStationType_Type.__name__ = "Integer32"
_KbWirelessStationType_Object = MibTableColumn
kbWirelessStationType = _KbWirelessStationType_Object(
    (1, 3, 6, 1, 4, 1, 762, 2, 5, 2, 1, 16),
    _KbWirelessStationType_Type()
)
kbWirelessStationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kbWirelessStationType.setStatus("current")


class _KbWirelessStationSNR_Type(Integer32):
    """Custom type kbWirelessStationSNR based on Integer32"""
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
        *(("excellent-SNR", 4),
          ("good-SNR", 3),
          ("low-SNR", 2),
          ("unknown-SNR", 1))
    )


_KbWirelessStationSNR_Type.__name__ = "Integer32"
_KbWirelessStationSNR_Object = MibTableColumn
kbWirelessStationSNR = _KbWirelessStationSNR_Object(
    (1, 3, 6, 1, 4, 1, 762, 2, 5, 2, 1, 17),
    _KbWirelessStationSNR_Type()
)
kbWirelessStationSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kbWirelessStationSNR.setStatus("current")


class _KbWirelessStationState_Type(Integer32):
    """Custom type kbWirelessStationState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("offline", 2),
          ("online", 1))
    )


_KbWirelessStationState_Type.__name__ = "Integer32"
_KbWirelessStationState_Object = MibTableColumn
kbWirelessStationState = _KbWirelessStationState_Object(
    (1, 3, 6, 1, 4, 1, 762, 2, 5, 2, 1, 18),
    _KbWirelessStationState_Type()
)
kbWirelessStationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kbWirelessStationState.setStatus("current")
_KbWirelessPoll_Type = Counter32
_KbWirelessPoll_Object = MibTableColumn
kbWirelessPoll = _KbWirelessPoll_Object(
    (1, 3, 6, 1, 4, 1, 762, 2, 5, 2, 1, 19),
    _KbWirelessPoll_Type()
)
kbWirelessPoll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kbWirelessPoll.setStatus("current")
_KbWirelessPollData_Type = Counter32
_KbWirelessPollData_Object = MibTableColumn
kbWirelessPollData = _KbWirelessPollData_Object(
    (1, 3, 6, 1, 4, 1, 762, 2, 5, 2, 1, 20),
    _KbWirelessPollData_Type()
)
kbWirelessPollData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kbWirelessPollData.setStatus("current")
_KbWirelessPollNoData_Type = Counter32
_KbWirelessPollNoData_Object = MibTableColumn
kbWirelessPollNoData = _KbWirelessPollNoData_Object(
    (1, 3, 6, 1, 4, 1, 762, 2, 5, 2, 1, 21),
    _KbWirelessPollNoData_Type()
)
kbWirelessPollNoData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kbWirelessPollNoData.setStatus("current")
_KbWirelessPollMoreData_Type = Counter32
_KbWirelessPollMoreData_Object = MibTableColumn
kbWirelessPollMoreData = _KbWirelessPollMoreData_Object(
    (1, 3, 6, 1, 4, 1, 762, 2, 5, 2, 1, 22),
    _KbWirelessPollMoreData_Type()
)
kbWirelessPollMoreData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kbWirelessPollMoreData.setStatus("deprecated")
_KbWirelessPollTimeouts_Type = Counter32
_KbWirelessPollTimeouts_Object = MibTableColumn
kbWirelessPollTimeouts = _KbWirelessPollTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 762, 2, 5, 2, 1, 23),
    _KbWirelessPollTimeouts_Type()
)
kbWirelessPollTimeouts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kbWirelessPollTimeouts.setStatus("current")
_KbWirelessPollOfflines_Type = Counter32
_KbWirelessPollOfflines_Object = MibTableColumn
kbWirelessPollOfflines = _KbWirelessPollOfflines_Object(
    (1, 3, 6, 1, 4, 1, 762, 2, 5, 2, 1, 24),
    _KbWirelessPollOfflines_Type()
)
kbWirelessPollOfflines.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kbWirelessPollOfflines.setStatus("current")
_KbWirelessTestTime_Type = Counter32
_KbWirelessTestTime_Object = MibTableColumn
kbWirelessTestTime = _KbWirelessTestTime_Object(
    (1, 3, 6, 1, 4, 1, 762, 2, 5, 2, 1, 25),
    _KbWirelessTestTime_Type()
)
kbWirelessTestTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kbWirelessTestTime.setStatus("current")


class _KbWirelessTestInterval_Type(Unsigned32):
    """Custom type kbWirelessTestInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_KbWirelessTestInterval_Type.__name__ = "Unsigned32"
_KbWirelessTestInterval_Object = MibTableColumn
kbWirelessTestInterval = _KbWirelessTestInterval_Object(
    (1, 3, 6, 1, 4, 1, 762, 2, 5, 2, 1, 26),
    _KbWirelessTestInterval_Type()
)
kbWirelessTestInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kbWirelessTestInterval.setStatus("current")


class _KbWirelessTestPacketSize_Type(Integer32):
    """Custom type kbWirelessTestPacketSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_KbWirelessTestPacketSize_Type.__name__ = "Integer32"
_KbWirelessTestPacketSize_Object = MibTableColumn
kbWirelessTestPacketSize = _KbWirelessTestPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 762, 2, 5, 2, 1, 27),
    _KbWirelessTestPacketSize_Type()
)
kbWirelessTestPacketSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kbWirelessTestPacketSize.setStatus("current")
_KbWirelessTestOurTx_Type = Counter32
_KbWirelessTestOurTx_Object = MibTableColumn
kbWirelessTestOurTx = _KbWirelessTestOurTx_Object(
    (1, 3, 6, 1, 4, 1, 762, 2, 5, 2, 1, 28),
    _KbWirelessTestOurTx_Type()
)
kbWirelessTestOurTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kbWirelessTestOurTx.setStatus("current")
_KbWirelessTestOurRx_Type = Counter32
_KbWirelessTestOurRx_Object = MibTableColumn
kbWirelessTestOurRx = _KbWirelessTestOurRx_Object(
    (1, 3, 6, 1, 4, 1, 762, 2, 5, 2, 1, 29),
    _KbWirelessTestOurRx_Type()
)
kbWirelessTestOurRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kbWirelessTestOurRx.setStatus("current")
_KbWirelessTestHisTx_Type = Counter32
_KbWirelessTestHisTx_Object = MibTableColumn
kbWirelessTestHisTx = _KbWirelessTestHisTx_Object(
    (1, 3, 6, 1, 4, 1, 762, 2, 5, 2, 1, 30),
    _KbWirelessTestHisTx_Type()
)
kbWirelessTestHisTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kbWirelessTestHisTx.setStatus("current")
_KbWirelessTestHisRx_Type = Counter32
_KbWirelessTestHisRx_Object = MibTableColumn
kbWirelessTestHisRx = _KbWirelessTestHisRx_Object(
    (1, 3, 6, 1, 4, 1, 762, 2, 5, 2, 1, 31),
    _KbWirelessTestHisRx_Type()
)
kbWirelessTestHisRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kbWirelessTestHisRx.setStatus("current")
_KbWirelessTestOurCurSignalLevel_Type = Gauge32
_KbWirelessTestOurCurSignalLevel_Object = MibTableColumn
kbWirelessTestOurCurSignalLevel = _KbWirelessTestOurCurSignalLevel_Object(
    (1, 3, 6, 1, 4, 1, 762, 2, 5, 2, 1, 32),
    _KbWirelessTestOurCurSignalLevel_Type()
)
kbWirelessTestOurCurSignalLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kbWirelessTestOurCurSignalLevel.setStatus("current")
_KbWirelessTestOurCurNoiseLevel_Type = Gauge32
_KbWirelessTestOurCurNoiseLevel_Object = MibTableColumn
kbWirelessTestOurCurNoiseLevel = _KbWirelessTestOurCurNoiseLevel_Object(
    (1, 3, 6, 1, 4, 1, 762, 2, 5, 2, 1, 33),
    _KbWirelessTestOurCurNoiseLevel_Type()
)
kbWirelessTestOurCurNoiseLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kbWirelessTestOurCurNoiseLevel.setStatus("current")
_KbWirelessTestOurCurSignalQuality_Type = Gauge32
_KbWirelessTestOurCurSignalQuality_Object = MibTableColumn
kbWirelessTestOurCurSignalQuality = _KbWirelessTestOurCurSignalQuality_Object(
    (1, 3, 6, 1, 4, 1, 762, 2, 5, 2, 1, 34),
    _KbWirelessTestOurCurSignalQuality_Type()
)
kbWirelessTestOurCurSignalQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kbWirelessTestOurCurSignalQuality.setStatus("current")
_KbWirelessTestOurCurSNR_Type = Gauge32
_KbWirelessTestOurCurSNR_Object = MibTableColumn
kbWirelessTestOurCurSNR = _KbWirelessTestOurCurSNR_Object(
    (1, 3, 6, 1, 4, 1, 762, 2, 5, 2, 1, 35),
    _KbWirelessTestOurCurSNR_Type()
)
kbWirelessTestOurCurSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kbWirelessTestOurCurSNR.setStatus("current")
_KbWirelessTestOurMinSignalLevel_Type = Gauge32
_KbWirelessTestOurMinSignalLevel_Object = MibTableColumn
kbWirelessTestOurMinSignalLevel = _KbWirelessTestOurMinSignalLevel_Object(
    (1, 3, 6, 1, 4, 1, 762, 2, 5, 2, 1, 36),
    _KbWirelessTestOurMinSignalLevel_Type()
)
kbWirelessTestOurMinSignalLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kbWirelessTestOurMinSignalLevel.setStatus("current")
_KbWirelessTestOurMinNoiseLevel_Type = Gauge32
_KbWirelessTestOurMinNoiseLevel_Object = MibTableColumn
kbWirelessTestOurMinNoiseLevel = _KbWirelessTestOurMinNoiseLevel_Object(
    (1, 3, 6, 1, 4, 1, 762, 2, 5, 2, 1, 37),
    _KbWirelessTestOurMinNoiseLevel_Type()
)
kbWirelessTestOurMinNoiseLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kbWirelessTestOurMinNoiseLevel.setStatus("current")
_KbWirelessTestOurMinSignalQuality_Type = Gauge32
_KbWirelessTestOurMinSignalQuality_Object = MibTableColumn
kbWirelessTestOurMinSignalQuality = _KbWirelessTestOurMinSignalQuality_Object(
    (1, 3, 6, 1, 4, 1, 762, 2, 5, 2, 1, 38),
    _KbWirelessTestOurMinSignalQuality_Type()
)
kbWirelessTestOurMinSignalQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kbWirelessTestOurMinSignalQuality.setStatus("current")
_KbWirelessTestOurMinSNR_Type = Gauge32
_KbWirelessTestOurMinSNR_Object = MibTableColumn
kbWirelessTestOurMinSNR = _KbWirelessTestOurMinSNR_Object(
    (1, 3, 6, 1, 4, 1, 762, 2, 5, 2, 1, 39),
    _KbWirelessTestOurMinSNR_Type()
)
kbWirelessTestOurMinSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kbWirelessTestOurMinSNR.setStatus("current")
_KbWirelessTestOurMaxSignalLevel_Type = Gauge32
_KbWirelessTestOurMaxSignalLevel_Object = MibTableColumn
kbWirelessTestOurMaxSignalLevel = _KbWirelessTestOurMaxSignalLevel_Object(
    (1, 3, 6, 1, 4, 1, 762, 2, 5, 2, 1, 40),
    _KbWirelessTestOurMaxSignalLevel_Type()
)
kbWirelessTestOurMaxSignalLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kbWirelessTestOurMaxSignalLevel.setStatus("current")
_KbWirelessTestOurMaxNoiseLevel_Type = Gauge32
_KbWirelessTestOurMaxNoiseLevel_Object = MibTableColumn
kbWirelessTestOurMaxNoiseLevel = _KbWirelessTestOurMaxNoiseLevel_Object(
    (1, 3, 6, 1, 4, 1, 762, 2, 5, 2, 1, 41),
    _KbWirelessTestOurMaxNoiseLevel_Type()
)
kbWirelessTestOurMaxNoiseLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kbWirelessTestOurMaxNoiseLevel.setStatus("current")
_KbWirelessTestOurMaxSignalQuality_Type = Gauge32
_KbWirelessTestOurMaxSignalQuality_Object = MibTableColumn
kbWirelessTestOurMaxSignalQuality = _KbWirelessTestOurMaxSignalQuality_Object(
    (1, 3, 6, 1, 4, 1, 762, 2, 5, 2, 1, 42),
    _KbWirelessTestOurMaxSignalQuality_Type()
)
kbWirelessTestOurMaxSignalQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kbWirelessTestOurMaxSignalQuality.setStatus("current")
_KbWirelessTestOurMaxSNR_Type = Gauge32
_KbWirelessTestOurMaxSNR_Object = MibTableColumn
kbWirelessTestOurMaxSNR = _KbWirelessTestOurMaxSNR_Object(
    (1, 3, 6, 1, 4, 1, 762, 2, 5, 2, 1, 43),
    _KbWirelessTestOurMaxSNR_Type()
)
kbWirelessTestOurMaxSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kbWirelessTestOurMaxSNR.setStatus("current")
_KbWirelessTestHisCurSignalLevel_Type = Gauge32
_KbWirelessTestHisCurSignalLevel_Object = MibTableColumn
kbWirelessTestHisCurSignalLevel = _KbWirelessTestHisCurSignalLevel_Object(
    (1, 3, 6, 1, 4, 1, 762, 2, 5, 2, 1, 44),
    _KbWirelessTestHisCurSignalLevel_Type()
)
kbWirelessTestHisCurSignalLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kbWirelessTestHisCurSignalLevel.setStatus("current")
_KbWirelessTestHisCurNoiseLevel_Type = Gauge32
_KbWirelessTestHisCurNoiseLevel_Object = MibTableColumn
kbWirelessTestHisCurNoiseLevel = _KbWirelessTestHisCurNoiseLevel_Object(
    (1, 3, 6, 1, 4, 1, 762, 2, 5, 2, 1, 45),
    _KbWirelessTestHisCurNoiseLevel_Type()
)
kbWirelessTestHisCurNoiseLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kbWirelessTestHisCurNoiseLevel.setStatus("current")
_KbWirelessTestHisCurSignalQuality_Type = Gauge32
_KbWirelessTestHisCurSignalQuality_Object = MibTableColumn
kbWirelessTestHisCurSignalQuality = _KbWirelessTestHisCurSignalQuality_Object(
    (1, 3, 6, 1, 4, 1, 762, 2, 5, 2, 1, 46),
    _KbWirelessTestHisCurSignalQuality_Type()
)
kbWirelessTestHisCurSignalQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kbWirelessTestHisCurSignalQuality.setStatus("current")
_KbWirelessTestHisCurSNR_Type = Gauge32
_KbWirelessTestHisCurSNR_Object = MibTableColumn
kbWirelessTestHisCurSNR = _KbWirelessTestHisCurSNR_Object(
    (1, 3, 6, 1, 4, 1, 762, 2, 5, 2, 1, 47),
    _KbWirelessTestHisCurSNR_Type()
)
kbWirelessTestHisCurSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kbWirelessTestHisCurSNR.setStatus("current")
_KbWirelessTestHisMinSignalLevel_Type = Gauge32
_KbWirelessTestHisMinSignalLevel_Object = MibTableColumn
kbWirelessTestHisMinSignalLevel = _KbWirelessTestHisMinSignalLevel_Object(
    (1, 3, 6, 1, 4, 1, 762, 2, 5, 2, 1, 48),
    _KbWirelessTestHisMinSignalLevel_Type()
)
kbWirelessTestHisMinSignalLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kbWirelessTestHisMinSignalLevel.setStatus("current")
_KbWirelessTestHisMinNoiseLevel_Type = Gauge32
_KbWirelessTestHisMinNoiseLevel_Object = MibTableColumn
kbWirelessTestHisMinNoiseLevel = _KbWirelessTestHisMinNoiseLevel_Object(
    (1, 3, 6, 1, 4, 1, 762, 2, 5, 2, 1, 49),
    _KbWirelessTestHisMinNoiseLevel_Type()
)
kbWirelessTestHisMinNoiseLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kbWirelessTestHisMinNoiseLevel.setStatus("current")
_KbWirelessTestHisMinSignalQuality_Type = Gauge32
_KbWirelessTestHisMinSignalQuality_Object = MibTableColumn
kbWirelessTestHisMinSignalQuality = _KbWirelessTestHisMinSignalQuality_Object(
    (1, 3, 6, 1, 4, 1, 762, 2, 5, 2, 1, 50),
    _KbWirelessTestHisMinSignalQuality_Type()
)
kbWirelessTestHisMinSignalQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kbWirelessTestHisMinSignalQuality.setStatus("current")
_KbWirelessTestHisMinSNR_Type = Gauge32
_KbWirelessTestHisMinSNR_Object = MibTableColumn
kbWirelessTestHisMinSNR = _KbWirelessTestHisMinSNR_Object(
    (1, 3, 6, 1, 4, 1, 762, 2, 5, 2, 1, 51),
    _KbWirelessTestHisMinSNR_Type()
)
kbWirelessTestHisMinSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kbWirelessTestHisMinSNR.setStatus("current")
_KbWirelessTestHisMaxSignalLevel_Type = Gauge32
_KbWirelessTestHisMaxSignalLevel_Object = MibTableColumn
kbWirelessTestHisMaxSignalLevel = _KbWirelessTestHisMaxSignalLevel_Object(
    (1, 3, 6, 1, 4, 1, 762, 2, 5, 2, 1, 52),
    _KbWirelessTestHisMaxSignalLevel_Type()
)
kbWirelessTestHisMaxSignalLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kbWirelessTestHisMaxSignalLevel.setStatus("current")
_KbWirelessTestHisMaxNoiseLevel_Type = Gauge32
_KbWirelessTestHisMaxNoiseLevel_Object = MibTableColumn
kbWirelessTestHisMaxNoiseLevel = _KbWirelessTestHisMaxNoiseLevel_Object(
    (1, 3, 6, 1, 4, 1, 762, 2, 5, 2, 1, 53),
    _KbWirelessTestHisMaxNoiseLevel_Type()
)
kbWirelessTestHisMaxNoiseLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kbWirelessTestHisMaxNoiseLevel.setStatus("current")
_KbWirelessTestHisMaxSignalQuality_Type = Gauge32
_KbWirelessTestHisMaxSignalQuality_Object = MibTableColumn
kbWirelessTestHisMaxSignalQuality = _KbWirelessTestHisMaxSignalQuality_Object(
    (1, 3, 6, 1, 4, 1, 762, 2, 5, 2, 1, 54),
    _KbWirelessTestHisMaxSignalQuality_Type()
)
kbWirelessTestHisMaxSignalQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kbWirelessTestHisMaxSignalQuality.setStatus("current")
_KbWirelessTestHisMaxSNR_Type = Gauge32
_KbWirelessTestHisMaxSNR_Object = MibTableColumn
kbWirelessTestHisMaxSNR = _KbWirelessTestHisMaxSNR_Object(
    (1, 3, 6, 1, 4, 1, 762, 2, 5, 2, 1, 55),
    _KbWirelessTestHisMaxSNR_Type()
)
kbWirelessTestHisMaxSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kbWirelessTestHisMaxSNR.setStatus("current")


class _KbWirelessTestLinkUp_Type(Integer32):
    """Custom type kbWirelessTestLinkUp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1))
    )


_KbWirelessTestLinkUp_Type.__name__ = "Integer32"
_KbWirelessTestLinkUp_Object = MibTableColumn
kbWirelessTestLinkUp = _KbWirelessTestLinkUp_Object(
    (1, 3, 6, 1, 4, 1, 762, 2, 5, 2, 1, 56),
    _KbWirelessTestLinkUp_Type()
)
kbWirelessTestLinkUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kbWirelessTestLinkUp.setStatus("current")
_KbWirelessTestLostLink_Type = Integer32
_KbWirelessTestLostLink_Object = MibTableColumn
kbWirelessTestLostLink = _KbWirelessTestLostLink_Object(
    (1, 3, 6, 1, 4, 1, 762, 2, 5, 2, 1, 57),
    _KbWirelessTestLostLink_Type()
)
kbWirelessTestLostLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kbWirelessTestLostLink.setStatus("current")
_KbWirelessTestLostTestPkts_Type = Integer32
_KbWirelessTestLostTestPkts_Object = MibTableColumn
kbWirelessTestLostTestPkts = _KbWirelessTestLostTestPkts_Object(
    (1, 3, 6, 1, 4, 1, 762, 2, 5, 2, 1, 58),
    _KbWirelessTestLostTestPkts_Type()
)
kbWirelessTestLostTestPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kbWirelessTestLostTestPkts.setStatus("current")


class _KbWirelessStationRadioType_Type(Integer32):
    """Custom type kbWirelessStationRadioType based on Integer32"""
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
        *(("clarion-M10", 1),
          ("microwave", 3),
          ("radioLAN", 4),
          ("waveLAN-I", 0),
          ("waveLAN-IEEE", 2))
    )


_KbWirelessStationRadioType_Type.__name__ = "Integer32"
_KbWirelessStationRadioType_Object = MibTableColumn
kbWirelessStationRadioType = _KbWirelessStationRadioType_Object(
    (1, 3, 6, 1, 4, 1, 762, 2, 5, 2, 1, 59),
    _KbWirelessStationRadioType_Type()
)
kbWirelessStationRadioType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kbWirelessStationRadioType.setStatus("current")


class _KbWirelessRecordType_Type(Integer32):
    """Custom type kbWirelessRecordType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("combination", 3),
          ("linktest", 1),
          ("turboCell", 2))
    )


_KbWirelessRecordType_Type.__name__ = "Integer32"
_KbWirelessRecordType_Object = MibTableColumn
kbWirelessRecordType = _KbWirelessRecordType_Object(
    (1, 3, 6, 1, 4, 1, 762, 2, 5, 2, 1, 60),
    _KbWirelessRecordType_Type()
)
kbWirelessRecordType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kbWirelessRecordType.setStatus("current")
_KbWirelessStationPktReceives_Type = Counter32
_KbWirelessStationPktReceives_Object = MibTableColumn
kbWirelessStationPktReceives = _KbWirelessStationPktReceives_Object(
    (1, 3, 6, 1, 4, 1, 762, 2, 5, 2, 1, 61),
    _KbWirelessStationPktReceives_Type()
)
kbWirelessStationPktReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kbWirelessStationPktReceives.setStatus("current")
_KbWirelessStationReceives_Type = Counter32
_KbWirelessStationReceives_Object = MibTableColumn
kbWirelessStationReceives = _KbWirelessStationReceives_Object(
    (1, 3, 6, 1, 4, 1, 762, 2, 5, 2, 1, 62),
    _KbWirelessStationReceives_Type()
)
kbWirelessStationReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kbWirelessStationReceives.setStatus("current")
_KbWirelessStationBytesReceives_Type = Counter32
_KbWirelessStationBytesReceives_Object = MibTableColumn
kbWirelessStationBytesReceives = _KbWirelessStationBytesReceives_Object(
    (1, 3, 6, 1, 4, 1, 762, 2, 5, 2, 1, 63),
    _KbWirelessStationBytesReceives_Type()
)
kbWirelessStationBytesReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kbWirelessStationBytesReceives.setStatus("current")
_KbWirelessStationBytesTransmits_Type = Counter32
_KbWirelessStationBytesTransmits_Object = MibTableColumn
kbWirelessStationBytesTransmits = _KbWirelessStationBytesTransmits_Object(
    (1, 3, 6, 1, 4, 1, 762, 2, 5, 2, 1, 64),
    _KbWirelessStationBytesTransmits_Type()
)
kbWirelessStationBytesTransmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kbWirelessStationBytesTransmits.setStatus("current")
_KbWirelessRegistrationRecord_Type = OctetString
_KbWirelessRegistrationRecord_Object = MibTableColumn
kbWirelessRegistrationRecord = _KbWirelessRegistrationRecord_Object(
    (1, 3, 6, 1, 4, 1, 762, 2, 5, 2, 1, 65),
    _KbWirelessRegistrationRecord_Type()
)
kbWirelessRegistrationRecord.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kbWirelessRegistrationRecord.setStatus("obsolete")
_KbWirelessStationFragmentDiscards_Type = Counter32
_KbWirelessStationFragmentDiscards_Object = MibTableColumn
kbWirelessStationFragmentDiscards = _KbWirelessStationFragmentDiscards_Object(
    (1, 3, 6, 1, 4, 1, 762, 2, 5, 2, 1, 66),
    _KbWirelessStationFragmentDiscards_Type()
)
kbWirelessStationFragmentDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kbWirelessStationFragmentDiscards.setStatus("current")
_KbWirelessStationFragmentMissings_Type = Counter32
_KbWirelessStationFragmentMissings_Object = MibTableColumn
kbWirelessStationFragmentMissings = _KbWirelessStationFragmentMissings_Object(
    (1, 3, 6, 1, 4, 1, 762, 2, 5, 2, 1, 67),
    _KbWirelessStationFragmentMissings_Type()
)
kbWirelessStationFragmentMissings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kbWirelessStationFragmentMissings.setStatus("current")
_KbWirelessStationFragmentLostFrames_Type = Counter32
_KbWirelessStationFragmentLostFrames_Object = MibTableColumn
kbWirelessStationFragmentLostFrames = _KbWirelessStationFragmentLostFrames_Object(
    (1, 3, 6, 1, 4, 1, 762, 2, 5, 2, 1, 68),
    _KbWirelessStationFragmentLostFrames_Type()
)
kbWirelessStationFragmentLostFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kbWirelessStationFragmentLostFrames.setStatus("current")
_KbWirelessStationFragmentErrors_Type = Counter32
_KbWirelessStationFragmentErrors_Object = MibTableColumn
kbWirelessStationFragmentErrors = _KbWirelessStationFragmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 762, 2, 5, 2, 1, 69),
    _KbWirelessStationFragmentErrors_Type()
)
kbWirelessStationFragmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kbWirelessStationFragmentErrors.setStatus("current")
_KbSEC_ObjectIdentity = ObjectIdentity
kbSEC = _KbSEC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 762, 2, 8)
)
_KbSECClientTable_Object = MibTable
kbSECClientTable = _KbSECClientTable_Object(
    (1, 3, 6, 1, 4, 1, 762, 2, 8, 1)
)
if mibBuilder.loadTexts:
    kbSECClientTable.setStatus("current")
_KbSECClientEntry_Object = MibTableRow
kbSECClientEntry = _KbSECClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 762, 2, 8, 1, 1)
)
kbSECClientEntry.setIndexNames(
    (0, "KBRIDGE-MIB", "kbSECClientAddress"),
)
if mibBuilder.loadTexts:
    kbSECClientEntry.setStatus("current")
_KbSECClientAddress_Type = MacAddress
_KbSECClientAddress_Object = MibTableColumn
kbSECClientAddress = _KbSECClientAddress_Object(
    (1, 3, 6, 1, 4, 1, 762, 2, 8, 1, 1, 1),
    _KbSECClientAddress_Type()
)
kbSECClientAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kbSECClientAddress.setStatus("current")
_KbSECStationAddress_Type = MacAddress
_KbSECStationAddress_Object = MibTableColumn
kbSECStationAddress = _KbSECStationAddress_Object(
    (1, 3, 6, 1, 4, 1, 762, 2, 8, 1, 1, 2),
    _KbSECStationAddress_Type()
)
kbSECStationAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kbSECStationAddress.setStatus("current")
_KbClientInfo_ObjectIdentity = ObjectIdentity
kbClientInfo = _KbClientInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 762, 2, 9)
)
_KbClientInfoByNumberTable_Object = MibTable
kbClientInfoByNumberTable = _KbClientInfoByNumberTable_Object(
    (1, 3, 6, 1, 4, 1, 762, 2, 9, 1)
)
if mibBuilder.loadTexts:
    kbClientInfoByNumberTable.setStatus("current")
_KbClientInfoByNumberEntry_Object = MibTableRow
kbClientInfoByNumberEntry = _KbClientInfoByNumberEntry_Object(
    (1, 3, 6, 1, 4, 1, 762, 2, 9, 1, 1)
)
kbClientInfoByNumberEntry.setIndexNames(
    (0, "KBRIDGE-MIB", "kbCIbyNumberVirtualPort"),
)
if mibBuilder.loadTexts:
    kbClientInfoByNumberEntry.setStatus("current")


class _KbCIbyNumberVirtualPort_Type(Unsigned32):
    """Custom type kbCIbyNumberVirtualPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_KbCIbyNumberVirtualPort_Type.__name__ = "Unsigned32"
_KbCIbyNumberVirtualPort_Object = MibTableColumn
kbCIbyNumberVirtualPort = _KbCIbyNumberVirtualPort_Object(
    (1, 3, 6, 1, 4, 1, 762, 2, 9, 1, 1, 1),
    _KbCIbyNumberVirtualPort_Type()
)
kbCIbyNumberVirtualPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kbCIbyNumberVirtualPort.setStatus("current")
_KbCIbyNumberMACAddress_Type = MacAddress
_KbCIbyNumberMACAddress_Object = MibTableColumn
kbCIbyNumberMACAddress = _KbCIbyNumberMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 762, 2, 9, 1, 1, 2),
    _KbCIbyNumberMACAddress_Type()
)
kbCIbyNumberMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kbCIbyNumberMACAddress.setStatus("current")


class _KbCIByNumberInterfaceNum_Type(Unsigned32):
    """Custom type kbCIByNumberInterfaceNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_KbCIByNumberInterfaceNum_Type.__name__ = "Unsigned32"
_KbCIByNumberInterfaceNum_Object = MibTableColumn
kbCIByNumberInterfaceNum = _KbCIByNumberInterfaceNum_Object(
    (1, 3, 6, 1, 4, 1, 762, 2, 9, 1, 1, 3),
    _KbCIByNumberInterfaceNum_Type()
)
kbCIByNumberInterfaceNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kbCIByNumberInterfaceNum.setStatus("current")
_KbCIbyNumberStationName_Type = OctetString
_KbCIbyNumberStationName_Object = MibTableColumn
kbCIbyNumberStationName = _KbCIbyNumberStationName_Object(
    (1, 3, 6, 1, 4, 1, 762, 2, 9, 1, 1, 4),
    _KbCIbyNumberStationName_Type()
)
kbCIbyNumberStationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kbCIbyNumberStationName.setStatus("current")
_KbCIbyNumberTotalBytes_Type = Counter32
_KbCIbyNumberTotalBytes_Object = MibTableColumn
kbCIbyNumberTotalBytes = _KbCIbyNumberTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 762, 2, 9, 1, 1, 5),
    _KbCIbyNumberTotalBytes_Type()
)
kbCIbyNumberTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kbCIbyNumberTotalBytes.setStatus("current")
_KbCIbyNumberTotalPackets_Type = Counter32
_KbCIbyNumberTotalPackets_Object = MibTableColumn
kbCIbyNumberTotalPackets = _KbCIbyNumberTotalPackets_Object(
    (1, 3, 6, 1, 4, 1, 762, 2, 9, 1, 1, 6),
    _KbCIbyNumberTotalPackets_Type()
)
kbCIbyNumberTotalPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kbCIbyNumberTotalPackets.setStatus("current")
_KbCIbyNumberSNRAverage_Type = Gauge32
_KbCIbyNumberSNRAverage_Object = MibTableColumn
kbCIbyNumberSNRAverage = _KbCIbyNumberSNRAverage_Object(
    (1, 3, 6, 1, 4, 1, 762, 2, 9, 1, 1, 7),
    _KbCIbyNumberSNRAverage_Type()
)
kbCIbyNumberSNRAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kbCIbyNumberSNRAverage.setStatus("current")
_KbCIbyNumberTimeLastRecv_Type = Counter32
_KbCIbyNumberTimeLastRecv_Object = MibTableColumn
kbCIbyNumberTimeLastRecv = _KbCIbyNumberTimeLastRecv_Object(
    (1, 3, 6, 1, 4, 1, 762, 2, 9, 1, 1, 8),
    _KbCIbyNumberTimeLastRecv_Type()
)
kbCIbyNumberTimeLastRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kbCIbyNumberTimeLastRecv.setStatus("current")
_KbClientInfoByMacTable_Object = MibTable
kbClientInfoByMacTable = _KbClientInfoByMacTable_Object(
    (1, 3, 6, 1, 4, 1, 762, 2, 9, 2)
)
if mibBuilder.loadTexts:
    kbClientInfoByMacTable.setStatus("current")
_KbClientInfoByMacEntry_Object = MibTableRow
kbClientInfoByMacEntry = _KbClientInfoByMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 762, 2, 9, 2, 1)
)
kbClientInfoByMacEntry.setIndexNames(
    (0, "KBRIDGE-MIB", "kbCIbyMacMACAddress"),
)
if mibBuilder.loadTexts:
    kbClientInfoByMacEntry.setStatus("current")
_KbCIbyMacMACAddress_Type = MacAddress
_KbCIbyMacMACAddress_Object = MibTableColumn
kbCIbyMacMACAddress = _KbCIbyMacMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 762, 2, 9, 2, 1, 1),
    _KbCIbyMacMACAddress_Type()
)
kbCIbyMacMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kbCIbyMacMACAddress.setStatus("current")


class _KbCIbyMacVirtualPort_Type(Unsigned32):
    """Custom type kbCIbyMacVirtualPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_KbCIbyMacVirtualPort_Type.__name__ = "Unsigned32"
_KbCIbyMacVirtualPort_Object = MibTableColumn
kbCIbyMacVirtualPort = _KbCIbyMacVirtualPort_Object(
    (1, 3, 6, 1, 4, 1, 762, 2, 9, 2, 1, 2),
    _KbCIbyMacVirtualPort_Type()
)
kbCIbyMacVirtualPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kbCIbyMacVirtualPort.setStatus("current")


class _KbCIbyMacInterfaceNum_Type(Unsigned32):
    """Custom type kbCIbyMacInterfaceNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_KbCIbyMacInterfaceNum_Type.__name__ = "Unsigned32"
_KbCIbyMacInterfaceNum_Object = MibTableColumn
kbCIbyMacInterfaceNum = _KbCIbyMacInterfaceNum_Object(
    (1, 3, 6, 1, 4, 1, 762, 2, 9, 2, 1, 3),
    _KbCIbyMacInterfaceNum_Type()
)
kbCIbyMacInterfaceNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kbCIbyMacInterfaceNum.setStatus("current")
_KbCIbyMacStationName_Type = OctetString
_KbCIbyMacStationName_Object = MibTableColumn
kbCIbyMacStationName = _KbCIbyMacStationName_Object(
    (1, 3, 6, 1, 4, 1, 762, 2, 9, 2, 1, 4),
    _KbCIbyMacStationName_Type()
)
kbCIbyMacStationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kbCIbyMacStationName.setStatus("current")
_KbCIbyMacTotalBytes_Type = Counter32
_KbCIbyMacTotalBytes_Object = MibTableColumn
kbCIbyMacTotalBytes = _KbCIbyMacTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 762, 2, 9, 2, 1, 5),
    _KbCIbyMacTotalBytes_Type()
)
kbCIbyMacTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kbCIbyMacTotalBytes.setStatus("current")
_KbCIbyMacTotalPackets_Type = Counter32
_KbCIbyMacTotalPackets_Object = MibTableColumn
kbCIbyMacTotalPackets = _KbCIbyMacTotalPackets_Object(
    (1, 3, 6, 1, 4, 1, 762, 2, 9, 2, 1, 6),
    _KbCIbyMacTotalPackets_Type()
)
kbCIbyMacTotalPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kbCIbyMacTotalPackets.setStatus("current")
_KbCIbyMacSNRAverage_Type = Gauge32
_KbCIbyMacSNRAverage_Object = MibTableColumn
kbCIbyMacSNRAverage = _KbCIbyMacSNRAverage_Object(
    (1, 3, 6, 1, 4, 1, 762, 2, 9, 2, 1, 7),
    _KbCIbyMacSNRAverage_Type()
)
kbCIbyMacSNRAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kbCIbyMacSNRAverage.setStatus("current")
_KbCIbyMacTimeLastRecv_Type = Counter32
_KbCIbyMacTimeLastRecv_Object = MibTableColumn
kbCIbyMacTimeLastRecv = _KbCIbyMacTimeLastRecv_Object(
    (1, 3, 6, 1, 4, 1, 762, 2, 9, 2, 1, 8),
    _KbCIbyMacTimeLastRecv_Type()
)
kbCIbyMacTimeLastRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kbCIbyMacTimeLastRecv.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "KBRIDGE-MIB",
    **{"MacAddress": MacAddress,
       "karlnet": karlnet,
       "kbridge-mib": kbridge_mib,
       "karlNetKBControl": karlNetKBControl,
       "kbControlReboot": kbControlReboot,
       "kbControlTestSNMPWrite": kbControlTestSNMPWrite,
       "kbControlShutdown": kbControlShutdown,
       "kbControlTemperature": kbControlTemperature,
       "kbWireless": kbWireless,
       "kbWirelessStationNumber": kbWirelessStationNumber,
       "kbWirelessStationTable": kbWirelessStationTable,
       "kbWirelessStationEntry": kbWirelessStationEntry,
       "kbWirelessStationIndex": kbWirelessStationIndex,
       "kbWirelessStationInterfaceNumber": kbWirelessStationInterfaceNumber,
       "kbWirelessStationName": kbWirelessStationName,
       "kbWirelessStationExclHellos": kbWirelessStationExclHellos,
       "kbWirelessStationGoodHellos": kbWirelessStationGoodHellos,
       "kbWirelessStationLowHellos": kbWirelessStationLowHellos,
       "kbWirelessStationSignalLevel": kbWirelessStationSignalLevel,
       "kbWirelessStationNoiseLevel": kbWirelessStationNoiseLevel,
       "kbWirelessStationSignalQuality": kbWirelessStationSignalQuality,
       "kbWirelessStationPktTransmits": kbWirelessStationPktTransmits,
       "kbWirelessStationMACAddress": kbWirelessStationMACAddress,
       "kbWirelessStationTransmits": kbWirelessStationTransmits,
       "kbWirelessStationBadTransmits": kbWirelessStationBadTransmits,
       "kbWirelessStationReTransmits": kbWirelessStationReTransmits,
       "kbWirelessStationIPAddress": kbWirelessStationIPAddress,
       "kbWirelessStationType": kbWirelessStationType,
       "kbWirelessStationSNR": kbWirelessStationSNR,
       "kbWirelessStationState": kbWirelessStationState,
       "kbWirelessPoll": kbWirelessPoll,
       "kbWirelessPollData": kbWirelessPollData,
       "kbWirelessPollNoData": kbWirelessPollNoData,
       "kbWirelessPollMoreData": kbWirelessPollMoreData,
       "kbWirelessPollTimeouts": kbWirelessPollTimeouts,
       "kbWirelessPollOfflines": kbWirelessPollOfflines,
       "kbWirelessTestTime": kbWirelessTestTime,
       "kbWirelessTestInterval": kbWirelessTestInterval,
       "kbWirelessTestPacketSize": kbWirelessTestPacketSize,
       "kbWirelessTestOurTx": kbWirelessTestOurTx,
       "kbWirelessTestOurRx": kbWirelessTestOurRx,
       "kbWirelessTestHisTx": kbWirelessTestHisTx,
       "kbWirelessTestHisRx": kbWirelessTestHisRx,
       "kbWirelessTestOurCurSignalLevel": kbWirelessTestOurCurSignalLevel,
       "kbWirelessTestOurCurNoiseLevel": kbWirelessTestOurCurNoiseLevel,
       "kbWirelessTestOurCurSignalQuality": kbWirelessTestOurCurSignalQuality,
       "kbWirelessTestOurCurSNR": kbWirelessTestOurCurSNR,
       "kbWirelessTestOurMinSignalLevel": kbWirelessTestOurMinSignalLevel,
       "kbWirelessTestOurMinNoiseLevel": kbWirelessTestOurMinNoiseLevel,
       "kbWirelessTestOurMinSignalQuality": kbWirelessTestOurMinSignalQuality,
       "kbWirelessTestOurMinSNR": kbWirelessTestOurMinSNR,
       "kbWirelessTestOurMaxSignalLevel": kbWirelessTestOurMaxSignalLevel,
       "kbWirelessTestOurMaxNoiseLevel": kbWirelessTestOurMaxNoiseLevel,
       "kbWirelessTestOurMaxSignalQuality": kbWirelessTestOurMaxSignalQuality,
       "kbWirelessTestOurMaxSNR": kbWirelessTestOurMaxSNR,
       "kbWirelessTestHisCurSignalLevel": kbWirelessTestHisCurSignalLevel,
       "kbWirelessTestHisCurNoiseLevel": kbWirelessTestHisCurNoiseLevel,
       "kbWirelessTestHisCurSignalQuality": kbWirelessTestHisCurSignalQuality,
       "kbWirelessTestHisCurSNR": kbWirelessTestHisCurSNR,
       "kbWirelessTestHisMinSignalLevel": kbWirelessTestHisMinSignalLevel,
       "kbWirelessTestHisMinNoiseLevel": kbWirelessTestHisMinNoiseLevel,
       "kbWirelessTestHisMinSignalQuality": kbWirelessTestHisMinSignalQuality,
       "kbWirelessTestHisMinSNR": kbWirelessTestHisMinSNR,
       "kbWirelessTestHisMaxSignalLevel": kbWirelessTestHisMaxSignalLevel,
       "kbWirelessTestHisMaxNoiseLevel": kbWirelessTestHisMaxNoiseLevel,
       "kbWirelessTestHisMaxSignalQuality": kbWirelessTestHisMaxSignalQuality,
       "kbWirelessTestHisMaxSNR": kbWirelessTestHisMaxSNR,
       "kbWirelessTestLinkUp": kbWirelessTestLinkUp,
       "kbWirelessTestLostLink": kbWirelessTestLostLink,
       "kbWirelessTestLostTestPkts": kbWirelessTestLostTestPkts,
       "kbWirelessStationRadioType": kbWirelessStationRadioType,
       "kbWirelessRecordType": kbWirelessRecordType,
       "kbWirelessStationPktReceives": kbWirelessStationPktReceives,
       "kbWirelessStationReceives": kbWirelessStationReceives,
       "kbWirelessStationBytesReceives": kbWirelessStationBytesReceives,
       "kbWirelessStationBytesTransmits": kbWirelessStationBytesTransmits,
       "kbWirelessRegistrationRecord": kbWirelessRegistrationRecord,
       "kbWirelessStationFragmentDiscards": kbWirelessStationFragmentDiscards,
       "kbWirelessStationFragmentMissings": kbWirelessStationFragmentMissings,
       "kbWirelessStationFragmentLostFrames": kbWirelessStationFragmentLostFrames,
       "kbWirelessStationFragmentErrors": kbWirelessStationFragmentErrors,
       "kbSEC": kbSEC,
       "kbSECClientTable": kbSECClientTable,
       "kbSECClientEntry": kbSECClientEntry,
       "kbSECClientAddress": kbSECClientAddress,
       "kbSECStationAddress": kbSECStationAddress,
       "kbClientInfo": kbClientInfo,
       "kbClientInfoByNumberTable": kbClientInfoByNumberTable,
       "kbClientInfoByNumberEntry": kbClientInfoByNumberEntry,
       "kbCIbyNumberVirtualPort": kbCIbyNumberVirtualPort,
       "kbCIbyNumberMACAddress": kbCIbyNumberMACAddress,
       "kbCIByNumberInterfaceNum": kbCIByNumberInterfaceNum,
       "kbCIbyNumberStationName": kbCIbyNumberStationName,
       "kbCIbyNumberTotalBytes": kbCIbyNumberTotalBytes,
       "kbCIbyNumberTotalPackets": kbCIbyNumberTotalPackets,
       "kbCIbyNumberSNRAverage": kbCIbyNumberSNRAverage,
       "kbCIbyNumberTimeLastRecv": kbCIbyNumberTimeLastRecv,
       "kbClientInfoByMacTable": kbClientInfoByMacTable,
       "kbClientInfoByMacEntry": kbClientInfoByMacEntry,
       "kbCIbyMacMACAddress": kbCIbyMacMACAddress,
       "kbCIbyMacVirtualPort": kbCIbyMacVirtualPort,
       "kbCIbyMacInterfaceNum": kbCIbyMacInterfaceNum,
       "kbCIbyMacStationName": kbCIbyMacStationName,
       "kbCIbyMacTotalBytes": kbCIbyMacTotalBytes,
       "kbCIbyMacTotalPackets": kbCIbyMacTotalPackets,
       "kbCIbyMacSNRAverage": kbCIbyMacSNRAverage,
       "kbCIbyMacTimeLastRecv": kbCIbyMacTimeLastRecv}
)
