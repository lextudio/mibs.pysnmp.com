# SNMP MIB module (CXFrameRelay-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CXFrameRelay-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:20:26 2024
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

(cxModuleHwPhysSlot,) = mibBuilder.importSymbols(
    "CXModuleHardware-MIB",
    "cxModuleHwPhysSlot")

(Alias,
 SapIndex,
 cxFrameRelay) = mibBuilder.importSymbols(
    "CXProduct-SMI",
    "Alias",
    "SapIndex",
    "cxFrameRelay")

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



class DLCI(Integer32):
    """Custom type DLCI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1022),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FrpSapTable_Object = MibTable
frpSapTable = _FrpSapTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 1)
)
if mibBuilder.loadTexts:
    frpSapTable.setStatus("mandatory")
_FrpSapEntry_Object = MibTableRow
frpSapEntry = _FrpSapEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 1, 1)
)
frpSapEntry.setIndexNames(
    (0, "CXFrameRelay-MIB", "frpSapNumber"),
)
if mibBuilder.loadTexts:
    frpSapEntry.setStatus("mandatory")
_FrpSapNumber_Type = SapIndex
_FrpSapNumber_Object = MibTableColumn
frpSapNumber = _FrpSapNumber_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 1, 1, 1),
    _FrpSapNumber_Type()
)
frpSapNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpSapNumber.setStatus("mandatory")


class _FrpSapRowStatus_Type(Integer32):
    """Custom type frpSapRowStatus based on Integer32"""
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


_FrpSapRowStatus_Type.__name__ = "Integer32"
_FrpSapRowStatus_Object = MibTableColumn
frpSapRowStatus = _FrpSapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 1, 1, 2),
    _FrpSapRowStatus_Type()
)
frpSapRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frpSapRowStatus.setStatus("mandatory")
_FrpSapAlias_Type = Alias
_FrpSapAlias_Object = MibTableColumn
frpSapAlias = _FrpSapAlias_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 1, 1, 3),
    _FrpSapAlias_Type()
)
frpSapAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frpSapAlias.setStatus("mandatory")
_FrpSapCompanionAlias_Type = Alias
_FrpSapCompanionAlias_Object = MibTableColumn
frpSapCompanionAlias = _FrpSapCompanionAlias_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 1, 1, 4),
    _FrpSapCompanionAlias_Type()
)
frpSapCompanionAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frpSapCompanionAlias.setStatus("mandatory")


class _FrpSapType_Type(Integer32):
    """Custom type frpSapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lower", 1),
          ("upper", 2))
    )


_FrpSapType_Type.__name__ = "Integer32"
_FrpSapType_Object = MibTableColumn
frpSapType = _FrpSapType_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 1, 1, 5),
    _FrpSapType_Type()
)
frpSapType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frpSapType.setStatus("mandatory")


class _FrpSapAddressLength_Type(Integer32):
    """Custom type frpSapAddressLength based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("four-octets", 4),
          ("three-octets", 3),
          ("two-octets", 2))
    )


_FrpSapAddressLength_Type.__name__ = "Integer32"
_FrpSapAddressLength_Object = MibTableColumn
frpSapAddressLength = _FrpSapAddressLength_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 1, 1, 6),
    _FrpSapAddressLength_Type()
)
frpSapAddressLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frpSapAddressLength.setStatus("mandatory")


class _FrpSapMaxSupportedVCs_Type(Integer32):
    """Custom type frpSapMaxSupportedVCs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1022),
    )


_FrpSapMaxSupportedVCs_Type.__name__ = "Integer32"
_FrpSapMaxSupportedVCs_Object = MibTableColumn
frpSapMaxSupportedVCs = _FrpSapMaxSupportedVCs_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 1, 1, 7),
    _FrpSapMaxSupportedVCs_Type()
)
frpSapMaxSupportedVCs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frpSapMaxSupportedVCs.setStatus("deprecated")


class _FrpSapVCBase_Type(Integer32):
    """Custom type frpSapVCBase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1022),
    )


_FrpSapVCBase_Type.__name__ = "Integer32"
_FrpSapVCBase_Object = MibTableColumn
frpSapVCBase = _FrpSapVCBase_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 1, 1, 8),
    _FrpSapVCBase_Type()
)
frpSapVCBase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frpSapVCBase.setStatus("deprecated")


class _FrpSapOutCongestionManagement_Type(Integer32):
    """Custom type frpSapOutCongestionManagement based on Integer32"""
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
          ("enabled", 2))
    )


_FrpSapOutCongestionManagement_Type.__name__ = "Integer32"
_FrpSapOutCongestionManagement_Object = MibTableColumn
frpSapOutCongestionManagement = _FrpSapOutCongestionManagement_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 1, 1, 9),
    _FrpSapOutCongestionManagement_Type()
)
frpSapOutCongestionManagement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frpSapOutCongestionManagement.setStatus("mandatory")


class _FrpSapResourceAllocation_Type(Integer32):
    """Custom type frpSapResourceAllocation based on Integer32"""
    defaultValue = 80

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_FrpSapResourceAllocation_Type.__name__ = "Integer32"
_FrpSapResourceAllocation_Object = MibTableColumn
frpSapResourceAllocation = _FrpSapResourceAllocation_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 1, 1, 10),
    _FrpSapResourceAllocation_Type()
)
frpSapResourceAllocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frpSapResourceAllocation.setStatus("mandatory")


class _FrpSapLinkManagement_Type(Integer32):
    """Custom type frpSapLinkManagement based on Integer32"""
    defaultValue = 1

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
        *(("ansiAnnexD", 3),
          ("auto", 7),
          ("ccittAnnexA", 4),
          ("dama1", 5),
          ("dama2", 6),
          ("frameRelayForum", 2),
          ("none", 1))
    )


_FrpSapLinkManagement_Type.__name__ = "Integer32"
_FrpSapLinkManagement_Object = MibTableColumn
frpSapLinkManagement = _FrpSapLinkManagement_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 1, 1, 11),
    _FrpSapLinkManagement_Type()
)
frpSapLinkManagement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frpSapLinkManagement.setStatus("mandatory")


class _FrpSapInterfaceType_Type(Integer32):
    """Custom type frpSapInterfaceType based on Integer32"""
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
        *(("nni", 3),
          ("uniNetwork", 2),
          ("uniUser", 1))
    )


_FrpSapInterfaceType_Type.__name__ = "Integer32"
_FrpSapInterfaceType_Object = MibTableColumn
frpSapInterfaceType = _FrpSapInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 1, 1, 12),
    _FrpSapInterfaceType_Type()
)
frpSapInterfaceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frpSapInterfaceType.setStatus("mandatory")


class _FrpSapPollingInterval_Type(Integer32):
    """Custom type frpSapPollingInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_FrpSapPollingInterval_Type.__name__ = "Integer32"
_FrpSapPollingInterval_Object = MibTableColumn
frpSapPollingInterval = _FrpSapPollingInterval_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 1, 1, 13),
    _FrpSapPollingInterval_Type()
)
frpSapPollingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frpSapPollingInterval.setStatus("mandatory")


class _FrpSapPollingVerification_Type(Integer32):
    """Custom type frpSapPollingVerification based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_FrpSapPollingVerification_Type.__name__ = "Integer32"
_FrpSapPollingVerification_Object = MibTableColumn
frpSapPollingVerification = _FrpSapPollingVerification_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 1, 1, 14),
    _FrpSapPollingVerification_Type()
)
frpSapPollingVerification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frpSapPollingVerification.setStatus("mandatory")


class _FrpSapFullEnquiryInterval_Type(Integer32):
    """Custom type frpSapFullEnquiryInterval based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FrpSapFullEnquiryInterval_Type.__name__ = "Integer32"
_FrpSapFullEnquiryInterval_Object = MibTableColumn
frpSapFullEnquiryInterval = _FrpSapFullEnquiryInterval_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 1, 1, 15),
    _FrpSapFullEnquiryInterval_Type()
)
frpSapFullEnquiryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frpSapFullEnquiryInterval.setStatus("mandatory")


class _FrpSapErrorThreshold_Type(Integer32):
    """Custom type frpSapErrorThreshold based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_FrpSapErrorThreshold_Type.__name__ = "Integer32"
_FrpSapErrorThreshold_Object = MibTableColumn
frpSapErrorThreshold = _FrpSapErrorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 1, 1, 16),
    _FrpSapErrorThreshold_Type()
)
frpSapErrorThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frpSapErrorThreshold.setStatus("mandatory")


class _FrpSapMonitoredEvents_Type(Integer32):
    """Custom type frpSapMonitoredEvents based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_FrpSapMonitoredEvents_Type.__name__ = "Integer32"
_FrpSapMonitoredEvents_Object = MibTableColumn
frpSapMonitoredEvents = _FrpSapMonitoredEvents_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 1, 1, 17),
    _FrpSapMonitoredEvents_Type()
)
frpSapMonitoredEvents.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frpSapMonitoredEvents.setStatus("mandatory")


class _FrpSapMode_Type(Integer32):
    """Custom type frpSapMode based on Integer32"""
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
        *(("frameRelay", 1),
          ("frameRelayAtmNIwf", 3),
          ("transparent", 2))
    )


_FrpSapMode_Type.__name__ = "Integer32"
_FrpSapMode_Object = MibTableColumn
frpSapMode = _FrpSapMode_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 1, 1, 18),
    _FrpSapMode_Type()
)
frpSapMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frpSapMode.setStatus("mandatory")


class _FrpSapPrioQueue1HitRatio_Type(Integer32):
    """Custom type frpSapPrioQueue1HitRatio based on Integer32"""
    defaultValue = 0


_FrpSapPrioQueue1HitRatio_Object = MibTableColumn
frpSapPrioQueue1HitRatio = _FrpSapPrioQueue1HitRatio_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 1, 1, 19),
    _FrpSapPrioQueue1HitRatio_Type()
)
frpSapPrioQueue1HitRatio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frpSapPrioQueue1HitRatio.setStatus("mandatory")


class _FrpSapPrioQueue2HitRatio_Type(Integer32):
    """Custom type frpSapPrioQueue2HitRatio based on Integer32"""
    defaultValue = 0


_FrpSapPrioQueue2HitRatio_Object = MibTableColumn
frpSapPrioQueue2HitRatio = _FrpSapPrioQueue2HitRatio_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 1, 1, 20),
    _FrpSapPrioQueue2HitRatio_Type()
)
frpSapPrioQueue2HitRatio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frpSapPrioQueue2HitRatio.setStatus("mandatory")


class _FrpSapPrioQueue3HitRatio_Type(Integer32):
    """Custom type frpSapPrioQueue3HitRatio based on Integer32"""
    defaultValue = 0


_FrpSapPrioQueue3HitRatio_Object = MibTableColumn
frpSapPrioQueue3HitRatio = _FrpSapPrioQueue3HitRatio_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 1, 1, 21),
    _FrpSapPrioQueue3HitRatio_Type()
)
frpSapPrioQueue3HitRatio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frpSapPrioQueue3HitRatio.setStatus("mandatory")


class _FrpSapPrioQueue4HitRatio_Type(Integer32):
    """Custom type frpSapPrioQueue4HitRatio based on Integer32"""
    defaultValue = 0


_FrpSapPrioQueue4HitRatio_Object = MibTableColumn
frpSapPrioQueue4HitRatio = _FrpSapPrioQueue4HitRatio_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 1, 1, 22),
    _FrpSapPrioQueue4HitRatio_Type()
)
frpSapPrioQueue4HitRatio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frpSapPrioQueue4HitRatio.setStatus("mandatory")


class _FrpSapDialEntry_Type(Integer32):
    """Custom type frpSapDialEntry based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FrpSapDialEntry_Type.__name__ = "Integer32"
_FrpSapDialEntry_Object = MibTableColumn
frpSapDialEntry = _FrpSapDialEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 1, 1, 23),
    _FrpSapDialEntry_Type()
)
frpSapDialEntry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frpSapDialEntry.setStatus("mandatory")


class _FrpSapFilterBitMap_Type(Integer32):
    """Custom type frpSapFilterBitMap based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FrpSapFilterBitMap_Type.__name__ = "Integer32"
_FrpSapFilterBitMap_Object = MibTableColumn
frpSapFilterBitMap = _FrpSapFilterBitMap_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 1, 1, 24),
    _FrpSapFilterBitMap_Type()
)
frpSapFilterBitMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frpSapFilterBitMap.setStatus("mandatory")


class _FrpSapLmiFlavor_Type(Integer32):
    """Custom type frpSapLmiFlavor based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("strict", 2),
          ("tolerant", 3))
    )


_FrpSapLmiFlavor_Type.__name__ = "Integer32"
_FrpSapLmiFlavor_Object = MibTableColumn
frpSapLmiFlavor = _FrpSapLmiFlavor_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 1, 1, 25),
    _FrpSapLmiFlavor_Type()
)
frpSapLmiFlavor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frpSapLmiFlavor.setStatus("mandatory")


class _FrpSapGenerator_Type(Integer32):
    """Custom type frpSapGenerator based on Integer32"""
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
        *(("disabled", 1),
          ("enabled", 2),
          ("retrigger", 3))
    )


_FrpSapGenerator_Type.__name__ = "Integer32"
_FrpSapGenerator_Object = MibTableColumn
frpSapGenerator = _FrpSapGenerator_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 1, 1, 33),
    _FrpSapGenerator_Type()
)
frpSapGenerator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frpSapGenerator.setStatus("mandatory")


class _FrpSapGeneratorDlciNumber_Type(DLCI):
    """Custom type frpSapGeneratorDlciNumber based on DLCI"""
    defaultValue = 16


_FrpSapGeneratorDlciNumber_Object = MibTableColumn
frpSapGeneratorDlciNumber = _FrpSapGeneratorDlciNumber_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 1, 1, 34),
    _FrpSapGeneratorDlciNumber_Type()
)
frpSapGeneratorDlciNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frpSapGeneratorDlciNumber.setStatus("mandatory")


class _FrpSapGeneratorFrameSize_Type(Integer32):
    """Custom type frpSapGeneratorFrameSize based on Integer32"""
    defaultValue = 32

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 4096),
    )


_FrpSapGeneratorFrameSize_Type.__name__ = "Integer32"
_FrpSapGeneratorFrameSize_Object = MibTableColumn
frpSapGeneratorFrameSize = _FrpSapGeneratorFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 1, 1, 35),
    _FrpSapGeneratorFrameSize_Type()
)
frpSapGeneratorFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frpSapGeneratorFrameSize.setStatus("mandatory")


class _FrpSapGeneratorNumberOfFrames_Type(Integer32):
    """Custom type frpSapGeneratorNumberOfFrames based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_FrpSapGeneratorNumberOfFrames_Type.__name__ = "Integer32"
_FrpSapGeneratorNumberOfFrames_Object = MibTableColumn
frpSapGeneratorNumberOfFrames = _FrpSapGeneratorNumberOfFrames_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 1, 1, 36),
    _FrpSapGeneratorNumberOfFrames_Type()
)
frpSapGeneratorNumberOfFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frpSapGeneratorNumberOfFrames.setStatus("mandatory")


class _FrpSapGeneratorInterFrameDelay_Type(Integer32):
    """Custom type frpSapGeneratorInterFrameDelay based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 60000),
    )


_FrpSapGeneratorInterFrameDelay_Type.__name__ = "Integer32"
_FrpSapGeneratorInterFrameDelay_Object = MibTableColumn
frpSapGeneratorInterFrameDelay = _FrpSapGeneratorInterFrameDelay_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 1, 1, 37),
    _FrpSapGeneratorInterFrameDelay_Type()
)
frpSapGeneratorInterFrameDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frpSapGeneratorInterFrameDelay.setStatus("mandatory")


class _FrpSapBillingTimer_Type(Integer32):
    """Custom type frpSapBillingTimer based on Integer32"""
    defaultValue = 1440

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 525600),
    )


_FrpSapBillingTimer_Type.__name__ = "Integer32"
_FrpSapBillingTimer_Object = MibTableColumn
frpSapBillingTimer = _FrpSapBillingTimer_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 1, 1, 38),
    _FrpSapBillingTimer_Type()
)
frpSapBillingTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frpSapBillingTimer.setStatus("mandatory")


class _FrpSapSdLmMessageInterval_Type(Integer32):
    """Custom type frpSapSdLmMessageInterval based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 65535),
    )


_FrpSapSdLmMessageInterval_Type.__name__ = "Integer32"
_FrpSapSdLmMessageInterval_Object = MibTableColumn
frpSapSdLmMessageInterval = _FrpSapSdLmMessageInterval_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 1, 1, 39),
    _FrpSapSdLmMessageInterval_Type()
)
frpSapSdLmMessageInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frpSapSdLmMessageInterval.setStatus("obsolete")


class _FrpSapSdLmActiveTimer_Type(Integer32):
    """Custom type frpSapSdLmActiveTimer based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 65535),
    )


_FrpSapSdLmActiveTimer_Type.__name__ = "Integer32"
_FrpSapSdLmActiveTimer_Object = MibTableColumn
frpSapSdLmActiveTimer = _FrpSapSdLmActiveTimer_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 1, 1, 40),
    _FrpSapSdLmActiveTimer_Type()
)
frpSapSdLmActiveTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frpSapSdLmActiveTimer.setStatus("obsolete")


class _FrpSaptrapTrap1_Type(Integer32):
    """Custom type frpSaptrapTrap1 based on Integer32"""
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
          ("enabled", 2))
    )


_FrpSaptrapTrap1_Type.__name__ = "Integer32"
_FrpSaptrapTrap1_Object = MibTableColumn
frpSaptrapTrap1 = _FrpSaptrapTrap1_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 1, 1, 48),
    _FrpSaptrapTrap1_Type()
)
frpSaptrapTrap1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frpSaptrapTrap1.setStatus("mandatory")


class _FrpSapControl_Type(Integer32):
    """Custom type frpSapControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("retriggerBillingTimer", 1)
    )


_FrpSapControl_Type.__name__ = "Integer32"
_FrpSapControl_Object = MibTableColumn
frpSapControl = _FrpSapControl_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 1, 1, 53),
    _FrpSapControl_Type()
)
frpSapControl.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    frpSapControl.setStatus("mandatory")


class _FrpSapControlStats_Type(Integer32):
    """Custom type frpSapControlStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clearAllCircuitStats", 2),
          ("clearSapStats", 1))
    )


_FrpSapControlStats_Type.__name__ = "Integer32"
_FrpSapControlStats_Object = MibTableColumn
frpSapControlStats = _FrpSapControlStats_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 1, 1, 54),
    _FrpSapControlStats_Type()
)
frpSapControlStats.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    frpSapControlStats.setStatus("mandatory")


class _FrpSapstatLinkManagementState_Type(Integer32):
    """Custom type frpSapstatLinkManagementState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("linkDown", 1),
          ("linkUp", 2))
    )


_FrpSapstatLinkManagementState_Type.__name__ = "Integer32"
_FrpSapstatLinkManagementState_Object = MibTableColumn
frpSapstatLinkManagementState = _FrpSapstatLinkManagementState_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 1, 1, 55),
    _FrpSapstatLinkManagementState_Type()
)
frpSapstatLinkManagementState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpSapstatLinkManagementState.setStatus("mandatory")


class _FrpSapstatCurrentLinkManagementType_Type(Integer32):
    """Custom type frpSapstatCurrentLinkManagementType based on Integer32"""
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
        *(("ansiAnnexD", 3),
          ("ccittAnnexA", 4),
          ("dama1", 5),
          ("dama2", 6),
          ("discovering", 7),
          ("frameRelayForum", 2),
          ("none", 1))
    )


_FrpSapstatCurrentLinkManagementType_Type.__name__ = "Integer32"
_FrpSapstatCurrentLinkManagementType_Object = MibTableColumn
frpSapstatCurrentLinkManagementType = _FrpSapstatCurrentLinkManagementType_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 1, 1, 56),
    _FrpSapstatCurrentLinkManagementType_Type()
)
frpSapstatCurrentLinkManagementType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpSapstatCurrentLinkManagementType.setStatus("mandatory")
_FrpSapstatTxDataFrames_Type = Counter32
_FrpSapstatTxDataFrames_Object = MibTableColumn
frpSapstatTxDataFrames = _FrpSapstatTxDataFrames_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 1, 1, 61),
    _FrpSapstatTxDataFrames_Type()
)
frpSapstatTxDataFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpSapstatTxDataFrames.setStatus("mandatory")
_FrpSapstatRxDataFrames_Type = Counter32
_FrpSapstatRxDataFrames_Object = MibTableColumn
frpSapstatRxDataFrames = _FrpSapstatRxDataFrames_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 1, 1, 62),
    _FrpSapstatRxDataFrames_Type()
)
frpSapstatRxDataFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpSapstatRxDataFrames.setStatus("mandatory")
_FrpSapstatTxDataOctets_Type = Counter32
_FrpSapstatTxDataOctets_Object = MibTableColumn
frpSapstatTxDataOctets = _FrpSapstatTxDataOctets_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 1, 1, 63),
    _FrpSapstatTxDataOctets_Type()
)
frpSapstatTxDataOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpSapstatTxDataOctets.setStatus("mandatory")
_FrpSapstatRxDataOctets_Type = Counter32
_FrpSapstatRxDataOctets_Object = MibTableColumn
frpSapstatRxDataOctets = _FrpSapstatRxDataOctets_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 1, 1, 64),
    _FrpSapstatRxDataOctets_Type()
)
frpSapstatRxDataOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpSapstatRxDataOctets.setStatus("mandatory")
_FrpSapstatTxLmiFrames_Type = Counter32
_FrpSapstatTxLmiFrames_Object = MibTableColumn
frpSapstatTxLmiFrames = _FrpSapstatTxLmiFrames_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 1, 1, 65),
    _FrpSapstatTxLmiFrames_Type()
)
frpSapstatTxLmiFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpSapstatTxLmiFrames.setStatus("mandatory")
_FrpSapstatRxLmiFrames_Type = Counter32
_FrpSapstatRxLmiFrames_Object = MibTableColumn
frpSapstatRxLmiFrames = _FrpSapstatRxLmiFrames_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 1, 1, 66),
    _FrpSapstatRxLmiFrames_Type()
)
frpSapstatRxLmiFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpSapstatRxLmiFrames.setStatus("mandatory")
_FrpSapstatTxQueuedDiscards_Type = Counter32
_FrpSapstatTxQueuedDiscards_Object = MibTableColumn
frpSapstatTxQueuedDiscards = _FrpSapstatTxQueuedDiscards_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 1, 1, 67),
    _FrpSapstatTxQueuedDiscards_Type()
)
frpSapstatTxQueuedDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpSapstatTxQueuedDiscards.setStatus("mandatory")
_FrpSapstatRxCIRExceededDiscards_Type = Counter32
_FrpSapstatRxCIRExceededDiscards_Object = MibTableColumn
frpSapstatRxCIRExceededDiscards = _FrpSapstatRxCIRExceededDiscards_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 1, 1, 79),
    _FrpSapstatRxCIRExceededDiscards_Type()
)
frpSapstatRxCIRExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpSapstatRxCIRExceededDiscards.setStatus("mandatory")
_FrpSapstatRxSysCongestionDiscards_Type = Counter32
_FrpSapstatRxSysCongestionDiscards_Object = MibTableColumn
frpSapstatRxSysCongestionDiscards = _FrpSapstatRxSysCongestionDiscards_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 1, 1, 80),
    _FrpSapstatRxSysCongestionDiscards_Type()
)
frpSapstatRxSysCongestionDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpSapstatRxSysCongestionDiscards.setStatus("mandatory")
_FrpSapstatRxUnavailInboundDiscards_Type = Counter32
_FrpSapstatRxUnavailInboundDiscards_Object = MibTableColumn
frpSapstatRxUnavailInboundDiscards = _FrpSapstatRxUnavailInboundDiscards_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 1, 1, 81),
    _FrpSapstatRxUnavailInboundDiscards_Type()
)
frpSapstatRxUnavailInboundDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpSapstatRxUnavailInboundDiscards.setStatus("mandatory")
_FrpSapstatRxUnavailOutboundDiscards_Type = Counter32
_FrpSapstatRxUnavailOutboundDiscards_Object = MibTableColumn
frpSapstatRxUnavailOutboundDiscards = _FrpSapstatRxUnavailOutboundDiscards_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 1, 1, 82),
    _FrpSapstatRxUnavailOutboundDiscards_Type()
)
frpSapstatRxUnavailOutboundDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpSapstatRxUnavailOutboundDiscards.setStatus("mandatory")
_FrpSapstatRxInvalidVCDiscards_Type = Counter32
_FrpSapstatRxInvalidVCDiscards_Object = MibTableColumn
frpSapstatRxInvalidVCDiscards = _FrpSapstatRxInvalidVCDiscards_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 1, 1, 83),
    _FrpSapstatRxInvalidVCDiscards_Type()
)
frpSapstatRxInvalidVCDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpSapstatRxInvalidVCDiscards.setStatus("mandatory")
_FrpSapstatRxBadStatusDiscards_Type = Counter32
_FrpSapstatRxBadStatusDiscards_Object = MibTableColumn
frpSapstatRxBadStatusDiscards = _FrpSapstatRxBadStatusDiscards_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 1, 1, 84),
    _FrpSapstatRxBadStatusDiscards_Type()
)
frpSapstatRxBadStatusDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpSapstatRxBadStatusDiscards.setStatus("mandatory")
_FrpSapstatRxMiscellaneousDiscards_Type = Counter32
_FrpSapstatRxMiscellaneousDiscards_Object = MibTableColumn
frpSapstatRxMiscellaneousDiscards = _FrpSapstatRxMiscellaneousDiscards_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 1, 1, 85),
    _FrpSapstatRxMiscellaneousDiscards_Type()
)
frpSapstatRxMiscellaneousDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpSapstatRxMiscellaneousDiscards.setStatus("mandatory")
_FrpSapstatRxCIRExceeds_Type = Counter32
_FrpSapstatRxCIRExceeds_Object = MibTableColumn
frpSapstatRxCIRExceeds = _FrpSapstatRxCIRExceeds_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 1, 1, 86),
    _FrpSapstatRxCIRExceeds_Type()
)
frpSapstatRxCIRExceeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpSapstatRxCIRExceeds.setStatus("mandatory")
_FrpSapstatRxShortFrameDiscards_Type = Counter32
_FrpSapstatRxShortFrameDiscards_Object = MibTableColumn
frpSapstatRxShortFrameDiscards = _FrpSapstatRxShortFrameDiscards_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 1, 1, 87),
    _FrpSapstatRxShortFrameDiscards_Type()
)
frpSapstatRxShortFrameDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpSapstatRxShortFrameDiscards.setStatus("mandatory")
_FrpSapstatLmiInvalidFieldDiscards_Type = Counter32
_FrpSapstatLmiInvalidFieldDiscards_Object = MibTableColumn
frpSapstatLmiInvalidFieldDiscards = _FrpSapstatLmiInvalidFieldDiscards_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 1, 1, 97),
    _FrpSapstatLmiInvalidFieldDiscards_Type()
)
frpSapstatLmiInvalidFieldDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpSapstatLmiInvalidFieldDiscards.setStatus("mandatory")
_FrpSapstatLmiInvalidSequenceDiscards_Type = Counter32
_FrpSapstatLmiInvalidSequenceDiscards_Object = MibTableColumn
frpSapstatLmiInvalidSequenceDiscards = _FrpSapstatLmiInvalidSequenceDiscards_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 1, 1, 98),
    _FrpSapstatLmiInvalidSequenceDiscards_Type()
)
frpSapstatLmiInvalidSequenceDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpSapstatLmiInvalidSequenceDiscards.setStatus("mandatory")
_FrpSapstatLmiTimeouts_Type = Counter32
_FrpSapstatLmiTimeouts_Object = MibTableColumn
frpSapstatLmiTimeouts = _FrpSapstatLmiTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 1, 1, 99),
    _FrpSapstatLmiTimeouts_Type()
)
frpSapstatLmiTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpSapstatLmiTimeouts.setStatus("mandatory")
_FrpSapstatLmiInvalidStatusDiscards_Type = Counter32
_FrpSapstatLmiInvalidStatusDiscards_Object = MibTableColumn
frpSapstatLmiInvalidStatusDiscards = _FrpSapstatLmiInvalidStatusDiscards_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 1, 1, 100),
    _FrpSapstatLmiInvalidStatusDiscards_Type()
)
frpSapstatLmiInvalidStatusDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpSapstatLmiInvalidStatusDiscards.setStatus("mandatory")
_FrpSapstatLmiInvalidStatusEnqDiscards_Type = Counter32
_FrpSapstatLmiInvalidStatusEnqDiscards_Object = MibTableColumn
frpSapstatLmiInvalidStatusEnqDiscards = _FrpSapstatLmiInvalidStatusEnqDiscards_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 1, 1, 101),
    _FrpSapstatLmiInvalidStatusEnqDiscards_Type()
)
frpSapstatLmiInvalidStatusEnqDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpSapstatLmiInvalidStatusEnqDiscards.setStatus("mandatory")
_FrpSapstatLmiInvalidUpdStatusDiscards_Type = Counter32
_FrpSapstatLmiInvalidUpdStatusDiscards_Object = MibTableColumn
frpSapstatLmiInvalidUpdStatusDiscards = _FrpSapstatLmiInvalidUpdStatusDiscards_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 1, 1, 102),
    _FrpSapstatLmiInvalidUpdStatusDiscards_Type()
)
frpSapstatLmiInvalidUpdStatusDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpSapstatLmiInvalidUpdStatusDiscards.setStatus("mandatory")
_FrpCircuitTable_Object = MibTable
frpCircuitTable = _FrpCircuitTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 2)
)
if mibBuilder.loadTexts:
    frpCircuitTable.setStatus("mandatory")
_FrpCircuitEntry_Object = MibTableRow
frpCircuitEntry = _FrpCircuitEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 2, 1)
)
frpCircuitEntry.setIndexNames(
    (0, "CXFrameRelay-MIB", "frpCircuitSapNumber"),
    (0, "CXFrameRelay-MIB", "frpCircuitDlci"),
)
if mibBuilder.loadTexts:
    frpCircuitEntry.setStatus("mandatory")
_FrpCircuitSapNumber_Type = SapIndex
_FrpCircuitSapNumber_Object = MibTableColumn
frpCircuitSapNumber = _FrpCircuitSapNumber_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 2, 1, 1),
    _FrpCircuitSapNumber_Type()
)
frpCircuitSapNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpCircuitSapNumber.setStatus("mandatory")
_FrpCircuitDlci_Type = DLCI
_FrpCircuitDlci_Object = MibTableColumn
frpCircuitDlci = _FrpCircuitDlci_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 2, 1, 2),
    _FrpCircuitDlci_Type()
)
frpCircuitDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpCircuitDlci.setStatus("mandatory")


class _FrpCircuitRowStatus_Type(Integer32):
    """Custom type frpCircuitRowStatus based on Integer32"""
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


_FrpCircuitRowStatus_Type.__name__ = "Integer32"
_FrpCircuitRowStatus_Object = MibTableColumn
frpCircuitRowStatus = _FrpCircuitRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 2, 1, 3),
    _FrpCircuitRowStatus_Type()
)
frpCircuitRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frpCircuitRowStatus.setStatus("mandatory")


class _FrpCircuitPriorityLevel_Type(Integer32):
    """Custom type frpCircuitPriorityLevel based on Integer32"""
    defaultValue = 3

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
        *(("high", 2),
          ("low", 4),
          ("medium", 3),
          ("veryHigh", 1))
    )


_FrpCircuitPriorityLevel_Type.__name__ = "Integer32"
_FrpCircuitPriorityLevel_Object = MibTableColumn
frpCircuitPriorityLevel = _FrpCircuitPriorityLevel_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 2, 1, 4),
    _FrpCircuitPriorityLevel_Type()
)
frpCircuitPriorityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frpCircuitPriorityLevel.setStatus("mandatory")


class _FrpCircuitCommittedBurst_Type(Integer32):
    """Custom type frpCircuitCommittedBurst based on Integer32"""
    defaultValue = 0


_FrpCircuitCommittedBurst_Object = MibTableColumn
frpCircuitCommittedBurst = _FrpCircuitCommittedBurst_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 2, 1, 5),
    _FrpCircuitCommittedBurst_Type()
)
frpCircuitCommittedBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frpCircuitCommittedBurst.setStatus("mandatory")


class _FrpCircuitExcessBurst_Type(Integer32):
    """Custom type frpCircuitExcessBurst based on Integer32"""
    defaultValue = 0


_FrpCircuitExcessBurst_Object = MibTableColumn
frpCircuitExcessBurst = _FrpCircuitExcessBurst_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 2, 1, 6),
    _FrpCircuitExcessBurst_Type()
)
frpCircuitExcessBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frpCircuitExcessBurst.setStatus("mandatory")


class _FrpCircuitCommittedInformationRate_Type(Integer32):
    """Custom type frpCircuitCommittedInformationRate based on Integer32"""
    defaultValue = 0


_FrpCircuitCommittedInformationRate_Object = MibTableColumn
frpCircuitCommittedInformationRate = _FrpCircuitCommittedInformationRate_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 2, 1, 7),
    _FrpCircuitCommittedInformationRate_Type()
)
frpCircuitCommittedInformationRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frpCircuitCommittedInformationRate.setStatus("mandatory")


class _FrpCircuitCIRManagement_Type(Integer32):
    """Custom type frpCircuitCIRManagement based on Integer32"""
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
        *(("disabled", 1),
          ("enabled-inbound", 2),
          ("enabled-outbound", 4),
          ("monitor-inbound", 3))
    )


_FrpCircuitCIRManagement_Type.__name__ = "Integer32"
_FrpCircuitCIRManagement_Object = MibTableColumn
frpCircuitCIRManagement = _FrpCircuitCIRManagement_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 2, 1, 8),
    _FrpCircuitCIRManagement_Type()
)
frpCircuitCIRManagement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frpCircuitCIRManagement.setStatus("mandatory")


class _FrpCircuitMultiProtEncaps_Type(Integer32):
    """Custom type frpCircuitMultiProtEncaps based on Integer32"""
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
          ("enabled", 2))
    )


_FrpCircuitMultiProtEncaps_Type.__name__ = "Integer32"
_FrpCircuitMultiProtEncaps_Object = MibTableColumn
frpCircuitMultiProtEncaps = _FrpCircuitMultiProtEncaps_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 2, 1, 9),
    _FrpCircuitMultiProtEncaps_Type()
)
frpCircuitMultiProtEncaps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frpCircuitMultiProtEncaps.setStatus("mandatory")


class _FrpCircuitHighPriorityBurst_Type(Integer32):
    """Custom type frpCircuitHighPriorityBurst based on Integer32"""
    defaultValue = 0


_FrpCircuitHighPriorityBurst_Object = MibTableColumn
frpCircuitHighPriorityBurst = _FrpCircuitHighPriorityBurst_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 2, 1, 10),
    _FrpCircuitHighPriorityBurst_Type()
)
frpCircuitHighPriorityBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frpCircuitHighPriorityBurst.setStatus("mandatory")


class _FrpCircuitLowPriorityBurst_Type(Integer32):
    """Custom type frpCircuitLowPriorityBurst based on Integer32"""
    defaultValue = 0


_FrpCircuitLowPriorityBurst_Object = MibTableColumn
frpCircuitLowPriorityBurst = _FrpCircuitLowPriorityBurst_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 2, 1, 11),
    _FrpCircuitLowPriorityBurst_Type()
)
frpCircuitLowPriorityBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frpCircuitLowPriorityBurst.setStatus("mandatory")


class _FrpCircuitFragmentationSize_Type(Integer32):
    """Custom type frpCircuitFragmentationSize based on Integer32"""
    defaultValue = 0


_FrpCircuitFragmentationSize_Object = MibTableColumn
frpCircuitFragmentationSize = _FrpCircuitFragmentationSize_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 2, 1, 18),
    _FrpCircuitFragmentationSize_Type()
)
frpCircuitFragmentationSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frpCircuitFragmentationSize.setStatus("mandatory")
_FrpCircuitAlias_Type = Alias
_FrpCircuitAlias_Object = MibTableColumn
frpCircuitAlias = _FrpCircuitAlias_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 2, 1, 19),
    _FrpCircuitAlias_Type()
)
frpCircuitAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frpCircuitAlias.setStatus("mandatory")


class _FrpCircuitCompanionSapNumber_Type(Integer32):
    """Custom type frpCircuitCompanionSapNumber based on Integer32"""
    defaultValue = 0


_FrpCircuitCompanionSapNumber_Object = MibTableColumn
frpCircuitCompanionSapNumber = _FrpCircuitCompanionSapNumber_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 2, 1, 20),
    _FrpCircuitCompanionSapNumber_Type()
)
frpCircuitCompanionSapNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frpCircuitCompanionSapNumber.setStatus("mandatory")


class _FrpCircuitCompanionDlci_Type(Integer32):
    """Custom type frpCircuitCompanionDlci based on Integer32"""
    defaultValue = 0


_FrpCircuitCompanionDlci_Object = MibTableColumn
frpCircuitCompanionDlci = _FrpCircuitCompanionDlci_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 2, 1, 21),
    _FrpCircuitCompanionDlci_Type()
)
frpCircuitCompanionDlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frpCircuitCompanionDlci.setStatus("mandatory")


class _FrpCircuitAlternateSapNumber_Type(Integer32):
    """Custom type frpCircuitAlternateSapNumber based on Integer32"""
    defaultValue = 0


_FrpCircuitAlternateSapNumber_Object = MibTableColumn
frpCircuitAlternateSapNumber = _FrpCircuitAlternateSapNumber_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 2, 1, 22),
    _FrpCircuitAlternateSapNumber_Type()
)
frpCircuitAlternateSapNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frpCircuitAlternateSapNumber.setStatus("mandatory")


class _FrpCircuitAlternateDlci_Type(Integer32):
    """Custom type frpCircuitAlternateDlci based on Integer32"""
    defaultValue = 0


_FrpCircuitAlternateDlci_Object = MibTableColumn
frpCircuitAlternateDlci = _FrpCircuitAlternateDlci_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 2, 1, 23),
    _FrpCircuitAlternateDlci_Type()
)
frpCircuitAlternateDlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frpCircuitAlternateDlci.setStatus("mandatory")


class _FrpCircuitMulticastGroupId_Type(Integer32):
    """Custom type frpCircuitMulticastGroupId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FrpCircuitMulticastGroupId_Type.__name__ = "Integer32"
_FrpCircuitMulticastGroupId_Object = MibTableColumn
frpCircuitMulticastGroupId = _FrpCircuitMulticastGroupId_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 2, 1, 24),
    _FrpCircuitMulticastGroupId_Type()
)
frpCircuitMulticastGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpCircuitMulticastGroupId.setStatus("mandatory")


class _FrpCircuitMulticastType_Type(Integer32):
    """Custom type frpCircuitMulticastType based on Integer32"""
    defaultValue = 1

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
        *(("leafOneWay", 3),
          ("leafTwoWay", 5),
          ("leafTwoWaySinglePass", 8),
          ("noMulticastAssociation", 1),
          ("rootNWay", 6),
          ("rootOneWay", 2),
          ("rootTwoWay", 4),
          ("rootTwoWaySinglePass", 7))
    )


_FrpCircuitMulticastType_Type.__name__ = "Integer32"
_FrpCircuitMulticastType_Object = MibTableColumn
frpCircuitMulticastType = _FrpCircuitMulticastType_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 2, 1, 25),
    _FrpCircuitMulticastType_Type()
)
frpCircuitMulticastType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpCircuitMulticastType.setStatus("mandatory")


class _FrpCircuitCompressionPort_Type(Integer32):
    """Custom type frpCircuitCompressionPort based on Integer32"""
    defaultValue = 0


_FrpCircuitCompressionPort_Object = MibTableColumn
frpCircuitCompressionPort = _FrpCircuitCompressionPort_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 2, 1, 26),
    _FrpCircuitCompressionPort_Type()
)
frpCircuitCompressionPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frpCircuitCompressionPort.setStatus("mandatory")


class _FrpCircuitExpressService_Type(Integer32):
    """Custom type frpCircuitExpressService based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_FrpCircuitExpressService_Type.__name__ = "Integer32"
_FrpCircuitExpressService_Object = MibTableColumn
frpCircuitExpressService = _FrpCircuitExpressService_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 2, 1, 27),
    _FrpCircuitExpressService_Type()
)
frpCircuitExpressService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frpCircuitExpressService.setStatus("mandatory")


class _FrpCircuittrapTrap1_Type(Integer32):
    """Custom type frpCircuittrapTrap1 based on Integer32"""
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
          ("enabled", 2))
    )


_FrpCircuittrapTrap1_Type.__name__ = "Integer32"
_FrpCircuittrapTrap1_Object = MibTableColumn
frpCircuittrapTrap1 = _FrpCircuittrapTrap1_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 2, 1, 32),
    _FrpCircuittrapTrap1_Type()
)
frpCircuittrapTrap1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frpCircuittrapTrap1.setStatus("mandatory")


class _FrpCircuittrapTrap2_Type(Integer32):
    """Custom type frpCircuittrapTrap2 based on Integer32"""
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
          ("enabled", 2))
    )


_FrpCircuittrapTrap2_Type.__name__ = "Integer32"
_FrpCircuittrapTrap2_Object = MibTableColumn
frpCircuittrapTrap2 = _FrpCircuittrapTrap2_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 2, 1, 33),
    _FrpCircuittrapTrap2_Type()
)
frpCircuittrapTrap2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frpCircuittrapTrap2.setStatus("mandatory")


class _FrpCircuitControlStats_Type(Integer32):
    """Custom type frpCircuitControlStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clearCircuitStats", 1)
    )


_FrpCircuitControlStats_Type.__name__ = "Integer32"
_FrpCircuitControlStats_Object = MibTableColumn
frpCircuitControlStats = _FrpCircuitControlStats_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 2, 1, 39),
    _FrpCircuitControlStats_Type()
)
frpCircuitControlStats.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    frpCircuitControlStats.setStatus("mandatory")


class _FrpCircuitstatReportedState_Type(Integer32):
    """Custom type frpCircuitstatReportedState based on Integer32"""
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
        *(("notReported", 1),
          ("reportedActive", 2),
          ("reportedInactive", 3))
    )


_FrpCircuitstatReportedState_Type.__name__ = "Integer32"
_FrpCircuitstatReportedState_Object = MibTableColumn
frpCircuitstatReportedState = _FrpCircuitstatReportedState_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 2, 1, 40),
    _FrpCircuitstatReportedState_Type()
)
frpCircuitstatReportedState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpCircuitstatReportedState.setStatus("mandatory")


class _FrpCircuitstatRouteState_Type(Integer32):
    """Custom type frpCircuitstatRouteState based on Integer32"""
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
        *(("noRoute", 1),
          ("routeNotOperational", 2),
          ("routeOperational", 3))
    )


_FrpCircuitstatRouteState_Type.__name__ = "Integer32"
_FrpCircuitstatRouteState_Object = MibTableColumn
frpCircuitstatRouteState = _FrpCircuitstatRouteState_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 2, 1, 41),
    _FrpCircuitstatRouteState_Type()
)
frpCircuitstatRouteState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpCircuitstatRouteState.setStatus("mandatory")


class _FrpCircuitstatAlternateRouteState_Type(Integer32):
    """Custom type frpCircuitstatAlternateRouteState based on Integer32"""
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
        *(("alternateCircuit", 4),
          ("noRoute", 1),
          ("routeNotOperational", 2),
          ("routeOperational", 3))
    )


_FrpCircuitstatAlternateRouteState_Type.__name__ = "Integer32"
_FrpCircuitstatAlternateRouteState_Object = MibTableColumn
frpCircuitstatAlternateRouteState = _FrpCircuitstatAlternateRouteState_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 2, 1, 42),
    _FrpCircuitstatAlternateRouteState_Type()
)
frpCircuitstatAlternateRouteState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpCircuitstatAlternateRouteState.setStatus("mandatory")
_FrpCircuitstatLocalCreationTime_Type = TimeTicks
_FrpCircuitstatLocalCreationTime_Object = MibTableColumn
frpCircuitstatLocalCreationTime = _FrpCircuitstatLocalCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 2, 1, 47),
    _FrpCircuitstatLocalCreationTime_Type()
)
frpCircuitstatLocalCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpCircuitstatLocalCreationTime.setStatus("mandatory")
_FrpCircuitstatRemoteCreationTime_Type = TimeTicks
_FrpCircuitstatRemoteCreationTime_Object = MibTableColumn
frpCircuitstatRemoteCreationTime = _FrpCircuitstatRemoteCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 2, 1, 48),
    _FrpCircuitstatRemoteCreationTime_Type()
)
frpCircuitstatRemoteCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpCircuitstatRemoteCreationTime.setStatus("mandatory")
_FrpCircuitstatTxFrames_Type = Counter32
_FrpCircuitstatTxFrames_Object = MibTableColumn
frpCircuitstatTxFrames = _FrpCircuitstatTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 2, 1, 49),
    _FrpCircuitstatTxFrames_Type()
)
frpCircuitstatTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpCircuitstatTxFrames.setStatus("mandatory")
_FrpCircuitstatRxFrames_Type = Counter32
_FrpCircuitstatRxFrames_Object = MibTableColumn
frpCircuitstatRxFrames = _FrpCircuitstatRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 2, 1, 50),
    _FrpCircuitstatRxFrames_Type()
)
frpCircuitstatRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpCircuitstatRxFrames.setStatus("mandatory")
_FrpCircuitstatTxOctets_Type = Counter32
_FrpCircuitstatTxOctets_Object = MibTableColumn
frpCircuitstatTxOctets = _FrpCircuitstatTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 2, 1, 51),
    _FrpCircuitstatTxOctets_Type()
)
frpCircuitstatTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpCircuitstatTxOctets.setStatus("mandatory")
_FrpCircuitstatRxOctets_Type = Counter32
_FrpCircuitstatRxOctets_Object = MibTableColumn
frpCircuitstatRxOctets = _FrpCircuitstatRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 2, 1, 52),
    _FrpCircuitstatRxOctets_Type()
)
frpCircuitstatRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpCircuitstatRxOctets.setStatus("mandatory")
_FrpCircuitstatTxFECNs_Type = Counter32
_FrpCircuitstatTxFECNs_Object = MibTableColumn
frpCircuitstatTxFECNs = _FrpCircuitstatTxFECNs_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 2, 1, 53),
    _FrpCircuitstatTxFECNs_Type()
)
frpCircuitstatTxFECNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpCircuitstatTxFECNs.setStatus("mandatory")
_FrpCircuitstatRxFECNs_Type = Counter32
_FrpCircuitstatRxFECNs_Object = MibTableColumn
frpCircuitstatRxFECNs = _FrpCircuitstatRxFECNs_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 2, 1, 54),
    _FrpCircuitstatRxFECNs_Type()
)
frpCircuitstatRxFECNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpCircuitstatRxFECNs.setStatus("mandatory")
_FrpCircuitstatTxBECNs_Type = Counter32
_FrpCircuitstatTxBECNs_Object = MibTableColumn
frpCircuitstatTxBECNs = _FrpCircuitstatTxBECNs_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 2, 1, 55),
    _FrpCircuitstatTxBECNs_Type()
)
frpCircuitstatTxBECNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpCircuitstatTxBECNs.setStatus("mandatory")
_FrpCircuitstatRxBECNs_Type = Counter32
_FrpCircuitstatRxBECNs_Object = MibTableColumn
frpCircuitstatRxBECNs = _FrpCircuitstatRxBECNs_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 2, 1, 56),
    _FrpCircuitstatRxBECNs_Type()
)
frpCircuitstatRxBECNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpCircuitstatRxBECNs.setStatus("mandatory")
_FrpCircuitstatTxQueuedDiscards_Type = Counter32
_FrpCircuitstatTxQueuedDiscards_Object = MibTableColumn
frpCircuitstatTxQueuedDiscards = _FrpCircuitstatTxQueuedDiscards_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 2, 1, 63),
    _FrpCircuitstatTxQueuedDiscards_Type()
)
frpCircuitstatTxQueuedDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpCircuitstatTxQueuedDiscards.setStatus("mandatory")
_FrpCircuitstatRxCIRExceededDiscards_Type = Counter32
_FrpCircuitstatRxCIRExceededDiscards_Object = MibTableColumn
frpCircuitstatRxCIRExceededDiscards = _FrpCircuitstatRxCIRExceededDiscards_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 2, 1, 70),
    _FrpCircuitstatRxCIRExceededDiscards_Type()
)
frpCircuitstatRxCIRExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpCircuitstatRxCIRExceededDiscards.setStatus("mandatory")
_FrpCircuitstatRxSysCongestionDiscards_Type = Counter32
_FrpCircuitstatRxSysCongestionDiscards_Object = MibTableColumn
frpCircuitstatRxSysCongestionDiscards = _FrpCircuitstatRxSysCongestionDiscards_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 2, 1, 71),
    _FrpCircuitstatRxSysCongestionDiscards_Type()
)
frpCircuitstatRxSysCongestionDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpCircuitstatRxSysCongestionDiscards.setStatus("mandatory")
_FrpCircuitstatRxUnavailInboundDiscards_Type = Counter32
_FrpCircuitstatRxUnavailInboundDiscards_Object = MibTableColumn
frpCircuitstatRxUnavailInboundDiscards = _FrpCircuitstatRxUnavailInboundDiscards_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 2, 1, 72),
    _FrpCircuitstatRxUnavailInboundDiscards_Type()
)
frpCircuitstatRxUnavailInboundDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpCircuitstatRxUnavailInboundDiscards.setStatus("mandatory")
_FrpCircuitstatRxUnavailOutboundDiscards_Type = Counter32
_FrpCircuitstatRxUnavailOutboundDiscards_Object = MibTableColumn
frpCircuitstatRxUnavailOutboundDiscards = _FrpCircuitstatRxUnavailOutboundDiscards_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 2, 1, 73),
    _FrpCircuitstatRxUnavailOutboundDiscards_Type()
)
frpCircuitstatRxUnavailOutboundDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpCircuitstatRxUnavailOutboundDiscards.setStatus("mandatory")
_FrpCircuitstatRxCIRExceeds_Type = Counter32
_FrpCircuitstatRxCIRExceeds_Object = MibTableColumn
frpCircuitstatRxCIRExceeds = _FrpCircuitstatRxCIRExceeds_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 2, 1, 74),
    _FrpCircuitstatRxCIRExceeds_Type()
)
frpCircuitstatRxCIRExceeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpCircuitstatRxCIRExceeds.setStatus("mandatory")
_FrpCircuitstatFragmentationFailures_Type = Counter32
_FrpCircuitstatFragmentationFailures_Object = MibTableColumn
frpCircuitstatFragmentationFailures = _FrpCircuitstatFragmentationFailures_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 2, 1, 75),
    _FrpCircuitstatFragmentationFailures_Type()
)
frpCircuitstatFragmentationFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpCircuitstatFragmentationFailures.setStatus("mandatory")
_FrpCircuitstatDeFragmentationFailures_Type = Counter32
_FrpCircuitstatDeFragmentationFailures_Object = MibTableColumn
frpCircuitstatDeFragmentationFailures = _FrpCircuitstatDeFragmentationFailures_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 2, 1, 76),
    _FrpCircuitstatDeFragmentationFailures_Type()
)
frpCircuitstatDeFragmentationFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpCircuitstatDeFragmentationFailures.setStatus("mandatory")
_FrpReportedPvcTable_Object = MibTable
frpReportedPvcTable = _FrpReportedPvcTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 3)
)
if mibBuilder.loadTexts:
    frpReportedPvcTable.setStatus("mandatory")
_FrpReportedPvcEntry_Object = MibTableRow
frpReportedPvcEntry = _FrpReportedPvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 3, 1)
)
frpReportedPvcEntry.setIndexNames(
    (0, "CXFrameRelay-MIB", "frpReportedPvcSapNumber"),
)
if mibBuilder.loadTexts:
    frpReportedPvcEntry.setStatus("mandatory")
_FrpReportedPvcSapNumber_Type = SapIndex
_FrpReportedPvcSapNumber_Object = MibTableColumn
frpReportedPvcSapNumber = _FrpReportedPvcSapNumber_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 3, 1, 1),
    _FrpReportedPvcSapNumber_Type()
)
frpReportedPvcSapNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpReportedPvcSapNumber.setStatus("mandatory")
_FrpReportedPvcDlci_Type = DLCI
_FrpReportedPvcDlci_Object = MibTableColumn
frpReportedPvcDlci = _FrpReportedPvcDlci_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 3, 1, 2),
    _FrpReportedPvcDlci_Type()
)
frpReportedPvcDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpReportedPvcDlci.setStatus("mandatory")


class _FrpReportedPvcLocallyConfigured_Type(Integer32):
    """Custom type frpReportedPvcLocallyConfigured based on Integer32"""
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


_FrpReportedPvcLocallyConfigured_Type.__name__ = "Integer32"
_FrpReportedPvcLocallyConfigured_Object = MibTableColumn
frpReportedPvcLocallyConfigured = _FrpReportedPvcLocallyConfigured_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 3, 1, 3),
    _FrpReportedPvcLocallyConfigured_Type()
)
frpReportedPvcLocallyConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpReportedPvcLocallyConfigured.setStatus("mandatory")


class _FrpReportedPvcStatus_Type(Integer32):
    """Custom type frpReportedPvcStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1))
    )


_FrpReportedPvcStatus_Type.__name__ = "Integer32"
_FrpReportedPvcStatus_Object = MibTableColumn
frpReportedPvcStatus = _FrpReportedPvcStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 3, 1, 4),
    _FrpReportedPvcStatus_Type()
)
frpReportedPvcStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpReportedPvcStatus.setStatus("mandatory")
_FrpMulticastTable_Object = MibTable
frpMulticastTable = _FrpMulticastTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 4)
)
if mibBuilder.loadTexts:
    frpMulticastTable.setStatus("mandatory")
_FrpMulticastEntry_Object = MibTableRow
frpMulticastEntry = _FrpMulticastEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 4, 1)
)
frpMulticastEntry.setIndexNames(
    (0, "CXFrameRelay-MIB", "frpMulticastGroupId"),
    (0, "CXFrameRelay-MIB", "frpMulticastSapNumber"),
    (0, "CXFrameRelay-MIB", "frpMulticastDlci"),
)
if mibBuilder.loadTexts:
    frpMulticastEntry.setStatus("mandatory")


class _FrpMulticastGroupId_Type(Integer32):
    """Custom type frpMulticastGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FrpMulticastGroupId_Type.__name__ = "Integer32"
_FrpMulticastGroupId_Object = MibTableColumn
frpMulticastGroupId = _FrpMulticastGroupId_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 4, 1, 1),
    _FrpMulticastGroupId_Type()
)
frpMulticastGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpMulticastGroupId.setStatus("mandatory")
_FrpMulticastSapNumber_Type = SapIndex
_FrpMulticastSapNumber_Object = MibTableColumn
frpMulticastSapNumber = _FrpMulticastSapNumber_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 4, 1, 2),
    _FrpMulticastSapNumber_Type()
)
frpMulticastSapNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpMulticastSapNumber.setStatus("mandatory")
_FrpMulticastDlci_Type = DLCI
_FrpMulticastDlci_Object = MibTableColumn
frpMulticastDlci = _FrpMulticastDlci_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 4, 1, 3),
    _FrpMulticastDlci_Type()
)
frpMulticastDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpMulticastDlci.setStatus("mandatory")


class _FrpMulticastRowStatus_Type(Integer32):
    """Custom type frpMulticastRowStatus based on Integer32"""
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


_FrpMulticastRowStatus_Type.__name__ = "Integer32"
_FrpMulticastRowStatus_Object = MibTableColumn
frpMulticastRowStatus = _FrpMulticastRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 4, 1, 4),
    _FrpMulticastRowStatus_Type()
)
frpMulticastRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frpMulticastRowStatus.setStatus("mandatory")


class _FrpMulticastMemberType_Type(Integer32):
    """Custom type frpMulticastMemberType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("leaf", 2),
          ("root", 1))
    )


_FrpMulticastMemberType_Type.__name__ = "Integer32"
_FrpMulticastMemberType_Object = MibTableColumn
frpMulticastMemberType = _FrpMulticastMemberType_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 4, 1, 5),
    _FrpMulticastMemberType_Type()
)
frpMulticastMemberType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frpMulticastMemberType.setStatus("mandatory")


class _FrpMulticastServiceType_Type(Integer32):
    """Custom type frpMulticastServiceType based on Integer32"""
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
        *(("nWay", 3),
          ("oneWay", 1),
          ("twoWay", 2),
          ("twoWaySinglePass", 4))
    )


_FrpMulticastServiceType_Type.__name__ = "Integer32"
_FrpMulticastServiceType_Object = MibTableColumn
frpMulticastServiceType = _FrpMulticastServiceType_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 4, 1, 6),
    _FrpMulticastServiceType_Type()
)
frpMulticastServiceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frpMulticastServiceType.setStatus("mandatory")


class _FrpMulticastMemberStatus_Type(Integer32):
    """Custom type frpMulticastMemberStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1))
    )


_FrpMulticastMemberStatus_Type.__name__ = "Integer32"
_FrpMulticastMemberStatus_Object = MibTableColumn
frpMulticastMemberStatus = _FrpMulticastMemberStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 4, 1, 7),
    _FrpMulticastMemberStatus_Type()
)
frpMulticastMemberStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpMulticastMemberStatus.setStatus("mandatory")


class _FrpMibLevel_Type(Integer32):
    """Custom type frpMibLevel based on Integer32"""
    defaultValue = 0


_FrpMibLevel_Object = MibScalar
frpMibLevel = _FrpMibLevel_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 5),
    _FrpMibLevel_Type()
)
frpMibLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpMibLevel.setStatus("mandatory")

# Managed Objects groups


# Notification objects

frpSapInterfaceStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 0, 1)
)
frpSapInterfaceStatusChange.setObjects(
      *(("CXModuleHardware-MIB", "cxModuleHwPhysSlot"),
        ("CXFrameRelay-MIB", "frpSapNumber"),
        ("CXFrameRelay-MIB", "frpSapstatLinkManagementState"))
)
if mibBuilder.loadTexts:
    frpSapInterfaceStatusChange.setStatus(
        ""
    )

frpPvcReportedStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 0, 2)
)
frpPvcReportedStatusChange.setObjects(
      *(("CXModuleHardware-MIB", "cxModuleHwPhysSlot"),
        ("CXFrameRelay-MIB", "frpCircuitSapNumber"),
        ("CXFrameRelay-MIB", "frpCircuitDlci"),
        ("CXFrameRelay-MIB", "frpCircuitstatReportedState"))
)
if mibBuilder.loadTexts:
    frpPvcReportedStatusChange.setStatus(
        ""
    )

frpPvcBillingStats = NotificationType(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 0, 3)
)
frpPvcBillingStats.setObjects(
      *(("CXModuleHardware-MIB", "cxModuleHwPhysSlot"),
        ("CXFrameRelay-MIB", "frpCircuitSapNumber"),
        ("CXFrameRelay-MIB", "frpCircuitDlci"),
        ("CXFrameRelay-MIB", "frpCircuitstatTxFrames"),
        ("CXFrameRelay-MIB", "frpCircuitstatRxFrames"),
        ("CXFrameRelay-MIB", "frpCircuitstatTxOctets"),
        ("CXFrameRelay-MIB", "frpCircuitstatRxOctets"))
)
if mibBuilder.loadTexts:
    frpPvcBillingStats.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CXFrameRelay-MIB",
    **{"DLCI": DLCI,
       "frpSapInterfaceStatusChange": frpSapInterfaceStatusChange,
       "frpPvcReportedStatusChange": frpPvcReportedStatusChange,
       "frpPvcBillingStats": frpPvcBillingStats,
       "frpSapTable": frpSapTable,
       "frpSapEntry": frpSapEntry,
       "frpSapNumber": frpSapNumber,
       "frpSapRowStatus": frpSapRowStatus,
       "frpSapAlias": frpSapAlias,
       "frpSapCompanionAlias": frpSapCompanionAlias,
       "frpSapType": frpSapType,
       "frpSapAddressLength": frpSapAddressLength,
       "frpSapMaxSupportedVCs": frpSapMaxSupportedVCs,
       "frpSapVCBase": frpSapVCBase,
       "frpSapOutCongestionManagement": frpSapOutCongestionManagement,
       "frpSapResourceAllocation": frpSapResourceAllocation,
       "frpSapLinkManagement": frpSapLinkManagement,
       "frpSapInterfaceType": frpSapInterfaceType,
       "frpSapPollingInterval": frpSapPollingInterval,
       "frpSapPollingVerification": frpSapPollingVerification,
       "frpSapFullEnquiryInterval": frpSapFullEnquiryInterval,
       "frpSapErrorThreshold": frpSapErrorThreshold,
       "frpSapMonitoredEvents": frpSapMonitoredEvents,
       "frpSapMode": frpSapMode,
       "frpSapPrioQueue1HitRatio": frpSapPrioQueue1HitRatio,
       "frpSapPrioQueue2HitRatio": frpSapPrioQueue2HitRatio,
       "frpSapPrioQueue3HitRatio": frpSapPrioQueue3HitRatio,
       "frpSapPrioQueue4HitRatio": frpSapPrioQueue4HitRatio,
       "frpSapDialEntry": frpSapDialEntry,
       "frpSapFilterBitMap": frpSapFilterBitMap,
       "frpSapLmiFlavor": frpSapLmiFlavor,
       "frpSapGenerator": frpSapGenerator,
       "frpSapGeneratorDlciNumber": frpSapGeneratorDlciNumber,
       "frpSapGeneratorFrameSize": frpSapGeneratorFrameSize,
       "frpSapGeneratorNumberOfFrames": frpSapGeneratorNumberOfFrames,
       "frpSapGeneratorInterFrameDelay": frpSapGeneratorInterFrameDelay,
       "frpSapBillingTimer": frpSapBillingTimer,
       "frpSapSdLmMessageInterval": frpSapSdLmMessageInterval,
       "frpSapSdLmActiveTimer": frpSapSdLmActiveTimer,
       "frpSaptrapTrap1": frpSaptrapTrap1,
       "frpSapControl": frpSapControl,
       "frpSapControlStats": frpSapControlStats,
       "frpSapstatLinkManagementState": frpSapstatLinkManagementState,
       "frpSapstatCurrentLinkManagementType": frpSapstatCurrentLinkManagementType,
       "frpSapstatTxDataFrames": frpSapstatTxDataFrames,
       "frpSapstatRxDataFrames": frpSapstatRxDataFrames,
       "frpSapstatTxDataOctets": frpSapstatTxDataOctets,
       "frpSapstatRxDataOctets": frpSapstatRxDataOctets,
       "frpSapstatTxLmiFrames": frpSapstatTxLmiFrames,
       "frpSapstatRxLmiFrames": frpSapstatRxLmiFrames,
       "frpSapstatTxQueuedDiscards": frpSapstatTxQueuedDiscards,
       "frpSapstatRxCIRExceededDiscards": frpSapstatRxCIRExceededDiscards,
       "frpSapstatRxSysCongestionDiscards": frpSapstatRxSysCongestionDiscards,
       "frpSapstatRxUnavailInboundDiscards": frpSapstatRxUnavailInboundDiscards,
       "frpSapstatRxUnavailOutboundDiscards": frpSapstatRxUnavailOutboundDiscards,
       "frpSapstatRxInvalidVCDiscards": frpSapstatRxInvalidVCDiscards,
       "frpSapstatRxBadStatusDiscards": frpSapstatRxBadStatusDiscards,
       "frpSapstatRxMiscellaneousDiscards": frpSapstatRxMiscellaneousDiscards,
       "frpSapstatRxCIRExceeds": frpSapstatRxCIRExceeds,
       "frpSapstatRxShortFrameDiscards": frpSapstatRxShortFrameDiscards,
       "frpSapstatLmiInvalidFieldDiscards": frpSapstatLmiInvalidFieldDiscards,
       "frpSapstatLmiInvalidSequenceDiscards": frpSapstatLmiInvalidSequenceDiscards,
       "frpSapstatLmiTimeouts": frpSapstatLmiTimeouts,
       "frpSapstatLmiInvalidStatusDiscards": frpSapstatLmiInvalidStatusDiscards,
       "frpSapstatLmiInvalidStatusEnqDiscards": frpSapstatLmiInvalidStatusEnqDiscards,
       "frpSapstatLmiInvalidUpdStatusDiscards": frpSapstatLmiInvalidUpdStatusDiscards,
       "frpCircuitTable": frpCircuitTable,
       "frpCircuitEntry": frpCircuitEntry,
       "frpCircuitSapNumber": frpCircuitSapNumber,
       "frpCircuitDlci": frpCircuitDlci,
       "frpCircuitRowStatus": frpCircuitRowStatus,
       "frpCircuitPriorityLevel": frpCircuitPriorityLevel,
       "frpCircuitCommittedBurst": frpCircuitCommittedBurst,
       "frpCircuitExcessBurst": frpCircuitExcessBurst,
       "frpCircuitCommittedInformationRate": frpCircuitCommittedInformationRate,
       "frpCircuitCIRManagement": frpCircuitCIRManagement,
       "frpCircuitMultiProtEncaps": frpCircuitMultiProtEncaps,
       "frpCircuitHighPriorityBurst": frpCircuitHighPriorityBurst,
       "frpCircuitLowPriorityBurst": frpCircuitLowPriorityBurst,
       "frpCircuitFragmentationSize": frpCircuitFragmentationSize,
       "frpCircuitAlias": frpCircuitAlias,
       "frpCircuitCompanionSapNumber": frpCircuitCompanionSapNumber,
       "frpCircuitCompanionDlci": frpCircuitCompanionDlci,
       "frpCircuitAlternateSapNumber": frpCircuitAlternateSapNumber,
       "frpCircuitAlternateDlci": frpCircuitAlternateDlci,
       "frpCircuitMulticastGroupId": frpCircuitMulticastGroupId,
       "frpCircuitMulticastType": frpCircuitMulticastType,
       "frpCircuitCompressionPort": frpCircuitCompressionPort,
       "frpCircuitExpressService": frpCircuitExpressService,
       "frpCircuittrapTrap1": frpCircuittrapTrap1,
       "frpCircuittrapTrap2": frpCircuittrapTrap2,
       "frpCircuitControlStats": frpCircuitControlStats,
       "frpCircuitstatReportedState": frpCircuitstatReportedState,
       "frpCircuitstatRouteState": frpCircuitstatRouteState,
       "frpCircuitstatAlternateRouteState": frpCircuitstatAlternateRouteState,
       "frpCircuitstatLocalCreationTime": frpCircuitstatLocalCreationTime,
       "frpCircuitstatRemoteCreationTime": frpCircuitstatRemoteCreationTime,
       "frpCircuitstatTxFrames": frpCircuitstatTxFrames,
       "frpCircuitstatRxFrames": frpCircuitstatRxFrames,
       "frpCircuitstatTxOctets": frpCircuitstatTxOctets,
       "frpCircuitstatRxOctets": frpCircuitstatRxOctets,
       "frpCircuitstatTxFECNs": frpCircuitstatTxFECNs,
       "frpCircuitstatRxFECNs": frpCircuitstatRxFECNs,
       "frpCircuitstatTxBECNs": frpCircuitstatTxBECNs,
       "frpCircuitstatRxBECNs": frpCircuitstatRxBECNs,
       "frpCircuitstatTxQueuedDiscards": frpCircuitstatTxQueuedDiscards,
       "frpCircuitstatRxCIRExceededDiscards": frpCircuitstatRxCIRExceededDiscards,
       "frpCircuitstatRxSysCongestionDiscards": frpCircuitstatRxSysCongestionDiscards,
       "frpCircuitstatRxUnavailInboundDiscards": frpCircuitstatRxUnavailInboundDiscards,
       "frpCircuitstatRxUnavailOutboundDiscards": frpCircuitstatRxUnavailOutboundDiscards,
       "frpCircuitstatRxCIRExceeds": frpCircuitstatRxCIRExceeds,
       "frpCircuitstatFragmentationFailures": frpCircuitstatFragmentationFailures,
       "frpCircuitstatDeFragmentationFailures": frpCircuitstatDeFragmentationFailures,
       "frpReportedPvcTable": frpReportedPvcTable,
       "frpReportedPvcEntry": frpReportedPvcEntry,
       "frpReportedPvcSapNumber": frpReportedPvcSapNumber,
       "frpReportedPvcDlci": frpReportedPvcDlci,
       "frpReportedPvcLocallyConfigured": frpReportedPvcLocallyConfigured,
       "frpReportedPvcStatus": frpReportedPvcStatus,
       "frpMulticastTable": frpMulticastTable,
       "frpMulticastEntry": frpMulticastEntry,
       "frpMulticastGroupId": frpMulticastGroupId,
       "frpMulticastSapNumber": frpMulticastSapNumber,
       "frpMulticastDlci": frpMulticastDlci,
       "frpMulticastRowStatus": frpMulticastRowStatus,
       "frpMulticastMemberType": frpMulticastMemberType,
       "frpMulticastServiceType": frpMulticastServiceType,
       "frpMulticastMemberStatus": frpMulticastMemberStatus,
       "frpMibLevel": frpMibLevel}
)
