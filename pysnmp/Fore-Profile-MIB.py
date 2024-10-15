# SNMP MIB module (Fore-Profile-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Fore-Profile-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:47:10 2024
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

(frameInternetworking,) = mibBuilder.importSymbols(
    "Fore-Common-MIB",
    "frameInternetworking")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

foreProfileModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 4)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ProfileLmiTable_Object = MibTable
profileLmiTable = _ProfileLmiTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 1)
)
if mibBuilder.loadTexts:
    profileLmiTable.setStatus("current")
_ProfileLmiEntry_Object = MibTableRow
profileLmiEntry = _ProfileLmiEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 1, 1)
)
profileLmiEntry.setIndexNames(
    (0, "Fore-Profile-MIB", "profileLmiIndex"),
)
if mibBuilder.loadTexts:
    profileLmiEntry.setStatus("current")
_ProfileLmiIndex_Type = Integer32
_ProfileLmiIndex_Object = MibTableColumn
profileLmiIndex = _ProfileLmiIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 1, 1, 1),
    _ProfileLmiIndex_Type()
)
profileLmiIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    profileLmiIndex.setStatus("current")
_ProfileLmiRowStatus_Type = RowStatus
_ProfileLmiRowStatus_Object = MibTableColumn
profileLmiRowStatus = _ProfileLmiRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 1, 1, 2),
    _ProfileLmiRowStatus_Type()
)
profileLmiRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    profileLmiRowStatus.setStatus("current")
_ProfileLmiName_Type = DisplayString
_ProfileLmiName_Object = MibTableColumn
profileLmiName = _ProfileLmiName_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 1, 1, 3),
    _ProfileLmiName_Type()
)
profileLmiName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    profileLmiName.setStatus("current")


class _ProfileLmiFlavour_Type(Integer32):
    """Custom type profileLmiFlavour based on Integer32"""
    defaultValue = 5

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
        *(("lmi", 2),
          ("none", 1),
          ("q933a", 5),
          ("t1617b", 4),
          ("t1617d", 3))
    )


_ProfileLmiFlavour_Type.__name__ = "Integer32"
_ProfileLmiFlavour_Object = MibTableColumn
profileLmiFlavour = _ProfileLmiFlavour_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 1, 1, 4),
    _ProfileLmiFlavour_Type()
)
profileLmiFlavour.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    profileLmiFlavour.setStatus("current")


class _ProfileLmiT391_Type(Integer32):
    """Custom type profileLmiT391 based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_ProfileLmiT391_Type.__name__ = "Integer32"
_ProfileLmiT391_Object = MibTableColumn
profileLmiT391 = _ProfileLmiT391_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 1, 1, 5),
    _ProfileLmiT391_Type()
)
profileLmiT391.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    profileLmiT391.setStatus("current")


class _ProfileLmiN391_Type(Integer32):
    """Custom type profileLmiN391 based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ProfileLmiN391_Type.__name__ = "Integer32"
_ProfileLmiN391_Object = MibTableColumn
profileLmiN391 = _ProfileLmiN391_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 1, 1, 6),
    _ProfileLmiN391_Type()
)
profileLmiN391.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    profileLmiN391.setStatus("current")


class _ProfileLmiT392_Type(Integer32):
    """Custom type profileLmiT392 based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_ProfileLmiT392_Type.__name__ = "Integer32"
_ProfileLmiT392_Object = MibTableColumn
profileLmiT392 = _ProfileLmiT392_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 1, 1, 7),
    _ProfileLmiT392_Type()
)
profileLmiT392.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    profileLmiT392.setStatus("current")


class _ProfileLmiN392_Type(Integer32):
    """Custom type profileLmiN392 based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_ProfileLmiN392_Type.__name__ = "Integer32"
_ProfileLmiN392_Object = MibTableColumn
profileLmiN392 = _ProfileLmiN392_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 1, 1, 8),
    _ProfileLmiN392_Type()
)
profileLmiN392.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    profileLmiN392.setStatus("current")


class _ProfileLmiN393_Type(Integer32):
    """Custom type profileLmiN393 based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_ProfileLmiN393_Type.__name__ = "Integer32"
_ProfileLmiN393_Object = MibTableColumn
profileLmiN393 = _ProfileLmiN393_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 1, 1, 9),
    _ProfileLmiN393_Type()
)
profileLmiN393.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    profileLmiN393.setStatus("current")


class _ProfileLminT3_Type(Integer32):
    """Custom type profileLminT3 based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 5),
        ValueRangeConstraint(10, 10),
        ValueRangeConstraint(15, 15),
        ValueRangeConstraint(20, 20),
        ValueRangeConstraint(25, 25),
        ValueRangeConstraint(30, 30),
    )


_ProfileLminT3_Type.__name__ = "Integer32"
_ProfileLminT3_Object = MibTableColumn
profileLminT3 = _ProfileLminT3_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 1, 1, 10),
    _ProfileLminT3_Type()
)
profileLminT3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    profileLminT3.setStatus("current")


class _ProfileLmiDirection_Type(Integer32):
    """Custom type profileLmiDirection based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bi", 2),
          ("uni", 1))
    )


_ProfileLmiDirection_Type.__name__ = "Integer32"
_ProfileLmiDirection_Object = MibTableColumn
profileLmiDirection = _ProfileLmiDirection_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 1, 1, 11),
    _ProfileLmiDirection_Type()
)
profileLmiDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    profileLmiDirection.setStatus("current")


class _ProfileLmiRole_Type(Integer32):
    """Custom type profileLmiRole based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("network", 2),
          ("user", 1))
    )


_ProfileLmiRole_Type.__name__ = "Integer32"
_ProfileLmiRole_Object = MibTableColumn
profileLmiRole = _ProfileLmiRole_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 1, 1, 12),
    _ProfileLmiRole_Type()
)
profileLmiRole.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    profileLmiRole.setStatus("current")


class _ProfileLmiRefCnt_Type(Integer32):
    """Custom type profileLmiRefCnt based on Integer32"""
    defaultValue = 0


_ProfileLmiRefCnt_Object = MibTableColumn
profileLmiRefCnt = _ProfileLmiRefCnt_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 1, 1, 13),
    _ProfileLmiRefCnt_Type()
)
profileLmiRefCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    profileLmiRefCnt.setStatus("current")
_ProfileFrRateTable_Object = MibTable
profileFrRateTable = _ProfileFrRateTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 2)
)
if mibBuilder.loadTexts:
    profileFrRateTable.setStatus("current")
_ProfileFrRateEntry_Object = MibTableRow
profileFrRateEntry = _ProfileFrRateEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 2, 1)
)
profileFrRateEntry.setIndexNames(
    (0, "Fore-Profile-MIB", "profileFrRateIndex"),
)
if mibBuilder.loadTexts:
    profileFrRateEntry.setStatus("current")
_ProfileFrRateIndex_Type = Integer32
_ProfileFrRateIndex_Object = MibTableColumn
profileFrRateIndex = _ProfileFrRateIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 2, 1, 1),
    _ProfileFrRateIndex_Type()
)
profileFrRateIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    profileFrRateIndex.setStatus("current")
_ProfileFrRateRowStatus_Type = RowStatus
_ProfileFrRateRowStatus_Object = MibTableColumn
profileFrRateRowStatus = _ProfileFrRateRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 2, 1, 2),
    _ProfileFrRateRowStatus_Type()
)
profileFrRateRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    profileFrRateRowStatus.setStatus("current")
_ProfileFrRateName_Type = DisplayString
_ProfileFrRateName_Object = MibTableColumn
profileFrRateName = _ProfileFrRateName_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 2, 1, 3),
    _ProfileFrRateName_Type()
)
profileFrRateName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    profileFrRateName.setStatus("current")
_ProfileFrRateInBc_Type = Integer32
_ProfileFrRateInBc_Object = MibTableColumn
profileFrRateInBc = _ProfileFrRateInBc_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 2, 1, 4),
    _ProfileFrRateInBc_Type()
)
profileFrRateInBc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    profileFrRateInBc.setStatus("current")
_ProfileFrRateInBe_Type = Integer32
_ProfileFrRateInBe_Object = MibTableColumn
profileFrRateInBe = _ProfileFrRateInBe_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 2, 1, 5),
    _ProfileFrRateInBe_Type()
)
profileFrRateInBe.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    profileFrRateInBe.setStatus("current")
_ProfileFrRateInCir_Type = Integer32
_ProfileFrRateInCir_Object = MibTableColumn
profileFrRateInCir = _ProfileFrRateInCir_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 2, 1, 6),
    _ProfileFrRateInCir_Type()
)
profileFrRateInCir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    profileFrRateInCir.setStatus("current")
_ProfileFrRateOutBc_Type = Integer32
_ProfileFrRateOutBc_Object = MibTableColumn
profileFrRateOutBc = _ProfileFrRateOutBc_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 2, 1, 7),
    _ProfileFrRateOutBc_Type()
)
profileFrRateOutBc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    profileFrRateOutBc.setStatus("current")
_ProfileFrRateOutBe_Type = Integer32
_ProfileFrRateOutBe_Object = MibTableColumn
profileFrRateOutBe = _ProfileFrRateOutBe_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 2, 1, 8),
    _ProfileFrRateOutBe_Type()
)
profileFrRateOutBe.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    profileFrRateOutBe.setStatus("current")
_ProfileFrRateOutCir_Type = Integer32
_ProfileFrRateOutCir_Object = MibTableColumn
profileFrRateOutCir = _ProfileFrRateOutCir_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 2, 1, 9),
    _ProfileFrRateOutCir_Type()
)
profileFrRateOutCir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    profileFrRateOutCir.setStatus("current")


class _ProfileFrRateMinBc_Type(Integer32):
    """Custom type profileFrRateMinBc based on Integer32"""
    defaultValue = 1000


_ProfileFrRateMinBc_Object = MibTableColumn
profileFrRateMinBc = _ProfileFrRateMinBc_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 2, 1, 10),
    _ProfileFrRateMinBc_Type()
)
profileFrRateMinBc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    profileFrRateMinBc.setStatus("current")


class _ProfileFrRateCmPeriod_Type(Integer32):
    """Custom type profileFrRateCmPeriod based on Integer32"""
    defaultValue = 1000


_ProfileFrRateCmPeriod_Object = MibTableColumn
profileFrRateCmPeriod = _ProfileFrRateCmPeriod_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 2, 1, 11),
    _ProfileFrRateCmPeriod_Type()
)
profileFrRateCmPeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    profileFrRateCmPeriod.setStatus("current")


class _ProfileFrRateRefCnt_Type(Integer32):
    """Custom type profileFrRateRefCnt based on Integer32"""
    defaultValue = 0


_ProfileFrRateRefCnt_Object = MibTableColumn
profileFrRateRefCnt = _ProfileFrRateRefCnt_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 2, 1, 12),
    _ProfileFrRateRefCnt_Type()
)
profileFrRateRefCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    profileFrRateRefCnt.setStatus("current")
_ProfileFuniTable_Object = MibTable
profileFuniTable = _ProfileFuniTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 3)
)
if mibBuilder.loadTexts:
    profileFuniTable.setStatus("current")
_ProfileFuniEntry_Object = MibTableRow
profileFuniEntry = _ProfileFuniEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 3, 1)
)
profileFuniEntry.setIndexNames(
    (0, "Fore-Profile-MIB", "profileFuniIndex"),
)
if mibBuilder.loadTexts:
    profileFuniEntry.setStatus("current")
_ProfileFuniIndex_Type = Integer32
_ProfileFuniIndex_Object = MibTableColumn
profileFuniIndex = _ProfileFuniIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 3, 1, 1),
    _ProfileFuniIndex_Type()
)
profileFuniIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    profileFuniIndex.setStatus("current")
_ProfileFuniRowStatus_Type = RowStatus
_ProfileFuniRowStatus_Object = MibTableColumn
profileFuniRowStatus = _ProfileFuniRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 3, 1, 2),
    _ProfileFuniRowStatus_Type()
)
profileFuniRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    profileFuniRowStatus.setStatus("current")
_ProfileFuniName_Type = DisplayString
_ProfileFuniName_Object = MibTableColumn
profileFuniName = _ProfileFuniName_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 3, 1, 3),
    _ProfileFuniName_Type()
)
profileFuniName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    profileFuniName.setStatus("current")


class _ProfileFuniIlmiVpi_Type(Integer32):
    """Custom type profileFuniIlmiVpi based on Integer32"""
    defaultValue = 0


_ProfileFuniIlmiVpi_Object = MibTableColumn
profileFuniIlmiVpi = _ProfileFuniIlmiVpi_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 3, 1, 4),
    _ProfileFuniIlmiVpi_Type()
)
profileFuniIlmiVpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    profileFuniIlmiVpi.setStatus("current")


class _ProfileFuniIlmiVci_Type(Integer32):
    """Custom type profileFuniIlmiVci based on Integer32"""
    defaultValue = 16


_ProfileFuniIlmiVci_Object = MibTableColumn
profileFuniIlmiVci = _ProfileFuniIlmiVci_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 3, 1, 5),
    _ProfileFuniIlmiVci_Type()
)
profileFuniIlmiVci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    profileFuniIlmiVci.setStatus("current")


class _ProfileFuniSigVpi_Type(Integer32):
    """Custom type profileFuniSigVpi based on Integer32"""
    defaultValue = 0


_ProfileFuniSigVpi_Object = MibTableColumn
profileFuniSigVpi = _ProfileFuniSigVpi_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 3, 1, 6),
    _ProfileFuniSigVpi_Type()
)
profileFuniSigVpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    profileFuniSigVpi.setStatus("current")


class _ProfileFuniSigVci_Type(Integer32):
    """Custom type profileFuniSigVci based on Integer32"""
    defaultValue = 5


_ProfileFuniSigVci_Object = MibTableColumn
profileFuniSigVci = _ProfileFuniSigVci_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 3, 1, 7),
    _ProfileFuniSigVci_Type()
)
profileFuniSigVci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    profileFuniSigVci.setStatus("current")


class _ProfileFuniMinVci_Type(Integer32):
    """Custom type profileFuniMinVci based on Integer32"""
    defaultValue = 32

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 63),
    )


_ProfileFuniMinVci_Type.__name__ = "Integer32"
_ProfileFuniMinVci_Object = MibTableColumn
profileFuniMinVci = _ProfileFuniMinVci_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 3, 1, 8),
    _ProfileFuniMinVci_Type()
)
profileFuniMinVci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    profileFuniMinVci.setStatus("current")


class _ProfileFuniMaxVci_Type(Integer32):
    """Custom type profileFuniMaxVci based on Integer32"""
    defaultValue = 63

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 63),
    )


_ProfileFuniMaxVci_Type.__name__ = "Integer32"
_ProfileFuniMaxVci_Object = MibTableColumn
profileFuniMaxVci = _ProfileFuniMaxVci_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 3, 1, 9),
    _ProfileFuniMaxVci_Type()
)
profileFuniMaxVci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    profileFuniMaxVci.setStatus("current")


class _ProfileFuniIlmiSupport_Type(Integer32):
    """Custom type profileFuniIlmiSupport based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_ProfileFuniIlmiSupport_Type.__name__ = "Integer32"
_ProfileFuniIlmiSupport_Object = MibTableColumn
profileFuniIlmiSupport = _ProfileFuniIlmiSupport_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 3, 1, 10),
    _ProfileFuniIlmiSupport_Type()
)
profileFuniIlmiSupport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    profileFuniIlmiSupport.setStatus("current")


class _ProfileFuniSigSupport_Type(Integer32):
    """Custom type profileFuniSigSupport based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_ProfileFuniSigSupport_Type.__name__ = "Integer32"
_ProfileFuniSigSupport_Object = MibTableColumn
profileFuniSigSupport = _ProfileFuniSigSupport_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 3, 1, 11),
    _ProfileFuniSigSupport_Type()
)
profileFuniSigSupport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    profileFuniSigSupport.setStatus("current")


class _ProfileFuniOamSupport_Type(Integer32):
    """Custom type profileFuniOamSupport based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_ProfileFuniOamSupport_Type.__name__ = "Integer32"
_ProfileFuniOamSupport_Object = MibTableColumn
profileFuniOamSupport = _ProfileFuniOamSupport_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 3, 1, 12),
    _ProfileFuniOamSupport_Type()
)
profileFuniOamSupport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    profileFuniOamSupport.setStatus("current")


class _ProfileFuniActiveVpiBits_Type(Integer32):
    """Custom type profileFuniActiveVpiBits based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_ProfileFuniActiveVpiBits_Type.__name__ = "Integer32"
_ProfileFuniActiveVpiBits_Object = MibTableColumn
profileFuniActiveVpiBits = _ProfileFuniActiveVpiBits_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 3, 1, 13),
    _ProfileFuniActiveVpiBits_Type()
)
profileFuniActiveVpiBits.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    profileFuniActiveVpiBits.setStatus("current")


class _ProfileFuniActiveVciBits_Type(Integer32):
    """Custom type profileFuniActiveVciBits based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_ProfileFuniActiveVciBits_Type.__name__ = "Integer32"
_ProfileFuniActiveVciBits_Object = MibTableColumn
profileFuniActiveVciBits = _ProfileFuniActiveVciBits_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 3, 1, 14),
    _ProfileFuniActiveVciBits_Type()
)
profileFuniActiveVciBits.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    profileFuniActiveVciBits.setStatus("current")


class _ProfileFuniConfMode_Type(Integer32):
    """Custom type profileFuniConfMode based on Integer32"""
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
        *(("mode1a", 1),
          ("mode1b", 2),
          ("mode3", 3),
          ("mode4", 4))
    )


_ProfileFuniConfMode_Type.__name__ = "Integer32"
_ProfileFuniConfMode_Object = MibTableColumn
profileFuniConfMode = _ProfileFuniConfMode_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 3, 1, 15),
    _ProfileFuniConfMode_Type()
)
profileFuniConfMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    profileFuniConfMode.setStatus("current")


class _ProfileFuniFcsBits_Type(Integer32):
    """Custom type profileFuniFcsBits based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fcsBits16", 1),
          ("fcsBits32", 2))
    )


_ProfileFuniFcsBits_Type.__name__ = "Integer32"
_ProfileFuniFcsBits_Object = MibTableColumn
profileFuniFcsBits = _ProfileFuniFcsBits_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 3, 1, 16),
    _ProfileFuniFcsBits_Type()
)
profileFuniFcsBits.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    profileFuniFcsBits.setStatus("current")


class _ProfileFuniHdrBytes_Type(Integer32):
    """Custom type profileFuniHdrBytes based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hdrBytes2", 1),
          ("hdrBytes4", 2))
    )


_ProfileFuniHdrBytes_Type.__name__ = "Integer32"
_ProfileFuniHdrBytes_Object = MibTableColumn
profileFuniHdrBytes = _ProfileFuniHdrBytes_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 3, 1, 17),
    _ProfileFuniHdrBytes_Type()
)
profileFuniHdrBytes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    profileFuniHdrBytes.setStatus("current")


class _ProfileFuniAal34Support_Type(Integer32):
    """Custom type profileFuniAal34Support based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_ProfileFuniAal34Support_Type.__name__ = "Integer32"
_ProfileFuniAal34Support_Object = MibTableColumn
profileFuniAal34Support = _ProfileFuniAal34Support_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 3, 1, 18),
    _ProfileFuniAal34Support_Type()
)
profileFuniAal34Support.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    profileFuniAal34Support.setStatus("current")


class _ProfileFuniRefCnt_Type(Integer32):
    """Custom type profileFuniRefCnt based on Integer32"""
    defaultValue = 0


_ProfileFuniRefCnt_Object = MibTableColumn
profileFuniRefCnt = _ProfileFuniRefCnt_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 3, 1, 19),
    _ProfileFuniRefCnt_Type()
)
profileFuniRefCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    profileFuniRefCnt.setStatus("current")
_ProfileFrf8Table_Object = MibTable
profileFrf8Table = _ProfileFrf8Table_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 4)
)
if mibBuilder.loadTexts:
    profileFrf8Table.setStatus("current")
_ProfileFrf8Entry_Object = MibTableRow
profileFrf8Entry = _ProfileFrf8Entry_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 4, 1)
)
profileFrf8Entry.setIndexNames(
    (0, "Fore-Profile-MIB", "profileFrf8Index"),
)
if mibBuilder.loadTexts:
    profileFrf8Entry.setStatus("current")
_ProfileFrf8Index_Type = Integer32
_ProfileFrf8Index_Object = MibTableColumn
profileFrf8Index = _ProfileFrf8Index_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 4, 1, 1),
    _ProfileFrf8Index_Type()
)
profileFrf8Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    profileFrf8Index.setStatus("current")
_ProfileFrf8RowStatus_Type = RowStatus
_ProfileFrf8RowStatus_Object = MibTableColumn
profileFrf8RowStatus = _ProfileFrf8RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 4, 1, 2),
    _ProfileFrf8RowStatus_Type()
)
profileFrf8RowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    profileFrf8RowStatus.setStatus("current")
_ProfileFrf8Name_Type = DisplayString
_ProfileFrf8Name_Object = MibTableColumn
profileFrf8Name = _ProfileFrf8Name_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 4, 1, 3),
    _ProfileFrf8Name_Type()
)
profileFrf8Name.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    profileFrf8Name.setStatus("current")


class _ProfileFrf8DeMode_Type(Integer32):
    """Custom type profileFrf8DeMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ignored", 2),
          ("mapped", 1))
    )


_ProfileFrf8DeMode_Type.__name__ = "Integer32"
_ProfileFrf8DeMode_Object = MibTableColumn
profileFrf8DeMode = _ProfileFrf8DeMode_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 4, 1, 4),
    _ProfileFrf8DeMode_Type()
)
profileFrf8DeMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    profileFrf8DeMode.setStatus("current")


class _ProfileFrf8ClpMode_Type(Integer32):
    """Custom type profileFrf8ClpMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ignored", 2),
          ("mapped", 1))
    )


_ProfileFrf8ClpMode_Type.__name__ = "Integer32"
_ProfileFrf8ClpMode_Object = MibTableColumn
profileFrf8ClpMode = _ProfileFrf8ClpMode_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 4, 1, 5),
    _ProfileFrf8ClpMode_Type()
)
profileFrf8ClpMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    profileFrf8ClpMode.setStatus("current")


class _ProfileFrf8FecnMode_Type(Integer32):
    """Custom type profileFrf8FecnMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ignored", 2),
          ("mapped", 1))
    )


_ProfileFrf8FecnMode_Type.__name__ = "Integer32"
_ProfileFrf8FecnMode_Object = MibTableColumn
profileFrf8FecnMode = _ProfileFrf8FecnMode_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 4, 1, 6),
    _ProfileFrf8FecnMode_Type()
)
profileFrf8FecnMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    profileFrf8FecnMode.setStatus("current")


class _ProfileFrf8DefaultDe_Type(Integer32):
    """Custom type profileFrf8DefaultDe based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ProfileFrf8DefaultDe_Type.__name__ = "Integer32"
_ProfileFrf8DefaultDe_Object = MibTableColumn
profileFrf8DefaultDe = _ProfileFrf8DefaultDe_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 4, 1, 7),
    _ProfileFrf8DefaultDe_Type()
)
profileFrf8DefaultDe.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    profileFrf8DefaultDe.setStatus("current")


class _ProfileFrf8DefaultClp_Type(Integer32):
    """Custom type profileFrf8DefaultClp based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ProfileFrf8DefaultClp_Type.__name__ = "Integer32"
_ProfileFrf8DefaultClp_Object = MibTableColumn
profileFrf8DefaultClp = _ProfileFrf8DefaultClp_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 4, 1, 8),
    _ProfileFrf8DefaultClp_Type()
)
profileFrf8DefaultClp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    profileFrf8DefaultClp.setStatus("current")


class _ProfileFrf8Protocols_Type(Integer32):
    """Custom type profileFrf8Protocols based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8191),
    )


_ProfileFrf8Protocols_Type.__name__ = "Integer32"
_ProfileFrf8Protocols_Object = MibTableColumn
profileFrf8Protocols = _ProfileFrf8Protocols_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 4, 1, 9),
    _ProfileFrf8Protocols_Type()
)
profileFrf8Protocols.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    profileFrf8Protocols.setStatus("current")


class _ProfileFrf8RefCnt_Type(Integer32):
    """Custom type profileFrf8RefCnt based on Integer32"""
    defaultValue = 0


_ProfileFrf8RefCnt_Object = MibTableColumn
profileFrf8RefCnt = _ProfileFrf8RefCnt_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 4, 1, 10),
    _ProfileFrf8RefCnt_Type()
)
profileFrf8RefCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    profileFrf8RefCnt.setStatus("current")
_ProfileServiceTable_Object = MibTable
profileServiceTable = _ProfileServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 5)
)
if mibBuilder.loadTexts:
    profileServiceTable.setStatus("current")
_ProfileServiceEntry_Object = MibTableRow
profileServiceEntry = _ProfileServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 5, 1)
)
profileServiceEntry.setIndexNames(
    (0, "Fore-Profile-MIB", "profileServiceIndex"),
)
if mibBuilder.loadTexts:
    profileServiceEntry.setStatus("current")
_ProfileServiceIndex_Type = Integer32
_ProfileServiceIndex_Object = MibTableColumn
profileServiceIndex = _ProfileServiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 5, 1, 1),
    _ProfileServiceIndex_Type()
)
profileServiceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    profileServiceIndex.setStatus("current")
_ProfileServiceRowStatus_Type = RowStatus
_ProfileServiceRowStatus_Object = MibTableColumn
profileServiceRowStatus = _ProfileServiceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 5, 1, 2),
    _ProfileServiceRowStatus_Type()
)
profileServiceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    profileServiceRowStatus.setStatus("current")
_ProfileServiceName_Type = DisplayString
_ProfileServiceName_Object = MibTableColumn
profileServiceName = _ProfileServiceName_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 5, 1, 3),
    _ProfileServiceName_Type()
)
profileServiceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    profileServiceName.setStatus("current")
_ProfileServiceAccRate_Type = Integer32
_ProfileServiceAccRate_Object = MibTableColumn
profileServiceAccRate = _ProfileServiceAccRate_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 5, 1, 4),
    _ProfileServiceAccRate_Type()
)
profileServiceAccRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    profileServiceAccRate.setStatus("current")


class _ProfileServiceMaxVccs_Type(Integer32):
    """Custom type profileServiceMaxVccs based on Integer32"""
    defaultValue = 10


_ProfileServiceMaxVccs_Object = MibTableColumn
profileServiceMaxVccs = _ProfileServiceMaxVccs_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 5, 1, 5),
    _ProfileServiceMaxVccs_Type()
)
profileServiceMaxVccs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    profileServiceMaxVccs.setStatus("current")


class _ProfileServiceMaxPayloadSize_Type(Integer32):
    """Custom type profileServiceMaxPayloadSize based on Integer32"""
    defaultValue = 4096


_ProfileServiceMaxPayloadSize_Object = MibTableColumn
profileServiceMaxPayloadSize = _ProfileServiceMaxPayloadSize_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 5, 1, 6),
    _ProfileServiceMaxPayloadSize_Type()
)
profileServiceMaxPayloadSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    profileServiceMaxPayloadSize.setStatus("current")


class _ProfileServiceInBwOb_Type(Integer32):
    """Custom type profileServiceInBwOb based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 500),
    )


_ProfileServiceInBwOb_Type.__name__ = "Integer32"
_ProfileServiceInBwOb_Object = MibTableColumn
profileServiceInBwOb = _ProfileServiceInBwOb_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 5, 1, 7),
    _ProfileServiceInBwOb_Type()
)
profileServiceInBwOb.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    profileServiceInBwOb.setStatus("current")


class _ProfileServiceOutBwOb_Type(Integer32):
    """Custom type profileServiceOutBwOb based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 500),
    )


_ProfileServiceOutBwOb_Type.__name__ = "Integer32"
_ProfileServiceOutBwOb_Object = MibTableColumn
profileServiceOutBwOb = _ProfileServiceOutBwOb_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 5, 1, 8),
    _ProfileServiceOutBwOb_Type()
)
profileServiceOutBwOb.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    profileServiceOutBwOb.setStatus("current")


class _ProfileServiceRefCnt_Type(Integer32):
    """Custom type profileServiceRefCnt based on Integer32"""
    defaultValue = 0


_ProfileServiceRefCnt_Object = MibTableColumn
profileServiceRefCnt = _ProfileServiceRefCnt_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 5, 1, 9),
    _ProfileServiceRefCnt_Type()
)
profileServiceRefCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    profileServiceRefCnt.setStatus("current")
_ProfileEpdPpdTable_Object = MibTable
profileEpdPpdTable = _ProfileEpdPpdTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 6)
)
if mibBuilder.loadTexts:
    profileEpdPpdTable.setStatus("current")
_ProfileEpdPpdEntry_Object = MibTableRow
profileEpdPpdEntry = _ProfileEpdPpdEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 6, 1)
)
profileEpdPpdEntry.setIndexNames(
    (0, "Fore-Profile-MIB", "profileEpdPpdIndex"),
)
if mibBuilder.loadTexts:
    profileEpdPpdEntry.setStatus("current")
_ProfileEpdPpdIndex_Type = Integer32
_ProfileEpdPpdIndex_Object = MibTableColumn
profileEpdPpdIndex = _ProfileEpdPpdIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 6, 1, 1),
    _ProfileEpdPpdIndex_Type()
)
profileEpdPpdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    profileEpdPpdIndex.setStatus("current")
_ProfileEpdPpdRowStatus_Type = RowStatus
_ProfileEpdPpdRowStatus_Object = MibTableColumn
profileEpdPpdRowStatus = _ProfileEpdPpdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 6, 1, 2),
    _ProfileEpdPpdRowStatus_Type()
)
profileEpdPpdRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    profileEpdPpdRowStatus.setStatus("current")
_ProfileEpdPpdName_Type = DisplayString
_ProfileEpdPpdName_Object = MibTableColumn
profileEpdPpdName = _ProfileEpdPpdName_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 6, 1, 3),
    _ProfileEpdPpdName_Type()
)
profileEpdPpdName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    profileEpdPpdName.setStatus("current")


class _ProfileEpdPpdPriority_Type(Integer32):
    """Custom type profileEpdPpdPriority based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("high", 2),
          ("low", 1))
    )


_ProfileEpdPpdPriority_Type.__name__ = "Integer32"
_ProfileEpdPpdPriority_Object = MibTableColumn
profileEpdPpdPriority = _ProfileEpdPpdPriority_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 6, 1, 4),
    _ProfileEpdPpdPriority_Type()
)
profileEpdPpdPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    profileEpdPpdPriority.setStatus("current")


class _ProfileEpdPpdClp0Epd_Type(Integer32):
    """Custom type profileEpdPpdClp0Epd based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_ProfileEpdPpdClp0Epd_Type.__name__ = "Integer32"
_ProfileEpdPpdClp0Epd_Object = MibTableColumn
profileEpdPpdClp0Epd = _ProfileEpdPpdClp0Epd_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 6, 1, 5),
    _ProfileEpdPpdClp0Epd_Type()
)
profileEpdPpdClp0Epd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    profileEpdPpdClp0Epd.setStatus("current")


class _ProfileEpdPpdClp1Ppd_Type(Integer32):
    """Custom type profileEpdPpdClp1Ppd based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_ProfileEpdPpdClp1Ppd_Type.__name__ = "Integer32"
_ProfileEpdPpdClp1Ppd_Object = MibTableColumn
profileEpdPpdClp1Ppd = _ProfileEpdPpdClp1Ppd_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 6, 1, 6),
    _ProfileEpdPpdClp1Ppd_Type()
)
profileEpdPpdClp1Ppd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    profileEpdPpdClp1Ppd.setStatus("current")


class _ProfileEpdPpdClp1Epd_Type(Integer32):
    """Custom type profileEpdPpdClp1Epd based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_ProfileEpdPpdClp1Epd_Type.__name__ = "Integer32"
_ProfileEpdPpdClp1Epd_Object = MibTableColumn
profileEpdPpdClp1Epd = _ProfileEpdPpdClp1Epd_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 6, 1, 7),
    _ProfileEpdPpdClp1Epd_Type()
)
profileEpdPpdClp1Epd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    profileEpdPpdClp1Epd.setStatus("current")


class _ProfileEpdPpdRefCnt_Type(Integer32):
    """Custom type profileEpdPpdRefCnt based on Integer32"""
    defaultValue = 0


_ProfileEpdPpdRefCnt_Object = MibTableColumn
profileEpdPpdRefCnt = _ProfileEpdPpdRefCnt_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 6, 1, 8),
    _ProfileEpdPpdRefCnt_Type()
)
profileEpdPpdRefCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    profileEpdPpdRefCnt.setStatus("current")
_ProfileFrf5Table_Object = MibTable
profileFrf5Table = _ProfileFrf5Table_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 7)
)
if mibBuilder.loadTexts:
    profileFrf5Table.setStatus("current")
_ProfileFrf5Entry_Object = MibTableRow
profileFrf5Entry = _ProfileFrf5Entry_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 7, 1)
)
profileFrf5Entry.setIndexNames(
    (0, "Fore-Profile-MIB", "profileFrf5Index"),
)
if mibBuilder.loadTexts:
    profileFrf5Entry.setStatus("current")
_ProfileFrf5Index_Type = Integer32
_ProfileFrf5Index_Object = MibTableColumn
profileFrf5Index = _ProfileFrf5Index_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 7, 1, 1),
    _ProfileFrf5Index_Type()
)
profileFrf5Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    profileFrf5Index.setStatus("current")
_ProfileFrf5RowStatus_Type = RowStatus
_ProfileFrf5RowStatus_Object = MibTableColumn
profileFrf5RowStatus = _ProfileFrf5RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 7, 1, 2),
    _ProfileFrf5RowStatus_Type()
)
profileFrf5RowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    profileFrf5RowStatus.setStatus("current")
_ProfileFrf5Name_Type = DisplayString
_ProfileFrf5Name_Object = MibTableColumn
profileFrf5Name = _ProfileFrf5Name_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 7, 1, 3),
    _ProfileFrf5Name_Type()
)
profileFrf5Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    profileFrf5Name.setStatus("current")


class _ProfileFrf5DeMode_Type(Integer32):
    """Custom type profileFrf5DeMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ignored", 2),
          ("mapped", 1))
    )


_ProfileFrf5DeMode_Type.__name__ = "Integer32"
_ProfileFrf5DeMode_Object = MibTableColumn
profileFrf5DeMode = _ProfileFrf5DeMode_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 7, 1, 4),
    _ProfileFrf5DeMode_Type()
)
profileFrf5DeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    profileFrf5DeMode.setStatus("current")


class _ProfileFrf5ClpFrsscsDeMode_Type(Integer32):
    """Custom type profileFrf5ClpFrsscsDeMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ignored", 2),
          ("mapped", 1))
    )


_ProfileFrf5ClpFrsscsDeMode_Type.__name__ = "Integer32"
_ProfileFrf5ClpFrsscsDeMode_Object = MibTableColumn
profileFrf5ClpFrsscsDeMode = _ProfileFrf5ClpFrsscsDeMode_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 7, 1, 5),
    _ProfileFrf5ClpFrsscsDeMode_Type()
)
profileFrf5ClpFrsscsDeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    profileFrf5ClpFrsscsDeMode.setStatus("current")


class _ProfileFrf5DefaultClp_Type(Integer32):
    """Custom type profileFrf5DefaultClp based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ProfileFrf5DefaultClp_Type.__name__ = "Integer32"
_ProfileFrf5DefaultClp_Object = MibTableColumn
profileFrf5DefaultClp = _ProfileFrf5DefaultClp_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 7, 1, 6),
    _ProfileFrf5DefaultClp_Type()
)
profileFrf5DefaultClp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    profileFrf5DefaultClp.setStatus("current")


class _ProfileFrf5MaxDlcis_Type(Integer32):
    """Custom type profileFrf5MaxDlcis based on Integer32"""
    defaultValue = 5


_ProfileFrf5MaxDlcis_Object = MibTableColumn
profileFrf5MaxDlcis = _ProfileFrf5MaxDlcis_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 7, 1, 7),
    _ProfileFrf5MaxDlcis_Type()
)
profileFrf5MaxDlcis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    profileFrf5MaxDlcis.setStatus("current")


class _ProfileFrf5MaxPayloadSize_Type(Integer32):
    """Custom type profileFrf5MaxPayloadSize based on Integer32"""
    defaultValue = 4092


_ProfileFrf5MaxPayloadSize_Object = MibTableColumn
profileFrf5MaxPayloadSize = _ProfileFrf5MaxPayloadSize_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 7, 1, 8),
    _ProfileFrf5MaxPayloadSize_Type()
)
profileFrf5MaxPayloadSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    profileFrf5MaxPayloadSize.setStatus("current")


class _ProfileFrf5RefCnt_Type(Integer32):
    """Custom type profileFrf5RefCnt based on Integer32"""
    defaultValue = 0


_ProfileFrf5RefCnt_Object = MibTableColumn
profileFrf5RefCnt = _ProfileFrf5RefCnt_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 7, 1, 9),
    _ProfileFrf5RefCnt_Type()
)
profileFrf5RefCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    profileFrf5RefCnt.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Fore-Profile-MIB",
    **{"foreProfileModule": foreProfileModule,
       "profileLmiTable": profileLmiTable,
       "profileLmiEntry": profileLmiEntry,
       "profileLmiIndex": profileLmiIndex,
       "profileLmiRowStatus": profileLmiRowStatus,
       "profileLmiName": profileLmiName,
       "profileLmiFlavour": profileLmiFlavour,
       "profileLmiT391": profileLmiT391,
       "profileLmiN391": profileLmiN391,
       "profileLmiT392": profileLmiT392,
       "profileLmiN392": profileLmiN392,
       "profileLmiN393": profileLmiN393,
       "profileLminT3": profileLminT3,
       "profileLmiDirection": profileLmiDirection,
       "profileLmiRole": profileLmiRole,
       "profileLmiRefCnt": profileLmiRefCnt,
       "profileFrRateTable": profileFrRateTable,
       "profileFrRateEntry": profileFrRateEntry,
       "profileFrRateIndex": profileFrRateIndex,
       "profileFrRateRowStatus": profileFrRateRowStatus,
       "profileFrRateName": profileFrRateName,
       "profileFrRateInBc": profileFrRateInBc,
       "profileFrRateInBe": profileFrRateInBe,
       "profileFrRateInCir": profileFrRateInCir,
       "profileFrRateOutBc": profileFrRateOutBc,
       "profileFrRateOutBe": profileFrRateOutBe,
       "profileFrRateOutCir": profileFrRateOutCir,
       "profileFrRateMinBc": profileFrRateMinBc,
       "profileFrRateCmPeriod": profileFrRateCmPeriod,
       "profileFrRateRefCnt": profileFrRateRefCnt,
       "profileFuniTable": profileFuniTable,
       "profileFuniEntry": profileFuniEntry,
       "profileFuniIndex": profileFuniIndex,
       "profileFuniRowStatus": profileFuniRowStatus,
       "profileFuniName": profileFuniName,
       "profileFuniIlmiVpi": profileFuniIlmiVpi,
       "profileFuniIlmiVci": profileFuniIlmiVci,
       "profileFuniSigVpi": profileFuniSigVpi,
       "profileFuniSigVci": profileFuniSigVci,
       "profileFuniMinVci": profileFuniMinVci,
       "profileFuniMaxVci": profileFuniMaxVci,
       "profileFuniIlmiSupport": profileFuniIlmiSupport,
       "profileFuniSigSupport": profileFuniSigSupport,
       "profileFuniOamSupport": profileFuniOamSupport,
       "profileFuniActiveVpiBits": profileFuniActiveVpiBits,
       "profileFuniActiveVciBits": profileFuniActiveVciBits,
       "profileFuniConfMode": profileFuniConfMode,
       "profileFuniFcsBits": profileFuniFcsBits,
       "profileFuniHdrBytes": profileFuniHdrBytes,
       "profileFuniAal34Support": profileFuniAal34Support,
       "profileFuniRefCnt": profileFuniRefCnt,
       "profileFrf8Table": profileFrf8Table,
       "profileFrf8Entry": profileFrf8Entry,
       "profileFrf8Index": profileFrf8Index,
       "profileFrf8RowStatus": profileFrf8RowStatus,
       "profileFrf8Name": profileFrf8Name,
       "profileFrf8DeMode": profileFrf8DeMode,
       "profileFrf8ClpMode": profileFrf8ClpMode,
       "profileFrf8FecnMode": profileFrf8FecnMode,
       "profileFrf8DefaultDe": profileFrf8DefaultDe,
       "profileFrf8DefaultClp": profileFrf8DefaultClp,
       "profileFrf8Protocols": profileFrf8Protocols,
       "profileFrf8RefCnt": profileFrf8RefCnt,
       "profileServiceTable": profileServiceTable,
       "profileServiceEntry": profileServiceEntry,
       "profileServiceIndex": profileServiceIndex,
       "profileServiceRowStatus": profileServiceRowStatus,
       "profileServiceName": profileServiceName,
       "profileServiceAccRate": profileServiceAccRate,
       "profileServiceMaxVccs": profileServiceMaxVccs,
       "profileServiceMaxPayloadSize": profileServiceMaxPayloadSize,
       "profileServiceInBwOb": profileServiceInBwOb,
       "profileServiceOutBwOb": profileServiceOutBwOb,
       "profileServiceRefCnt": profileServiceRefCnt,
       "profileEpdPpdTable": profileEpdPpdTable,
       "profileEpdPpdEntry": profileEpdPpdEntry,
       "profileEpdPpdIndex": profileEpdPpdIndex,
       "profileEpdPpdRowStatus": profileEpdPpdRowStatus,
       "profileEpdPpdName": profileEpdPpdName,
       "profileEpdPpdPriority": profileEpdPpdPriority,
       "profileEpdPpdClp0Epd": profileEpdPpdClp0Epd,
       "profileEpdPpdClp1Ppd": profileEpdPpdClp1Ppd,
       "profileEpdPpdClp1Epd": profileEpdPpdClp1Epd,
       "profileEpdPpdRefCnt": profileEpdPpdRefCnt,
       "profileFrf5Table": profileFrf5Table,
       "profileFrf5Entry": profileFrf5Entry,
       "profileFrf5Index": profileFrf5Index,
       "profileFrf5RowStatus": profileFrf5RowStatus,
       "profileFrf5Name": profileFrf5Name,
       "profileFrf5DeMode": profileFrf5DeMode,
       "profileFrf5ClpFrsscsDeMode": profileFrf5ClpFrsscsDeMode,
       "profileFrf5DefaultClp": profileFrf5DefaultClp,
       "profileFrf5MaxDlcis": profileFrf5MaxDlcis,
       "profileFrf5MaxPayloadSize": profileFrf5MaxPayloadSize,
       "profileFrf5RefCnt": profileFrf5RefCnt}
)
