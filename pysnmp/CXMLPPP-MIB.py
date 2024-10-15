# SNMP MIB module (CXMLPPP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CXMLPPP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:20:41 2024
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
 cxMLPPP) = mibBuilder.importSymbols(
    "CXProduct-SMI",
    "Alias",
    "SapIndex",
    "cxMLPPP")

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



class _MlpppNbSmallBufs_Type(Integer32):
    """Custom type mlpppNbSmallBufs based on Integer32"""
    defaultValue = 1


_MlpppNbSmallBufs_Object = MibScalar
mlpppNbSmallBufs = _MlpppNbSmallBufs_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 49, 1),
    _MlpppNbSmallBufs_Type()
)
mlpppNbSmallBufs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mlpppNbSmallBufs.setStatus("mandatory")


class _MlpppSmallBufSize_Type(Integer32):
    """Custom type mlpppSmallBufSize based on Integer32"""
    defaultValue = 128


_MlpppSmallBufSize_Object = MibScalar
mlpppSmallBufSize = _MlpppSmallBufSize_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 49, 2),
    _MlpppSmallBufSize_Type()
)
mlpppSmallBufSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mlpppSmallBufSize.setStatus("mandatory")


class _MlpppNbLargeBufs_Type(Integer32):
    """Custom type mlpppNbLargeBufs based on Integer32"""
    defaultValue = 1


_MlpppNbLargeBufs_Object = MibScalar
mlpppNbLargeBufs = _MlpppNbLargeBufs_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 49, 3),
    _MlpppNbLargeBufs_Type()
)
mlpppNbLargeBufs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mlpppNbLargeBufs.setStatus("mandatory")


class _MlpppLargeBufSize_Type(Integer32):
    """Custom type mlpppLargeBufSize based on Integer32"""
    defaultValue = 1600


_MlpppLargeBufSize_Object = MibScalar
mlpppLargeBufSize = _MlpppLargeBufSize_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 49, 4),
    _MlpppLargeBufSize_Type()
)
mlpppLargeBufSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mlpppLargeBufSize.setStatus("mandatory")


class _MlpppSoftwareVersion_Type(DisplayString):
    """Custom type mlpppSoftwareVersion based on DisplayString"""
    defaultValue = OctetString("1.00")


_MlpppSoftwareVersion_Object = MibScalar
mlpppSoftwareVersion = _MlpppSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 49, 40),
    _MlpppSoftwareVersion_Type()
)
mlpppSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlpppSoftwareVersion.setStatus("mandatory")


class _MlpppNbActiveUSap_Type(Integer32):
    """Custom type mlpppNbActiveUSap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MlpppNbActiveUSap_Type.__name__ = "Integer32"
_MlpppNbActiveUSap_Object = MibScalar
mlpppNbActiveUSap = _MlpppNbActiveUSap_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 49, 41),
    _MlpppNbActiveUSap_Type()
)
mlpppNbActiveUSap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlpppNbActiveUSap.setStatus("mandatory")


class _MlpppNbActiveLSap_Type(Integer32):
    """Custom type mlpppNbActiveLSap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MlpppNbActiveLSap_Type.__name__ = "Integer32"
_MlpppNbActiveLSap_Object = MibScalar
mlpppNbActiveLSap = _MlpppNbActiveLSap_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 49, 42),
    _MlpppNbActiveLSap_Type()
)
mlpppNbActiveLSap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlpppNbActiveLSap.setStatus("mandatory")


class _MlpppNbActiveBundle_Type(Integer32):
    """Custom type mlpppNbActiveBundle based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MlpppNbActiveBundle_Type.__name__ = "Integer32"
_MlpppNbActiveBundle_Object = MibScalar
mlpppNbActiveBundle = _MlpppNbActiveBundle_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 49, 43),
    _MlpppNbActiveBundle_Type()
)
mlpppNbActiveBundle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlpppNbActiveBundle.setStatus("mandatory")
_MlpppNbSmallBufsFree_Type = Integer32
_MlpppNbSmallBufsFree_Object = MibScalar
mlpppNbSmallBufsFree = _MlpppNbSmallBufsFree_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 49, 44),
    _MlpppNbSmallBufsFree_Type()
)
mlpppNbSmallBufsFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlpppNbSmallBufsFree.setStatus("mandatory")
_MlpppNbLargeBufsFree_Type = Integer32
_MlpppNbLargeBufsFree_Object = MibScalar
mlpppNbLargeBufsFree = _MlpppNbLargeBufsFree_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 49, 45),
    _MlpppNbLargeBufsFree_Type()
)
mlpppNbLargeBufsFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlpppNbLargeBufsFree.setStatus("mandatory")
_MlpppMibLevel_Type = Integer32
_MlpppMibLevel_Object = MibScalar
mlpppMibLevel = _MlpppMibLevel_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 49, 49),
    _MlpppMibLevel_Type()
)
mlpppMibLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlpppMibLevel.setStatus("mandatory")
_MlpppLSapTable_Object = MibTable
mlpppLSapTable = _MlpppLSapTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 49, 50)
)
if mibBuilder.loadTexts:
    mlpppLSapTable.setStatus("mandatory")
_MlpppLSapEntry_Object = MibTableRow
mlpppLSapEntry = _MlpppLSapEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 49, 50, 1)
)
mlpppLSapEntry.setIndexNames(
    (0, "CXMLPPP-MIB", "mlpppLSapNumber"),
)
if mibBuilder.loadTexts:
    mlpppLSapEntry.setStatus("mandatory")
_MlpppLSapNumber_Type = SapIndex
_MlpppLSapNumber_Object = MibTableColumn
mlpppLSapNumber = _MlpppLSapNumber_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 49, 50, 1, 1),
    _MlpppLSapNumber_Type()
)
mlpppLSapNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlpppLSapNumber.setStatus("mandatory")


class _MlpppLSapRowStatus_Type(Integer32):
    """Custom type mlpppLSapRowStatus based on Integer32"""
    defaultValue = 1

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


_MlpppLSapRowStatus_Type.__name__ = "Integer32"
_MlpppLSapRowStatus_Object = MibTableColumn
mlpppLSapRowStatus = _MlpppLSapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 49, 50, 1, 2),
    _MlpppLSapRowStatus_Type()
)
mlpppLSapRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mlpppLSapRowStatus.setStatus("mandatory")
_MlpppLSapAlias_Type = Alias
_MlpppLSapAlias_Object = MibTableColumn
mlpppLSapAlias = _MlpppLSapAlias_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 49, 50, 1, 3),
    _MlpppLSapAlias_Type()
)
mlpppLSapAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mlpppLSapAlias.setStatus("mandatory")
_MlpppLSapCompanionAlias_Type = Alias
_MlpppLSapCompanionAlias_Object = MibTableColumn
mlpppLSapCompanionAlias = _MlpppLSapCompanionAlias_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 49, 50, 1, 4),
    _MlpppLSapCompanionAlias_Type()
)
mlpppLSapCompanionAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mlpppLSapCompanionAlias.setStatus("mandatory")


class _MlpppLSapDialEntry_Type(Integer32):
    """Custom type mlpppLSapDialEntry based on Integer32"""
    defaultValue = 1


_MlpppLSapDialEntry_Object = MibTableColumn
mlpppLSapDialEntry = _MlpppLSapDialEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 49, 50, 1, 12),
    _MlpppLSapDialEntry_Type()
)
mlpppLSapDialEntry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mlpppLSapDialEntry.setStatus("mandatory")


class _MlpppLSapLcInitialMRU_Type(Integer32):
    """Custom type mlpppLSapLcInitialMRU based on Integer32"""
    defaultValue = 1500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MlpppLSapLcInitialMRU_Type.__name__ = "Integer32"
_MlpppLSapLcInitialMRU_Object = MibTableColumn
mlpppLSapLcInitialMRU = _MlpppLSapLcInitialMRU_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 49, 50, 1, 14),
    _MlpppLSapLcInitialMRU_Type()
)
mlpppLSapLcInitialMRU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mlpppLSapLcInitialMRU.setStatus("mandatory")


class _MlpppLSapLcTransmitACCMap_Type(DisplayString):
    """Custom type mlpppLSapLcTransmitACCMap based on DisplayString"""
    defaultValue = OctetString("FFFFFFFF")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_MlpppLSapLcTransmitACCMap_Type.__name__ = "DisplayString"
_MlpppLSapLcTransmitACCMap_Object = MibTableColumn
mlpppLSapLcTransmitACCMap = _MlpppLSapLcTransmitACCMap_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 49, 50, 1, 15),
    _MlpppLSapLcTransmitACCMap_Type()
)
mlpppLSapLcTransmitACCMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mlpppLSapLcTransmitACCMap.setStatus("mandatory")


class _MlpppLSapLcMaxConfigure_Type(Integer32):
    """Custom type mlpppLSapLcMaxConfigure based on Integer32"""
    defaultValue = 10


_MlpppLSapLcMaxConfigure_Object = MibTableColumn
mlpppLSapLcMaxConfigure = _MlpppLSapLcMaxConfigure_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 49, 50, 1, 16),
    _MlpppLSapLcMaxConfigure_Type()
)
mlpppLSapLcMaxConfigure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mlpppLSapLcMaxConfigure.setStatus("mandatory")


class _MlpppLSapLcMaxTerminate_Type(Integer32):
    """Custom type mlpppLSapLcMaxTerminate based on Integer32"""
    defaultValue = 2


_MlpppLSapLcMaxTerminate_Object = MibTableColumn
mlpppLSapLcMaxTerminate = _MlpppLSapLcMaxTerminate_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 49, 50, 1, 17),
    _MlpppLSapLcMaxTerminate_Type()
)
mlpppLSapLcMaxTerminate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mlpppLSapLcMaxTerminate.setStatus("mandatory")


class _MlpppLSapLcMaxFailure_Type(Integer32):
    """Custom type mlpppLSapLcMaxFailure based on Integer32"""
    defaultValue = 5


_MlpppLSapLcMaxFailure_Object = MibTableColumn
mlpppLSapLcMaxFailure = _MlpppLSapLcMaxFailure_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 49, 50, 1, 18),
    _MlpppLSapLcMaxFailure_Type()
)
mlpppLSapLcMaxFailure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mlpppLSapLcMaxFailure.setStatus("mandatory")


class _MlpppLSapLcRestartTimer_Type(Integer32):
    """Custom type mlpppLSapLcRestartTimer based on Integer32"""
    defaultValue = 3


_MlpppLSapLcRestartTimer_Object = MibTableColumn
mlpppLSapLcRestartTimer = _MlpppLSapLcRestartTimer_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 49, 50, 1, 19),
    _MlpppLSapLcRestartTimer_Type()
)
mlpppLSapLcRestartTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mlpppLSapLcRestartTimer.setStatus("mandatory")


class _MlpppLSapLcProtFieldComp_Type(Integer32):
    """Custom type mlpppLSapLcProtFieldComp based on Integer32"""
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


_MlpppLSapLcProtFieldComp_Type.__name__ = "Integer32"
_MlpppLSapLcProtFieldComp_Object = MibTableColumn
mlpppLSapLcProtFieldComp = _MlpppLSapLcProtFieldComp_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 49, 50, 1, 20),
    _MlpppLSapLcProtFieldComp_Type()
)
mlpppLSapLcProtFieldComp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mlpppLSapLcProtFieldComp.setStatus("mandatory")


class _MlpppLSapLcACFieldComp_Type(Integer32):
    """Custom type mlpppLSapLcACFieldComp based on Integer32"""
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


_MlpppLSapLcACFieldComp_Type.__name__ = "Integer32"
_MlpppLSapLcACFieldComp_Object = MibTableColumn
mlpppLSapLcACFieldComp = _MlpppLSapLcACFieldComp_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 49, 50, 1, 21),
    _MlpppLSapLcACFieldComp_Type()
)
mlpppLSapLcACFieldComp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mlpppLSapLcACFieldComp.setStatus("mandatory")


class _MlpppLSapLcMagicNumber_Type(Integer32):
    """Custom type mlpppLSapLcMagicNumber based on Integer32"""
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


_MlpppLSapLcMagicNumber_Type.__name__ = "Integer32"
_MlpppLSapLcMagicNumber_Object = MibTableColumn
mlpppLSapLcMagicNumber = _MlpppLSapLcMagicNumber_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 49, 50, 1, 22),
    _MlpppLSapLcMagicNumber_Type()
)
mlpppLSapLcMagicNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mlpppLSapLcMagicNumber.setStatus("mandatory")


class _MlpppLSapLinkControl_Type(Integer32):
    """Custom type mlpppLSapLinkControl based on Integer32"""
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
        *(("disable", 2),
          ("enable", 1),
          ("start", 4),
          ("stop", 3))
    )


_MlpppLSapLinkControl_Type.__name__ = "Integer32"
_MlpppLSapLinkControl_Object = MibTableColumn
mlpppLSapLinkControl = _MlpppLSapLinkControl_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 49, 50, 1, 23),
    _MlpppLSapLinkControl_Type()
)
mlpppLSapLinkControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mlpppLSapLinkControl.setStatus("mandatory")
_MlpppLSapClearStats_Type = Integer32
_MlpppLSapClearStats_Object = MibTableColumn
mlpppLSapClearStats = _MlpppLSapClearStats_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 49, 50, 1, 30),
    _MlpppLSapClearStats_Type()
)
mlpppLSapClearStats.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mlpppLSapClearStats.setStatus("mandatory")


class _MlpppLSapState_Type(Integer32):
    """Custom type mlpppLSapState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bound", 3),
          ("not-used", 1),
          ("unbound", 2))
    )


_MlpppLSapState_Type.__name__ = "Integer32"
_MlpppLSapState_Object = MibTableColumn
mlpppLSapState = _MlpppLSapState_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 49, 50, 1, 40),
    _MlpppLSapState_Type()
)
mlpppLSapState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlpppLSapState.setStatus("mandatory")


class _MlpppLSapPhysNetStatus_Type(Integer32):
    """Custom type mlpppLSapPhysNetStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pif-attached", 1),
          ("pif-detached", 2))
    )


_MlpppLSapPhysNetStatus_Type.__name__ = "Integer32"
_MlpppLSapPhysNetStatus_Object = MibTableColumn
mlpppLSapPhysNetStatus = _MlpppLSapPhysNetStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 49, 50, 1, 41),
    _MlpppLSapPhysNetStatus_Type()
)
mlpppLSapPhysNetStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlpppLSapPhysNetStatus.setStatus("mandatory")


class _MlpppLSapVirtNetStatus_Type(Integer32):
    """Custom type mlpppLSapVirtNetStatus based on Integer32"""
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
        *(("vif-attached", 1),
          ("vif-detached", 2),
          ("vif-down", 4),
          ("vif-finished", 5),
          ("vif-up", 3))
    )


_MlpppLSapVirtNetStatus_Type.__name__ = "Integer32"
_MlpppLSapVirtNetStatus_Object = MibTableColumn
mlpppLSapVirtNetStatus = _MlpppLSapVirtNetStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 49, 50, 1, 42),
    _MlpppLSapVirtNetStatus_Type()
)
mlpppLSapVirtNetStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlpppLSapVirtNetStatus.setStatus("mandatory")
_MlpppLSapLsBadAddresses_Type = Counter32
_MlpppLSapLsBadAddresses_Object = MibTableColumn
mlpppLSapLsBadAddresses = _MlpppLSapLsBadAddresses_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 49, 50, 1, 43),
    _MlpppLSapLsBadAddresses_Type()
)
mlpppLSapLsBadAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlpppLSapLsBadAddresses.setStatus("mandatory")
_MlpppLSapLsBadControls_Type = Counter32
_MlpppLSapLsBadControls_Object = MibTableColumn
mlpppLSapLsBadControls = _MlpppLSapLsBadControls_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 49, 50, 1, 44),
    _MlpppLSapLsBadControls_Type()
)
mlpppLSapLsBadControls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlpppLSapLsBadControls.setStatus("mandatory")
_MlpppLSapLsPacketTooLongs_Type = Counter32
_MlpppLSapLsPacketTooLongs_Object = MibTableColumn
mlpppLSapLsPacketTooLongs = _MlpppLSapLsPacketTooLongs_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 49, 50, 1, 45),
    _MlpppLSapLsPacketTooLongs_Type()
)
mlpppLSapLsPacketTooLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlpppLSapLsPacketTooLongs.setStatus("mandatory")
_MlpppLSapLsBadFCSs_Type = Counter32
_MlpppLSapLsBadFCSs_Object = MibTableColumn
mlpppLSapLsBadFCSs = _MlpppLSapLsBadFCSs_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 49, 50, 1, 46),
    _MlpppLSapLsBadFCSs_Type()
)
mlpppLSapLsBadFCSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlpppLSapLsBadFCSs.setStatus("mandatory")


class _MlpppLSapLsLocalMRU_Type(Integer32):
    """Custom type mlpppLSapLsLocalMRU based on Integer32"""
    defaultValue = 1500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483648),
    )


_MlpppLSapLsLocalMRU_Type.__name__ = "Integer32"
_MlpppLSapLsLocalMRU_Object = MibTableColumn
mlpppLSapLsLocalMRU = _MlpppLSapLsLocalMRU_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 49, 50, 1, 47),
    _MlpppLSapLsLocalMRU_Type()
)
mlpppLSapLsLocalMRU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlpppLSapLsLocalMRU.setStatus("mandatory")


class _MlpppLSapLsRemoteMRU_Type(Integer32):
    """Custom type mlpppLSapLsRemoteMRU based on Integer32"""
    defaultValue = 1500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483648),
    )


_MlpppLSapLsRemoteMRU_Type.__name__ = "Integer32"
_MlpppLSapLsRemoteMRU_Object = MibTableColumn
mlpppLSapLsRemoteMRU = _MlpppLSapLsRemoteMRU_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 49, 50, 1, 48),
    _MlpppLSapLsRemoteMRU_Type()
)
mlpppLSapLsRemoteMRU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlpppLSapLsRemoteMRU.setStatus("mandatory")


class _MlpppLSapLsLocalToPeerACCMap_Type(DisplayString):
    """Custom type mlpppLSapLsLocalToPeerACCMap based on DisplayString"""
    defaultValue = OctetString("FFFFFFFF")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_MlpppLSapLsLocalToPeerACCMap_Type.__name__ = "DisplayString"
_MlpppLSapLsLocalToPeerACCMap_Object = MibTableColumn
mlpppLSapLsLocalToPeerACCMap = _MlpppLSapLsLocalToPeerACCMap_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 49, 50, 1, 49),
    _MlpppLSapLsLocalToPeerACCMap_Type()
)
mlpppLSapLsLocalToPeerACCMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlpppLSapLsLocalToPeerACCMap.setStatus("mandatory")


class _MlpppLSapLsPeerToLocalACCMap_Type(DisplayString):
    """Custom type mlpppLSapLsPeerToLocalACCMap based on DisplayString"""
    defaultValue = OctetString("FFFFFFFF")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_MlpppLSapLsPeerToLocalACCMap_Type.__name__ = "DisplayString"
_MlpppLSapLsPeerToLocalACCMap_Object = MibTableColumn
mlpppLSapLsPeerToLocalACCMap = _MlpppLSapLsPeerToLocalACCMap_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 49, 50, 1, 50),
    _MlpppLSapLsPeerToLocalACCMap_Type()
)
mlpppLSapLsPeerToLocalACCMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlpppLSapLsPeerToLocalACCMap.setStatus("mandatory")


class _MlpppLSapLsLocalToRemoteProtComp_Type(Integer32):
    """Custom type mlpppLSapLsLocalToRemoteProtComp based on Integer32"""
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


_MlpppLSapLsLocalToRemoteProtComp_Type.__name__ = "Integer32"
_MlpppLSapLsLocalToRemoteProtComp_Object = MibTableColumn
mlpppLSapLsLocalToRemoteProtComp = _MlpppLSapLsLocalToRemoteProtComp_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 49, 50, 1, 51),
    _MlpppLSapLsLocalToRemoteProtComp_Type()
)
mlpppLSapLsLocalToRemoteProtComp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlpppLSapLsLocalToRemoteProtComp.setStatus("mandatory")


class _MlpppLSapLsRemoteToLocalProtComp_Type(Integer32):
    """Custom type mlpppLSapLsRemoteToLocalProtComp based on Integer32"""
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


_MlpppLSapLsRemoteToLocalProtComp_Type.__name__ = "Integer32"
_MlpppLSapLsRemoteToLocalProtComp_Object = MibTableColumn
mlpppLSapLsRemoteToLocalProtComp = _MlpppLSapLsRemoteToLocalProtComp_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 49, 50, 1, 52),
    _MlpppLSapLsRemoteToLocalProtComp_Type()
)
mlpppLSapLsRemoteToLocalProtComp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlpppLSapLsRemoteToLocalProtComp.setStatus("mandatory")


class _MlpppLSapLsLocalToRemoteACComp_Type(Integer32):
    """Custom type mlpppLSapLsLocalToRemoteACComp based on Integer32"""
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


_MlpppLSapLsLocalToRemoteACComp_Type.__name__ = "Integer32"
_MlpppLSapLsLocalToRemoteACComp_Object = MibTableColumn
mlpppLSapLsLocalToRemoteACComp = _MlpppLSapLsLocalToRemoteACComp_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 49, 50, 1, 53),
    _MlpppLSapLsLocalToRemoteACComp_Type()
)
mlpppLSapLsLocalToRemoteACComp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlpppLSapLsLocalToRemoteACComp.setStatus("mandatory")


class _MlpppLSapLsRemoteToLocalACComp_Type(Integer32):
    """Custom type mlpppLSapLsRemoteToLocalACComp based on Integer32"""
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


_MlpppLSapLsRemoteToLocalACComp_Type.__name__ = "Integer32"
_MlpppLSapLsRemoteToLocalACComp_Object = MibTableColumn
mlpppLSapLsRemoteToLocalACComp = _MlpppLSapLsRemoteToLocalACComp_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 49, 50, 1, 54),
    _MlpppLSapLsRemoteToLocalACComp_Type()
)
mlpppLSapLsRemoteToLocalACComp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlpppLSapLsRemoteToLocalACComp.setStatus("mandatory")
_MlpppLSapNbBytesSent_Type = Counter32
_MlpppLSapNbBytesSent_Object = MibTableColumn
mlpppLSapNbBytesSent = _MlpppLSapNbBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 49, 50, 1, 70),
    _MlpppLSapNbBytesSent_Type()
)
mlpppLSapNbBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlpppLSapNbBytesSent.setStatus("mandatory")
_MlpppLSapNbBytesReceived_Type = Counter32
_MlpppLSapNbBytesReceived_Object = MibTableColumn
mlpppLSapNbBytesReceived = _MlpppLSapNbBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 49, 50, 1, 71),
    _MlpppLSapNbBytesReceived_Type()
)
mlpppLSapNbBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlpppLSapNbBytesReceived.setStatus("mandatory")


class _MlpppLSapLinkUSapNumber_Type(Integer32):
    """Custom type mlpppLSapLinkUSapNumber based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MlpppLSapLinkUSapNumber_Type.__name__ = "Integer32"
_MlpppLSapLinkUSapNumber_Object = MibTableColumn
mlpppLSapLinkUSapNumber = _MlpppLSapLinkUSapNumber_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 49, 50, 1, 100),
    _MlpppLSapLinkUSapNumber_Type()
)
mlpppLSapLinkUSapNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mlpppLSapLinkUSapNumber.setStatus("mandatory")
_MlpppUSapTable_Object = MibTable
mlpppUSapTable = _MlpppUSapTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 49, 51)
)
if mibBuilder.loadTexts:
    mlpppUSapTable.setStatus("mandatory")
_MlpppUSapEntry_Object = MibTableRow
mlpppUSapEntry = _MlpppUSapEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 49, 51, 1)
)
mlpppUSapEntry.setIndexNames(
    (0, "CXMLPPP-MIB", "mlpppUSapNumber"),
)
if mibBuilder.loadTexts:
    mlpppUSapEntry.setStatus("mandatory")
_MlpppUSapNumber_Type = SapIndex
_MlpppUSapNumber_Object = MibTableColumn
mlpppUSapNumber = _MlpppUSapNumber_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 49, 51, 1, 1),
    _MlpppUSapNumber_Type()
)
mlpppUSapNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlpppUSapNumber.setStatus("mandatory")


class _MlpppUSapRowStatus_Type(Integer32):
    """Custom type mlpppUSapRowStatus based on Integer32"""
    defaultValue = 1

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


_MlpppUSapRowStatus_Type.__name__ = "Integer32"
_MlpppUSapRowStatus_Object = MibTableColumn
mlpppUSapRowStatus = _MlpppUSapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 49, 51, 1, 2),
    _MlpppUSapRowStatus_Type()
)
mlpppUSapRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mlpppUSapRowStatus.setStatus("mandatory")
_MlpppUSapAlias_Type = Alias
_MlpppUSapAlias_Object = MibTableColumn
mlpppUSapAlias = _MlpppUSapAlias_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 49, 51, 1, 3),
    _MlpppUSapAlias_Type()
)
mlpppUSapAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mlpppUSapAlias.setStatus("mandatory")


class _MlpppUSapLcInitialMRRU_Type(Integer32):
    """Custom type mlpppUSapLcInitialMRRU based on Integer32"""
    defaultValue = 1500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MlpppUSapLcInitialMRRU_Type.__name__ = "Integer32"
_MlpppUSapLcInitialMRRU_Object = MibTableColumn
mlpppUSapLcInitialMRRU = _MlpppUSapLcInitialMRRU_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 49, 51, 1, 20),
    _MlpppUSapLcInitialMRRU_Type()
)
mlpppUSapLcInitialMRRU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mlpppUSapLcInitialMRRU.setStatus("mandatory")


class _MlpppUSapLcSeqFieldComp_Type(Integer32):
    """Custom type mlpppUSapLcSeqFieldComp based on Integer32"""
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


_MlpppUSapLcSeqFieldComp_Type.__name__ = "Integer32"
_MlpppUSapLcSeqFieldComp_Object = MibTableColumn
mlpppUSapLcSeqFieldComp = _MlpppUSapLcSeqFieldComp_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 49, 51, 1, 21),
    _MlpppUSapLcSeqFieldComp_Type()
)
mlpppUSapLcSeqFieldComp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mlpppUSapLcSeqFieldComp.setStatus("mandatory")


class _MlpppUSapLcUseBACP_Type(Integer32):
    """Custom type mlpppUSapLcUseBACP based on Integer32"""
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


_MlpppUSapLcUseBACP_Type.__name__ = "Integer32"
_MlpppUSapLcUseBACP_Object = MibTableColumn
mlpppUSapLcUseBACP = _MlpppUSapLcUseBACP_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 49, 51, 1, 22),
    _MlpppUSapLcUseBACP_Type()
)
mlpppUSapLcUseBACP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mlpppUSapLcUseBACP.setStatus("mandatory")


class _MlpppUSapTransmitWindow_Type(Integer32):
    """Custom type mlpppUSapTransmitWindow based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MlpppUSapTransmitWindow_Type.__name__ = "Integer32"
_MlpppUSapTransmitWindow_Object = MibTableColumn
mlpppUSapTransmitWindow = _MlpppUSapTransmitWindow_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 49, 51, 1, 23),
    _MlpppUSapTransmitWindow_Type()
)
mlpppUSapTransmitWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mlpppUSapTransmitWindow.setStatus("mandatory")


class _MlpppUSapGenerator_Type(Integer32):
    """Custom type mlpppUSapGenerator based on Integer32"""
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
          ("enabled", 2),
          ("enabledos", 3),
          ("retrigger", 4))
    )


_MlpppUSapGenerator_Type.__name__ = "Integer32"
_MlpppUSapGenerator_Object = MibTableColumn
mlpppUSapGenerator = _MlpppUSapGenerator_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 49, 51, 1, 24),
    _MlpppUSapGenerator_Type()
)
mlpppUSapGenerator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mlpppUSapGenerator.setStatus("mandatory")
_MlpppUSapGeneratorLinkUSap_Type = Integer32
_MlpppUSapGeneratorLinkUSap_Object = MibTableColumn
mlpppUSapGeneratorLinkUSap = _MlpppUSapGeneratorLinkUSap_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 49, 51, 1, 25),
    _MlpppUSapGeneratorLinkUSap_Type()
)
mlpppUSapGeneratorLinkUSap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mlpppUSapGeneratorLinkUSap.setStatus("mandatory")


class _MlpppUSapGeneratorFrameSize_Type(Integer32):
    """Custom type mlpppUSapGeneratorFrameSize based on Integer32"""
    defaultValue = 32

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 4096),
    )


_MlpppUSapGeneratorFrameSize_Type.__name__ = "Integer32"
_MlpppUSapGeneratorFrameSize_Object = MibTableColumn
mlpppUSapGeneratorFrameSize = _MlpppUSapGeneratorFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 49, 51, 1, 26),
    _MlpppUSapGeneratorFrameSize_Type()
)
mlpppUSapGeneratorFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mlpppUSapGeneratorFrameSize.setStatus("mandatory")


class _MlpppUSapGeneratorNumberOfFrames_Type(Integer32):
    """Custom type mlpppUSapGeneratorNumberOfFrames based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_MlpppUSapGeneratorNumberOfFrames_Type.__name__ = "Integer32"
_MlpppUSapGeneratorNumberOfFrames_Object = MibTableColumn
mlpppUSapGeneratorNumberOfFrames = _MlpppUSapGeneratorNumberOfFrames_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 49, 51, 1, 27),
    _MlpppUSapGeneratorNumberOfFrames_Type()
)
mlpppUSapGeneratorNumberOfFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mlpppUSapGeneratorNumberOfFrames.setStatus("mandatory")


class _MlpppUSapGeneratorInterFrameDelay_Type(Integer32):
    """Custom type mlpppUSapGeneratorInterFrameDelay based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 60000),
    )


_MlpppUSapGeneratorInterFrameDelay_Type.__name__ = "Integer32"
_MlpppUSapGeneratorInterFrameDelay_Object = MibTableColumn
mlpppUSapGeneratorInterFrameDelay = _MlpppUSapGeneratorInterFrameDelay_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 49, 51, 1, 28),
    _MlpppUSapGeneratorInterFrameDelay_Type()
)
mlpppUSapGeneratorInterFrameDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mlpppUSapGeneratorInterFrameDelay.setStatus("mandatory")


class _MlpppUSapGeneratorFramePriority_Type(Integer32):
    """Custom type mlpppUSapGeneratorFramePriority based on Integer32"""
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
        *(("highpri", 3),
          ("lowpri", 1),
          ("medpri", 2),
          ("veryhighpri", 4))
    )


_MlpppUSapGeneratorFramePriority_Type.__name__ = "Integer32"
_MlpppUSapGeneratorFramePriority_Object = MibTableColumn
mlpppUSapGeneratorFramePriority = _MlpppUSapGeneratorFramePriority_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 49, 51, 1, 29),
    _MlpppUSapGeneratorFramePriority_Type()
)
mlpppUSapGeneratorFramePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mlpppUSapGeneratorFramePriority.setStatus("mandatory")
_MlpppUSapClearStats_Type = Integer32
_MlpppUSapClearStats_Object = MibTableColumn
mlpppUSapClearStats = _MlpppUSapClearStats_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 49, 51, 1, 30),
    _MlpppUSapClearStats_Type()
)
mlpppUSapClearStats.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mlpppUSapClearStats.setStatus("mandatory")


class _MlpppUSapMlpppMode_Type(Integer32):
    """Custom type mlpppUSapMlpppMode based on Integer32"""
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


_MlpppUSapMlpppMode_Type.__name__ = "Integer32"
_MlpppUSapMlpppMode_Object = MibTableColumn
mlpppUSapMlpppMode = _MlpppUSapMlpppMode_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 49, 51, 1, 31),
    _MlpppUSapMlpppMode_Type()
)
mlpppUSapMlpppMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mlpppUSapMlpppMode.setStatus("mandatory")


class _MlpppUSapState_Type(Integer32):
    """Custom type mlpppUSapState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bound", 3),
          ("not-used", 1),
          ("unbound", 2))
    )


_MlpppUSapState_Type.__name__ = "Integer32"
_MlpppUSapState_Object = MibTableColumn
mlpppUSapState = _MlpppUSapState_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 49, 51, 1, 40),
    _MlpppUSapState_Type()
)
mlpppUSapState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlpppUSapState.setStatus("mandatory")


class _MlpppUSapNbPPPLink_Type(Integer32):
    """Custom type mlpppUSapNbPPPLink based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MlpppUSapNbPPPLink_Type.__name__ = "Integer32"
_MlpppUSapNbPPPLink_Object = MibTableColumn
mlpppUSapNbPPPLink = _MlpppUSapNbPPPLink_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 49, 51, 1, 41),
    _MlpppUSapNbPPPLink_Type()
)
mlpppUSapNbPPPLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlpppUSapNbPPPLink.setStatus("mandatory")


class _MlpppUSapLsLocalMRRU_Type(Integer32):
    """Custom type mlpppUSapLsLocalMRRU based on Integer32"""
    defaultValue = 1500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483648),
    )


_MlpppUSapLsLocalMRRU_Type.__name__ = "Integer32"
_MlpppUSapLsLocalMRRU_Object = MibTableColumn
mlpppUSapLsLocalMRRU = _MlpppUSapLsLocalMRRU_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 49, 51, 1, 42),
    _MlpppUSapLsLocalMRRU_Type()
)
mlpppUSapLsLocalMRRU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlpppUSapLsLocalMRRU.setStatus("mandatory")


class _MlpppUSapLsRemoteMRRU_Type(Integer32):
    """Custom type mlpppUSapLsRemoteMRRU based on Integer32"""
    defaultValue = 1500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483648),
    )


_MlpppUSapLsRemoteMRRU_Type.__name__ = "Integer32"
_MlpppUSapLsRemoteMRRU_Object = MibTableColumn
mlpppUSapLsRemoteMRRU = _MlpppUSapLsRemoteMRRU_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 49, 51, 1, 43),
    _MlpppUSapLsRemoteMRRU_Type()
)
mlpppUSapLsRemoteMRRU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlpppUSapLsRemoteMRRU.setStatus("mandatory")


class _MlpppUSapLsLocalToRemoteSeqFieldComp_Type(Integer32):
    """Custom type mlpppUSapLsLocalToRemoteSeqFieldComp based on Integer32"""
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


_MlpppUSapLsLocalToRemoteSeqFieldComp_Type.__name__ = "Integer32"
_MlpppUSapLsLocalToRemoteSeqFieldComp_Object = MibTableColumn
mlpppUSapLsLocalToRemoteSeqFieldComp = _MlpppUSapLsLocalToRemoteSeqFieldComp_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 49, 51, 1, 44),
    _MlpppUSapLsLocalToRemoteSeqFieldComp_Type()
)
mlpppUSapLsLocalToRemoteSeqFieldComp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlpppUSapLsLocalToRemoteSeqFieldComp.setStatus("mandatory")


class _MlpppUSapLsRemoteToLocalSeqFieldComp_Type(Integer32):
    """Custom type mlpppUSapLsRemoteToLocalSeqFieldComp based on Integer32"""
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


_MlpppUSapLsRemoteToLocalSeqFieldComp_Type.__name__ = "Integer32"
_MlpppUSapLsRemoteToLocalSeqFieldComp_Object = MibTableColumn
mlpppUSapLsRemoteToLocalSeqFieldComp = _MlpppUSapLsRemoteToLocalSeqFieldComp_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 49, 51, 1, 45),
    _MlpppUSapLsRemoteToLocalSeqFieldComp_Type()
)
mlpppUSapLsRemoteToLocalSeqFieldComp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlpppUSapLsRemoteToLocalSeqFieldComp.setStatus("mandatory")
_MlpppUSapNbPPPLinkUP_Type = Integer32
_MlpppUSapNbPPPLinkUP_Object = MibTableColumn
mlpppUSapNbPPPLinkUP = _MlpppUSapNbPPPLinkUP_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 49, 51, 1, 46),
    _MlpppUSapNbPPPLinkUP_Type()
)
mlpppUSapNbPPPLinkUP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlpppUSapNbPPPLinkUP.setStatus("mandatory")


class _MlpppUsapMlpNcpState_Type(Integer32):
    """Custom type mlpppUsapMlpNcpState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ncp-down", 2),
          ("ncp-na", 3),
          ("ncp-up", 1))
    )


_MlpppUsapMlpNcpState_Type.__name__ = "Integer32"
_MlpppUsapMlpNcpState_Object = MibTableColumn
mlpppUsapMlpNcpState = _MlpppUsapMlpNcpState_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 49, 51, 1, 47),
    _MlpppUsapMlpNcpState_Type()
)
mlpppUsapMlpNcpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlpppUsapMlpNcpState.setStatus("mandatory")


class _MlpppUsapGenNcpState_Type(Integer32):
    """Custom type mlpppUsapGenNcpState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ncp-down", 2),
          ("ncp-na", 3),
          ("ncp-up", 1))
    )


_MlpppUsapGenNcpState_Type.__name__ = "Integer32"
_MlpppUsapGenNcpState_Object = MibTableColumn
mlpppUsapGenNcpState = _MlpppUsapGenNcpState_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 49, 51, 1, 48),
    _MlpppUsapGenNcpState_Type()
)
mlpppUsapGenNcpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlpppUsapGenNcpState.setStatus("mandatory")


class _MlpppUsapBapNcpState_Type(Integer32):
    """Custom type mlpppUsapBapNcpState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ncp-down", 2),
          ("ncp-na", 3),
          ("ncp-up", 1))
    )


_MlpppUsapBapNcpState_Type.__name__ = "Integer32"
_MlpppUsapBapNcpState_Object = MibTableColumn
mlpppUsapBapNcpState = _MlpppUsapBapNcpState_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 49, 51, 1, 49),
    _MlpppUsapBapNcpState_Type()
)
mlpppUsapBapNcpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlpppUsapBapNcpState.setStatus("mandatory")


class _MlpppUsapFrNcpState_Type(Integer32):
    """Custom type mlpppUsapFrNcpState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ncp-down", 2),
          ("ncp-na", 3),
          ("ncp-up", 1))
    )


_MlpppUsapFrNcpState_Type.__name__ = "Integer32"
_MlpppUsapFrNcpState_Object = MibTableColumn
mlpppUsapFrNcpState = _MlpppUsapFrNcpState_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 49, 51, 1, 50),
    _MlpppUsapFrNcpState_Type()
)
mlpppUsapFrNcpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlpppUsapFrNcpState.setStatus("mandatory")


class _MlpppUsapIpNcpState_Type(Integer32):
    """Custom type mlpppUsapIpNcpState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ncp-down", 2),
          ("ncp-na", 3),
          ("ncp-up", 1))
    )


_MlpppUsapIpNcpState_Type.__name__ = "Integer32"
_MlpppUsapIpNcpState_Object = MibTableColumn
mlpppUsapIpNcpState = _MlpppUsapIpNcpState_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 49, 51, 1, 51),
    _MlpppUsapIpNcpState_Type()
)
mlpppUsapIpNcpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlpppUsapIpNcpState.setStatus("mandatory")
_MlpppUSapNbBytesSent_Type = Counter32
_MlpppUSapNbBytesSent_Object = MibTableColumn
mlpppUSapNbBytesSent = _MlpppUSapNbBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 49, 51, 1, 70),
    _MlpppUSapNbBytesSent_Type()
)
mlpppUSapNbBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlpppUSapNbBytesSent.setStatus("mandatory")
_MlpppUSapNbBytesReceived_Type = Counter32
_MlpppUSapNbBytesReceived_Object = MibTableColumn
mlpppUSapNbBytesReceived = _MlpppUSapNbBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 49, 51, 1, 71),
    _MlpppUSapNbBytesReceived_Type()
)
mlpppUSapNbBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlpppUSapNbBytesReceived.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CXMLPPP-MIB",
    **{"mlpppNbSmallBufs": mlpppNbSmallBufs,
       "mlpppSmallBufSize": mlpppSmallBufSize,
       "mlpppNbLargeBufs": mlpppNbLargeBufs,
       "mlpppLargeBufSize": mlpppLargeBufSize,
       "mlpppSoftwareVersion": mlpppSoftwareVersion,
       "mlpppNbActiveUSap": mlpppNbActiveUSap,
       "mlpppNbActiveLSap": mlpppNbActiveLSap,
       "mlpppNbActiveBundle": mlpppNbActiveBundle,
       "mlpppNbSmallBufsFree": mlpppNbSmallBufsFree,
       "mlpppNbLargeBufsFree": mlpppNbLargeBufsFree,
       "mlpppMibLevel": mlpppMibLevel,
       "mlpppLSapTable": mlpppLSapTable,
       "mlpppLSapEntry": mlpppLSapEntry,
       "mlpppLSapNumber": mlpppLSapNumber,
       "mlpppLSapRowStatus": mlpppLSapRowStatus,
       "mlpppLSapAlias": mlpppLSapAlias,
       "mlpppLSapCompanionAlias": mlpppLSapCompanionAlias,
       "mlpppLSapDialEntry": mlpppLSapDialEntry,
       "mlpppLSapLcInitialMRU": mlpppLSapLcInitialMRU,
       "mlpppLSapLcTransmitACCMap": mlpppLSapLcTransmitACCMap,
       "mlpppLSapLcMaxConfigure": mlpppLSapLcMaxConfigure,
       "mlpppLSapLcMaxTerminate": mlpppLSapLcMaxTerminate,
       "mlpppLSapLcMaxFailure": mlpppLSapLcMaxFailure,
       "mlpppLSapLcRestartTimer": mlpppLSapLcRestartTimer,
       "mlpppLSapLcProtFieldComp": mlpppLSapLcProtFieldComp,
       "mlpppLSapLcACFieldComp": mlpppLSapLcACFieldComp,
       "mlpppLSapLcMagicNumber": mlpppLSapLcMagicNumber,
       "mlpppLSapLinkControl": mlpppLSapLinkControl,
       "mlpppLSapClearStats": mlpppLSapClearStats,
       "mlpppLSapState": mlpppLSapState,
       "mlpppLSapPhysNetStatus": mlpppLSapPhysNetStatus,
       "mlpppLSapVirtNetStatus": mlpppLSapVirtNetStatus,
       "mlpppLSapLsBadAddresses": mlpppLSapLsBadAddresses,
       "mlpppLSapLsBadControls": mlpppLSapLsBadControls,
       "mlpppLSapLsPacketTooLongs": mlpppLSapLsPacketTooLongs,
       "mlpppLSapLsBadFCSs": mlpppLSapLsBadFCSs,
       "mlpppLSapLsLocalMRU": mlpppLSapLsLocalMRU,
       "mlpppLSapLsRemoteMRU": mlpppLSapLsRemoteMRU,
       "mlpppLSapLsLocalToPeerACCMap": mlpppLSapLsLocalToPeerACCMap,
       "mlpppLSapLsPeerToLocalACCMap": mlpppLSapLsPeerToLocalACCMap,
       "mlpppLSapLsLocalToRemoteProtComp": mlpppLSapLsLocalToRemoteProtComp,
       "mlpppLSapLsRemoteToLocalProtComp": mlpppLSapLsRemoteToLocalProtComp,
       "mlpppLSapLsLocalToRemoteACComp": mlpppLSapLsLocalToRemoteACComp,
       "mlpppLSapLsRemoteToLocalACComp": mlpppLSapLsRemoteToLocalACComp,
       "mlpppLSapNbBytesSent": mlpppLSapNbBytesSent,
       "mlpppLSapNbBytesReceived": mlpppLSapNbBytesReceived,
       "mlpppLSapLinkUSapNumber": mlpppLSapLinkUSapNumber,
       "mlpppUSapTable": mlpppUSapTable,
       "mlpppUSapEntry": mlpppUSapEntry,
       "mlpppUSapNumber": mlpppUSapNumber,
       "mlpppUSapRowStatus": mlpppUSapRowStatus,
       "mlpppUSapAlias": mlpppUSapAlias,
       "mlpppUSapLcInitialMRRU": mlpppUSapLcInitialMRRU,
       "mlpppUSapLcSeqFieldComp": mlpppUSapLcSeqFieldComp,
       "mlpppUSapLcUseBACP": mlpppUSapLcUseBACP,
       "mlpppUSapTransmitWindow": mlpppUSapTransmitWindow,
       "mlpppUSapGenerator": mlpppUSapGenerator,
       "mlpppUSapGeneratorLinkUSap": mlpppUSapGeneratorLinkUSap,
       "mlpppUSapGeneratorFrameSize": mlpppUSapGeneratorFrameSize,
       "mlpppUSapGeneratorNumberOfFrames": mlpppUSapGeneratorNumberOfFrames,
       "mlpppUSapGeneratorInterFrameDelay": mlpppUSapGeneratorInterFrameDelay,
       "mlpppUSapGeneratorFramePriority": mlpppUSapGeneratorFramePriority,
       "mlpppUSapClearStats": mlpppUSapClearStats,
       "mlpppUSapMlpppMode": mlpppUSapMlpppMode,
       "mlpppUSapState": mlpppUSapState,
       "mlpppUSapNbPPPLink": mlpppUSapNbPPPLink,
       "mlpppUSapLsLocalMRRU": mlpppUSapLsLocalMRRU,
       "mlpppUSapLsRemoteMRRU": mlpppUSapLsRemoteMRRU,
       "mlpppUSapLsLocalToRemoteSeqFieldComp": mlpppUSapLsLocalToRemoteSeqFieldComp,
       "mlpppUSapLsRemoteToLocalSeqFieldComp": mlpppUSapLsRemoteToLocalSeqFieldComp,
       "mlpppUSapNbPPPLinkUP": mlpppUSapNbPPPLinkUP,
       "mlpppUsapMlpNcpState": mlpppUsapMlpNcpState,
       "mlpppUsapGenNcpState": mlpppUsapGenNcpState,
       "mlpppUsapBapNcpState": mlpppUsapBapNcpState,
       "mlpppUsapFrNcpState": mlpppUsapFrNcpState,
       "mlpppUsapIpNcpState": mlpppUsapIpNcpState,
       "mlpppUSapNbBytesSent": mlpppUSapNbBytesSent,
       "mlpppUSapNbBytesReceived": mlpppUSapNbBytesReceived}
)
