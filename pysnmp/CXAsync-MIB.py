# SNMP MIB module (CXAsync-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CXAsync-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:20:03 2024
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

(Alias,
 SapIndex,
 ThruputClass,
 cxAsync) = mibBuilder.importSymbols(
    "CXProduct-SMI",
    "Alias",
    "SapIndex",
    "ThruputClass",
    "cxAsync")

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


# Types definitions



class PacketSize(Integer32):
    """Custom type PacketSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("bytes1024", 10),
          ("bytes128", 7),
          ("bytes16", 4),
          ("bytes2048", 11),
          ("bytes256", 8),
          ("bytes32", 5),
          ("bytes4096", 12),
          ("bytes512", 9),
          ("bytes64", 6))
    )





class YesNo(Integer32):
    """Custom type YesNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )





class ProfIndex(Integer32):
    """Custom type ProfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )





class DteIndex(Integer32):
    """Custom type DteIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _AsyX25TxQThreshold_Type(Integer32):
    """Custom type asyX25TxQThreshold based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AsyX25TxQThreshold_Type.__name__ = "Integer32"
_AsyX25TxQThreshold_Object = MibScalar
asyX25TxQThreshold = _AsyX25TxQThreshold_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 1),
    _AsyX25TxQThreshold_Type()
)
asyX25TxQThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asyX25TxQThreshold.setStatus("mandatory")


class _AsyPadIdBanner_Type(DisplayString):
    """Custom type asyPadIdBanner based on DisplayString"""
    defaultValue = OctetString("Async PAD")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_AsyPadIdBanner_Type.__name__ = "DisplayString"
_AsyPadIdBanner_Object = MibScalar
asyPadIdBanner = _AsyPadIdBanner_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 2),
    _AsyPadIdBanner_Type()
)
asyPadIdBanner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asyPadIdBanner.setStatus("mandatory")


class _AsyAlarms_Type(Integer32):
    """Custom type asyAlarms based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enable", 2))
    )


_AsyAlarms_Type.__name__ = "Integer32"
_AsyAlarms_Object = MibScalar
asyAlarms = _AsyAlarms_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 7),
    _AsyAlarms_Type()
)
asyAlarms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asyAlarms.setStatus("mandatory")


class _AsySapStatusEvent_Type(Integer32):
    """Custom type asySapStatusEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("noEvent", 1)
    )


_AsySapStatusEvent_Type.__name__ = "Integer32"
_AsySapStatusEvent_Object = MibScalar
asySapStatusEvent = _AsySapStatusEvent_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 8),
    _AsySapStatusEvent_Type()
)
asySapStatusEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asySapStatusEvent.setStatus("mandatory")
_AsySoftwareVersions_Type = DisplayString
_AsySoftwareVersions_Object = MibScalar
asySoftwareVersions = _AsySoftwareVersions_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 9),
    _AsySoftwareVersions_Type()
)
asySoftwareVersions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asySoftwareVersions.setStatus("mandatory")
_AsyMibLevel_Type = Integer32
_AsyMibLevel_Object = MibScalar
asyMibLevel = _AsyMibLevel_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 10),
    _AsyMibLevel_Type()
)
asyMibLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asyMibLevel.setStatus("mandatory")
_AsySapTable_Object = MibTable
asySapTable = _AsySapTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20)
)
if mibBuilder.loadTexts:
    asySapTable.setStatus("mandatory")
_AsySapEntry_Object = MibTableRow
asySapEntry = _AsySapEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20, 1)
)
asySapEntry.setIndexNames(
    (0, "CXAsync-MIB", "asySapNumber"),
)
if mibBuilder.loadTexts:
    asySapEntry.setStatus("mandatory")
_AsySapNumber_Type = SapIndex
_AsySapNumber_Object = MibTableColumn
asySapNumber = _AsySapNumber_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20, 1, 1),
    _AsySapNumber_Type()
)
asySapNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asySapNumber.setStatus("mandatory")


class _AsySapRowStatus_Type(Integer32):
    """Custom type asySapRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_AsySapRowStatus_Type.__name__ = "Integer32"
_AsySapRowStatus_Object = MibTableColumn
asySapRowStatus = _AsySapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20, 1, 2),
    _AsySapRowStatus_Type()
)
asySapRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asySapRowStatus.setStatus("mandatory")
_AsySapAlias_Type = Alias
_AsySapAlias_Object = MibTableColumn
asySapAlias = _AsySapAlias_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20, 1, 3),
    _AsySapAlias_Type()
)
asySapAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asySapAlias.setStatus("mandatory")
_AsySapMCompanionAlias_Type = Alias
_AsySapMCompanionAlias_Object = MibTableColumn
asySapMCompanionAlias = _AsySapMCompanionAlias_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20, 1, 4),
    _AsySapMCompanionAlias_Type()
)
asySapMCompanionAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asySapMCompanionAlias.setStatus("mandatory")
_AsySapNCompanionAlias_Type = Alias
_AsySapNCompanionAlias_Object = MibTableColumn
asySapNCompanionAlias = _AsySapNCompanionAlias_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20, 1, 5),
    _AsySapNCompanionAlias_Type()
)
asySapNCompanionAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asySapNCompanionAlias.setStatus("mandatory")


class _AsySapX3Profile_Type(Integer32):
    """Custom type asySapX3Profile based on Integer32"""
    defaultValue = 92

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AsySapX3Profile_Type.__name__ = "Integer32"
_AsySapX3Profile_Object = MibTableColumn
asySapX3Profile = _AsySapX3Profile_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20, 1, 6),
    _AsySapX3Profile_Type()
)
asySapX3Profile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asySapX3Profile.setStatus("mandatory")


class _AsySapNUI_Type(DisplayString):
    """Custom type asySapNUI based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_AsySapNUI_Type.__name__ = "DisplayString"
_AsySapNUI_Object = MibTableColumn
asySapNUI = _AsySapNUI_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20, 1, 7),
    _AsySapNUI_Type()
)
asySapNUI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asySapNUI.setStatus("mandatory")


class _AsySapAddress_Type(DisplayString):
    """Custom type asySapAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_AsySapAddress_Type.__name__ = "DisplayString"
_AsySapAddress_Object = MibTableColumn
asySapAddress = _AsySapAddress_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20, 1, 8),
    _AsySapAddress_Type()
)
asySapAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asySapAddress.setStatus("mandatory")


class _AsySapDisconnectRequest_Type(YesNo):
    """Custom type asySapDisconnectRequest based on YesNo"""


_AsySapDisconnectRequest_Object = MibTableColumn
asySapDisconnectRequest = _AsySapDisconnectRequest_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20, 1, 9),
    _AsySapDisconnectRequest_Type()
)
asySapDisconnectRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asySapDisconnectRequest.setStatus("mandatory")


class _AsySapRxThruputClass_Type(ThruputClass):
    """Custom type asySapRxThruputClass based on ThruputClass"""


_AsySapRxThruputClass_Object = MibTableColumn
asySapRxThruputClass = _AsySapRxThruputClass_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20, 1, 10),
    _AsySapRxThruputClass_Type()
)
asySapRxThruputClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asySapRxThruputClass.setStatus("mandatory")


class _AsySapTxThruputClass_Type(ThruputClass):
    """Custom type asySapTxThruputClass based on ThruputClass"""


_AsySapTxThruputClass_Object = MibTableColumn
asySapTxThruputClass = _AsySapTxThruputClass_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20, 1, 11),
    _AsySapTxThruputClass_Type()
)
asySapTxThruputClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asySapTxThruputClass.setStatus("mandatory")


class _AsySapTxPacketSize_Type(PacketSize):
    """Custom type asySapTxPacketSize based on PacketSize"""


_AsySapTxPacketSize_Object = MibTableColumn
asySapTxPacketSize = _AsySapTxPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20, 1, 12),
    _AsySapTxPacketSize_Type()
)
asySapTxPacketSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asySapTxPacketSize.setStatus("mandatory")


class _AsySapRxPacketSize_Type(PacketSize):
    """Custom type asySapRxPacketSize based on PacketSize"""


_AsySapRxPacketSize_Object = MibTableColumn
asySapRxPacketSize = _AsySapRxPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20, 1, 13),
    _AsySapRxPacketSize_Type()
)
asySapRxPacketSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asySapRxPacketSize.setStatus("mandatory")


class _AsySapTxWindowSize_Type(Integer32):
    """Custom type asySapTxWindowSize based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_AsySapTxWindowSize_Type.__name__ = "Integer32"
_AsySapTxWindowSize_Object = MibTableColumn
asySapTxWindowSize = _AsySapTxWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20, 1, 14),
    _AsySapTxWindowSize_Type()
)
asySapTxWindowSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asySapTxWindowSize.setStatus("mandatory")


class _AsySapRxWindowSize_Type(Integer32):
    """Custom type asySapRxWindowSize based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_AsySapRxWindowSize_Type.__name__ = "Integer32"
_AsySapRxWindowSize_Object = MibTableColumn
asySapRxWindowSize = _AsySapRxWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20, 1, 15),
    _AsySapRxWindowSize_Type()
)
asySapRxWindowSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asySapRxWindowSize.setStatus("mandatory")


class _AsySapYTTimer_Type(Integer32):
    """Custom type asySapYTTimer based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AsySapYTTimer_Type.__name__ = "Integer32"
_AsySapYTTimer_Object = MibTableColumn
asySapYTTimer = _AsySapYTTimer_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20, 1, 16),
    _AsySapYTTimer_Type()
)
asySapYTTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asySapYTTimer.setStatus("mandatory")


class _AsySapSRTimer_Type(Integer32):
    """Custom type asySapSRTimer based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AsySapSRTimer_Type.__name__ = "Integer32"
_AsySapSRTimer_Object = MibTableColumn
asySapSRTimer = _AsySapSRTimer_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20, 1, 17),
    _AsySapSRTimer_Type()
)
asySapSRTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asySapSRTimer.setStatus("mandatory")


class _AsySapNUILength_Type(Integer32):
    """Custom type asySapNUILength based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14),
    )


_AsySapNUILength_Type.__name__ = "Integer32"
_AsySapNUILength_Object = MibTableColumn
asySapNUILength = _AsySapNUILength_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20, 1, 18),
    _AsySapNUILength_Type()
)
asySapNUILength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asySapNUILength.setStatus("obsolete")


class _AsySapReverseChargingAcceptance_Type(YesNo):
    """Custom type asySapReverseChargingAcceptance based on YesNo"""


_AsySapReverseChargingAcceptance_Object = MibTableColumn
asySapReverseChargingAcceptance = _AsySapReverseChargingAcceptance_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20, 1, 19),
    _AsySapReverseChargingAcceptance_Type()
)
asySapReverseChargingAcceptance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asySapReverseChargingAcceptance.setStatus("mandatory")


class _AsySapChargingInformation_Type(YesNo):
    """Custom type asySapChargingInformation based on YesNo"""


_AsySapChargingInformation_Object = MibTableColumn
asySapChargingInformation = _AsySapChargingInformation_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20, 1, 20),
    _AsySapChargingInformation_Type()
)
asySapChargingInformation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asySapChargingInformation.setStatus("mandatory")


class _AsySapSubscriptionCUG_Type(YesNo):
    """Custom type asySapSubscriptionCUG based on YesNo"""


_AsySapSubscriptionCUG_Object = MibTableColumn
asySapSubscriptionCUG = _AsySapSubscriptionCUG_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20, 1, 21),
    _AsySapSubscriptionCUG_Type()
)
asySapSubscriptionCUG.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asySapSubscriptionCUG.setStatus("mandatory")


class _AsySapSubscriptionCUGOA_Type(YesNo):
    """Custom type asySapSubscriptionCUGOA based on YesNo"""


_AsySapSubscriptionCUGOA_Object = MibTableColumn
asySapSubscriptionCUGOA = _AsySapSubscriptionCUGOA_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20, 1, 22),
    _AsySapSubscriptionCUGOA_Type()
)
asySapSubscriptionCUGOA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asySapSubscriptionCUGOA.setStatus("mandatory")


class _AsySapSubscriptionCUGIA_Type(YesNo):
    """Custom type asySapSubscriptionCUGIA based on YesNo"""


_AsySapSubscriptionCUGIA_Object = MibTableColumn
asySapSubscriptionCUGIA = _AsySapSubscriptionCUGIA_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20, 1, 23),
    _AsySapSubscriptionCUGIA_Type()
)
asySapSubscriptionCUGIA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asySapSubscriptionCUGIA.setStatus("mandatory")


class _AsySapPreferentialCUGIndex_Type(Integer32):
    """Custom type asySapPreferentialCUGIndex based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_AsySapPreferentialCUGIndex_Type.__name__ = "Integer32"
_AsySapPreferentialCUGIndex_Object = MibTableColumn
asySapPreferentialCUGIndex = _AsySapPreferentialCUGIndex_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20, 1, 24),
    _AsySapPreferentialCUGIndex_Type()
)
asySapPreferentialCUGIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asySapPreferentialCUGIndex.setStatus("mandatory")


class _AsySapReceiptConfirmation_Type(Integer32):
    """Custom type asySapReceiptConfirmation based on Integer32"""
    defaultValue = 1

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
        *(("dBit", 2),
          ("localAck", 3),
          ("noAck", 1),
          ("xmitAck", 4))
    )


_AsySapReceiptConfirmation_Type.__name__ = "Integer32"
_AsySapReceiptConfirmation_Object = MibTableColumn
asySapReceiptConfirmation = _AsySapReceiptConfirmation_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20, 1, 25),
    _AsySapReceiptConfirmation_Type()
)
asySapReceiptConfirmation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asySapReceiptConfirmation.setStatus("mandatory")


class _AsySapEnableProtocolId_Type(YesNo):
    """Custom type asySapEnableProtocolId based on YesNo"""


_AsySapEnableProtocolId_Object = MibTableColumn
asySapEnableProtocolId = _AsySapEnableProtocolId_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20, 1, 26),
    _AsySapEnableProtocolId_Type()
)
asySapEnableProtocolId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asySapEnableProtocolId.setStatus("mandatory")


class _AsySapProtocolId_Type(DisplayString):
    """Custom type asySapProtocolId based on DisplayString"""
    defaultValue = OctetString("01,00,00,00")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 11),
    )


_AsySapProtocolId_Type.__name__ = "DisplayString"
_AsySapProtocolId_Object = MibTableColumn
asySapProtocolId = _AsySapProtocolId_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20, 1, 27),
    _AsySapProtocolId_Type()
)
asySapProtocolId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asySapProtocolId.setStatus("mandatory")


class _AsySapPromptSignal_Type(DisplayString):
    """Custom type asySapPromptSignal based on DisplayString"""
    defaultValue = OctetString("*")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_AsySapPromptSignal_Type.__name__ = "DisplayString"
_AsySapPromptSignal_Object = MibTableColumn
asySapPromptSignal = _AsySapPromptSignal_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20, 1, 28),
    _AsySapPromptSignal_Type()
)
asySapPromptSignal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asySapPromptSignal.setStatus("mandatory")
_AsySapAutoConnectDteId_Type = DisplayString
_AsySapAutoConnectDteId_Object = MibTableColumn
asySapAutoConnectDteId = _AsySapAutoConnectDteId_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20, 1, 29),
    _AsySapAutoConnectDteId_Type()
)
asySapAutoConnectDteId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asySapAutoConnectDteId.setStatus("mandatory")


class _AsySapAutoConnectRetry_Type(Integer32):
    """Custom type asySapAutoConnectRetry based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AsySapAutoConnectRetry_Type.__name__ = "Integer32"
_AsySapAutoConnectRetry_Object = MibTableColumn
asySapAutoConnectRetry = _AsySapAutoConnectRetry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20, 1, 30),
    _AsySapAutoConnectRetry_Type()
)
asySapAutoConnectRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asySapAutoConnectRetry.setStatus("mandatory")


class _AsySapAutoConnectDelayTimer_Type(Integer32):
    """Custom type asySapAutoConnectDelayTimer based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_AsySapAutoConnectDelayTimer_Type.__name__ = "Integer32"
_AsySapAutoConnectDelayTimer_Object = MibTableColumn
asySapAutoConnectDelayTimer = _AsySapAutoConnectDelayTimer_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20, 1, 31),
    _AsySapAutoConnectDelayTimer_Type()
)
asySapAutoConnectDelayTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asySapAutoConnectDelayTimer.setStatus("mandatory")


class _AsySapHardwareFlowControl_Type(YesNo):
    """Custom type asySapHardwareFlowControl based on YesNo"""


_AsySapHardwareFlowControl_Object = MibTableColumn
asySapHardwareFlowControl = _AsySapHardwareFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20, 1, 32),
    _AsySapHardwareFlowControl_Type()
)
asySapHardwareFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asySapHardwareFlowControl.setStatus("mandatory")


class _AsySapProtocolType_Type(Integer32):
    """Custom type asySapProtocolType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("iocProtocol", 2),
          ("modifiedudf", 3),
          ("normal", 1))
    )


_AsySapProtocolType_Type.__name__ = "Integer32"
_AsySapProtocolType_Object = MibTableColumn
asySapProtocolType = _AsySapProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20, 1, 33),
    _AsySapProtocolType_Type()
)
asySapProtocolType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asySapProtocolType.setStatus("mandatory")


class _AsySapControl_Type(Integer32):
    """Custom type asySapControl based on Integer32"""
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
        *(("clearStats", 1),
          ("disableSapGracefully", 4),
          ("disableSapImmediately", 3),
          ("enableSap", 2))
    )


_AsySapControl_Type.__name__ = "Integer32"
_AsySapControl_Object = MibTableColumn
asySapControl = _AsySapControl_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20, 1, 37),
    _AsySapControl_Type()
)
asySapControl.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    asySapControl.setStatus("mandatory")


class _AsySapState_Type(Integer32):
    """Custom type asySapState based on Integer32"""
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
        *(("connecting", 3),
          ("dataTransfer", 4),
          ("disconnected", 1),
          ("enabled", 2),
          ("resetting", 5))
    )


_AsySapState_Type.__name__ = "Integer32"
_AsySapState_Object = MibTableColumn
asySapState = _AsySapState_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20, 1, 40),
    _AsySapState_Type()
)
asySapState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asySapState.setStatus("mandatory")


class _AsySapAsyncFlowControlState_Type(Integer32):
    """Custom type asySapAsyncFlowControlState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("flowControlOff", 1),
          ("flowControlOn", 2))
    )


_AsySapAsyncFlowControlState_Type.__name__ = "Integer32"
_AsySapAsyncFlowControlState_Object = MibTableColumn
asySapAsyncFlowControlState = _AsySapAsyncFlowControlState_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20, 1, 41),
    _AsySapAsyncFlowControlState_Type()
)
asySapAsyncFlowControlState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asySapAsyncFlowControlState.setStatus("mandatory")


class _AsySapNetworkFlowControlState_Type(Integer32):
    """Custom type asySapNetworkFlowControlState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("flowControlOff", 1),
          ("flowControlOn", 2))
    )


_AsySapNetworkFlowControlState_Type.__name__ = "Integer32"
_AsySapNetworkFlowControlState_Object = MibTableColumn
asySapNetworkFlowControlState = _AsySapNetworkFlowControlState_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20, 1, 42),
    _AsySapNetworkFlowControlState_Type()
)
asySapNetworkFlowControlState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asySapNetworkFlowControlState.setStatus("mandatory")
_AsySapAsyncTxQueueSize_Type = Counter32
_AsySapAsyncTxQueueSize_Object = MibTableColumn
asySapAsyncTxQueueSize = _AsySapAsyncTxQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20, 1, 43),
    _AsySapAsyncTxQueueSize_Type()
)
asySapAsyncTxQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asySapAsyncTxQueueSize.setStatus("mandatory")
_AsySapX25TxQueueSize_Type = Counter32
_AsySapX25TxQueueSize_Object = MibTableColumn
asySapX25TxQueueSize = _AsySapX25TxQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20, 1, 44),
    _AsySapX25TxQueueSize_Type()
)
asySapX25TxQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asySapX25TxQueueSize.setStatus("mandatory")
_AsySapNumberConnects_Type = Counter32
_AsySapNumberConnects_Object = MibTableColumn
asySapNumberConnects = _AsySapNumberConnects_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20, 1, 50),
    _AsySapNumberConnects_Type()
)
asySapNumberConnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asySapNumberConnects.setStatus("mandatory")
_AsySapNumberDisconnects_Type = Counter32
_AsySapNumberDisconnects_Object = MibTableColumn
asySapNumberDisconnects = _AsySapNumberDisconnects_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20, 1, 51),
    _AsySapNumberDisconnects_Type()
)
asySapNumberDisconnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asySapNumberDisconnects.setStatus("mandatory")
_AsySapTxDataCharacters_Type = Counter32
_AsySapTxDataCharacters_Object = MibTableColumn
asySapTxDataCharacters = _AsySapTxDataCharacters_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20, 1, 52),
    _AsySapTxDataCharacters_Type()
)
asySapTxDataCharacters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asySapTxDataCharacters.setStatus("mandatory")
_AsySapRxDataCharacters_Type = Counter32
_AsySapRxDataCharacters_Object = MibTableColumn
asySapRxDataCharacters = _AsySapRxDataCharacters_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20, 1, 53),
    _AsySapRxDataCharacters_Type()
)
asySapRxDataCharacters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asySapRxDataCharacters.setStatus("mandatory")
_AsySapParityErrors_Type = Counter32
_AsySapParityErrors_Object = MibTableColumn
asySapParityErrors = _AsySapParityErrors_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20, 1, 54),
    _AsySapParityErrors_Type()
)
asySapParityErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asySapParityErrors.setStatus("mandatory")
_AsySapOverruns_Type = Counter32
_AsySapOverruns_Object = MibTableColumn
asySapOverruns = _AsySapOverruns_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20, 1, 55),
    _AsySapOverruns_Type()
)
asySapOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asySapOverruns.setStatus("mandatory")
_AsySapFlowControlByUser_Type = Counter32
_AsySapFlowControlByUser_Object = MibTableColumn
asySapFlowControlByUser = _AsySapFlowControlByUser_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20, 1, 56),
    _AsySapFlowControlByUser_Type()
)
asySapFlowControlByUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asySapFlowControlByUser.setStatus("mandatory")
_AsySapFlowControlByX25_Type = Counter32
_AsySapFlowControlByX25_Object = MibTableColumn
asySapFlowControlByX25 = _AsySapFlowControlByX25_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20, 1, 57),
    _AsySapFlowControlByX25_Type()
)
asySapFlowControlByX25.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asySapFlowControlByX25.setStatus("mandatory")
_AsySapFlowControlToUser_Type = Counter32
_AsySapFlowControlToUser_Object = MibTableColumn
asySapFlowControlToUser = _AsySapFlowControlToUser_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20, 1, 58),
    _AsySapFlowControlToUser_Type()
)
asySapFlowControlToUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asySapFlowControlToUser.setStatus("mandatory")
_AsySapFlowControlToX25_Type = Counter32
_AsySapFlowControlToX25_Object = MibTableColumn
asySapFlowControlToX25 = _AsySapFlowControlToX25_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20, 1, 59),
    _AsySapFlowControlToX25_Type()
)
asySapFlowControlToX25.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asySapFlowControlToX25.setStatus("mandatory")
_AsySapRxReset_Type = Counter32
_AsySapRxReset_Object = MibTableColumn
asySapRxReset = _AsySapRxReset_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20, 1, 60),
    _AsySapRxReset_Type()
)
asySapRxReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asySapRxReset.setStatus("mandatory")
_AsySapRxBreak_Type = Counter32
_AsySapRxBreak_Object = MibTableColumn
asySapRxBreak = _AsySapRxBreak_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20, 1, 61),
    _AsySapRxBreak_Type()
)
asySapRxBreak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asySapRxBreak.setStatus("mandatory")
_AsySapTxBreak_Type = Counter32
_AsySapTxBreak_Object = MibTableColumn
asySapTxBreak = _AsySapTxBreak_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20, 1, 62),
    _AsySapTxBreak_Type()
)
asySapTxBreak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asySapTxBreak.setStatus("mandatory")
_AsySapRxDiscardCharacters_Type = Counter32
_AsySapRxDiscardCharacters_Object = MibTableColumn
asySapRxDiscardCharacters = _AsySapRxDiscardCharacters_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20, 1, 63),
    _AsySapRxDiscardCharacters_Type()
)
asySapRxDiscardCharacters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asySapRxDiscardCharacters.setStatus("mandatory")
_AsyProfTable_Object = MibTable
asyProfTable = _AsyProfTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 21)
)
if mibBuilder.loadTexts:
    asyProfTable.setStatus("mandatory")
_AsyProfEntry_Object = MibTableRow
asyProfEntry = _AsyProfEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 21, 1)
)
asyProfEntry.setIndexNames(
    (0, "CXAsync-MIB", "asyProfNumber"),
)
if mibBuilder.loadTexts:
    asyProfEntry.setStatus("mandatory")
_AsyProfNumber_Type = ProfIndex
_AsyProfNumber_Object = MibTableColumn
asyProfNumber = _AsyProfNumber_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 21, 1, 1),
    _AsyProfNumber_Type()
)
asyProfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asyProfNumber.setStatus("mandatory")


class _AsyProfRowStatus_Type(Integer32):
    """Custom type asyProfRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_AsyProfRowStatus_Type.__name__ = "Integer32"
_AsyProfRowStatus_Object = MibTableColumn
asyProfRowStatus = _AsyProfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 21, 1, 2),
    _AsyProfRowStatus_Type()
)
asyProfRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asyProfRowStatus.setStatus("mandatory")
_AsyProfAlias_Type = Alias
_AsyProfAlias_Object = MibTableColumn
asyProfAlias = _AsyProfAlias_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 21, 1, 3),
    _AsyProfAlias_Type()
)
asyProfAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asyProfAlias.setStatus("mandatory")


class _AsyProfParameter1_Type(Integer32):
    """Custom type asyProfParameter1 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 126),
    )


_AsyProfParameter1_Type.__name__ = "Integer32"
_AsyProfParameter1_Object = MibTableColumn
asyProfParameter1 = _AsyProfParameter1_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 21, 1, 5),
    _AsyProfParameter1_Type()
)
asyProfParameter1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asyProfParameter1.setStatus("mandatory")


class _AsyProfParameter2_Type(Integer32):
    """Custom type asyProfParameter2 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AsyProfParameter2_Type.__name__ = "Integer32"
_AsyProfParameter2_Object = MibTableColumn
asyProfParameter2 = _AsyProfParameter2_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 21, 1, 6),
    _AsyProfParameter2_Type()
)
asyProfParameter2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asyProfParameter2.setStatus("mandatory")


class _AsyProfParameter3_Type(Integer32):
    """Custom type asyProfParameter3 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 126),
    )


_AsyProfParameter3_Type.__name__ = "Integer32"
_AsyProfParameter3_Object = MibTableColumn
asyProfParameter3 = _AsyProfParameter3_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 21, 1, 7),
    _AsyProfParameter3_Type()
)
asyProfParameter3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asyProfParameter3.setStatus("mandatory")


class _AsyProfParameter4_Type(Integer32):
    """Custom type asyProfParameter4 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AsyProfParameter4_Type.__name__ = "Integer32"
_AsyProfParameter4_Object = MibTableColumn
asyProfParameter4 = _AsyProfParameter4_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 21, 1, 8),
    _AsyProfParameter4_Type()
)
asyProfParameter4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asyProfParameter4.setStatus("mandatory")


class _AsyProfParameter5_Type(Integer32):
    """Custom type asyProfParameter5 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AsyProfParameter5_Type.__name__ = "Integer32"
_AsyProfParameter5_Object = MibTableColumn
asyProfParameter5 = _AsyProfParameter5_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 21, 1, 9),
    _AsyProfParameter5_Type()
)
asyProfParameter5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asyProfParameter5.setStatus("mandatory")


class _AsyProfParameter6_Type(Integer32):
    """Custom type asyProfParameter6 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_AsyProfParameter6_Type.__name__ = "Integer32"
_AsyProfParameter6_Object = MibTableColumn
asyProfParameter6 = _AsyProfParameter6_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 21, 1, 10),
    _AsyProfParameter6_Type()
)
asyProfParameter6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asyProfParameter6.setStatus("mandatory")


class _AsyProfParameter7_Type(Integer32):
    """Custom type asyProfParameter7 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 21),
    )


_AsyProfParameter7_Type.__name__ = "Integer32"
_AsyProfParameter7_Object = MibTableColumn
asyProfParameter7 = _AsyProfParameter7_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 21, 1, 11),
    _AsyProfParameter7_Type()
)
asyProfParameter7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asyProfParameter7.setStatus("mandatory")


class _AsyProfParameter8_Type(Integer32):
    """Custom type asyProfParameter8 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AsyProfParameter8_Type.__name__ = "Integer32"
_AsyProfParameter8_Object = MibTableColumn
asyProfParameter8 = _AsyProfParameter8_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 21, 1, 12),
    _AsyProfParameter8_Type()
)
asyProfParameter8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asyProfParameter8.setStatus("mandatory")


class _AsyProfParameter9_Type(Integer32):
    """Custom type asyProfParameter9 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AsyProfParameter9_Type.__name__ = "Integer32"
_AsyProfParameter9_Object = MibTableColumn
asyProfParameter9 = _AsyProfParameter9_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 21, 1, 13),
    _AsyProfParameter9_Type()
)
asyProfParameter9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asyProfParameter9.setStatus("mandatory")


class _AsyProfParameter10_Type(Integer32):
    """Custom type asyProfParameter10 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AsyProfParameter10_Type.__name__ = "Integer32"
_AsyProfParameter10_Object = MibTableColumn
asyProfParameter10 = _AsyProfParameter10_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 21, 1, 14),
    _AsyProfParameter10_Type()
)
asyProfParameter10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asyProfParameter10.setStatus("mandatory")


class _AsyProfParameter11_Type(Integer32):
    """Custom type asyProfParameter11 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 22),
    )


_AsyProfParameter11_Type.__name__ = "Integer32"
_AsyProfParameter11_Object = MibTableColumn
asyProfParameter11 = _AsyProfParameter11_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 21, 1, 15),
    _AsyProfParameter11_Type()
)
asyProfParameter11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asyProfParameter11.setStatus("mandatory")


class _AsyProfParameter12_Type(Integer32):
    """Custom type asyProfParameter12 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AsyProfParameter12_Type.__name__ = "Integer32"
_AsyProfParameter12_Object = MibTableColumn
asyProfParameter12 = _AsyProfParameter12_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 21, 1, 16),
    _AsyProfParameter12_Type()
)
asyProfParameter12.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asyProfParameter12.setStatus("mandatory")


class _AsyProfParameter13_Type(Integer32):
    """Custom type asyProfParameter13 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AsyProfParameter13_Type.__name__ = "Integer32"
_AsyProfParameter13_Object = MibTableColumn
asyProfParameter13 = _AsyProfParameter13_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 21, 1, 17),
    _AsyProfParameter13_Type()
)
asyProfParameter13.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asyProfParameter13.setStatus("mandatory")


class _AsyProfParameter14_Type(Integer32):
    """Custom type asyProfParameter14 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AsyProfParameter14_Type.__name__ = "Integer32"
_AsyProfParameter14_Object = MibTableColumn
asyProfParameter14 = _AsyProfParameter14_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 21, 1, 18),
    _AsyProfParameter14_Type()
)
asyProfParameter14.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asyProfParameter14.setStatus("mandatory")


class _AsyProfParameter15_Type(Integer32):
    """Custom type asyProfParameter15 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AsyProfParameter15_Type.__name__ = "Integer32"
_AsyProfParameter15_Object = MibTableColumn
asyProfParameter15 = _AsyProfParameter15_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 21, 1, 19),
    _AsyProfParameter15_Type()
)
asyProfParameter15.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asyProfParameter15.setStatus("mandatory")


class _AsyProfParameter16_Type(Integer32):
    """Custom type asyProfParameter16 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_AsyProfParameter16_Type.__name__ = "Integer32"
_AsyProfParameter16_Object = MibTableColumn
asyProfParameter16 = _AsyProfParameter16_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 21, 1, 20),
    _AsyProfParameter16_Type()
)
asyProfParameter16.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asyProfParameter16.setStatus("mandatory")


class _AsyProfParameter17_Type(Integer32):
    """Custom type asyProfParameter17 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_AsyProfParameter17_Type.__name__ = "Integer32"
_AsyProfParameter17_Object = MibTableColumn
asyProfParameter17 = _AsyProfParameter17_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 21, 1, 21),
    _AsyProfParameter17_Type()
)
asyProfParameter17.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asyProfParameter17.setStatus("mandatory")


class _AsyProfParameter18_Type(Integer32):
    """Custom type asyProfParameter18 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_AsyProfParameter18_Type.__name__ = "Integer32"
_AsyProfParameter18_Object = MibTableColumn
asyProfParameter18 = _AsyProfParameter18_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 21, 1, 22),
    _AsyProfParameter18_Type()
)
asyProfParameter18.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asyProfParameter18.setStatus("mandatory")


class _AsyProfParameter19_Type(Integer32):
    """Custom type asyProfParameter19 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_AsyProfParameter19_Type.__name__ = "Integer32"
_AsyProfParameter19_Object = MibTableColumn
asyProfParameter19 = _AsyProfParameter19_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 21, 1, 23),
    _AsyProfParameter19_Type()
)
asyProfParameter19.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asyProfParameter19.setStatus("mandatory")


class _AsyProfParameter20_Type(Integer32):
    """Custom type asyProfParameter20 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_AsyProfParameter20_Type.__name__ = "Integer32"
_AsyProfParameter20_Object = MibTableColumn
asyProfParameter20 = _AsyProfParameter20_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 21, 1, 24),
    _AsyProfParameter20_Type()
)
asyProfParameter20.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asyProfParameter20.setStatus("mandatory")


class _AsyProfParameter21_Type(Integer32):
    """Custom type asyProfParameter21 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_AsyProfParameter21_Type.__name__ = "Integer32"
_AsyProfParameter21_Object = MibTableColumn
asyProfParameter21 = _AsyProfParameter21_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 21, 1, 25),
    _AsyProfParameter21_Type()
)
asyProfParameter21.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asyProfParameter21.setStatus("mandatory")


class _AsyProfParameter22_Type(Integer32):
    """Custom type asyProfParameter22 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AsyProfParameter22_Type.__name__ = "Integer32"
_AsyProfParameter22_Object = MibTableColumn
asyProfParameter22 = _AsyProfParameter22_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 21, 1, 26),
    _AsyProfParameter22_Type()
)
asyProfParameter22.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asyProfParameter22.setStatus("mandatory")


class _AsyProfParameter23_Type(Integer32):
    """Custom type asyProfParameter23 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_AsyProfParameter23_Type.__name__ = "Integer32"
_AsyProfParameter23_Object = MibTableColumn
asyProfParameter23 = _AsyProfParameter23_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 21, 1, 27),
    _AsyProfParameter23_Type()
)
asyProfParameter23.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asyProfParameter23.setStatus("mandatory")


class _AsyProfParameter24_Type(Integer32):
    """Custom type asyProfParameter24 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_AsyProfParameter24_Type.__name__ = "Integer32"
_AsyProfParameter24_Object = MibTableColumn
asyProfParameter24 = _AsyProfParameter24_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 21, 1, 28),
    _AsyProfParameter24_Type()
)
asyProfParameter24.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asyProfParameter24.setStatus("mandatory")


class _AsyProfParameter25_Type(Integer32):
    """Custom type asyProfParameter25 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_AsyProfParameter25_Type.__name__ = "Integer32"
_AsyProfParameter25_Object = MibTableColumn
asyProfParameter25 = _AsyProfParameter25_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 21, 1, 29),
    _AsyProfParameter25_Type()
)
asyProfParameter25.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asyProfParameter25.setStatus("mandatory")


class _AsyProfParameter26_Type(Integer32):
    """Custom type asyProfParameter26 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_AsyProfParameter26_Type.__name__ = "Integer32"
_AsyProfParameter26_Object = MibTableColumn
asyProfParameter26 = _AsyProfParameter26_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 21, 1, 30),
    _AsyProfParameter26_Type()
)
asyProfParameter26.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asyProfParameter26.setStatus("mandatory")


class _AsyProfParameter27_Type(Integer32):
    """Custom type asyProfParameter27 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_AsyProfParameter27_Type.__name__ = "Integer32"
_AsyProfParameter27_Object = MibTableColumn
asyProfParameter27 = _AsyProfParameter27_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 21, 1, 31),
    _AsyProfParameter27_Type()
)
asyProfParameter27.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asyProfParameter27.setStatus("mandatory")


class _AsyProfParameter28_Type(Integer32):
    """Custom type asyProfParameter28 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_AsyProfParameter28_Type.__name__ = "Integer32"
_AsyProfParameter28_Object = MibTableColumn
asyProfParameter28 = _AsyProfParameter28_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 21, 1, 32),
    _AsyProfParameter28_Type()
)
asyProfParameter28.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asyProfParameter28.setStatus("mandatory")
_AsySapProfTable_Object = MibTable
asySapProfTable = _AsySapProfTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 22)
)
if mibBuilder.loadTexts:
    asySapProfTable.setStatus("mandatory")
_AsySapProfEntry_Object = MibTableRow
asySapProfEntry = _AsySapProfEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 22, 1)
)
asySapProfEntry.setIndexNames(
    (0, "CXAsync-MIB", "asySapProfSapNumber"),
)
if mibBuilder.loadTexts:
    asySapProfEntry.setStatus("mandatory")
_AsySapProfSapNumber_Type = SapIndex
_AsySapProfSapNumber_Object = MibTableColumn
asySapProfSapNumber = _AsySapProfSapNumber_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 22, 1, 1),
    _AsySapProfSapNumber_Type()
)
asySapProfSapNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asySapProfSapNumber.setStatus("mandatory")


class _AsySapProfParameter1_Type(Integer32):
    """Custom type asySapProfParameter1 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 126),
    )


_AsySapProfParameter1_Type.__name__ = "Integer32"
_AsySapProfParameter1_Object = MibTableColumn
asySapProfParameter1 = _AsySapProfParameter1_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 22, 1, 5),
    _AsySapProfParameter1_Type()
)
asySapProfParameter1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asySapProfParameter1.setStatus("mandatory")


class _AsySapProfParameter2_Type(Integer32):
    """Custom type asySapProfParameter2 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AsySapProfParameter2_Type.__name__ = "Integer32"
_AsySapProfParameter2_Object = MibTableColumn
asySapProfParameter2 = _AsySapProfParameter2_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 22, 1, 6),
    _AsySapProfParameter2_Type()
)
asySapProfParameter2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asySapProfParameter2.setStatus("mandatory")


class _AsySapProfParameter3_Type(Integer32):
    """Custom type asySapProfParameter3 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 126),
    )


_AsySapProfParameter3_Type.__name__ = "Integer32"
_AsySapProfParameter3_Object = MibTableColumn
asySapProfParameter3 = _AsySapProfParameter3_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 22, 1, 7),
    _AsySapProfParameter3_Type()
)
asySapProfParameter3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asySapProfParameter3.setStatus("mandatory")


class _AsySapProfParameter4_Type(Integer32):
    """Custom type asySapProfParameter4 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AsySapProfParameter4_Type.__name__ = "Integer32"
_AsySapProfParameter4_Object = MibTableColumn
asySapProfParameter4 = _AsySapProfParameter4_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 22, 1, 8),
    _AsySapProfParameter4_Type()
)
asySapProfParameter4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asySapProfParameter4.setStatus("mandatory")


class _AsySapProfParameter5_Type(Integer32):
    """Custom type asySapProfParameter5 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AsySapProfParameter5_Type.__name__ = "Integer32"
_AsySapProfParameter5_Object = MibTableColumn
asySapProfParameter5 = _AsySapProfParameter5_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 22, 1, 9),
    _AsySapProfParameter5_Type()
)
asySapProfParameter5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asySapProfParameter5.setStatus("mandatory")


class _AsySapProfParameter6_Type(Integer32):
    """Custom type asySapProfParameter6 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_AsySapProfParameter6_Type.__name__ = "Integer32"
_AsySapProfParameter6_Object = MibTableColumn
asySapProfParameter6 = _AsySapProfParameter6_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 22, 1, 10),
    _AsySapProfParameter6_Type()
)
asySapProfParameter6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asySapProfParameter6.setStatus("mandatory")


class _AsySapProfParameter7_Type(Integer32):
    """Custom type asySapProfParameter7 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 21),
    )


_AsySapProfParameter7_Type.__name__ = "Integer32"
_AsySapProfParameter7_Object = MibTableColumn
asySapProfParameter7 = _AsySapProfParameter7_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 22, 1, 11),
    _AsySapProfParameter7_Type()
)
asySapProfParameter7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asySapProfParameter7.setStatus("mandatory")


class _AsySapProfParameter8_Type(Integer32):
    """Custom type asySapProfParameter8 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AsySapProfParameter8_Type.__name__ = "Integer32"
_AsySapProfParameter8_Object = MibTableColumn
asySapProfParameter8 = _AsySapProfParameter8_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 22, 1, 12),
    _AsySapProfParameter8_Type()
)
asySapProfParameter8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asySapProfParameter8.setStatus("mandatory")


class _AsySapProfParameter9_Type(Integer32):
    """Custom type asySapProfParameter9 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AsySapProfParameter9_Type.__name__ = "Integer32"
_AsySapProfParameter9_Object = MibTableColumn
asySapProfParameter9 = _AsySapProfParameter9_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 22, 1, 13),
    _AsySapProfParameter9_Type()
)
asySapProfParameter9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asySapProfParameter9.setStatus("mandatory")


class _AsySapProfParameter10_Type(Integer32):
    """Custom type asySapProfParameter10 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AsySapProfParameter10_Type.__name__ = "Integer32"
_AsySapProfParameter10_Object = MibTableColumn
asySapProfParameter10 = _AsySapProfParameter10_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 22, 1, 14),
    _AsySapProfParameter10_Type()
)
asySapProfParameter10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asySapProfParameter10.setStatus("mandatory")


class _AsySapProfParameter11_Type(Integer32):
    """Custom type asySapProfParameter11 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 22),
    )


_AsySapProfParameter11_Type.__name__ = "Integer32"
_AsySapProfParameter11_Object = MibTableColumn
asySapProfParameter11 = _AsySapProfParameter11_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 22, 1, 15),
    _AsySapProfParameter11_Type()
)
asySapProfParameter11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asySapProfParameter11.setStatus("mandatory")


class _AsySapProfParameter12_Type(Integer32):
    """Custom type asySapProfParameter12 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AsySapProfParameter12_Type.__name__ = "Integer32"
_AsySapProfParameter12_Object = MibTableColumn
asySapProfParameter12 = _AsySapProfParameter12_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 22, 1, 16),
    _AsySapProfParameter12_Type()
)
asySapProfParameter12.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asySapProfParameter12.setStatus("mandatory")


class _AsySapProfParameter13_Type(Integer32):
    """Custom type asySapProfParameter13 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AsySapProfParameter13_Type.__name__ = "Integer32"
_AsySapProfParameter13_Object = MibTableColumn
asySapProfParameter13 = _AsySapProfParameter13_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 22, 1, 17),
    _AsySapProfParameter13_Type()
)
asySapProfParameter13.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asySapProfParameter13.setStatus("mandatory")


class _AsySapProfParameter14_Type(Integer32):
    """Custom type asySapProfParameter14 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AsySapProfParameter14_Type.__name__ = "Integer32"
_AsySapProfParameter14_Object = MibTableColumn
asySapProfParameter14 = _AsySapProfParameter14_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 22, 1, 18),
    _AsySapProfParameter14_Type()
)
asySapProfParameter14.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asySapProfParameter14.setStatus("mandatory")


class _AsySapProfParameter15_Type(Integer32):
    """Custom type asySapProfParameter15 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AsySapProfParameter15_Type.__name__ = "Integer32"
_AsySapProfParameter15_Object = MibTableColumn
asySapProfParameter15 = _AsySapProfParameter15_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 22, 1, 19),
    _AsySapProfParameter15_Type()
)
asySapProfParameter15.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asySapProfParameter15.setStatus("mandatory")


class _AsySapProfParameter16_Type(Integer32):
    """Custom type asySapProfParameter16 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_AsySapProfParameter16_Type.__name__ = "Integer32"
_AsySapProfParameter16_Object = MibTableColumn
asySapProfParameter16 = _AsySapProfParameter16_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 22, 1, 20),
    _AsySapProfParameter16_Type()
)
asySapProfParameter16.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asySapProfParameter16.setStatus("mandatory")


class _AsySapProfParameter17_Type(Integer32):
    """Custom type asySapProfParameter17 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_AsySapProfParameter17_Type.__name__ = "Integer32"
_AsySapProfParameter17_Object = MibTableColumn
asySapProfParameter17 = _AsySapProfParameter17_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 22, 1, 21),
    _AsySapProfParameter17_Type()
)
asySapProfParameter17.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asySapProfParameter17.setStatus("mandatory")


class _AsySapProfParameter18_Type(Integer32):
    """Custom type asySapProfParameter18 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_AsySapProfParameter18_Type.__name__ = "Integer32"
_AsySapProfParameter18_Object = MibTableColumn
asySapProfParameter18 = _AsySapProfParameter18_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 22, 1, 22),
    _AsySapProfParameter18_Type()
)
asySapProfParameter18.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asySapProfParameter18.setStatus("mandatory")


class _AsySapProfParameter19_Type(Integer32):
    """Custom type asySapProfParameter19 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_AsySapProfParameter19_Type.__name__ = "Integer32"
_AsySapProfParameter19_Object = MibTableColumn
asySapProfParameter19 = _AsySapProfParameter19_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 22, 1, 23),
    _AsySapProfParameter19_Type()
)
asySapProfParameter19.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asySapProfParameter19.setStatus("mandatory")


class _AsySapProfParameter20_Type(Integer32):
    """Custom type asySapProfParameter20 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_AsySapProfParameter20_Type.__name__ = "Integer32"
_AsySapProfParameter20_Object = MibTableColumn
asySapProfParameter20 = _AsySapProfParameter20_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 22, 1, 24),
    _AsySapProfParameter20_Type()
)
asySapProfParameter20.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asySapProfParameter20.setStatus("mandatory")


class _AsySapProfParameter21_Type(Integer32):
    """Custom type asySapProfParameter21 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_AsySapProfParameter21_Type.__name__ = "Integer32"
_AsySapProfParameter21_Object = MibTableColumn
asySapProfParameter21 = _AsySapProfParameter21_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 22, 1, 25),
    _AsySapProfParameter21_Type()
)
asySapProfParameter21.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asySapProfParameter21.setStatus("mandatory")


class _AsySapProfParameter22_Type(Integer32):
    """Custom type asySapProfParameter22 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AsySapProfParameter22_Type.__name__ = "Integer32"
_AsySapProfParameter22_Object = MibTableColumn
asySapProfParameter22 = _AsySapProfParameter22_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 22, 1, 26),
    _AsySapProfParameter22_Type()
)
asySapProfParameter22.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asySapProfParameter22.setStatus("mandatory")


class _AsySapProfParameter23_Type(Integer32):
    """Custom type asySapProfParameter23 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_AsySapProfParameter23_Type.__name__ = "Integer32"
_AsySapProfParameter23_Object = MibTableColumn
asySapProfParameter23 = _AsySapProfParameter23_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 22, 1, 27),
    _AsySapProfParameter23_Type()
)
asySapProfParameter23.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asySapProfParameter23.setStatus("mandatory")


class _AsySapProfParameter24_Type(Integer32):
    """Custom type asySapProfParameter24 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_AsySapProfParameter24_Type.__name__ = "Integer32"
_AsySapProfParameter24_Object = MibTableColumn
asySapProfParameter24 = _AsySapProfParameter24_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 22, 1, 28),
    _AsySapProfParameter24_Type()
)
asySapProfParameter24.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asySapProfParameter24.setStatus("mandatory")


class _AsySapProfParameter25_Type(Integer32):
    """Custom type asySapProfParameter25 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_AsySapProfParameter25_Type.__name__ = "Integer32"
_AsySapProfParameter25_Object = MibTableColumn
asySapProfParameter25 = _AsySapProfParameter25_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 22, 1, 29),
    _AsySapProfParameter25_Type()
)
asySapProfParameter25.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asySapProfParameter25.setStatus("mandatory")


class _AsySapProfParameter26_Type(Integer32):
    """Custom type asySapProfParameter26 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_AsySapProfParameter26_Type.__name__ = "Integer32"
_AsySapProfParameter26_Object = MibTableColumn
asySapProfParameter26 = _AsySapProfParameter26_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 22, 1, 30),
    _AsySapProfParameter26_Type()
)
asySapProfParameter26.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asySapProfParameter26.setStatus("mandatory")


class _AsySapProfParameter27_Type(Integer32):
    """Custom type asySapProfParameter27 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_AsySapProfParameter27_Type.__name__ = "Integer32"
_AsySapProfParameter27_Object = MibTableColumn
asySapProfParameter27 = _AsySapProfParameter27_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 22, 1, 31),
    _AsySapProfParameter27_Type()
)
asySapProfParameter27.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asySapProfParameter27.setStatus("mandatory")


class _AsySapProfParameter28_Type(Integer32):
    """Custom type asySapProfParameter28 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_AsySapProfParameter28_Type.__name__ = "Integer32"
_AsySapProfParameter28_Object = MibTableColumn
asySapProfParameter28 = _AsySapProfParameter28_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 22, 1, 32),
    _AsySapProfParameter28_Type()
)
asySapProfParameter28.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asySapProfParameter28.setStatus("mandatory")
_AsyDteTable_Object = MibTable
asyDteTable = _AsyDteTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 23)
)
if mibBuilder.loadTexts:
    asyDteTable.setStatus("mandatory")
_AsyDteEntry_Object = MibTableRow
asyDteEntry = _AsyDteEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 23, 1)
)
asyDteEntry.setIndexNames(
    (0, "CXAsync-MIB", "asyDteNumber"),
)
if mibBuilder.loadTexts:
    asyDteEntry.setStatus("mandatory")
_AsyDteNumber_Type = DteIndex
_AsyDteNumber_Object = MibTableColumn
asyDteNumber = _AsyDteNumber_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 23, 1, 1),
    _AsyDteNumber_Type()
)
asyDteNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asyDteNumber.setStatus("mandatory")


class _AsyDteRowStatus_Type(Integer32):
    """Custom type asyDteRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_AsyDteRowStatus_Type.__name__ = "Integer32"
_AsyDteRowStatus_Object = MibTableColumn
asyDteRowStatus = _AsyDteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 23, 1, 2),
    _AsyDteRowStatus_Type()
)
asyDteRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asyDteRowStatus.setStatus("mandatory")
_AsyDteAlias_Type = Alias
_AsyDteAlias_Object = MibTableColumn
asyDteAlias = _AsyDteAlias_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 23, 1, 3),
    _AsyDteAlias_Type()
)
asyDteAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asyDteAlias.setStatus("mandatory")


class _AsyDteCalledAddress_Type(DisplayString):
    """Custom type asyDteCalledAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_AsyDteCalledAddress_Type.__name__ = "DisplayString"
_AsyDteCalledAddress_Object = MibTableColumn
asyDteCalledAddress = _AsyDteCalledAddress_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 23, 1, 5),
    _AsyDteCalledAddress_Type()
)
asyDteCalledAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asyDteCalledAddress.setStatus("mandatory")


class _AsyDteFacilityField_Type(DisplayString):
    """Custom type asyDteFacilityField based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AsyDteFacilityField_Type.__name__ = "DisplayString"
_AsyDteFacilityField_Object = MibTableColumn
asyDteFacilityField = _AsyDteFacilityField_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 23, 1, 6),
    _AsyDteFacilityField_Type()
)
asyDteFacilityField.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asyDteFacilityField.setStatus("mandatory")


class _AsyDteUserDataField_Type(DisplayString):
    """Custom type asyDteUserDataField based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AsyDteUserDataField_Type.__name__ = "DisplayString"
_AsyDteUserDataField_Object = MibTableColumn
asyDteUserDataField = _AsyDteUserDataField_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 23, 1, 7),
    _AsyDteUserDataField_Type()
)
asyDteUserDataField.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asyDteUserDataField.setStatus("mandatory")


class _AsyDteX3Profile_Type(Integer32):
    """Custom type asyDteX3Profile based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AsyDteX3Profile_Type.__name__ = "Integer32"
_AsyDteX3Profile_Object = MibTableColumn
asyDteX3Profile = _AsyDteX3Profile_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 23, 1, 8),
    _AsyDteX3Profile_Type()
)
asyDteX3Profile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asyDteX3Profile.setStatus("mandatory")

# Managed Objects groups


# Notification objects

asySapAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 0, 1)
)
asySapAlarm.setObjects(
      *(("CXAsync-MIB", "asySapNumber"),
        ("CXAsync-MIB", "asySapStatusEvent"))
)
if mibBuilder.loadTexts:
    asySapAlarm.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CXAsync-MIB",
    **{"PacketSize": PacketSize,
       "YesNo": YesNo,
       "ProfIndex": ProfIndex,
       "DteIndex": DteIndex,
       "asySapAlarm": asySapAlarm,
       "asyX25TxQThreshold": asyX25TxQThreshold,
       "asyPadIdBanner": asyPadIdBanner,
       "asyAlarms": asyAlarms,
       "asySapStatusEvent": asySapStatusEvent,
       "asySoftwareVersions": asySoftwareVersions,
       "asyMibLevel": asyMibLevel,
       "asySapTable": asySapTable,
       "asySapEntry": asySapEntry,
       "asySapNumber": asySapNumber,
       "asySapRowStatus": asySapRowStatus,
       "asySapAlias": asySapAlias,
       "asySapMCompanionAlias": asySapMCompanionAlias,
       "asySapNCompanionAlias": asySapNCompanionAlias,
       "asySapX3Profile": asySapX3Profile,
       "asySapNUI": asySapNUI,
       "asySapAddress": asySapAddress,
       "asySapDisconnectRequest": asySapDisconnectRequest,
       "asySapRxThruputClass": asySapRxThruputClass,
       "asySapTxThruputClass": asySapTxThruputClass,
       "asySapTxPacketSize": asySapTxPacketSize,
       "asySapRxPacketSize": asySapRxPacketSize,
       "asySapTxWindowSize": asySapTxWindowSize,
       "asySapRxWindowSize": asySapRxWindowSize,
       "asySapYTTimer": asySapYTTimer,
       "asySapSRTimer": asySapSRTimer,
       "asySapNUILength": asySapNUILength,
       "asySapReverseChargingAcceptance": asySapReverseChargingAcceptance,
       "asySapChargingInformation": asySapChargingInformation,
       "asySapSubscriptionCUG": asySapSubscriptionCUG,
       "asySapSubscriptionCUGOA": asySapSubscriptionCUGOA,
       "asySapSubscriptionCUGIA": asySapSubscriptionCUGIA,
       "asySapPreferentialCUGIndex": asySapPreferentialCUGIndex,
       "asySapReceiptConfirmation": asySapReceiptConfirmation,
       "asySapEnableProtocolId": asySapEnableProtocolId,
       "asySapProtocolId": asySapProtocolId,
       "asySapPromptSignal": asySapPromptSignal,
       "asySapAutoConnectDteId": asySapAutoConnectDteId,
       "asySapAutoConnectRetry": asySapAutoConnectRetry,
       "asySapAutoConnectDelayTimer": asySapAutoConnectDelayTimer,
       "asySapHardwareFlowControl": asySapHardwareFlowControl,
       "asySapProtocolType": asySapProtocolType,
       "asySapControl": asySapControl,
       "asySapState": asySapState,
       "asySapAsyncFlowControlState": asySapAsyncFlowControlState,
       "asySapNetworkFlowControlState": asySapNetworkFlowControlState,
       "asySapAsyncTxQueueSize": asySapAsyncTxQueueSize,
       "asySapX25TxQueueSize": asySapX25TxQueueSize,
       "asySapNumberConnects": asySapNumberConnects,
       "asySapNumberDisconnects": asySapNumberDisconnects,
       "asySapTxDataCharacters": asySapTxDataCharacters,
       "asySapRxDataCharacters": asySapRxDataCharacters,
       "asySapParityErrors": asySapParityErrors,
       "asySapOverruns": asySapOverruns,
       "asySapFlowControlByUser": asySapFlowControlByUser,
       "asySapFlowControlByX25": asySapFlowControlByX25,
       "asySapFlowControlToUser": asySapFlowControlToUser,
       "asySapFlowControlToX25": asySapFlowControlToX25,
       "asySapRxReset": asySapRxReset,
       "asySapRxBreak": asySapRxBreak,
       "asySapTxBreak": asySapTxBreak,
       "asySapRxDiscardCharacters": asySapRxDiscardCharacters,
       "asyProfTable": asyProfTable,
       "asyProfEntry": asyProfEntry,
       "asyProfNumber": asyProfNumber,
       "asyProfRowStatus": asyProfRowStatus,
       "asyProfAlias": asyProfAlias,
       "asyProfParameter1": asyProfParameter1,
       "asyProfParameter2": asyProfParameter2,
       "asyProfParameter3": asyProfParameter3,
       "asyProfParameter4": asyProfParameter4,
       "asyProfParameter5": asyProfParameter5,
       "asyProfParameter6": asyProfParameter6,
       "asyProfParameter7": asyProfParameter7,
       "asyProfParameter8": asyProfParameter8,
       "asyProfParameter9": asyProfParameter9,
       "asyProfParameter10": asyProfParameter10,
       "asyProfParameter11": asyProfParameter11,
       "asyProfParameter12": asyProfParameter12,
       "asyProfParameter13": asyProfParameter13,
       "asyProfParameter14": asyProfParameter14,
       "asyProfParameter15": asyProfParameter15,
       "asyProfParameter16": asyProfParameter16,
       "asyProfParameter17": asyProfParameter17,
       "asyProfParameter18": asyProfParameter18,
       "asyProfParameter19": asyProfParameter19,
       "asyProfParameter20": asyProfParameter20,
       "asyProfParameter21": asyProfParameter21,
       "asyProfParameter22": asyProfParameter22,
       "asyProfParameter23": asyProfParameter23,
       "asyProfParameter24": asyProfParameter24,
       "asyProfParameter25": asyProfParameter25,
       "asyProfParameter26": asyProfParameter26,
       "asyProfParameter27": asyProfParameter27,
       "asyProfParameter28": asyProfParameter28,
       "asySapProfTable": asySapProfTable,
       "asySapProfEntry": asySapProfEntry,
       "asySapProfSapNumber": asySapProfSapNumber,
       "asySapProfParameter1": asySapProfParameter1,
       "asySapProfParameter2": asySapProfParameter2,
       "asySapProfParameter3": asySapProfParameter3,
       "asySapProfParameter4": asySapProfParameter4,
       "asySapProfParameter5": asySapProfParameter5,
       "asySapProfParameter6": asySapProfParameter6,
       "asySapProfParameter7": asySapProfParameter7,
       "asySapProfParameter8": asySapProfParameter8,
       "asySapProfParameter9": asySapProfParameter9,
       "asySapProfParameter10": asySapProfParameter10,
       "asySapProfParameter11": asySapProfParameter11,
       "asySapProfParameter12": asySapProfParameter12,
       "asySapProfParameter13": asySapProfParameter13,
       "asySapProfParameter14": asySapProfParameter14,
       "asySapProfParameter15": asySapProfParameter15,
       "asySapProfParameter16": asySapProfParameter16,
       "asySapProfParameter17": asySapProfParameter17,
       "asySapProfParameter18": asySapProfParameter18,
       "asySapProfParameter19": asySapProfParameter19,
       "asySapProfParameter20": asySapProfParameter20,
       "asySapProfParameter21": asySapProfParameter21,
       "asySapProfParameter22": asySapProfParameter22,
       "asySapProfParameter23": asySapProfParameter23,
       "asySapProfParameter24": asySapProfParameter24,
       "asySapProfParameter25": asySapProfParameter25,
       "asySapProfParameter26": asySapProfParameter26,
       "asySapProfParameter27": asySapProfParameter27,
       "asySapProfParameter28": asySapProfParameter28,
       "asyDteTable": asyDteTable,
       "asyDteEntry": asyDteEntry,
       "asyDteNumber": asyDteNumber,
       "asyDteRowStatus": asyDteRowStatus,
       "asyDteAlias": asyDteAlias,
       "asyDteCalledAddress": asyDteCalledAddress,
       "asyDteFacilityField": asyDteFacilityField,
       "asyDteUserDataField": asyDteUserDataField,
       "asyDteX3Profile": asyDteX3Profile}
)
