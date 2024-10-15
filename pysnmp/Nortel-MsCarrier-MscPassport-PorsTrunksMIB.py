# SNMP MIB module (Nortel-MsCarrier-MscPassport-PorsTrunksMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-MsCarrier-MscPassport-PorsTrunksMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:32:55 2024
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

(DisplayString,
 Integer32,
 RowPointer,
 RowStatus,
 StorageType,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB",
    "DisplayString",
    "Integer32",
    "RowPointer",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(AsciiString,
 NonReplicated) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-TextualConventionsMIB",
    "AsciiString",
    "NonReplicated")

(mscTrk,
 mscTrkIndex) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-TrunksMIB",
    "mscTrk",
    "mscTrkIndex")

(mscPassportMIBs,) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-UsefulDefinitionsMIB",
    "mscPassportMIBs")

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

_MscTrkPa_ObjectIdentity = ObjectIdentity
mscTrkPa = _MscTrkPa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4)
)
_MscTrkPaRowStatusTable_Object = MibTable
mscTrkPaRowStatusTable = _MscTrkPaRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 1)
)
if mibBuilder.loadTexts:
    mscTrkPaRowStatusTable.setStatus("mandatory")
_MscTrkPaRowStatusEntry_Object = MibTableRow
mscTrkPaRowStatusEntry = _MscTrkPaRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 1, 1)
)
mscTrkPaRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkIndex"),
    (0, "Nortel-MsCarrier-MscPassport-PorsTrunksMIB", "mscTrkPaIndex"),
)
if mibBuilder.loadTexts:
    mscTrkPaRowStatusEntry.setStatus("mandatory")
_MscTrkPaRowStatus_Type = RowStatus
_MscTrkPaRowStatus_Object = MibTableColumn
mscTrkPaRowStatus = _MscTrkPaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 1, 1, 1),
    _MscTrkPaRowStatus_Type()
)
mscTrkPaRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTrkPaRowStatus.setStatus("mandatory")
_MscTrkPaComponentName_Type = DisplayString
_MscTrkPaComponentName_Object = MibTableColumn
mscTrkPaComponentName = _MscTrkPaComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 1, 1, 2),
    _MscTrkPaComponentName_Type()
)
mscTrkPaComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkPaComponentName.setStatus("mandatory")
_MscTrkPaStorageType_Type = StorageType
_MscTrkPaStorageType_Object = MibTableColumn
mscTrkPaStorageType = _MscTrkPaStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 1, 1, 4),
    _MscTrkPaStorageType_Type()
)
mscTrkPaStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkPaStorageType.setStatus("mandatory")
_MscTrkPaIndex_Type = NonReplicated
_MscTrkPaIndex_Object = MibTableColumn
mscTrkPaIndex = _MscTrkPaIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 1, 1, 10),
    _MscTrkPaIndex_Type()
)
mscTrkPaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscTrkPaIndex.setStatus("mandatory")
_MscTrkPaProvTable_Object = MibTable
mscTrkPaProvTable = _MscTrkPaProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 10)
)
if mibBuilder.loadTexts:
    mscTrkPaProvTable.setStatus("mandatory")
_MscTrkPaProvEntry_Object = MibTableRow
mscTrkPaProvEntry = _MscTrkPaProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 10, 1)
)
mscTrkPaProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkIndex"),
    (0, "Nortel-MsCarrier-MscPassport-PorsTrunksMIB", "mscTrkPaIndex"),
)
if mibBuilder.loadTexts:
    mscTrkPaProvEntry.setStatus("mandatory")


class _MscTrkPaMaxLc_Type(Unsigned32):
    """Custom type mscTrkPaMaxLc based on Unsigned32"""
    defaultValue = 512

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65435),
    )


_MscTrkPaMaxLc_Type.__name__ = "Unsigned32"
_MscTrkPaMaxLc_Object = MibTableColumn
mscTrkPaMaxLc = _MscTrkPaMaxLc_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 10, 1, 1),
    _MscTrkPaMaxLc_Type()
)
mscTrkPaMaxLc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTrkPaMaxLc.setStatus("mandatory")


class _MscTrkPaMaxReservedBwOut_Type(Unsigned32):
    """Custom type mscTrkPaMaxReservedBwOut based on Unsigned32"""
    defaultValue = 50

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MscTrkPaMaxReservedBwOut_Type.__name__ = "Unsigned32"
_MscTrkPaMaxReservedBwOut_Object = MibTableColumn
mscTrkPaMaxReservedBwOut = _MscTrkPaMaxReservedBwOut_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 10, 1, 2),
    _MscTrkPaMaxReservedBwOut_Type()
)
mscTrkPaMaxReservedBwOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTrkPaMaxReservedBwOut.setStatus("mandatory")


class _MscTrkPaTrunkSecurity_Type(Unsigned32):
    """Custom type mscTrkPaTrunkSecurity based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MscTrkPaTrunkSecurity_Type.__name__ = "Unsigned32"
_MscTrkPaTrunkSecurity_Object = MibTableColumn
mscTrkPaTrunkSecurity = _MscTrkPaTrunkSecurity_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 10, 1, 3),
    _MscTrkPaTrunkSecurity_Type()
)
mscTrkPaTrunkSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTrkPaTrunkSecurity.setStatus("mandatory")


class _MscTrkPaSupportedTrafficTypes_Type(OctetString):
    """Custom type mscTrkPaSupportedTrafficTypes based on OctetString"""
    defaultHexValue = "f8"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscTrkPaSupportedTrafficTypes_Type.__name__ = "OctetString"
_MscTrkPaSupportedTrafficTypes_Object = MibTableColumn
mscTrkPaSupportedTrafficTypes = _MscTrkPaSupportedTrafficTypes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 10, 1, 4),
    _MscTrkPaSupportedTrafficTypes_Type()
)
mscTrkPaSupportedTrafficTypes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTrkPaSupportedTrafficTypes.setStatus("mandatory")


class _MscTrkPaTrunkType_Type(Integer32):
    """Custom type mscTrkPaTrunkType based on Integer32"""
    defaultValue = 0

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
        *(("satellite", 1),
          ("terrestrial", 0),
          ("trunkType1", 2),
          ("trunkType2", 3),
          ("trunkType3", 4),
          ("trunkType4", 5),
          ("trunkType5", 6),
          ("trunkType6", 7))
    )


_MscTrkPaTrunkType_Type.__name__ = "Integer32"
_MscTrkPaTrunkType_Object = MibTableColumn
mscTrkPaTrunkType = _MscTrkPaTrunkType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 10, 1, 5),
    _MscTrkPaTrunkType_Type()
)
mscTrkPaTrunkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTrkPaTrunkType.setStatus("mandatory")


class _MscTrkPaCustomerParameter_Type(Unsigned32):
    """Custom type mscTrkPaCustomerParameter based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MscTrkPaCustomerParameter_Type.__name__ = "Unsigned32"
_MscTrkPaCustomerParameter_Object = MibTableColumn
mscTrkPaCustomerParameter = _MscTrkPaCustomerParameter_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 10, 1, 6),
    _MscTrkPaCustomerParameter_Type()
)
mscTrkPaCustomerParameter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTrkPaCustomerParameter.setStatus("mandatory")


class _MscTrkPaTrunkCost_Type(Unsigned32):
    """Custom type mscTrkPaTrunkCost based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MscTrkPaTrunkCost_Type.__name__ = "Unsigned32"
_MscTrkPaTrunkCost_Object = MibTableColumn
mscTrkPaTrunkCost = _MscTrkPaTrunkCost_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 10, 1, 7),
    _MscTrkPaTrunkCost_Type()
)
mscTrkPaTrunkCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTrkPaTrunkCost.setStatus("mandatory")
_MscTrkPaOperTable_Object = MibTable
mscTrkPaOperTable = _MscTrkPaOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 11)
)
if mibBuilder.loadTexts:
    mscTrkPaOperTable.setStatus("mandatory")
_MscTrkPaOperEntry_Object = MibTableRow
mscTrkPaOperEntry = _MscTrkPaOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 11, 1)
)
mscTrkPaOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkIndex"),
    (0, "Nortel-MsCarrier-MscPassport-PorsTrunksMIB", "mscTrkPaIndex"),
)
if mibBuilder.loadTexts:
    mscTrkPaOperEntry.setStatus("mandatory")


class _MscTrkPaState_Type(AsciiString):
    """Custom type mscTrkPaState based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_MscTrkPaState_Type.__name__ = "AsciiString"
_MscTrkPaState_Object = MibTableColumn
mscTrkPaState = _MscTrkPaState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 11, 1, 1),
    _MscTrkPaState_Type()
)
mscTrkPaState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkPaState.setStatus("mandatory")


class _MscTrkPaUsedLc_Type(Unsigned32):
    """Custom type mscTrkPaUsedLc based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscTrkPaUsedLc_Type.__name__ = "Unsigned32"
_MscTrkPaUsedLc_Object = MibTableColumn
mscTrkPaUsedLc = _MscTrkPaUsedLc_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 11, 1, 2),
    _MscTrkPaUsedLc_Type()
)
mscTrkPaUsedLc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkPaUsedLc.setStatus("mandatory")


class _MscTrkPaNegotiatedMaxLc_Type(Unsigned32):
    """Custom type mscTrkPaNegotiatedMaxLc based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscTrkPaNegotiatedMaxLc_Type.__name__ = "Unsigned32"
_MscTrkPaNegotiatedMaxLc_Object = MibTableColumn
mscTrkPaNegotiatedMaxLc = _MscTrkPaNegotiatedMaxLc_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 11, 1, 3),
    _MscTrkPaNegotiatedMaxLc_Type()
)
mscTrkPaNegotiatedMaxLc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkPaNegotiatedMaxLc.setStatus("mandatory")


class _MscTrkPaMaxReservableBwOut_Type(Unsigned32):
    """Custom type mscTrkPaMaxReservableBwOut based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscTrkPaMaxReservableBwOut_Type.__name__ = "Unsigned32"
_MscTrkPaMaxReservableBwOut_Object = MibTableColumn
mscTrkPaMaxReservableBwOut = _MscTrkPaMaxReservableBwOut_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 11, 1, 4),
    _MscTrkPaMaxReservableBwOut_Type()
)
mscTrkPaMaxReservableBwOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkPaMaxReservableBwOut.setStatus("mandatory")


class _MscTrkPaOverReservedBwOut_Type(Unsigned32):
    """Custom type mscTrkPaOverReservedBwOut based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscTrkPaOverReservedBwOut_Type.__name__ = "Unsigned32"
_MscTrkPaOverReservedBwOut_Object = MibTableColumn
mscTrkPaOverReservedBwOut = _MscTrkPaOverReservedBwOut_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 11, 1, 5),
    _MscTrkPaOverReservedBwOut_Type()
)
mscTrkPaOverReservedBwOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkPaOverReservedBwOut.setStatus("mandatory")


class _MscTrkPaUnreservedBwOut_Type(Unsigned32):
    """Custom type mscTrkPaUnreservedBwOut based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscTrkPaUnreservedBwOut_Type.__name__ = "Unsigned32"
_MscTrkPaUnreservedBwOut_Object = MibTableColumn
mscTrkPaUnreservedBwOut = _MscTrkPaUnreservedBwOut_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 11, 1, 6),
    _MscTrkPaUnreservedBwOut_Type()
)
mscTrkPaUnreservedBwOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkPaUnreservedBwOut.setStatus("mandatory")


class _MscTrkPaClashCount_Type(Unsigned32):
    """Custom type mscTrkPaClashCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscTrkPaClashCount_Type.__name__ = "Unsigned32"
_MscTrkPaClashCount_Object = MibTableColumn
mscTrkPaClashCount = _MscTrkPaClashCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 11, 1, 7),
    _MscTrkPaClashCount_Type()
)
mscTrkPaClashCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkPaClashCount.setStatus("mandatory")


class _MscTrkPaNegotiatedSupportedTrafficTypes_Type(OctetString):
    """Custom type mscTrkPaNegotiatedSupportedTrafficTypes based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscTrkPaNegotiatedSupportedTrafficTypes_Type.__name__ = "OctetString"
_MscTrkPaNegotiatedSupportedTrafficTypes_Object = MibTableColumn
mscTrkPaNegotiatedSupportedTrafficTypes = _MscTrkPaNegotiatedSupportedTrafficTypes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 11, 1, 9),
    _MscTrkPaNegotiatedSupportedTrafficTypes_Type()
)
mscTrkPaNegotiatedSupportedTrafficTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkPaNegotiatedSupportedTrafficTypes.setStatus("mandatory")


class _MscTrkPaNegotiatedTrunkSecurity_Type(Unsigned32):
    """Custom type mscTrkPaNegotiatedTrunkSecurity based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MscTrkPaNegotiatedTrunkSecurity_Type.__name__ = "Unsigned32"
_MscTrkPaNegotiatedTrunkSecurity_Object = MibTableColumn
mscTrkPaNegotiatedTrunkSecurity = _MscTrkPaNegotiatedTrunkSecurity_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 11, 1, 10),
    _MscTrkPaNegotiatedTrunkSecurity_Type()
)
mscTrkPaNegotiatedTrunkSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkPaNegotiatedTrunkSecurity.setStatus("mandatory")


class _MscTrkPaNegotiatedCustomerParameter_Type(Unsigned32):
    """Custom type mscTrkPaNegotiatedCustomerParameter based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MscTrkPaNegotiatedCustomerParameter_Type.__name__ = "Unsigned32"
_MscTrkPaNegotiatedCustomerParameter_Object = MibTableColumn
mscTrkPaNegotiatedCustomerParameter = _MscTrkPaNegotiatedCustomerParameter_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 11, 1, 11),
    _MscTrkPaNegotiatedCustomerParameter_Type()
)
mscTrkPaNegotiatedCustomerParameter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkPaNegotiatedCustomerParameter.setStatus("mandatory")


class _MscTrkPaNegotiatedTrunkCost_Type(Unsigned32):
    """Custom type mscTrkPaNegotiatedTrunkCost based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MscTrkPaNegotiatedTrunkCost_Type.__name__ = "Unsigned32"
_MscTrkPaNegotiatedTrunkCost_Object = MibTableColumn
mscTrkPaNegotiatedTrunkCost = _MscTrkPaNegotiatedTrunkCost_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 11, 1, 12),
    _MscTrkPaNegotiatedTrunkCost_Type()
)
mscTrkPaNegotiatedTrunkCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkPaNegotiatedTrunkCost.setStatus("mandatory")


class _MscTrkPaNegotiatedAtmMode_Type(Integer32):
    """Custom type mscTrkPaNegotiatedAtmMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mapping", 1),
          ("multiplexing", 0),
          ("notApplicable", 2))
    )


_MscTrkPaNegotiatedAtmMode_Type.__name__ = "Integer32"
_MscTrkPaNegotiatedAtmMode_Object = MibTableColumn
mscTrkPaNegotiatedAtmMode = _MscTrkPaNegotiatedAtmMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 11, 1, 13),
    _MscTrkPaNegotiatedAtmMode_Type()
)
mscTrkPaNegotiatedAtmMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkPaNegotiatedAtmMode.setStatus("mandatory")


class _MscTrkPaNegotiatedTrunkDelay_Type(Unsigned32):
    """Custom type mscTrkPaNegotiatedTrunkDelay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1500),
    )


_MscTrkPaNegotiatedTrunkDelay_Type.__name__ = "Unsigned32"
_MscTrkPaNegotiatedTrunkDelay_Object = MibTableColumn
mscTrkPaNegotiatedTrunkDelay = _MscTrkPaNegotiatedTrunkDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 11, 1, 14),
    _MscTrkPaNegotiatedTrunkDelay_Type()
)
mscTrkPaNegotiatedTrunkDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkPaNegotiatedTrunkDelay.setStatus("mandatory")


class _MscTrkPaNegotiatedTrunkType_Type(Integer32):
    """Custom type mscTrkPaNegotiatedTrunkType based on Integer32"""
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
        *(("satellite", 1),
          ("terrestrial", 0),
          ("trunkType1", 2),
          ("trunkType2", 3),
          ("trunkType3", 4),
          ("trunkType4", 5),
          ("trunkType5", 6),
          ("trunkType6", 7))
    )


_MscTrkPaNegotiatedTrunkType_Type.__name__ = "Integer32"
_MscTrkPaNegotiatedTrunkType_Object = MibTableColumn
mscTrkPaNegotiatedTrunkType = _MscTrkPaNegotiatedTrunkType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 11, 1, 15),
    _MscTrkPaNegotiatedTrunkType_Type()
)
mscTrkPaNegotiatedTrunkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkPaNegotiatedTrunkType.setStatus("mandatory")
_MscTrkPaRbwTable_Object = MibTable
mscTrkPaRbwTable = _MscTrkPaRbwTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 214)
)
if mibBuilder.loadTexts:
    mscTrkPaRbwTable.setStatus("mandatory")
_MscTrkPaRbwEntry_Object = MibTableRow
mscTrkPaRbwEntry = _MscTrkPaRbwEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 214, 1)
)
mscTrkPaRbwEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkIndex"),
    (0, "Nortel-MsCarrier-MscPassport-PorsTrunksMIB", "mscTrkPaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-PorsTrunksMIB", "mscTrkPaRbwIndex"),
)
if mibBuilder.loadTexts:
    mscTrkPaRbwEntry.setStatus("mandatory")


class _MscTrkPaRbwIndex_Type(Integer32):
    """Custom type mscTrkPaRbwIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_MscTrkPaRbwIndex_Type.__name__ = "Integer32"
_MscTrkPaRbwIndex_Object = MibTableColumn
mscTrkPaRbwIndex = _MscTrkPaRbwIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 214, 1, 1),
    _MscTrkPaRbwIndex_Type()
)
mscTrkPaRbwIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscTrkPaRbwIndex.setStatus("mandatory")


class _MscTrkPaRbwValue_Type(Unsigned32):
    """Custom type mscTrkPaRbwValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscTrkPaRbwValue_Type.__name__ = "Unsigned32"
_MscTrkPaRbwValue_Object = MibTableColumn
mscTrkPaRbwValue = _MscTrkPaRbwValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 214, 1, 2),
    _MscTrkPaRbwValue_Type()
)
mscTrkPaRbwValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkPaRbwValue.setStatus("mandatory")
_MscTrkPaPacntTable_Object = MibTable
mscTrkPaPacntTable = _MscTrkPaPacntTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 215)
)
if mibBuilder.loadTexts:
    mscTrkPaPacntTable.setStatus("mandatory")
_MscTrkPaPacntEntry_Object = MibTableRow
mscTrkPaPacntEntry = _MscTrkPaPacntEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 215, 1)
)
mscTrkPaPacntEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkIndex"),
    (0, "Nortel-MsCarrier-MscPassport-PorsTrunksMIB", "mscTrkPaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-PorsTrunksMIB", "mscTrkPaPacntIndex"),
)
if mibBuilder.loadTexts:
    mscTrkPaPacntEntry.setStatus("mandatory")


class _MscTrkPaPacntIndex_Type(Integer32):
    """Custom type mscTrkPaPacntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_MscTrkPaPacntIndex_Type.__name__ = "Integer32"
_MscTrkPaPacntIndex_Object = MibTableColumn
mscTrkPaPacntIndex = _MscTrkPaPacntIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 215, 1, 1),
    _MscTrkPaPacntIndex_Type()
)
mscTrkPaPacntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscTrkPaPacntIndex.setStatus("mandatory")


class _MscTrkPaPacntValue_Type(Unsigned32):
    """Custom type mscTrkPaPacntValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscTrkPaPacntValue_Type.__name__ = "Unsigned32"
_MscTrkPaPacntValue_Object = MibTableColumn
mscTrkPaPacntValue = _MscTrkPaPacntValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 215, 1, 2),
    _MscTrkPaPacntValue_Type()
)
mscTrkPaPacntValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkPaPacntValue.setStatus("mandatory")
_MscTrkPaPfcntTable_Object = MibTable
mscTrkPaPfcntTable = _MscTrkPaPfcntTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 216)
)
if mibBuilder.loadTexts:
    mscTrkPaPfcntTable.setStatus("mandatory")
_MscTrkPaPfcntEntry_Object = MibTableRow
mscTrkPaPfcntEntry = _MscTrkPaPfcntEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 216, 1)
)
mscTrkPaPfcntEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkIndex"),
    (0, "Nortel-MsCarrier-MscPassport-PorsTrunksMIB", "mscTrkPaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-PorsTrunksMIB", "mscTrkPaPfcntIndex"),
)
if mibBuilder.loadTexts:
    mscTrkPaPfcntEntry.setStatus("mandatory")


class _MscTrkPaPfcntIndex_Type(Integer32):
    """Custom type mscTrkPaPfcntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_MscTrkPaPfcntIndex_Type.__name__ = "Integer32"
_MscTrkPaPfcntIndex_Object = MibTableColumn
mscTrkPaPfcntIndex = _MscTrkPaPfcntIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 216, 1, 1),
    _MscTrkPaPfcntIndex_Type()
)
mscTrkPaPfcntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscTrkPaPfcntIndex.setStatus("mandatory")


class _MscTrkPaPfcntValue_Type(Unsigned32):
    """Custom type mscTrkPaPfcntValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscTrkPaPfcntValue_Type.__name__ = "Unsigned32"
_MscTrkPaPfcntValue_Object = MibTableColumn
mscTrkPaPfcntValue = _MscTrkPaPfcntValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 216, 1, 2),
    _MscTrkPaPfcntValue_Type()
)
mscTrkPaPfcntValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkPaPfcntValue.setStatus("mandatory")
_MscTrkPaPccntTable_Object = MibTable
mscTrkPaPccntTable = _MscTrkPaPccntTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 217)
)
if mibBuilder.loadTexts:
    mscTrkPaPccntTable.setStatus("mandatory")
_MscTrkPaPccntEntry_Object = MibTableRow
mscTrkPaPccntEntry = _MscTrkPaPccntEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 217, 1)
)
mscTrkPaPccntEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkIndex"),
    (0, "Nortel-MsCarrier-MscPassport-PorsTrunksMIB", "mscTrkPaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-PorsTrunksMIB", "mscTrkPaPccntIndex"),
)
if mibBuilder.loadTexts:
    mscTrkPaPccntEntry.setStatus("mandatory")


class _MscTrkPaPccntIndex_Type(Integer32):
    """Custom type mscTrkPaPccntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_MscTrkPaPccntIndex_Type.__name__ = "Integer32"
_MscTrkPaPccntIndex_Object = MibTableColumn
mscTrkPaPccntIndex = _MscTrkPaPccntIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 217, 1, 1),
    _MscTrkPaPccntIndex_Type()
)
mscTrkPaPccntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscTrkPaPccntIndex.setStatus("mandatory")


class _MscTrkPaPccntValue_Type(Unsigned32):
    """Custom type mscTrkPaPccntValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscTrkPaPccntValue_Type.__name__ = "Unsigned32"
_MscTrkPaPccntValue_Object = MibTableColumn
mscTrkPaPccntValue = _MscTrkPaPccntValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 217, 1, 2),
    _MscTrkPaPccntValue_Type()
)
mscTrkPaPccntValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkPaPccntValue.setStatus("mandatory")
_MscTrkPaPbcntTable_Object = MibTable
mscTrkPaPbcntTable = _MscTrkPaPbcntTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 218)
)
if mibBuilder.loadTexts:
    mscTrkPaPbcntTable.setStatus("mandatory")
_MscTrkPaPbcntEntry_Object = MibTableRow
mscTrkPaPbcntEntry = _MscTrkPaPbcntEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 218, 1)
)
mscTrkPaPbcntEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkIndex"),
    (0, "Nortel-MsCarrier-MscPassport-PorsTrunksMIB", "mscTrkPaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-PorsTrunksMIB", "mscTrkPaPbcntIndex"),
)
if mibBuilder.loadTexts:
    mscTrkPaPbcntEntry.setStatus("mandatory")


class _MscTrkPaPbcntIndex_Type(Integer32):
    """Custom type mscTrkPaPbcntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_MscTrkPaPbcntIndex_Type.__name__ = "Integer32"
_MscTrkPaPbcntIndex_Object = MibTableColumn
mscTrkPaPbcntIndex = _MscTrkPaPbcntIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 218, 1, 1),
    _MscTrkPaPbcntIndex_Type()
)
mscTrkPaPbcntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscTrkPaPbcntIndex.setStatus("mandatory")


class _MscTrkPaPbcntValue_Type(Unsigned32):
    """Custom type mscTrkPaPbcntValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscTrkPaPbcntValue_Type.__name__ = "Unsigned32"
_MscTrkPaPbcntValue_Object = MibTableColumn
mscTrkPaPbcntValue = _MscTrkPaPbcntValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 218, 1, 2),
    _MscTrkPaPbcntValue_Type()
)
mscTrkPaPbcntValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkPaPbcntValue.setStatus("mandatory")
_MscTrkLCh_ObjectIdentity = ObjectIdentity
mscTrkLCh = _MscTrkLCh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 5)
)
_MscTrkLChRowStatusTable_Object = MibTable
mscTrkLChRowStatusTable = _MscTrkLChRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 5, 1)
)
if mibBuilder.loadTexts:
    mscTrkLChRowStatusTable.setStatus("mandatory")
_MscTrkLChRowStatusEntry_Object = MibTableRow
mscTrkLChRowStatusEntry = _MscTrkLChRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 5, 1, 1)
)
mscTrkLChRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkIndex"),
    (0, "Nortel-MsCarrier-MscPassport-PorsTrunksMIB", "mscTrkLChIndex"),
)
if mibBuilder.loadTexts:
    mscTrkLChRowStatusEntry.setStatus("mandatory")
_MscTrkLChRowStatus_Type = RowStatus
_MscTrkLChRowStatus_Object = MibTableColumn
mscTrkLChRowStatus = _MscTrkLChRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 5, 1, 1, 1),
    _MscTrkLChRowStatus_Type()
)
mscTrkLChRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkLChRowStatus.setStatus("mandatory")
_MscTrkLChComponentName_Type = DisplayString
_MscTrkLChComponentName_Object = MibTableColumn
mscTrkLChComponentName = _MscTrkLChComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 5, 1, 1, 2),
    _MscTrkLChComponentName_Type()
)
mscTrkLChComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkLChComponentName.setStatus("mandatory")
_MscTrkLChStorageType_Type = StorageType
_MscTrkLChStorageType_Object = MibTableColumn
mscTrkLChStorageType = _MscTrkLChStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 5, 1, 1, 4),
    _MscTrkLChStorageType_Type()
)
mscTrkLChStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkLChStorageType.setStatus("mandatory")


class _MscTrkLChIndex_Type(Integer32):
    """Custom type mscTrkLChIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscTrkLChIndex_Type.__name__ = "Integer32"
_MscTrkLChIndex_Object = MibTableColumn
mscTrkLChIndex = _MscTrkLChIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 5, 1, 1, 10),
    _MscTrkLChIndex_Type()
)
mscTrkLChIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscTrkLChIndex.setStatus("mandatory")
_MscTrkLChOperTable_Object = MibTable
mscTrkLChOperTable = _MscTrkLChOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 5, 10)
)
if mibBuilder.loadTexts:
    mscTrkLChOperTable.setStatus("mandatory")
_MscTrkLChOperEntry_Object = MibTableRow
mscTrkLChOperEntry = _MscTrkLChOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 5, 10, 1)
)
mscTrkLChOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkIndex"),
    (0, "Nortel-MsCarrier-MscPassport-PorsTrunksMIB", "mscTrkLChIndex"),
)
if mibBuilder.loadTexts:
    mscTrkLChOperEntry.setStatus("mandatory")
_MscTrkLChNextHop_Type = RowPointer
_MscTrkLChNextHop_Object = MibTableColumn
mscTrkLChNextHop = _MscTrkLChNextHop_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 5, 10, 1, 2),
    _MscTrkLChNextHop_Type()
)
mscTrkLChNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkLChNextHop.setStatus("mandatory")


class _MscTrkLChSetupPriority_Type(Unsigned32):
    """Custom type mscTrkLChSetupPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_MscTrkLChSetupPriority_Type.__name__ = "Unsigned32"
_MscTrkLChSetupPriority_Object = MibTableColumn
mscTrkLChSetupPriority = _MscTrkLChSetupPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 5, 10, 1, 3),
    _MscTrkLChSetupPriority_Type()
)
mscTrkLChSetupPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkLChSetupPriority.setStatus("mandatory")


class _MscTrkLChHoldingPriority_Type(Unsigned32):
    """Custom type mscTrkLChHoldingPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_MscTrkLChHoldingPriority_Type.__name__ = "Unsigned32"
_MscTrkLChHoldingPriority_Object = MibTableColumn
mscTrkLChHoldingPriority = _MscTrkLChHoldingPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 5, 10, 1, 4),
    _MscTrkLChHoldingPriority_Type()
)
mscTrkLChHoldingPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkLChHoldingPriority.setStatus("mandatory")


class _MscTrkLChEmissionPriority_Type(Unsigned32):
    """Custom type mscTrkLChEmissionPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MscTrkLChEmissionPriority_Type.__name__ = "Unsigned32"
_MscTrkLChEmissionPriority_Object = MibTableColumn
mscTrkLChEmissionPriority = _MscTrkLChEmissionPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 5, 10, 1, 5),
    _MscTrkLChEmissionPriority_Type()
)
mscTrkLChEmissionPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkLChEmissionPriority.setStatus("mandatory")


class _MscTrkLChDiscardPriority_Type(Unsigned32):
    """Custom type mscTrkLChDiscardPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MscTrkLChDiscardPriority_Type.__name__ = "Unsigned32"
_MscTrkLChDiscardPriority_Object = MibTableColumn
mscTrkLChDiscardPriority = _MscTrkLChDiscardPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 5, 10, 1, 6),
    _MscTrkLChDiscardPriority_Type()
)
mscTrkLChDiscardPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkLChDiscardPriority.setStatus("mandatory")


class _MscTrkLChRequiredTxBandwidth_Type(Unsigned32):
    """Custom type mscTrkLChRequiredTxBandwidth based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscTrkLChRequiredTxBandwidth_Type.__name__ = "Unsigned32"
_MscTrkLChRequiredTxBandwidth_Object = MibTableColumn
mscTrkLChRequiredTxBandwidth = _MscTrkLChRequiredTxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 5, 10, 1, 7),
    _MscTrkLChRequiredTxBandwidth_Type()
)
mscTrkLChRequiredTxBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkLChRequiredTxBandwidth.setStatus("mandatory")


class _MscTrkLChRequiredRxBandwidth_Type(Unsigned32):
    """Custom type mscTrkLChRequiredRxBandwidth based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscTrkLChRequiredRxBandwidth_Type.__name__ = "Unsigned32"
_MscTrkLChRequiredRxBandwidth_Object = MibTableColumn
mscTrkLChRequiredRxBandwidth = _MscTrkLChRequiredRxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 5, 10, 1, 8),
    _MscTrkLChRequiredRxBandwidth_Type()
)
mscTrkLChRequiredRxBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkLChRequiredRxBandwidth.setStatus("mandatory")


class _MscTrkLChMode_Type(Integer32):
    """Custom type mscTrkLChMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("aal5FrmMap", 5),
          ("aal5FrmMux", 2),
          ("cellMap", 6),
          ("hdlcFrmMux", 1),
          ("spoFrmMap", 4),
          ("spoFrmMux", 3),
          ("unknown", 0))
    )


_MscTrkLChMode_Type.__name__ = "Integer32"
_MscTrkLChMode_Object = MibTableColumn
mscTrkLChMode = _MscTrkLChMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 5, 10, 1, 9),
    _MscTrkLChMode_Type()
)
mscTrkLChMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkLChMode.setStatus("mandatory")


class _MscTrkLChMaximumTransmissionUnit_Type(Unsigned32):
    """Custom type mscTrkLChMaximumTransmissionUnit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscTrkLChMaximumTransmissionUnit_Type.__name__ = "Unsigned32"
_MscTrkLChMaximumTransmissionUnit_Object = MibTableColumn
mscTrkLChMaximumTransmissionUnit = _MscTrkLChMaximumTransmissionUnit_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 5, 10, 1, 10),
    _MscTrkLChMaximumTransmissionUnit_Type()
)
mscTrkLChMaximumTransmissionUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkLChMaximumTransmissionUnit.setStatus("mandatory")
_MscTrkLChLocalConnection_Type = RowPointer
_MscTrkLChLocalConnection_Object = MibTableColumn
mscTrkLChLocalConnection = _MscTrkLChLocalConnection_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 5, 10, 1, 11),
    _MscTrkLChLocalConnection_Type()
)
mscTrkLChLocalConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkLChLocalConnection.setStatus("mandatory")
_PorsTrunksMIB_ObjectIdentity = ObjectIdentity
porsTrunksMIB = _PorsTrunksMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 39)
)
_PorsTrunksGroup_ObjectIdentity = ObjectIdentity
porsTrunksGroup = _PorsTrunksGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 39, 1)
)
_PorsTrunksGroupCA_ObjectIdentity = ObjectIdentity
porsTrunksGroupCA = _PorsTrunksGroupCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 39, 1, 1)
)
_PorsTrunksGroupCA02_ObjectIdentity = ObjectIdentity
porsTrunksGroupCA02 = _PorsTrunksGroupCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 39, 1, 1, 3)
)
_PorsTrunksGroupCA02A_ObjectIdentity = ObjectIdentity
porsTrunksGroupCA02A = _PorsTrunksGroupCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 39, 1, 1, 3, 2)
)
_PorsTrunksCapabilities_ObjectIdentity = ObjectIdentity
porsTrunksCapabilities = _PorsTrunksCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 39, 3)
)
_PorsTrunksCapabilitiesCA_ObjectIdentity = ObjectIdentity
porsTrunksCapabilitiesCA = _PorsTrunksCapabilitiesCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 39, 3, 1)
)
_PorsTrunksCapabilitiesCA02_ObjectIdentity = ObjectIdentity
porsTrunksCapabilitiesCA02 = _PorsTrunksCapabilitiesCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 39, 3, 1, 3)
)
_PorsTrunksCapabilitiesCA02A_ObjectIdentity = ObjectIdentity
porsTrunksCapabilitiesCA02A = _PorsTrunksCapabilitiesCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 39, 3, 1, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-MsCarrier-MscPassport-PorsTrunksMIB",
    **{"mscTrkPa": mscTrkPa,
       "mscTrkPaRowStatusTable": mscTrkPaRowStatusTable,
       "mscTrkPaRowStatusEntry": mscTrkPaRowStatusEntry,
       "mscTrkPaRowStatus": mscTrkPaRowStatus,
       "mscTrkPaComponentName": mscTrkPaComponentName,
       "mscTrkPaStorageType": mscTrkPaStorageType,
       "mscTrkPaIndex": mscTrkPaIndex,
       "mscTrkPaProvTable": mscTrkPaProvTable,
       "mscTrkPaProvEntry": mscTrkPaProvEntry,
       "mscTrkPaMaxLc": mscTrkPaMaxLc,
       "mscTrkPaMaxReservedBwOut": mscTrkPaMaxReservedBwOut,
       "mscTrkPaTrunkSecurity": mscTrkPaTrunkSecurity,
       "mscTrkPaSupportedTrafficTypes": mscTrkPaSupportedTrafficTypes,
       "mscTrkPaTrunkType": mscTrkPaTrunkType,
       "mscTrkPaCustomerParameter": mscTrkPaCustomerParameter,
       "mscTrkPaTrunkCost": mscTrkPaTrunkCost,
       "mscTrkPaOperTable": mscTrkPaOperTable,
       "mscTrkPaOperEntry": mscTrkPaOperEntry,
       "mscTrkPaState": mscTrkPaState,
       "mscTrkPaUsedLc": mscTrkPaUsedLc,
       "mscTrkPaNegotiatedMaxLc": mscTrkPaNegotiatedMaxLc,
       "mscTrkPaMaxReservableBwOut": mscTrkPaMaxReservableBwOut,
       "mscTrkPaOverReservedBwOut": mscTrkPaOverReservedBwOut,
       "mscTrkPaUnreservedBwOut": mscTrkPaUnreservedBwOut,
       "mscTrkPaClashCount": mscTrkPaClashCount,
       "mscTrkPaNegotiatedSupportedTrafficTypes": mscTrkPaNegotiatedSupportedTrafficTypes,
       "mscTrkPaNegotiatedTrunkSecurity": mscTrkPaNegotiatedTrunkSecurity,
       "mscTrkPaNegotiatedCustomerParameter": mscTrkPaNegotiatedCustomerParameter,
       "mscTrkPaNegotiatedTrunkCost": mscTrkPaNegotiatedTrunkCost,
       "mscTrkPaNegotiatedAtmMode": mscTrkPaNegotiatedAtmMode,
       "mscTrkPaNegotiatedTrunkDelay": mscTrkPaNegotiatedTrunkDelay,
       "mscTrkPaNegotiatedTrunkType": mscTrkPaNegotiatedTrunkType,
       "mscTrkPaRbwTable": mscTrkPaRbwTable,
       "mscTrkPaRbwEntry": mscTrkPaRbwEntry,
       "mscTrkPaRbwIndex": mscTrkPaRbwIndex,
       "mscTrkPaRbwValue": mscTrkPaRbwValue,
       "mscTrkPaPacntTable": mscTrkPaPacntTable,
       "mscTrkPaPacntEntry": mscTrkPaPacntEntry,
       "mscTrkPaPacntIndex": mscTrkPaPacntIndex,
       "mscTrkPaPacntValue": mscTrkPaPacntValue,
       "mscTrkPaPfcntTable": mscTrkPaPfcntTable,
       "mscTrkPaPfcntEntry": mscTrkPaPfcntEntry,
       "mscTrkPaPfcntIndex": mscTrkPaPfcntIndex,
       "mscTrkPaPfcntValue": mscTrkPaPfcntValue,
       "mscTrkPaPccntTable": mscTrkPaPccntTable,
       "mscTrkPaPccntEntry": mscTrkPaPccntEntry,
       "mscTrkPaPccntIndex": mscTrkPaPccntIndex,
       "mscTrkPaPccntValue": mscTrkPaPccntValue,
       "mscTrkPaPbcntTable": mscTrkPaPbcntTable,
       "mscTrkPaPbcntEntry": mscTrkPaPbcntEntry,
       "mscTrkPaPbcntIndex": mscTrkPaPbcntIndex,
       "mscTrkPaPbcntValue": mscTrkPaPbcntValue,
       "mscTrkLCh": mscTrkLCh,
       "mscTrkLChRowStatusTable": mscTrkLChRowStatusTable,
       "mscTrkLChRowStatusEntry": mscTrkLChRowStatusEntry,
       "mscTrkLChRowStatus": mscTrkLChRowStatus,
       "mscTrkLChComponentName": mscTrkLChComponentName,
       "mscTrkLChStorageType": mscTrkLChStorageType,
       "mscTrkLChIndex": mscTrkLChIndex,
       "mscTrkLChOperTable": mscTrkLChOperTable,
       "mscTrkLChOperEntry": mscTrkLChOperEntry,
       "mscTrkLChNextHop": mscTrkLChNextHop,
       "mscTrkLChSetupPriority": mscTrkLChSetupPriority,
       "mscTrkLChHoldingPriority": mscTrkLChHoldingPriority,
       "mscTrkLChEmissionPriority": mscTrkLChEmissionPriority,
       "mscTrkLChDiscardPriority": mscTrkLChDiscardPriority,
       "mscTrkLChRequiredTxBandwidth": mscTrkLChRequiredTxBandwidth,
       "mscTrkLChRequiredRxBandwidth": mscTrkLChRequiredRxBandwidth,
       "mscTrkLChMode": mscTrkLChMode,
       "mscTrkLChMaximumTransmissionUnit": mscTrkLChMaximumTransmissionUnit,
       "mscTrkLChLocalConnection": mscTrkLChLocalConnection,
       "porsTrunksMIB": porsTrunksMIB,
       "porsTrunksGroup": porsTrunksGroup,
       "porsTrunksGroupCA": porsTrunksGroupCA,
       "porsTrunksGroupCA02": porsTrunksGroupCA02,
       "porsTrunksGroupCA02A": porsTrunksGroupCA02A,
       "porsTrunksCapabilities": porsTrunksCapabilities,
       "porsTrunksCapabilitiesCA": porsTrunksCapabilitiesCA,
       "porsTrunksCapabilitiesCA02": porsTrunksCapabilitiesCA02,
       "porsTrunksCapabilitiesCA02A": porsTrunksCapabilitiesCA02A}
)
