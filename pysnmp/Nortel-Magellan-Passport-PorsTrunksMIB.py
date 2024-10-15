# SNMP MIB module (Nortel-Magellan-Passport-PorsTrunksMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-Magellan-Passport-PorsTrunksMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:31:15 2024
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
    "Nortel-Magellan-Passport-StandardTextualConventionsMIB",
    "DisplayString",
    "Integer32",
    "RowPointer",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(AsciiString,
 NonReplicated) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-TextualConventionsMIB",
    "AsciiString",
    "NonReplicated")

(trk,
 trkIndex) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-TrunksMIB",
    "trk",
    "trkIndex")

(passportMIBs,) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-UsefulDefinitionsMIB",
    "passportMIBs")

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

_TrkPa_ObjectIdentity = ObjectIdentity
trkPa = _TrkPa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4)
)
_TrkPaRowStatusTable_Object = MibTable
trkPaRowStatusTable = _TrkPaRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 1)
)
if mibBuilder.loadTexts:
    trkPaRowStatusTable.setStatus("mandatory")
_TrkPaRowStatusEntry_Object = MibTableRow
trkPaRowStatusEntry = _TrkPaRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 1, 1)
)
trkPaRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TrunksMIB", "trkIndex"),
    (0, "Nortel-Magellan-Passport-PorsTrunksMIB", "trkPaIndex"),
)
if mibBuilder.loadTexts:
    trkPaRowStatusEntry.setStatus("mandatory")
_TrkPaRowStatus_Type = RowStatus
_TrkPaRowStatus_Object = MibTableColumn
trkPaRowStatus = _TrkPaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 1, 1, 1),
    _TrkPaRowStatus_Type()
)
trkPaRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trkPaRowStatus.setStatus("mandatory")
_TrkPaComponentName_Type = DisplayString
_TrkPaComponentName_Object = MibTableColumn
trkPaComponentName = _TrkPaComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 1, 1, 2),
    _TrkPaComponentName_Type()
)
trkPaComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkPaComponentName.setStatus("mandatory")
_TrkPaStorageType_Type = StorageType
_TrkPaStorageType_Object = MibTableColumn
trkPaStorageType = _TrkPaStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 1, 1, 4),
    _TrkPaStorageType_Type()
)
trkPaStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkPaStorageType.setStatus("mandatory")
_TrkPaIndex_Type = NonReplicated
_TrkPaIndex_Object = MibTableColumn
trkPaIndex = _TrkPaIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 1, 1, 10),
    _TrkPaIndex_Type()
)
trkPaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trkPaIndex.setStatus("mandatory")
_TrkPaProvTable_Object = MibTable
trkPaProvTable = _TrkPaProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 10)
)
if mibBuilder.loadTexts:
    trkPaProvTable.setStatus("mandatory")
_TrkPaProvEntry_Object = MibTableRow
trkPaProvEntry = _TrkPaProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 10, 1)
)
trkPaProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TrunksMIB", "trkIndex"),
    (0, "Nortel-Magellan-Passport-PorsTrunksMIB", "trkPaIndex"),
)
if mibBuilder.loadTexts:
    trkPaProvEntry.setStatus("mandatory")


class _TrkPaMaxLc_Type(Unsigned32):
    """Custom type trkPaMaxLc based on Unsigned32"""
    defaultValue = 512

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65435),
    )


_TrkPaMaxLc_Type.__name__ = "Unsigned32"
_TrkPaMaxLc_Object = MibTableColumn
trkPaMaxLc = _TrkPaMaxLc_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 10, 1, 1),
    _TrkPaMaxLc_Type()
)
trkPaMaxLc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trkPaMaxLc.setStatus("mandatory")


class _TrkPaMaxReservedBwOut_Type(Unsigned32):
    """Custom type trkPaMaxReservedBwOut based on Unsigned32"""
    defaultValue = 50

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_TrkPaMaxReservedBwOut_Type.__name__ = "Unsigned32"
_TrkPaMaxReservedBwOut_Object = MibTableColumn
trkPaMaxReservedBwOut = _TrkPaMaxReservedBwOut_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 10, 1, 2),
    _TrkPaMaxReservedBwOut_Type()
)
trkPaMaxReservedBwOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trkPaMaxReservedBwOut.setStatus("mandatory")


class _TrkPaTrunkSecurity_Type(Unsigned32):
    """Custom type trkPaTrunkSecurity based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TrkPaTrunkSecurity_Type.__name__ = "Unsigned32"
_TrkPaTrunkSecurity_Object = MibTableColumn
trkPaTrunkSecurity = _TrkPaTrunkSecurity_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 10, 1, 3),
    _TrkPaTrunkSecurity_Type()
)
trkPaTrunkSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trkPaTrunkSecurity.setStatus("mandatory")


class _TrkPaSupportedTrafficTypes_Type(OctetString):
    """Custom type trkPaSupportedTrafficTypes based on OctetString"""
    defaultHexValue = "f8"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_TrkPaSupportedTrafficTypes_Type.__name__ = "OctetString"
_TrkPaSupportedTrafficTypes_Object = MibTableColumn
trkPaSupportedTrafficTypes = _TrkPaSupportedTrafficTypes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 10, 1, 4),
    _TrkPaSupportedTrafficTypes_Type()
)
trkPaSupportedTrafficTypes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trkPaSupportedTrafficTypes.setStatus("mandatory")


class _TrkPaTrunkType_Type(Integer32):
    """Custom type trkPaTrunkType based on Integer32"""
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


_TrkPaTrunkType_Type.__name__ = "Integer32"
_TrkPaTrunkType_Object = MibTableColumn
trkPaTrunkType = _TrkPaTrunkType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 10, 1, 5),
    _TrkPaTrunkType_Type()
)
trkPaTrunkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trkPaTrunkType.setStatus("mandatory")


class _TrkPaCustomerParameter_Type(Unsigned32):
    """Custom type trkPaCustomerParameter based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TrkPaCustomerParameter_Type.__name__ = "Unsigned32"
_TrkPaCustomerParameter_Object = MibTableColumn
trkPaCustomerParameter = _TrkPaCustomerParameter_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 10, 1, 6),
    _TrkPaCustomerParameter_Type()
)
trkPaCustomerParameter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trkPaCustomerParameter.setStatus("mandatory")


class _TrkPaTrunkCost_Type(Unsigned32):
    """Custom type trkPaTrunkCost based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TrkPaTrunkCost_Type.__name__ = "Unsigned32"
_TrkPaTrunkCost_Object = MibTableColumn
trkPaTrunkCost = _TrkPaTrunkCost_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 10, 1, 7),
    _TrkPaTrunkCost_Type()
)
trkPaTrunkCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trkPaTrunkCost.setStatus("mandatory")


class _TrkPaOverrideTrunkDelay_Type(Unsigned32):
    """Custom type trkPaOverrideTrunkDelay based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1500),
    )


_TrkPaOverrideTrunkDelay_Type.__name__ = "Unsigned32"
_TrkPaOverrideTrunkDelay_Object = MibTableColumn
trkPaOverrideTrunkDelay = _TrkPaOverrideTrunkDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 10, 1, 8),
    _TrkPaOverrideTrunkDelay_Type()
)
trkPaOverrideTrunkDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trkPaOverrideTrunkDelay.setStatus("mandatory")
_TrkPaOperTable_Object = MibTable
trkPaOperTable = _TrkPaOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 11)
)
if mibBuilder.loadTexts:
    trkPaOperTable.setStatus("mandatory")
_TrkPaOperEntry_Object = MibTableRow
trkPaOperEntry = _TrkPaOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 11, 1)
)
trkPaOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TrunksMIB", "trkIndex"),
    (0, "Nortel-Magellan-Passport-PorsTrunksMIB", "trkPaIndex"),
)
if mibBuilder.loadTexts:
    trkPaOperEntry.setStatus("mandatory")


class _TrkPaState_Type(AsciiString):
    """Custom type trkPaState based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_TrkPaState_Type.__name__ = "AsciiString"
_TrkPaState_Object = MibTableColumn
trkPaState = _TrkPaState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 11, 1, 1),
    _TrkPaState_Type()
)
trkPaState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkPaState.setStatus("mandatory")


class _TrkPaUsedLc_Type(Unsigned32):
    """Custom type trkPaUsedLc based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_TrkPaUsedLc_Type.__name__ = "Unsigned32"
_TrkPaUsedLc_Object = MibTableColumn
trkPaUsedLc = _TrkPaUsedLc_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 11, 1, 2),
    _TrkPaUsedLc_Type()
)
trkPaUsedLc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkPaUsedLc.setStatus("mandatory")


class _TrkPaNegotiatedMaxLc_Type(Unsigned32):
    """Custom type trkPaNegotiatedMaxLc based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_TrkPaNegotiatedMaxLc_Type.__name__ = "Unsigned32"
_TrkPaNegotiatedMaxLc_Object = MibTableColumn
trkPaNegotiatedMaxLc = _TrkPaNegotiatedMaxLc_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 11, 1, 3),
    _TrkPaNegotiatedMaxLc_Type()
)
trkPaNegotiatedMaxLc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkPaNegotiatedMaxLc.setStatus("mandatory")


class _TrkPaMaxReservableBwOut_Type(Unsigned32):
    """Custom type trkPaMaxReservableBwOut based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_TrkPaMaxReservableBwOut_Type.__name__ = "Unsigned32"
_TrkPaMaxReservableBwOut_Object = MibTableColumn
trkPaMaxReservableBwOut = _TrkPaMaxReservableBwOut_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 11, 1, 4),
    _TrkPaMaxReservableBwOut_Type()
)
trkPaMaxReservableBwOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkPaMaxReservableBwOut.setStatus("mandatory")


class _TrkPaOverReservedBwOut_Type(Unsigned32):
    """Custom type trkPaOverReservedBwOut based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_TrkPaOverReservedBwOut_Type.__name__ = "Unsigned32"
_TrkPaOverReservedBwOut_Object = MibTableColumn
trkPaOverReservedBwOut = _TrkPaOverReservedBwOut_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 11, 1, 5),
    _TrkPaOverReservedBwOut_Type()
)
trkPaOverReservedBwOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkPaOverReservedBwOut.setStatus("mandatory")


class _TrkPaUnreservedBwOut_Type(Unsigned32):
    """Custom type trkPaUnreservedBwOut based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_TrkPaUnreservedBwOut_Type.__name__ = "Unsigned32"
_TrkPaUnreservedBwOut_Object = MibTableColumn
trkPaUnreservedBwOut = _TrkPaUnreservedBwOut_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 11, 1, 6),
    _TrkPaUnreservedBwOut_Type()
)
trkPaUnreservedBwOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkPaUnreservedBwOut.setStatus("mandatory")


class _TrkPaClashCount_Type(Unsigned32):
    """Custom type trkPaClashCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_TrkPaClashCount_Type.__name__ = "Unsigned32"
_TrkPaClashCount_Object = MibTableColumn
trkPaClashCount = _TrkPaClashCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 11, 1, 7),
    _TrkPaClashCount_Type()
)
trkPaClashCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkPaClashCount.setStatus("mandatory")


class _TrkPaNegotiatedSupportedTrafficTypes_Type(OctetString):
    """Custom type trkPaNegotiatedSupportedTrafficTypes based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_TrkPaNegotiatedSupportedTrafficTypes_Type.__name__ = "OctetString"
_TrkPaNegotiatedSupportedTrafficTypes_Object = MibTableColumn
trkPaNegotiatedSupportedTrafficTypes = _TrkPaNegotiatedSupportedTrafficTypes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 11, 1, 9),
    _TrkPaNegotiatedSupportedTrafficTypes_Type()
)
trkPaNegotiatedSupportedTrafficTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkPaNegotiatedSupportedTrafficTypes.setStatus("mandatory")


class _TrkPaNegotiatedTrunkSecurity_Type(Unsigned32):
    """Custom type trkPaNegotiatedTrunkSecurity based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TrkPaNegotiatedTrunkSecurity_Type.__name__ = "Unsigned32"
_TrkPaNegotiatedTrunkSecurity_Object = MibTableColumn
trkPaNegotiatedTrunkSecurity = _TrkPaNegotiatedTrunkSecurity_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 11, 1, 10),
    _TrkPaNegotiatedTrunkSecurity_Type()
)
trkPaNegotiatedTrunkSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkPaNegotiatedTrunkSecurity.setStatus("mandatory")


class _TrkPaNegotiatedCustomerParameter_Type(Unsigned32):
    """Custom type trkPaNegotiatedCustomerParameter based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TrkPaNegotiatedCustomerParameter_Type.__name__ = "Unsigned32"
_TrkPaNegotiatedCustomerParameter_Object = MibTableColumn
trkPaNegotiatedCustomerParameter = _TrkPaNegotiatedCustomerParameter_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 11, 1, 11),
    _TrkPaNegotiatedCustomerParameter_Type()
)
trkPaNegotiatedCustomerParameter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkPaNegotiatedCustomerParameter.setStatus("mandatory")


class _TrkPaNegotiatedTrunkCost_Type(Unsigned32):
    """Custom type trkPaNegotiatedTrunkCost based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TrkPaNegotiatedTrunkCost_Type.__name__ = "Unsigned32"
_TrkPaNegotiatedTrunkCost_Object = MibTableColumn
trkPaNegotiatedTrunkCost = _TrkPaNegotiatedTrunkCost_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 11, 1, 12),
    _TrkPaNegotiatedTrunkCost_Type()
)
trkPaNegotiatedTrunkCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkPaNegotiatedTrunkCost.setStatus("mandatory")


class _TrkPaNegotiatedAtmMode_Type(Integer32):
    """Custom type trkPaNegotiatedAtmMode based on Integer32"""
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


_TrkPaNegotiatedAtmMode_Type.__name__ = "Integer32"
_TrkPaNegotiatedAtmMode_Object = MibTableColumn
trkPaNegotiatedAtmMode = _TrkPaNegotiatedAtmMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 11, 1, 13),
    _TrkPaNegotiatedAtmMode_Type()
)
trkPaNegotiatedAtmMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkPaNegotiatedAtmMode.setStatus("mandatory")


class _TrkPaNegotiatedTrunkDelay_Type(Unsigned32):
    """Custom type trkPaNegotiatedTrunkDelay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1500),
    )


_TrkPaNegotiatedTrunkDelay_Type.__name__ = "Unsigned32"
_TrkPaNegotiatedTrunkDelay_Object = MibTableColumn
trkPaNegotiatedTrunkDelay = _TrkPaNegotiatedTrunkDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 11, 1, 14),
    _TrkPaNegotiatedTrunkDelay_Type()
)
trkPaNegotiatedTrunkDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkPaNegotiatedTrunkDelay.setStatus("mandatory")


class _TrkPaNegotiatedTrunkType_Type(Integer32):
    """Custom type trkPaNegotiatedTrunkType based on Integer32"""
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


_TrkPaNegotiatedTrunkType_Type.__name__ = "Integer32"
_TrkPaNegotiatedTrunkType_Object = MibTableColumn
trkPaNegotiatedTrunkType = _TrkPaNegotiatedTrunkType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 11, 1, 15),
    _TrkPaNegotiatedTrunkType_Type()
)
trkPaNegotiatedTrunkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkPaNegotiatedTrunkType.setStatus("mandatory")


class _TrkPaAdaptationLevel_Type(Unsigned32):
    """Custom type trkPaAdaptationLevel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_TrkPaAdaptationLevel_Type.__name__ = "Unsigned32"
_TrkPaAdaptationLevel_Object = MibTableColumn
trkPaAdaptationLevel = _TrkPaAdaptationLevel_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 11, 1, 16),
    _TrkPaAdaptationLevel_Type()
)
trkPaAdaptationLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkPaAdaptationLevel.setStatus("mandatory")
_TrkPaAdaptationTable_Object = MibTable
trkPaAdaptationTable = _TrkPaAdaptationTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 12)
)
if mibBuilder.loadTexts:
    trkPaAdaptationTable.setStatus("mandatory")
_TrkPaAdaptationEntry_Object = MibTableRow
trkPaAdaptationEntry = _TrkPaAdaptationEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 12, 1)
)
trkPaAdaptationEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TrunksMIB", "trkIndex"),
    (0, "Nortel-Magellan-Passport-PorsTrunksMIB", "trkPaIndex"),
)
if mibBuilder.loadTexts:
    trkPaAdaptationEntry.setStatus("mandatory")


class _TrkPaMaxAdaptationLevel_Type(Unsigned32):
    """Custom type trkPaMaxAdaptationLevel based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_TrkPaMaxAdaptationLevel_Type.__name__ = "Unsigned32"
_TrkPaMaxAdaptationLevel_Object = MibTableColumn
trkPaMaxAdaptationLevel = _TrkPaMaxAdaptationLevel_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 12, 1, 1),
    _TrkPaMaxAdaptationLevel_Type()
)
trkPaMaxAdaptationLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trkPaMaxAdaptationLevel.setStatus("mandatory")


class _TrkPaAdaptationBandwidth_Type(Unsigned32):
    """Custom type trkPaAdaptationBandwidth based on Unsigned32"""
    defaultValue = 64000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_TrkPaAdaptationBandwidth_Type.__name__ = "Unsigned32"
_TrkPaAdaptationBandwidth_Object = MibTableColumn
trkPaAdaptationBandwidth = _TrkPaAdaptationBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 12, 1, 2),
    _TrkPaAdaptationBandwidth_Type()
)
trkPaAdaptationBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trkPaAdaptationBandwidth.setStatus("mandatory")
_TrkPaRbwTable_Object = MibTable
trkPaRbwTable = _TrkPaRbwTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 214)
)
if mibBuilder.loadTexts:
    trkPaRbwTable.setStatus("mandatory")
_TrkPaRbwEntry_Object = MibTableRow
trkPaRbwEntry = _TrkPaRbwEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 214, 1)
)
trkPaRbwEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TrunksMIB", "trkIndex"),
    (0, "Nortel-Magellan-Passport-PorsTrunksMIB", "trkPaIndex"),
    (0, "Nortel-Magellan-Passport-PorsTrunksMIB", "trkPaRbwIndex"),
)
if mibBuilder.loadTexts:
    trkPaRbwEntry.setStatus("mandatory")


class _TrkPaRbwIndex_Type(Integer32):
    """Custom type trkPaRbwIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_TrkPaRbwIndex_Type.__name__ = "Integer32"
_TrkPaRbwIndex_Object = MibTableColumn
trkPaRbwIndex = _TrkPaRbwIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 214, 1, 1),
    _TrkPaRbwIndex_Type()
)
trkPaRbwIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trkPaRbwIndex.setStatus("mandatory")


class _TrkPaRbwValue_Type(Unsigned32):
    """Custom type trkPaRbwValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_TrkPaRbwValue_Type.__name__ = "Unsigned32"
_TrkPaRbwValue_Object = MibTableColumn
trkPaRbwValue = _TrkPaRbwValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 214, 1, 2),
    _TrkPaRbwValue_Type()
)
trkPaRbwValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkPaRbwValue.setStatus("mandatory")
_TrkPaPacntTable_Object = MibTable
trkPaPacntTable = _TrkPaPacntTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 215)
)
if mibBuilder.loadTexts:
    trkPaPacntTable.setStatus("mandatory")
_TrkPaPacntEntry_Object = MibTableRow
trkPaPacntEntry = _TrkPaPacntEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 215, 1)
)
trkPaPacntEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TrunksMIB", "trkIndex"),
    (0, "Nortel-Magellan-Passport-PorsTrunksMIB", "trkPaIndex"),
    (0, "Nortel-Magellan-Passport-PorsTrunksMIB", "trkPaPacntIndex"),
)
if mibBuilder.loadTexts:
    trkPaPacntEntry.setStatus("mandatory")


class _TrkPaPacntIndex_Type(Integer32):
    """Custom type trkPaPacntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_TrkPaPacntIndex_Type.__name__ = "Integer32"
_TrkPaPacntIndex_Object = MibTableColumn
trkPaPacntIndex = _TrkPaPacntIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 215, 1, 1),
    _TrkPaPacntIndex_Type()
)
trkPaPacntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trkPaPacntIndex.setStatus("mandatory")


class _TrkPaPacntValue_Type(Unsigned32):
    """Custom type trkPaPacntValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_TrkPaPacntValue_Type.__name__ = "Unsigned32"
_TrkPaPacntValue_Object = MibTableColumn
trkPaPacntValue = _TrkPaPacntValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 215, 1, 2),
    _TrkPaPacntValue_Type()
)
trkPaPacntValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkPaPacntValue.setStatus("mandatory")
_TrkPaPfcntTable_Object = MibTable
trkPaPfcntTable = _TrkPaPfcntTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 216)
)
if mibBuilder.loadTexts:
    trkPaPfcntTable.setStatus("mandatory")
_TrkPaPfcntEntry_Object = MibTableRow
trkPaPfcntEntry = _TrkPaPfcntEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 216, 1)
)
trkPaPfcntEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TrunksMIB", "trkIndex"),
    (0, "Nortel-Magellan-Passport-PorsTrunksMIB", "trkPaIndex"),
    (0, "Nortel-Magellan-Passport-PorsTrunksMIB", "trkPaPfcntIndex"),
)
if mibBuilder.loadTexts:
    trkPaPfcntEntry.setStatus("mandatory")


class _TrkPaPfcntIndex_Type(Integer32):
    """Custom type trkPaPfcntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_TrkPaPfcntIndex_Type.__name__ = "Integer32"
_TrkPaPfcntIndex_Object = MibTableColumn
trkPaPfcntIndex = _TrkPaPfcntIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 216, 1, 1),
    _TrkPaPfcntIndex_Type()
)
trkPaPfcntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trkPaPfcntIndex.setStatus("mandatory")


class _TrkPaPfcntValue_Type(Unsigned32):
    """Custom type trkPaPfcntValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_TrkPaPfcntValue_Type.__name__ = "Unsigned32"
_TrkPaPfcntValue_Object = MibTableColumn
trkPaPfcntValue = _TrkPaPfcntValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 216, 1, 2),
    _TrkPaPfcntValue_Type()
)
trkPaPfcntValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkPaPfcntValue.setStatus("mandatory")
_TrkPaPccntTable_Object = MibTable
trkPaPccntTable = _TrkPaPccntTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 217)
)
if mibBuilder.loadTexts:
    trkPaPccntTable.setStatus("mandatory")
_TrkPaPccntEntry_Object = MibTableRow
trkPaPccntEntry = _TrkPaPccntEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 217, 1)
)
trkPaPccntEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TrunksMIB", "trkIndex"),
    (0, "Nortel-Magellan-Passport-PorsTrunksMIB", "trkPaIndex"),
    (0, "Nortel-Magellan-Passport-PorsTrunksMIB", "trkPaPccntIndex"),
)
if mibBuilder.loadTexts:
    trkPaPccntEntry.setStatus("mandatory")


class _TrkPaPccntIndex_Type(Integer32):
    """Custom type trkPaPccntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_TrkPaPccntIndex_Type.__name__ = "Integer32"
_TrkPaPccntIndex_Object = MibTableColumn
trkPaPccntIndex = _TrkPaPccntIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 217, 1, 1),
    _TrkPaPccntIndex_Type()
)
trkPaPccntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trkPaPccntIndex.setStatus("mandatory")


class _TrkPaPccntValue_Type(Unsigned32):
    """Custom type trkPaPccntValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_TrkPaPccntValue_Type.__name__ = "Unsigned32"
_TrkPaPccntValue_Object = MibTableColumn
trkPaPccntValue = _TrkPaPccntValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 217, 1, 2),
    _TrkPaPccntValue_Type()
)
trkPaPccntValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkPaPccntValue.setStatus("mandatory")
_TrkPaPbcntTable_Object = MibTable
trkPaPbcntTable = _TrkPaPbcntTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 218)
)
if mibBuilder.loadTexts:
    trkPaPbcntTable.setStatus("mandatory")
_TrkPaPbcntEntry_Object = MibTableRow
trkPaPbcntEntry = _TrkPaPbcntEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 218, 1)
)
trkPaPbcntEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TrunksMIB", "trkIndex"),
    (0, "Nortel-Magellan-Passport-PorsTrunksMIB", "trkPaIndex"),
    (0, "Nortel-Magellan-Passport-PorsTrunksMIB", "trkPaPbcntIndex"),
)
if mibBuilder.loadTexts:
    trkPaPbcntEntry.setStatus("mandatory")


class _TrkPaPbcntIndex_Type(Integer32):
    """Custom type trkPaPbcntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_TrkPaPbcntIndex_Type.__name__ = "Integer32"
_TrkPaPbcntIndex_Object = MibTableColumn
trkPaPbcntIndex = _TrkPaPbcntIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 218, 1, 1),
    _TrkPaPbcntIndex_Type()
)
trkPaPbcntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trkPaPbcntIndex.setStatus("mandatory")


class _TrkPaPbcntValue_Type(Unsigned32):
    """Custom type trkPaPbcntValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_TrkPaPbcntValue_Type.__name__ = "Unsigned32"
_TrkPaPbcntValue_Object = MibTableColumn
trkPaPbcntValue = _TrkPaPbcntValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 218, 1, 2),
    _TrkPaPbcntValue_Type()
)
trkPaPbcntValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkPaPbcntValue.setStatus("mandatory")
_TrkPaAdpthTable_Object = MibTable
trkPaAdpthTable = _TrkPaAdpthTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 653)
)
if mibBuilder.loadTexts:
    trkPaAdpthTable.setStatus("mandatory")
_TrkPaAdpthEntry_Object = MibTableRow
trkPaAdpthEntry = _TrkPaAdpthEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 653, 1)
)
trkPaAdpthEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TrunksMIB", "trkIndex"),
    (0, "Nortel-Magellan-Passport-PorsTrunksMIB", "trkPaIndex"),
    (0, "Nortel-Magellan-Passport-PorsTrunksMIB", "trkPaAdpthIndex"),
)
if mibBuilder.loadTexts:
    trkPaAdpthEntry.setStatus("mandatory")


class _TrkPaAdpthIndex_Type(Integer32):
    """Custom type trkPaAdpthIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("level1", 0),
          ("level2", 1),
          ("level3", 2))
    )


_TrkPaAdpthIndex_Type.__name__ = "Integer32"
_TrkPaAdpthIndex_Object = MibTableColumn
trkPaAdpthIndex = _TrkPaAdpthIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 653, 1, 1),
    _TrkPaAdpthIndex_Type()
)
trkPaAdpthIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trkPaAdpthIndex.setStatus("mandatory")


class _TrkPaAdpthValue_Type(Unsigned32):
    """Custom type trkPaAdpthValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_TrkPaAdpthValue_Type.__name__ = "Unsigned32"
_TrkPaAdpthValue_Object = MibTableColumn
trkPaAdpthValue = _TrkPaAdpthValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 653, 1, 2),
    _TrkPaAdpthValue_Type()
)
trkPaAdpthValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trkPaAdpthValue.setStatus("mandatory")
_TrkPaAdphoTable_Object = MibTable
trkPaAdphoTable = _TrkPaAdphoTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 654)
)
if mibBuilder.loadTexts:
    trkPaAdphoTable.setStatus("mandatory")
_TrkPaAdphoEntry_Object = MibTableRow
trkPaAdphoEntry = _TrkPaAdphoEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 654, 1)
)
trkPaAdphoEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TrunksMIB", "trkIndex"),
    (0, "Nortel-Magellan-Passport-PorsTrunksMIB", "trkPaIndex"),
    (0, "Nortel-Magellan-Passport-PorsTrunksMIB", "trkPaAdphoIndex"),
)
if mibBuilder.loadTexts:
    trkPaAdphoEntry.setStatus("mandatory")


class _TrkPaAdphoIndex_Type(Integer32):
    """Custom type trkPaAdphoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("set", 0))
    )


_TrkPaAdphoIndex_Type.__name__ = "Integer32"
_TrkPaAdphoIndex_Object = MibTableColumn
trkPaAdphoIndex = _TrkPaAdphoIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 654, 1, 1),
    _TrkPaAdphoIndex_Type()
)
trkPaAdphoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trkPaAdphoIndex.setStatus("mandatory")


class _TrkPaAdphoValue_Type(Unsigned32):
    """Custom type trkPaAdphoValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 60),
    )


_TrkPaAdphoValue_Type.__name__ = "Unsigned32"
_TrkPaAdphoValue_Object = MibTableColumn
trkPaAdphoValue = _TrkPaAdphoValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 654, 1, 2),
    _TrkPaAdphoValue_Type()
)
trkPaAdphoValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trkPaAdphoValue.setStatus("mandatory")
_TrkLCh_ObjectIdentity = ObjectIdentity
trkLCh = _TrkLCh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 5)
)
_TrkLChRowStatusTable_Object = MibTable
trkLChRowStatusTable = _TrkLChRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 5, 1)
)
if mibBuilder.loadTexts:
    trkLChRowStatusTable.setStatus("mandatory")
_TrkLChRowStatusEntry_Object = MibTableRow
trkLChRowStatusEntry = _TrkLChRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 5, 1, 1)
)
trkLChRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TrunksMIB", "trkIndex"),
    (0, "Nortel-Magellan-Passport-PorsTrunksMIB", "trkLChIndex"),
)
if mibBuilder.loadTexts:
    trkLChRowStatusEntry.setStatus("mandatory")
_TrkLChRowStatus_Type = RowStatus
_TrkLChRowStatus_Object = MibTableColumn
trkLChRowStatus = _TrkLChRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 5, 1, 1, 1),
    _TrkLChRowStatus_Type()
)
trkLChRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkLChRowStatus.setStatus("mandatory")
_TrkLChComponentName_Type = DisplayString
_TrkLChComponentName_Object = MibTableColumn
trkLChComponentName = _TrkLChComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 5, 1, 1, 2),
    _TrkLChComponentName_Type()
)
trkLChComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkLChComponentName.setStatus("mandatory")
_TrkLChStorageType_Type = StorageType
_TrkLChStorageType_Object = MibTableColumn
trkLChStorageType = _TrkLChStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 5, 1, 1, 4),
    _TrkLChStorageType_Type()
)
trkLChStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkLChStorageType.setStatus("mandatory")


class _TrkLChIndex_Type(Integer32):
    """Custom type trkLChIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TrkLChIndex_Type.__name__ = "Integer32"
_TrkLChIndex_Object = MibTableColumn
trkLChIndex = _TrkLChIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 5, 1, 1, 10),
    _TrkLChIndex_Type()
)
trkLChIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trkLChIndex.setStatus("mandatory")
_TrkLChOperTable_Object = MibTable
trkLChOperTable = _TrkLChOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 5, 10)
)
if mibBuilder.loadTexts:
    trkLChOperTable.setStatus("mandatory")
_TrkLChOperEntry_Object = MibTableRow
trkLChOperEntry = _TrkLChOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 5, 10, 1)
)
trkLChOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TrunksMIB", "trkIndex"),
    (0, "Nortel-Magellan-Passport-PorsTrunksMIB", "trkLChIndex"),
)
if mibBuilder.loadTexts:
    trkLChOperEntry.setStatus("mandatory")
_TrkLChNextHop_Type = RowPointer
_TrkLChNextHop_Object = MibTableColumn
trkLChNextHop = _TrkLChNextHop_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 5, 10, 1, 2),
    _TrkLChNextHop_Type()
)
trkLChNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkLChNextHop.setStatus("mandatory")


class _TrkLChSetupPriority_Type(Unsigned32):
    """Custom type trkLChSetupPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_TrkLChSetupPriority_Type.__name__ = "Unsigned32"
_TrkLChSetupPriority_Object = MibTableColumn
trkLChSetupPriority = _TrkLChSetupPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 5, 10, 1, 3),
    _TrkLChSetupPriority_Type()
)
trkLChSetupPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkLChSetupPriority.setStatus("mandatory")


class _TrkLChHoldingPriority_Type(Unsigned32):
    """Custom type trkLChHoldingPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_TrkLChHoldingPriority_Type.__name__ = "Unsigned32"
_TrkLChHoldingPriority_Object = MibTableColumn
trkLChHoldingPriority = _TrkLChHoldingPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 5, 10, 1, 4),
    _TrkLChHoldingPriority_Type()
)
trkLChHoldingPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkLChHoldingPriority.setStatus("mandatory")


class _TrkLChEmissionPriority_Type(Unsigned32):
    """Custom type trkLChEmissionPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_TrkLChEmissionPriority_Type.__name__ = "Unsigned32"
_TrkLChEmissionPriority_Object = MibTableColumn
trkLChEmissionPriority = _TrkLChEmissionPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 5, 10, 1, 5),
    _TrkLChEmissionPriority_Type()
)
trkLChEmissionPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkLChEmissionPriority.setStatus("mandatory")


class _TrkLChDiscardPriority_Type(Unsigned32):
    """Custom type trkLChDiscardPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_TrkLChDiscardPriority_Type.__name__ = "Unsigned32"
_TrkLChDiscardPriority_Object = MibTableColumn
trkLChDiscardPriority = _TrkLChDiscardPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 5, 10, 1, 6),
    _TrkLChDiscardPriority_Type()
)
trkLChDiscardPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkLChDiscardPriority.setStatus("mandatory")


class _TrkLChRequiredTxBandwidth_Type(Unsigned32):
    """Custom type trkLChRequiredTxBandwidth based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_TrkLChRequiredTxBandwidth_Type.__name__ = "Unsigned32"
_TrkLChRequiredTxBandwidth_Object = MibTableColumn
trkLChRequiredTxBandwidth = _TrkLChRequiredTxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 5, 10, 1, 7),
    _TrkLChRequiredTxBandwidth_Type()
)
trkLChRequiredTxBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkLChRequiredTxBandwidth.setStatus("mandatory")


class _TrkLChRequiredRxBandwidth_Type(Unsigned32):
    """Custom type trkLChRequiredRxBandwidth based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_TrkLChRequiredRxBandwidth_Type.__name__ = "Unsigned32"
_TrkLChRequiredRxBandwidth_Object = MibTableColumn
trkLChRequiredRxBandwidth = _TrkLChRequiredRxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 5, 10, 1, 8),
    _TrkLChRequiredRxBandwidth_Type()
)
trkLChRequiredRxBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkLChRequiredRxBandwidth.setStatus("mandatory")


class _TrkLChMode_Type(Integer32):
    """Custom type trkLChMode based on Integer32"""
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


_TrkLChMode_Type.__name__ = "Integer32"
_TrkLChMode_Object = MibTableColumn
trkLChMode = _TrkLChMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 5, 10, 1, 9),
    _TrkLChMode_Type()
)
trkLChMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkLChMode.setStatus("mandatory")


class _TrkLChMaximumTransmissionUnit_Type(Unsigned32):
    """Custom type trkLChMaximumTransmissionUnit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_TrkLChMaximumTransmissionUnit_Type.__name__ = "Unsigned32"
_TrkLChMaximumTransmissionUnit_Object = MibTableColumn
trkLChMaximumTransmissionUnit = _TrkLChMaximumTransmissionUnit_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 5, 10, 1, 10),
    _TrkLChMaximumTransmissionUnit_Type()
)
trkLChMaximumTransmissionUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkLChMaximumTransmissionUnit.setStatus("mandatory")
_TrkLChLocalConnection_Type = RowPointer
_TrkLChLocalConnection_Object = MibTableColumn
trkLChLocalConnection = _TrkLChLocalConnection_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 5, 10, 1, 11),
    _TrkLChLocalConnection_Type()
)
trkLChLocalConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkLChLocalConnection.setStatus("mandatory")
_PorsTrunksMIB_ObjectIdentity = ObjectIdentity
porsTrunksMIB = _PorsTrunksMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 39)
)
_PorsTrunksGroup_ObjectIdentity = ObjectIdentity
porsTrunksGroup = _PorsTrunksGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 39, 1)
)
_PorsTrunksGroupBE_ObjectIdentity = ObjectIdentity
porsTrunksGroupBE = _PorsTrunksGroupBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 39, 1, 5)
)
_PorsTrunksGroupBE00_ObjectIdentity = ObjectIdentity
porsTrunksGroupBE00 = _PorsTrunksGroupBE00_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 39, 1, 5, 1)
)
_PorsTrunksGroupBE00A_ObjectIdentity = ObjectIdentity
porsTrunksGroupBE00A = _PorsTrunksGroupBE00A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 39, 1, 5, 1, 2)
)
_PorsTrunksCapabilities_ObjectIdentity = ObjectIdentity
porsTrunksCapabilities = _PorsTrunksCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 39, 3)
)
_PorsTrunksCapabilitiesBE_ObjectIdentity = ObjectIdentity
porsTrunksCapabilitiesBE = _PorsTrunksCapabilitiesBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 39, 3, 5)
)
_PorsTrunksCapabilitiesBE00_ObjectIdentity = ObjectIdentity
porsTrunksCapabilitiesBE00 = _PorsTrunksCapabilitiesBE00_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 39, 3, 5, 1)
)
_PorsTrunksCapabilitiesBE00A_ObjectIdentity = ObjectIdentity
porsTrunksCapabilitiesBE00A = _PorsTrunksCapabilitiesBE00A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 39, 3, 5, 1, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-Magellan-Passport-PorsTrunksMIB",
    **{"trkPa": trkPa,
       "trkPaRowStatusTable": trkPaRowStatusTable,
       "trkPaRowStatusEntry": trkPaRowStatusEntry,
       "trkPaRowStatus": trkPaRowStatus,
       "trkPaComponentName": trkPaComponentName,
       "trkPaStorageType": trkPaStorageType,
       "trkPaIndex": trkPaIndex,
       "trkPaProvTable": trkPaProvTable,
       "trkPaProvEntry": trkPaProvEntry,
       "trkPaMaxLc": trkPaMaxLc,
       "trkPaMaxReservedBwOut": trkPaMaxReservedBwOut,
       "trkPaTrunkSecurity": trkPaTrunkSecurity,
       "trkPaSupportedTrafficTypes": trkPaSupportedTrafficTypes,
       "trkPaTrunkType": trkPaTrunkType,
       "trkPaCustomerParameter": trkPaCustomerParameter,
       "trkPaTrunkCost": trkPaTrunkCost,
       "trkPaOverrideTrunkDelay": trkPaOverrideTrunkDelay,
       "trkPaOperTable": trkPaOperTable,
       "trkPaOperEntry": trkPaOperEntry,
       "trkPaState": trkPaState,
       "trkPaUsedLc": trkPaUsedLc,
       "trkPaNegotiatedMaxLc": trkPaNegotiatedMaxLc,
       "trkPaMaxReservableBwOut": trkPaMaxReservableBwOut,
       "trkPaOverReservedBwOut": trkPaOverReservedBwOut,
       "trkPaUnreservedBwOut": trkPaUnreservedBwOut,
       "trkPaClashCount": trkPaClashCount,
       "trkPaNegotiatedSupportedTrafficTypes": trkPaNegotiatedSupportedTrafficTypes,
       "trkPaNegotiatedTrunkSecurity": trkPaNegotiatedTrunkSecurity,
       "trkPaNegotiatedCustomerParameter": trkPaNegotiatedCustomerParameter,
       "trkPaNegotiatedTrunkCost": trkPaNegotiatedTrunkCost,
       "trkPaNegotiatedAtmMode": trkPaNegotiatedAtmMode,
       "trkPaNegotiatedTrunkDelay": trkPaNegotiatedTrunkDelay,
       "trkPaNegotiatedTrunkType": trkPaNegotiatedTrunkType,
       "trkPaAdaptationLevel": trkPaAdaptationLevel,
       "trkPaAdaptationTable": trkPaAdaptationTable,
       "trkPaAdaptationEntry": trkPaAdaptationEntry,
       "trkPaMaxAdaptationLevel": trkPaMaxAdaptationLevel,
       "trkPaAdaptationBandwidth": trkPaAdaptationBandwidth,
       "trkPaRbwTable": trkPaRbwTable,
       "trkPaRbwEntry": trkPaRbwEntry,
       "trkPaRbwIndex": trkPaRbwIndex,
       "trkPaRbwValue": trkPaRbwValue,
       "trkPaPacntTable": trkPaPacntTable,
       "trkPaPacntEntry": trkPaPacntEntry,
       "trkPaPacntIndex": trkPaPacntIndex,
       "trkPaPacntValue": trkPaPacntValue,
       "trkPaPfcntTable": trkPaPfcntTable,
       "trkPaPfcntEntry": trkPaPfcntEntry,
       "trkPaPfcntIndex": trkPaPfcntIndex,
       "trkPaPfcntValue": trkPaPfcntValue,
       "trkPaPccntTable": trkPaPccntTable,
       "trkPaPccntEntry": trkPaPccntEntry,
       "trkPaPccntIndex": trkPaPccntIndex,
       "trkPaPccntValue": trkPaPccntValue,
       "trkPaPbcntTable": trkPaPbcntTable,
       "trkPaPbcntEntry": trkPaPbcntEntry,
       "trkPaPbcntIndex": trkPaPbcntIndex,
       "trkPaPbcntValue": trkPaPbcntValue,
       "trkPaAdpthTable": trkPaAdpthTable,
       "trkPaAdpthEntry": trkPaAdpthEntry,
       "trkPaAdpthIndex": trkPaAdpthIndex,
       "trkPaAdpthValue": trkPaAdpthValue,
       "trkPaAdphoTable": trkPaAdphoTable,
       "trkPaAdphoEntry": trkPaAdphoEntry,
       "trkPaAdphoIndex": trkPaAdphoIndex,
       "trkPaAdphoValue": trkPaAdphoValue,
       "trkLCh": trkLCh,
       "trkLChRowStatusTable": trkLChRowStatusTable,
       "trkLChRowStatusEntry": trkLChRowStatusEntry,
       "trkLChRowStatus": trkLChRowStatus,
       "trkLChComponentName": trkLChComponentName,
       "trkLChStorageType": trkLChStorageType,
       "trkLChIndex": trkLChIndex,
       "trkLChOperTable": trkLChOperTable,
       "trkLChOperEntry": trkLChOperEntry,
       "trkLChNextHop": trkLChNextHop,
       "trkLChSetupPriority": trkLChSetupPriority,
       "trkLChHoldingPriority": trkLChHoldingPriority,
       "trkLChEmissionPriority": trkLChEmissionPriority,
       "trkLChDiscardPriority": trkLChDiscardPriority,
       "trkLChRequiredTxBandwidth": trkLChRequiredTxBandwidth,
       "trkLChRequiredRxBandwidth": trkLChRequiredRxBandwidth,
       "trkLChMode": trkLChMode,
       "trkLChMaximumTransmissionUnit": trkLChMaximumTransmissionUnit,
       "trkLChLocalConnection": trkLChLocalConnection,
       "porsTrunksMIB": porsTrunksMIB,
       "porsTrunksGroup": porsTrunksGroup,
       "porsTrunksGroupBE": porsTrunksGroupBE,
       "porsTrunksGroupBE00": porsTrunksGroupBE00,
       "porsTrunksGroupBE00A": porsTrunksGroupBE00A,
       "porsTrunksCapabilities": porsTrunksCapabilities,
       "porsTrunksCapabilitiesBE": porsTrunksCapabilitiesBE,
       "porsTrunksCapabilitiesBE00": porsTrunksCapabilitiesBE00,
       "porsTrunksCapabilitiesBE00A": porsTrunksCapabilitiesBE00A}
)
