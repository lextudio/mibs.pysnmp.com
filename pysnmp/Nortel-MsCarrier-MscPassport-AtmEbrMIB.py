# SNMP MIB module (Nortel-MsCarrier-MscPassport-AtmEbrMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-MsCarrier-MscPassport-AtmEbrMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:31:51 2024
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

(mscAtmIfIndex,
 mscAtmIfVcc,
 mscAtmIfVccIndex,
 mscAtmIfVpc,
 mscAtmIfVpcIndex,
 mscAtmIfVptIndex,
 mscAtmIfVptVcc,
 mscAtmIfVptVccIndex) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-AtmCoreMIB",
    "mscAtmIfIndex",
    "mscAtmIfVcc",
    "mscAtmIfVccIndex",
    "mscAtmIfVpc",
    "mscAtmIfVpcIndex",
    "mscAtmIfVptIndex",
    "mscAtmIfVptVcc",
    "mscAtmIfVptVccIndex")

(mscAtmIfIisp,
 mscAtmIfIispIndex,
 mscAtmIfVptIisp,
 mscAtmIfVptIispIndex) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-AtmIispMIB",
    "mscAtmIfIisp",
    "mscAtmIfIispIndex",
    "mscAtmIfVptIisp",
    "mscAtmIfVptIispIndex")

(mscAtmIfVccSrc,
 mscAtmIfVccSrcIndex,
 mscAtmIfVpcSrc,
 mscAtmIfVpcSrcIndex,
 mscAtmIfVptVccSrc,
 mscAtmIfVptVccSrcIndex) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB",
    "mscAtmIfVccSrc",
    "mscAtmIfVccSrcIndex",
    "mscAtmIfVpcSrc",
    "mscAtmIfVpcSrcIndex",
    "mscAtmIfVptVccSrc",
    "mscAtmIfVptVccSrcIndex")

(mscAtmIfPnni,
 mscAtmIfPnniIndex,
 mscAtmIfVptPnni,
 mscAtmIfVptPnniIndex) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-AtmPnniMIB",
    "mscAtmIfPnni",
    "mscAtmIfPnniIndex",
    "mscAtmIfVptPnni",
    "mscAtmIfVptPnniIndex")

(mscAtmIfUni,
 mscAtmIfUniIndex,
 mscAtmIfVptUni,
 mscAtmIfVptUniIndex) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-AtmUniMIB",
    "mscAtmIfUni",
    "mscAtmIfUniIndex",
    "mscAtmIfVptUni",
    "mscAtmIfVptUniIndex")

(Counter32,
 DisplayString,
 Gauge32,
 RowStatus,
 StorageType) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB",
    "Counter32",
    "DisplayString",
    "Gauge32",
    "RowStatus",
    "StorageType")

(NonReplicated,) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-TextualConventionsMIB",
    "NonReplicated")

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

_MscAtmIfVpcSrcEbrOv_ObjectIdentity = ObjectIdentity
mscAtmIfVpcSrcEbrOv = _MscAtmIfVpcSrcEbrOv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 4, 6, 2)
)
_MscAtmIfVpcSrcEbrOvRowStatusTable_Object = MibTable
mscAtmIfVpcSrcEbrOvRowStatusTable = _MscAtmIfVpcSrcEbrOvRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 4, 6, 2, 1)
)
if mibBuilder.loadTexts:
    mscAtmIfVpcSrcEbrOvRowStatusTable.setStatus("mandatory")
_MscAtmIfVpcSrcEbrOvRowStatusEntry_Object = MibTableRow
mscAtmIfVpcSrcEbrOvRowStatusEntry = _MscAtmIfVpcSrcEbrOvRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 4, 6, 2, 1, 1)
)
mscAtmIfVpcSrcEbrOvRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVpcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscAtmIfVpcSrcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmEbrMIB", "mscAtmIfVpcSrcEbrOvIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVpcSrcEbrOvRowStatusEntry.setStatus("mandatory")
_MscAtmIfVpcSrcEbrOvRowStatus_Type = RowStatus
_MscAtmIfVpcSrcEbrOvRowStatus_Object = MibTableColumn
mscAtmIfVpcSrcEbrOvRowStatus = _MscAtmIfVpcSrcEbrOvRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 4, 6, 2, 1, 1, 1),
    _MscAtmIfVpcSrcEbrOvRowStatus_Type()
)
mscAtmIfVpcSrcEbrOvRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVpcSrcEbrOvRowStatus.setStatus("mandatory")
_MscAtmIfVpcSrcEbrOvComponentName_Type = DisplayString
_MscAtmIfVpcSrcEbrOvComponentName_Object = MibTableColumn
mscAtmIfVpcSrcEbrOvComponentName = _MscAtmIfVpcSrcEbrOvComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 4, 6, 2, 1, 1, 2),
    _MscAtmIfVpcSrcEbrOvComponentName_Type()
)
mscAtmIfVpcSrcEbrOvComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVpcSrcEbrOvComponentName.setStatus("mandatory")
_MscAtmIfVpcSrcEbrOvStorageType_Type = StorageType
_MscAtmIfVpcSrcEbrOvStorageType_Object = MibTableColumn
mscAtmIfVpcSrcEbrOvStorageType = _MscAtmIfVpcSrcEbrOvStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 4, 6, 2, 1, 1, 4),
    _MscAtmIfVpcSrcEbrOvStorageType_Type()
)
mscAtmIfVpcSrcEbrOvStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVpcSrcEbrOvStorageType.setStatus("mandatory")
_MscAtmIfVpcSrcEbrOvIndex_Type = NonReplicated
_MscAtmIfVpcSrcEbrOvIndex_Object = MibTableColumn
mscAtmIfVpcSrcEbrOvIndex = _MscAtmIfVpcSrcEbrOvIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 4, 6, 2, 1, 1, 10),
    _MscAtmIfVpcSrcEbrOvIndex_Type()
)
mscAtmIfVpcSrcEbrOvIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmIfVpcSrcEbrOvIndex.setStatus("mandatory")
_MscAtmIfVpcSrcEbrOvProvTable_Object = MibTable
mscAtmIfVpcSrcEbrOvProvTable = _MscAtmIfVpcSrcEbrOvProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 4, 6, 2, 20)
)
if mibBuilder.loadTexts:
    mscAtmIfVpcSrcEbrOvProvTable.setStatus("mandatory")
_MscAtmIfVpcSrcEbrOvProvEntry_Object = MibTableRow
mscAtmIfVpcSrcEbrOvProvEntry = _MscAtmIfVpcSrcEbrOvProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 4, 6, 2, 20, 1)
)
mscAtmIfVpcSrcEbrOvProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVpcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscAtmIfVpcSrcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmEbrMIB", "mscAtmIfVpcSrcEbrOvIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVpcSrcEbrOvProvEntry.setStatus("mandatory")


class _MscAtmIfVpcSrcEbrOvRecoverySubscribed_Type(Integer32):
    """Custom type mscAtmIfVpcSrcEbrOvRecoverySubscribed based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_MscAtmIfVpcSrcEbrOvRecoverySubscribed_Type.__name__ = "Integer32"
_MscAtmIfVpcSrcEbrOvRecoverySubscribed_Object = MibTableColumn
mscAtmIfVpcSrcEbrOvRecoverySubscribed = _MscAtmIfVpcSrcEbrOvRecoverySubscribed_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 4, 6, 2, 20, 1, 1),
    _MscAtmIfVpcSrcEbrOvRecoverySubscribed_Type()
)
mscAtmIfVpcSrcEbrOvRecoverySubscribed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVpcSrcEbrOvRecoverySubscribed.setStatus("mandatory")


class _MscAtmIfVpcSrcEbrOvOptimizationSubscribed_Type(Integer32):
    """Custom type mscAtmIfVpcSrcEbrOvOptimizationSubscribed based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_MscAtmIfVpcSrcEbrOvOptimizationSubscribed_Type.__name__ = "Integer32"
_MscAtmIfVpcSrcEbrOvOptimizationSubscribed_Object = MibTableColumn
mscAtmIfVpcSrcEbrOvOptimizationSubscribed = _MscAtmIfVpcSrcEbrOvOptimizationSubscribed_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 4, 6, 2, 20, 1, 2),
    _MscAtmIfVpcSrcEbrOvOptimizationSubscribed_Type()
)
mscAtmIfVpcSrcEbrOvOptimizationSubscribed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVpcSrcEbrOvOptimizationSubscribed.setStatus("mandatory")
_MscAtmIfVpcEbrInfo_ObjectIdentity = ObjectIdentity
mscAtmIfVpcEbrInfo = _MscAtmIfVpcEbrInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 4, 11)
)
_MscAtmIfVpcEbrInfoRowStatusTable_Object = MibTable
mscAtmIfVpcEbrInfoRowStatusTable = _MscAtmIfVpcEbrInfoRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 4, 11, 1)
)
if mibBuilder.loadTexts:
    mscAtmIfVpcEbrInfoRowStatusTable.setStatus("mandatory")
_MscAtmIfVpcEbrInfoRowStatusEntry_Object = MibTableRow
mscAtmIfVpcEbrInfoRowStatusEntry = _MscAtmIfVpcEbrInfoRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 4, 11, 1, 1)
)
mscAtmIfVpcEbrInfoRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVpcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmEbrMIB", "mscAtmIfVpcEbrInfoIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVpcEbrInfoRowStatusEntry.setStatus("mandatory")
_MscAtmIfVpcEbrInfoRowStatus_Type = RowStatus
_MscAtmIfVpcEbrInfoRowStatus_Object = MibTableColumn
mscAtmIfVpcEbrInfoRowStatus = _MscAtmIfVpcEbrInfoRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 4, 11, 1, 1, 1),
    _MscAtmIfVpcEbrInfoRowStatus_Type()
)
mscAtmIfVpcEbrInfoRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVpcEbrInfoRowStatus.setStatus("mandatory")
_MscAtmIfVpcEbrInfoComponentName_Type = DisplayString
_MscAtmIfVpcEbrInfoComponentName_Object = MibTableColumn
mscAtmIfVpcEbrInfoComponentName = _MscAtmIfVpcEbrInfoComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 4, 11, 1, 1, 2),
    _MscAtmIfVpcEbrInfoComponentName_Type()
)
mscAtmIfVpcEbrInfoComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVpcEbrInfoComponentName.setStatus("mandatory")
_MscAtmIfVpcEbrInfoStorageType_Type = StorageType
_MscAtmIfVpcEbrInfoStorageType_Object = MibTableColumn
mscAtmIfVpcEbrInfoStorageType = _MscAtmIfVpcEbrInfoStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 4, 11, 1, 1, 4),
    _MscAtmIfVpcEbrInfoStorageType_Type()
)
mscAtmIfVpcEbrInfoStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVpcEbrInfoStorageType.setStatus("mandatory")
_MscAtmIfVpcEbrInfoIndex_Type = NonReplicated
_MscAtmIfVpcEbrInfoIndex_Object = MibTableColumn
mscAtmIfVpcEbrInfoIndex = _MscAtmIfVpcEbrInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 4, 11, 1, 1, 10),
    _MscAtmIfVpcEbrInfoIndex_Type()
)
mscAtmIfVpcEbrInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmIfVpcEbrInfoIndex.setStatus("mandatory")
_MscAtmIfVpcEbrInfoOperTable_Object = MibTable
mscAtmIfVpcEbrInfoOperTable = _MscAtmIfVpcEbrInfoOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 4, 11, 30)
)
if mibBuilder.loadTexts:
    mscAtmIfVpcEbrInfoOperTable.setStatus("mandatory")
_MscAtmIfVpcEbrInfoOperEntry_Object = MibTableRow
mscAtmIfVpcEbrInfoOperEntry = _MscAtmIfVpcEbrInfoOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 4, 11, 30, 1)
)
mscAtmIfVpcEbrInfoOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVpcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmEbrMIB", "mscAtmIfVpcEbrInfoIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVpcEbrInfoOperEntry.setStatus("mandatory")


class _MscAtmIfVpcEbrInfoRecoverySubscribed_Type(Integer32):
    """Custom type mscAtmIfVpcEbrInfoRecoverySubscribed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_MscAtmIfVpcEbrInfoRecoverySubscribed_Type.__name__ = "Integer32"
_MscAtmIfVpcEbrInfoRecoverySubscribed_Object = MibTableColumn
mscAtmIfVpcEbrInfoRecoverySubscribed = _MscAtmIfVpcEbrInfoRecoverySubscribed_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 4, 11, 30, 1, 1),
    _MscAtmIfVpcEbrInfoRecoverySubscribed_Type()
)
mscAtmIfVpcEbrInfoRecoverySubscribed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVpcEbrInfoRecoverySubscribed.setStatus("mandatory")


class _MscAtmIfVpcEbrInfoOptimizationSubscribed_Type(Integer32):
    """Custom type mscAtmIfVpcEbrInfoOptimizationSubscribed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_MscAtmIfVpcEbrInfoOptimizationSubscribed_Type.__name__ = "Integer32"
_MscAtmIfVpcEbrInfoOptimizationSubscribed_Object = MibTableColumn
mscAtmIfVpcEbrInfoOptimizationSubscribed = _MscAtmIfVpcEbrInfoOptimizationSubscribed_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 4, 11, 30, 1, 2),
    _MscAtmIfVpcEbrInfoOptimizationSubscribed_Type()
)
mscAtmIfVpcEbrInfoOptimizationSubscribed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVpcEbrInfoOptimizationSubscribed.setStatus("mandatory")


class _MscAtmIfVpcEbrInfoConnectionRecovered_Type(Integer32):
    """Custom type mscAtmIfVpcEbrInfoConnectionRecovered based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_MscAtmIfVpcEbrInfoConnectionRecovered_Type.__name__ = "Integer32"
_MscAtmIfVpcEbrInfoConnectionRecovered_Object = MibTableColumn
mscAtmIfVpcEbrInfoConnectionRecovered = _MscAtmIfVpcEbrInfoConnectionRecovered_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 4, 11, 30, 1, 3),
    _MscAtmIfVpcEbrInfoConnectionRecovered_Type()
)
mscAtmIfVpcEbrInfoConnectionRecovered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVpcEbrInfoConnectionRecovered.setStatus("mandatory")
_MscAtmIfVpcEbrInfoStatsTable_Object = MibTable
mscAtmIfVpcEbrInfoStatsTable = _MscAtmIfVpcEbrInfoStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 4, 11, 40)
)
if mibBuilder.loadTexts:
    mscAtmIfVpcEbrInfoStatsTable.setStatus("mandatory")
_MscAtmIfVpcEbrInfoStatsEntry_Object = MibTableRow
mscAtmIfVpcEbrInfoStatsEntry = _MscAtmIfVpcEbrInfoStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 4, 11, 40, 1)
)
mscAtmIfVpcEbrInfoStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVpcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmEbrMIB", "mscAtmIfVpcEbrInfoIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVpcEbrInfoStatsEntry.setStatus("mandatory")
_MscAtmIfVpcEbrInfoTotalConnectionRecoveries_Type = Counter32
_MscAtmIfVpcEbrInfoTotalConnectionRecoveries_Object = MibTableColumn
mscAtmIfVpcEbrInfoTotalConnectionRecoveries = _MscAtmIfVpcEbrInfoTotalConnectionRecoveries_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 4, 11, 40, 1, 1),
    _MscAtmIfVpcEbrInfoTotalConnectionRecoveries_Type()
)
mscAtmIfVpcEbrInfoTotalConnectionRecoveries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVpcEbrInfoTotalConnectionRecoveries.setStatus("mandatory")
_MscAtmIfVpcEbrInfoTotalPathOptimizations_Type = Counter32
_MscAtmIfVpcEbrInfoTotalPathOptimizations_Object = MibTableColumn
mscAtmIfVpcEbrInfoTotalPathOptimizations = _MscAtmIfVpcEbrInfoTotalPathOptimizations_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 4, 11, 40, 1, 2),
    _MscAtmIfVpcEbrInfoTotalPathOptimizations_Type()
)
mscAtmIfVpcEbrInfoTotalPathOptimizations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVpcEbrInfoTotalPathOptimizations.setStatus("mandatory")
_MscAtmIfVccSrcEbrOv_ObjectIdentity = ObjectIdentity
mscAtmIfVccSrcEbrOv = _MscAtmIfVccSrcEbrOv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 8, 2)
)
_MscAtmIfVccSrcEbrOvRowStatusTable_Object = MibTable
mscAtmIfVccSrcEbrOvRowStatusTable = _MscAtmIfVccSrcEbrOvRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 8, 2, 1)
)
if mibBuilder.loadTexts:
    mscAtmIfVccSrcEbrOvRowStatusTable.setStatus("mandatory")
_MscAtmIfVccSrcEbrOvRowStatusEntry_Object = MibTableRow
mscAtmIfVccSrcEbrOvRowStatusEntry = _MscAtmIfVccSrcEbrOvRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 8, 2, 1, 1)
)
mscAtmIfVccSrcEbrOvRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVccIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscAtmIfVccSrcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmEbrMIB", "mscAtmIfVccSrcEbrOvIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVccSrcEbrOvRowStatusEntry.setStatus("mandatory")
_MscAtmIfVccSrcEbrOvRowStatus_Type = RowStatus
_MscAtmIfVccSrcEbrOvRowStatus_Object = MibTableColumn
mscAtmIfVccSrcEbrOvRowStatus = _MscAtmIfVccSrcEbrOvRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 8, 2, 1, 1, 1),
    _MscAtmIfVccSrcEbrOvRowStatus_Type()
)
mscAtmIfVccSrcEbrOvRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVccSrcEbrOvRowStatus.setStatus("mandatory")
_MscAtmIfVccSrcEbrOvComponentName_Type = DisplayString
_MscAtmIfVccSrcEbrOvComponentName_Object = MibTableColumn
mscAtmIfVccSrcEbrOvComponentName = _MscAtmIfVccSrcEbrOvComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 8, 2, 1, 1, 2),
    _MscAtmIfVccSrcEbrOvComponentName_Type()
)
mscAtmIfVccSrcEbrOvComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVccSrcEbrOvComponentName.setStatus("mandatory")
_MscAtmIfVccSrcEbrOvStorageType_Type = StorageType
_MscAtmIfVccSrcEbrOvStorageType_Object = MibTableColumn
mscAtmIfVccSrcEbrOvStorageType = _MscAtmIfVccSrcEbrOvStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 8, 2, 1, 1, 4),
    _MscAtmIfVccSrcEbrOvStorageType_Type()
)
mscAtmIfVccSrcEbrOvStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVccSrcEbrOvStorageType.setStatus("mandatory")
_MscAtmIfVccSrcEbrOvIndex_Type = NonReplicated
_MscAtmIfVccSrcEbrOvIndex_Object = MibTableColumn
mscAtmIfVccSrcEbrOvIndex = _MscAtmIfVccSrcEbrOvIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 8, 2, 1, 1, 10),
    _MscAtmIfVccSrcEbrOvIndex_Type()
)
mscAtmIfVccSrcEbrOvIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmIfVccSrcEbrOvIndex.setStatus("mandatory")
_MscAtmIfVccSrcEbrOvProvTable_Object = MibTable
mscAtmIfVccSrcEbrOvProvTable = _MscAtmIfVccSrcEbrOvProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 8, 2, 20)
)
if mibBuilder.loadTexts:
    mscAtmIfVccSrcEbrOvProvTable.setStatus("mandatory")
_MscAtmIfVccSrcEbrOvProvEntry_Object = MibTableRow
mscAtmIfVccSrcEbrOvProvEntry = _MscAtmIfVccSrcEbrOvProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 8, 2, 20, 1)
)
mscAtmIfVccSrcEbrOvProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVccIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscAtmIfVccSrcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmEbrMIB", "mscAtmIfVccSrcEbrOvIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVccSrcEbrOvProvEntry.setStatus("mandatory")


class _MscAtmIfVccSrcEbrOvRecoverySubscribed_Type(Integer32):
    """Custom type mscAtmIfVccSrcEbrOvRecoverySubscribed based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_MscAtmIfVccSrcEbrOvRecoverySubscribed_Type.__name__ = "Integer32"
_MscAtmIfVccSrcEbrOvRecoverySubscribed_Object = MibTableColumn
mscAtmIfVccSrcEbrOvRecoverySubscribed = _MscAtmIfVccSrcEbrOvRecoverySubscribed_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 8, 2, 20, 1, 1),
    _MscAtmIfVccSrcEbrOvRecoverySubscribed_Type()
)
mscAtmIfVccSrcEbrOvRecoverySubscribed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVccSrcEbrOvRecoverySubscribed.setStatus("mandatory")


class _MscAtmIfVccSrcEbrOvOptimizationSubscribed_Type(Integer32):
    """Custom type mscAtmIfVccSrcEbrOvOptimizationSubscribed based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_MscAtmIfVccSrcEbrOvOptimizationSubscribed_Type.__name__ = "Integer32"
_MscAtmIfVccSrcEbrOvOptimizationSubscribed_Object = MibTableColumn
mscAtmIfVccSrcEbrOvOptimizationSubscribed = _MscAtmIfVccSrcEbrOvOptimizationSubscribed_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 8, 2, 20, 1, 2),
    _MscAtmIfVccSrcEbrOvOptimizationSubscribed_Type()
)
mscAtmIfVccSrcEbrOvOptimizationSubscribed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVccSrcEbrOvOptimizationSubscribed.setStatus("mandatory")
_MscAtmIfVccEbrInfo_ObjectIdentity = ObjectIdentity
mscAtmIfVccEbrInfo = _MscAtmIfVccEbrInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 12)
)
_MscAtmIfVccEbrInfoRowStatusTable_Object = MibTable
mscAtmIfVccEbrInfoRowStatusTable = _MscAtmIfVccEbrInfoRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 12, 1)
)
if mibBuilder.loadTexts:
    mscAtmIfVccEbrInfoRowStatusTable.setStatus("mandatory")
_MscAtmIfVccEbrInfoRowStatusEntry_Object = MibTableRow
mscAtmIfVccEbrInfoRowStatusEntry = _MscAtmIfVccEbrInfoRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 12, 1, 1)
)
mscAtmIfVccEbrInfoRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVccIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmEbrMIB", "mscAtmIfVccEbrInfoIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVccEbrInfoRowStatusEntry.setStatus("mandatory")
_MscAtmIfVccEbrInfoRowStatus_Type = RowStatus
_MscAtmIfVccEbrInfoRowStatus_Object = MibTableColumn
mscAtmIfVccEbrInfoRowStatus = _MscAtmIfVccEbrInfoRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 12, 1, 1, 1),
    _MscAtmIfVccEbrInfoRowStatus_Type()
)
mscAtmIfVccEbrInfoRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVccEbrInfoRowStatus.setStatus("mandatory")
_MscAtmIfVccEbrInfoComponentName_Type = DisplayString
_MscAtmIfVccEbrInfoComponentName_Object = MibTableColumn
mscAtmIfVccEbrInfoComponentName = _MscAtmIfVccEbrInfoComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 12, 1, 1, 2),
    _MscAtmIfVccEbrInfoComponentName_Type()
)
mscAtmIfVccEbrInfoComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVccEbrInfoComponentName.setStatus("mandatory")
_MscAtmIfVccEbrInfoStorageType_Type = StorageType
_MscAtmIfVccEbrInfoStorageType_Object = MibTableColumn
mscAtmIfVccEbrInfoStorageType = _MscAtmIfVccEbrInfoStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 12, 1, 1, 4),
    _MscAtmIfVccEbrInfoStorageType_Type()
)
mscAtmIfVccEbrInfoStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVccEbrInfoStorageType.setStatus("mandatory")
_MscAtmIfVccEbrInfoIndex_Type = NonReplicated
_MscAtmIfVccEbrInfoIndex_Object = MibTableColumn
mscAtmIfVccEbrInfoIndex = _MscAtmIfVccEbrInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 12, 1, 1, 10),
    _MscAtmIfVccEbrInfoIndex_Type()
)
mscAtmIfVccEbrInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmIfVccEbrInfoIndex.setStatus("mandatory")
_MscAtmIfVccEbrInfoOperTable_Object = MibTable
mscAtmIfVccEbrInfoOperTable = _MscAtmIfVccEbrInfoOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 12, 30)
)
if mibBuilder.loadTexts:
    mscAtmIfVccEbrInfoOperTable.setStatus("mandatory")
_MscAtmIfVccEbrInfoOperEntry_Object = MibTableRow
mscAtmIfVccEbrInfoOperEntry = _MscAtmIfVccEbrInfoOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 12, 30, 1)
)
mscAtmIfVccEbrInfoOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVccIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmEbrMIB", "mscAtmIfVccEbrInfoIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVccEbrInfoOperEntry.setStatus("mandatory")


class _MscAtmIfVccEbrInfoRecoverySubscribed_Type(Integer32):
    """Custom type mscAtmIfVccEbrInfoRecoverySubscribed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_MscAtmIfVccEbrInfoRecoverySubscribed_Type.__name__ = "Integer32"
_MscAtmIfVccEbrInfoRecoverySubscribed_Object = MibTableColumn
mscAtmIfVccEbrInfoRecoverySubscribed = _MscAtmIfVccEbrInfoRecoverySubscribed_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 12, 30, 1, 1),
    _MscAtmIfVccEbrInfoRecoverySubscribed_Type()
)
mscAtmIfVccEbrInfoRecoverySubscribed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVccEbrInfoRecoverySubscribed.setStatus("mandatory")


class _MscAtmIfVccEbrInfoOptimizationSubscribed_Type(Integer32):
    """Custom type mscAtmIfVccEbrInfoOptimizationSubscribed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_MscAtmIfVccEbrInfoOptimizationSubscribed_Type.__name__ = "Integer32"
_MscAtmIfVccEbrInfoOptimizationSubscribed_Object = MibTableColumn
mscAtmIfVccEbrInfoOptimizationSubscribed = _MscAtmIfVccEbrInfoOptimizationSubscribed_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 12, 30, 1, 2),
    _MscAtmIfVccEbrInfoOptimizationSubscribed_Type()
)
mscAtmIfVccEbrInfoOptimizationSubscribed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVccEbrInfoOptimizationSubscribed.setStatus("mandatory")


class _MscAtmIfVccEbrInfoConnectionRecovered_Type(Integer32):
    """Custom type mscAtmIfVccEbrInfoConnectionRecovered based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_MscAtmIfVccEbrInfoConnectionRecovered_Type.__name__ = "Integer32"
_MscAtmIfVccEbrInfoConnectionRecovered_Object = MibTableColumn
mscAtmIfVccEbrInfoConnectionRecovered = _MscAtmIfVccEbrInfoConnectionRecovered_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 12, 30, 1, 3),
    _MscAtmIfVccEbrInfoConnectionRecovered_Type()
)
mscAtmIfVccEbrInfoConnectionRecovered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVccEbrInfoConnectionRecovered.setStatus("mandatory")
_MscAtmIfVccEbrInfoStatsTable_Object = MibTable
mscAtmIfVccEbrInfoStatsTable = _MscAtmIfVccEbrInfoStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 12, 40)
)
if mibBuilder.loadTexts:
    mscAtmIfVccEbrInfoStatsTable.setStatus("mandatory")
_MscAtmIfVccEbrInfoStatsEntry_Object = MibTableRow
mscAtmIfVccEbrInfoStatsEntry = _MscAtmIfVccEbrInfoStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 12, 40, 1)
)
mscAtmIfVccEbrInfoStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVccIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmEbrMIB", "mscAtmIfVccEbrInfoIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVccEbrInfoStatsEntry.setStatus("mandatory")
_MscAtmIfVccEbrInfoTotalConnectionRecoveries_Type = Counter32
_MscAtmIfVccEbrInfoTotalConnectionRecoveries_Object = MibTableColumn
mscAtmIfVccEbrInfoTotalConnectionRecoveries = _MscAtmIfVccEbrInfoTotalConnectionRecoveries_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 12, 40, 1, 1),
    _MscAtmIfVccEbrInfoTotalConnectionRecoveries_Type()
)
mscAtmIfVccEbrInfoTotalConnectionRecoveries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVccEbrInfoTotalConnectionRecoveries.setStatus("mandatory")
_MscAtmIfVccEbrInfoTotalPathOptimizations_Type = Counter32
_MscAtmIfVccEbrInfoTotalPathOptimizations_Object = MibTableColumn
mscAtmIfVccEbrInfoTotalPathOptimizations = _MscAtmIfVccEbrInfoTotalPathOptimizations_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 12, 40, 1, 2),
    _MscAtmIfVccEbrInfoTotalPathOptimizations_Type()
)
mscAtmIfVccEbrInfoTotalPathOptimizations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVccEbrInfoTotalPathOptimizations.setStatus("mandatory")
_MscAtmIfUniEbr_ObjectIdentity = ObjectIdentity
mscAtmIfUniEbr = _MscAtmIfUniEbr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 7)
)
_MscAtmIfUniEbrRowStatusTable_Object = MibTable
mscAtmIfUniEbrRowStatusTable = _MscAtmIfUniEbrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 7, 1)
)
if mibBuilder.loadTexts:
    mscAtmIfUniEbrRowStatusTable.setStatus("mandatory")
_MscAtmIfUniEbrRowStatusEntry_Object = MibTableRow
mscAtmIfUniEbrRowStatusEntry = _MscAtmIfUniEbrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 7, 1, 1)
)
mscAtmIfUniEbrRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmEbrMIB", "mscAtmIfUniEbrIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfUniEbrRowStatusEntry.setStatus("mandatory")
_MscAtmIfUniEbrRowStatus_Type = RowStatus
_MscAtmIfUniEbrRowStatus_Object = MibTableColumn
mscAtmIfUniEbrRowStatus = _MscAtmIfUniEbrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 7, 1, 1, 1),
    _MscAtmIfUniEbrRowStatus_Type()
)
mscAtmIfUniEbrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfUniEbrRowStatus.setStatus("mandatory")
_MscAtmIfUniEbrComponentName_Type = DisplayString
_MscAtmIfUniEbrComponentName_Object = MibTableColumn
mscAtmIfUniEbrComponentName = _MscAtmIfUniEbrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 7, 1, 1, 2),
    _MscAtmIfUniEbrComponentName_Type()
)
mscAtmIfUniEbrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfUniEbrComponentName.setStatus("mandatory")
_MscAtmIfUniEbrStorageType_Type = StorageType
_MscAtmIfUniEbrStorageType_Object = MibTableColumn
mscAtmIfUniEbrStorageType = _MscAtmIfUniEbrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 7, 1, 1, 4),
    _MscAtmIfUniEbrStorageType_Type()
)
mscAtmIfUniEbrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfUniEbrStorageType.setStatus("mandatory")
_MscAtmIfUniEbrIndex_Type = NonReplicated
_MscAtmIfUniEbrIndex_Object = MibTableColumn
mscAtmIfUniEbrIndex = _MscAtmIfUniEbrIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 7, 1, 1, 10),
    _MscAtmIfUniEbrIndex_Type()
)
mscAtmIfUniEbrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmIfUniEbrIndex.setStatus("mandatory")
_MscAtmIfUniEbrProvTable_Object = MibTable
mscAtmIfUniEbrProvTable = _MscAtmIfUniEbrProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 7, 20)
)
if mibBuilder.loadTexts:
    mscAtmIfUniEbrProvTable.setStatus("mandatory")
_MscAtmIfUniEbrProvEntry_Object = MibTableRow
mscAtmIfUniEbrProvEntry = _MscAtmIfUniEbrProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 7, 20, 1)
)
mscAtmIfUniEbrProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmEbrMIB", "mscAtmIfUniEbrIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfUniEbrProvEntry.setStatus("mandatory")


class _MscAtmIfUniEbrConnectionRecovery_Type(OctetString):
    """Custom type mscAtmIfUniEbrConnectionRecovery based on OctetString"""
    defaultHexValue = "c0"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscAtmIfUniEbrConnectionRecovery_Type.__name__ = "OctetString"
_MscAtmIfUniEbrConnectionRecovery_Object = MibTableColumn
mscAtmIfUniEbrConnectionRecovery = _MscAtmIfUniEbrConnectionRecovery_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 7, 20, 1, 1),
    _MscAtmIfUniEbrConnectionRecovery_Type()
)
mscAtmIfUniEbrConnectionRecovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfUniEbrConnectionRecovery.setStatus("mandatory")


class _MscAtmIfUniEbrPathOptimization_Type(OctetString):
    """Custom type mscAtmIfUniEbrPathOptimization based on OctetString"""
    defaultHexValue = "c0"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscAtmIfUniEbrPathOptimization_Type.__name__ = "OctetString"
_MscAtmIfUniEbrPathOptimization_Object = MibTableColumn
mscAtmIfUniEbrPathOptimization = _MscAtmIfUniEbrPathOptimization_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 7, 20, 1, 2),
    _MscAtmIfUniEbrPathOptimization_Type()
)
mscAtmIfUniEbrPathOptimization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfUniEbrPathOptimization.setStatus("mandatory")
_MscAtmIfUniEbrOperTable_Object = MibTable
mscAtmIfUniEbrOperTable = _MscAtmIfUniEbrOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 7, 30)
)
if mibBuilder.loadTexts:
    mscAtmIfUniEbrOperTable.setStatus("mandatory")
_MscAtmIfUniEbrOperEntry_Object = MibTableRow
mscAtmIfUniEbrOperEntry = _MscAtmIfUniEbrOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 7, 30, 1)
)
mscAtmIfUniEbrOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmEbrMIB", "mscAtmIfUniEbrIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfUniEbrOperEntry.setStatus("mandatory")


class _MscAtmIfUniEbrSubscribedConnections_Type(Gauge32):
    """Custom type mscAtmIfUniEbrSubscribedConnections based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscAtmIfUniEbrSubscribedConnections_Type.__name__ = "Gauge32"
_MscAtmIfUniEbrSubscribedConnections_Object = MibTableColumn
mscAtmIfUniEbrSubscribedConnections = _MscAtmIfUniEbrSubscribedConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 7, 30, 1, 1),
    _MscAtmIfUniEbrSubscribedConnections_Type()
)
mscAtmIfUniEbrSubscribedConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfUniEbrSubscribedConnections.setStatus("mandatory")


class _MscAtmIfUniEbrEligibleRecoveredConnections_Type(Gauge32):
    """Custom type mscAtmIfUniEbrEligibleRecoveredConnections based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscAtmIfUniEbrEligibleRecoveredConnections_Type.__name__ = "Gauge32"
_MscAtmIfUniEbrEligibleRecoveredConnections_Object = MibTableColumn
mscAtmIfUniEbrEligibleRecoveredConnections = _MscAtmIfUniEbrEligibleRecoveredConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 7, 30, 1, 2),
    _MscAtmIfUniEbrEligibleRecoveredConnections_Type()
)
mscAtmIfUniEbrEligibleRecoveredConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfUniEbrEligibleRecoveredConnections.setStatus("mandatory")


class _MscAtmIfUniEbrIneligibleRecoveredConnections_Type(Gauge32):
    """Custom type mscAtmIfUniEbrIneligibleRecoveredConnections based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscAtmIfUniEbrIneligibleRecoveredConnections_Type.__name__ = "Gauge32"
_MscAtmIfUniEbrIneligibleRecoveredConnections_Object = MibTableColumn
mscAtmIfUniEbrIneligibleRecoveredConnections = _MscAtmIfUniEbrIneligibleRecoveredConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 7, 30, 1, 3),
    _MscAtmIfUniEbrIneligibleRecoveredConnections_Type()
)
mscAtmIfUniEbrIneligibleRecoveredConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfUniEbrIneligibleRecoveredConnections.setStatus("mandatory")
_MscAtmIfUniEbrStatsTable_Object = MibTable
mscAtmIfUniEbrStatsTable = _MscAtmIfUniEbrStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 7, 40)
)
if mibBuilder.loadTexts:
    mscAtmIfUniEbrStatsTable.setStatus("mandatory")
_MscAtmIfUniEbrStatsEntry_Object = MibTableRow
mscAtmIfUniEbrStatsEntry = _MscAtmIfUniEbrStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 7, 40, 1)
)
mscAtmIfUniEbrStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmEbrMIB", "mscAtmIfUniEbrIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfUniEbrStatsEntry.setStatus("mandatory")
_MscAtmIfUniEbrTotalConnectionRecoveries_Type = Counter32
_MscAtmIfUniEbrTotalConnectionRecoveries_Object = MibTableColumn
mscAtmIfUniEbrTotalConnectionRecoveries = _MscAtmIfUniEbrTotalConnectionRecoveries_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 7, 40, 1, 1),
    _MscAtmIfUniEbrTotalConnectionRecoveries_Type()
)
mscAtmIfUniEbrTotalConnectionRecoveries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfUniEbrTotalConnectionRecoveries.setStatus("mandatory")
_MscAtmIfUniEbrTotalPathOptimizations_Type = Counter32
_MscAtmIfUniEbrTotalPathOptimizations_Object = MibTableColumn
mscAtmIfUniEbrTotalPathOptimizations = _MscAtmIfUniEbrTotalPathOptimizations_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 7, 40, 1, 2),
    _MscAtmIfUniEbrTotalPathOptimizations_Type()
)
mscAtmIfUniEbrTotalPathOptimizations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfUniEbrTotalPathOptimizations.setStatus("mandatory")
_MscAtmIfIispEbr_ObjectIdentity = ObjectIdentity
mscAtmIfIispEbr = _MscAtmIfIispEbr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 7)
)
_MscAtmIfIispEbrRowStatusTable_Object = MibTable
mscAtmIfIispEbrRowStatusTable = _MscAtmIfIispEbrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 7, 1)
)
if mibBuilder.loadTexts:
    mscAtmIfIispEbrRowStatusTable.setStatus("mandatory")
_MscAtmIfIispEbrRowStatusEntry_Object = MibTableRow
mscAtmIfIispEbrRowStatusEntry = _MscAtmIfIispEbrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 7, 1, 1)
)
mscAtmIfIispEbrRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfIispIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmEbrMIB", "mscAtmIfIispEbrIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfIispEbrRowStatusEntry.setStatus("mandatory")
_MscAtmIfIispEbrRowStatus_Type = RowStatus
_MscAtmIfIispEbrRowStatus_Object = MibTableColumn
mscAtmIfIispEbrRowStatus = _MscAtmIfIispEbrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 7, 1, 1, 1),
    _MscAtmIfIispEbrRowStatus_Type()
)
mscAtmIfIispEbrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfIispEbrRowStatus.setStatus("mandatory")
_MscAtmIfIispEbrComponentName_Type = DisplayString
_MscAtmIfIispEbrComponentName_Object = MibTableColumn
mscAtmIfIispEbrComponentName = _MscAtmIfIispEbrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 7, 1, 1, 2),
    _MscAtmIfIispEbrComponentName_Type()
)
mscAtmIfIispEbrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfIispEbrComponentName.setStatus("mandatory")
_MscAtmIfIispEbrStorageType_Type = StorageType
_MscAtmIfIispEbrStorageType_Object = MibTableColumn
mscAtmIfIispEbrStorageType = _MscAtmIfIispEbrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 7, 1, 1, 4),
    _MscAtmIfIispEbrStorageType_Type()
)
mscAtmIfIispEbrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfIispEbrStorageType.setStatus("mandatory")
_MscAtmIfIispEbrIndex_Type = NonReplicated
_MscAtmIfIispEbrIndex_Object = MibTableColumn
mscAtmIfIispEbrIndex = _MscAtmIfIispEbrIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 7, 1, 1, 10),
    _MscAtmIfIispEbrIndex_Type()
)
mscAtmIfIispEbrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmIfIispEbrIndex.setStatus("mandatory")
_MscAtmIfIispEbrProvTable_Object = MibTable
mscAtmIfIispEbrProvTable = _MscAtmIfIispEbrProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 7, 20)
)
if mibBuilder.loadTexts:
    mscAtmIfIispEbrProvTable.setStatus("mandatory")
_MscAtmIfIispEbrProvEntry_Object = MibTableRow
mscAtmIfIispEbrProvEntry = _MscAtmIfIispEbrProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 7, 20, 1)
)
mscAtmIfIispEbrProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfIispIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmEbrMIB", "mscAtmIfIispEbrIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfIispEbrProvEntry.setStatus("mandatory")


class _MscAtmIfIispEbrConnectionRecovery_Type(OctetString):
    """Custom type mscAtmIfIispEbrConnectionRecovery based on OctetString"""
    defaultHexValue = "c0"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscAtmIfIispEbrConnectionRecovery_Type.__name__ = "OctetString"
_MscAtmIfIispEbrConnectionRecovery_Object = MibTableColumn
mscAtmIfIispEbrConnectionRecovery = _MscAtmIfIispEbrConnectionRecovery_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 7, 20, 1, 1),
    _MscAtmIfIispEbrConnectionRecovery_Type()
)
mscAtmIfIispEbrConnectionRecovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfIispEbrConnectionRecovery.setStatus("mandatory")


class _MscAtmIfIispEbrPathOptimization_Type(OctetString):
    """Custom type mscAtmIfIispEbrPathOptimization based on OctetString"""
    defaultHexValue = "c0"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscAtmIfIispEbrPathOptimization_Type.__name__ = "OctetString"
_MscAtmIfIispEbrPathOptimization_Object = MibTableColumn
mscAtmIfIispEbrPathOptimization = _MscAtmIfIispEbrPathOptimization_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 7, 20, 1, 2),
    _MscAtmIfIispEbrPathOptimization_Type()
)
mscAtmIfIispEbrPathOptimization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfIispEbrPathOptimization.setStatus("mandatory")
_MscAtmIfIispEbrOperTable_Object = MibTable
mscAtmIfIispEbrOperTable = _MscAtmIfIispEbrOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 7, 30)
)
if mibBuilder.loadTexts:
    mscAtmIfIispEbrOperTable.setStatus("mandatory")
_MscAtmIfIispEbrOperEntry_Object = MibTableRow
mscAtmIfIispEbrOperEntry = _MscAtmIfIispEbrOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 7, 30, 1)
)
mscAtmIfIispEbrOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfIispIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmEbrMIB", "mscAtmIfIispEbrIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfIispEbrOperEntry.setStatus("mandatory")


class _MscAtmIfIispEbrSubscribedConnections_Type(Gauge32):
    """Custom type mscAtmIfIispEbrSubscribedConnections based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscAtmIfIispEbrSubscribedConnections_Type.__name__ = "Gauge32"
_MscAtmIfIispEbrSubscribedConnections_Object = MibTableColumn
mscAtmIfIispEbrSubscribedConnections = _MscAtmIfIispEbrSubscribedConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 7, 30, 1, 1),
    _MscAtmIfIispEbrSubscribedConnections_Type()
)
mscAtmIfIispEbrSubscribedConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfIispEbrSubscribedConnections.setStatus("mandatory")


class _MscAtmIfIispEbrEligibleRecoveredConnections_Type(Gauge32):
    """Custom type mscAtmIfIispEbrEligibleRecoveredConnections based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscAtmIfIispEbrEligibleRecoveredConnections_Type.__name__ = "Gauge32"
_MscAtmIfIispEbrEligibleRecoveredConnections_Object = MibTableColumn
mscAtmIfIispEbrEligibleRecoveredConnections = _MscAtmIfIispEbrEligibleRecoveredConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 7, 30, 1, 2),
    _MscAtmIfIispEbrEligibleRecoveredConnections_Type()
)
mscAtmIfIispEbrEligibleRecoveredConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfIispEbrEligibleRecoveredConnections.setStatus("mandatory")


class _MscAtmIfIispEbrIneligibleRecoveredConnections_Type(Gauge32):
    """Custom type mscAtmIfIispEbrIneligibleRecoveredConnections based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscAtmIfIispEbrIneligibleRecoveredConnections_Type.__name__ = "Gauge32"
_MscAtmIfIispEbrIneligibleRecoveredConnections_Object = MibTableColumn
mscAtmIfIispEbrIneligibleRecoveredConnections = _MscAtmIfIispEbrIneligibleRecoveredConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 7, 30, 1, 3),
    _MscAtmIfIispEbrIneligibleRecoveredConnections_Type()
)
mscAtmIfIispEbrIneligibleRecoveredConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfIispEbrIneligibleRecoveredConnections.setStatus("mandatory")
_MscAtmIfIispEbrStatsTable_Object = MibTable
mscAtmIfIispEbrStatsTable = _MscAtmIfIispEbrStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 7, 40)
)
if mibBuilder.loadTexts:
    mscAtmIfIispEbrStatsTable.setStatus("mandatory")
_MscAtmIfIispEbrStatsEntry_Object = MibTableRow
mscAtmIfIispEbrStatsEntry = _MscAtmIfIispEbrStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 7, 40, 1)
)
mscAtmIfIispEbrStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfIispIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmEbrMIB", "mscAtmIfIispEbrIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfIispEbrStatsEntry.setStatus("mandatory")
_MscAtmIfIispEbrTotalConnectionRecoveries_Type = Counter32
_MscAtmIfIispEbrTotalConnectionRecoveries_Object = MibTableColumn
mscAtmIfIispEbrTotalConnectionRecoveries = _MscAtmIfIispEbrTotalConnectionRecoveries_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 7, 40, 1, 1),
    _MscAtmIfIispEbrTotalConnectionRecoveries_Type()
)
mscAtmIfIispEbrTotalConnectionRecoveries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfIispEbrTotalConnectionRecoveries.setStatus("mandatory")
_MscAtmIfIispEbrTotalPathOptimizations_Type = Counter32
_MscAtmIfIispEbrTotalPathOptimizations_Object = MibTableColumn
mscAtmIfIispEbrTotalPathOptimizations = _MscAtmIfIispEbrTotalPathOptimizations_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 7, 40, 1, 2),
    _MscAtmIfIispEbrTotalPathOptimizations_Type()
)
mscAtmIfIispEbrTotalPathOptimizations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfIispEbrTotalPathOptimizations.setStatus("mandatory")
_MscAtmIfVptIispEbr_ObjectIdentity = ObjectIdentity
mscAtmIfVptIispEbr = _MscAtmIfVptIispEbr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 7)
)
_MscAtmIfVptIispEbrRowStatusTable_Object = MibTable
mscAtmIfVptIispEbrRowStatusTable = _MscAtmIfVptIispEbrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 7, 1)
)
if mibBuilder.loadTexts:
    mscAtmIfVptIispEbrRowStatusTable.setStatus("mandatory")
_MscAtmIfVptIispEbrRowStatusEntry_Object = MibTableRow
mscAtmIfVptIispEbrRowStatusEntry = _MscAtmIfVptIispEbrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 7, 1, 1)
)
mscAtmIfVptIispEbrRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfVptIispIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmEbrMIB", "mscAtmIfVptIispEbrIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptIispEbrRowStatusEntry.setStatus("mandatory")
_MscAtmIfVptIispEbrRowStatus_Type = RowStatus
_MscAtmIfVptIispEbrRowStatus_Object = MibTableColumn
mscAtmIfVptIispEbrRowStatus = _MscAtmIfVptIispEbrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 7, 1, 1, 1),
    _MscAtmIfVptIispEbrRowStatus_Type()
)
mscAtmIfVptIispEbrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptIispEbrRowStatus.setStatus("mandatory")
_MscAtmIfVptIispEbrComponentName_Type = DisplayString
_MscAtmIfVptIispEbrComponentName_Object = MibTableColumn
mscAtmIfVptIispEbrComponentName = _MscAtmIfVptIispEbrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 7, 1, 1, 2),
    _MscAtmIfVptIispEbrComponentName_Type()
)
mscAtmIfVptIispEbrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptIispEbrComponentName.setStatus("mandatory")
_MscAtmIfVptIispEbrStorageType_Type = StorageType
_MscAtmIfVptIispEbrStorageType_Object = MibTableColumn
mscAtmIfVptIispEbrStorageType = _MscAtmIfVptIispEbrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 7, 1, 1, 4),
    _MscAtmIfVptIispEbrStorageType_Type()
)
mscAtmIfVptIispEbrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptIispEbrStorageType.setStatus("mandatory")
_MscAtmIfVptIispEbrIndex_Type = NonReplicated
_MscAtmIfVptIispEbrIndex_Object = MibTableColumn
mscAtmIfVptIispEbrIndex = _MscAtmIfVptIispEbrIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 7, 1, 1, 10),
    _MscAtmIfVptIispEbrIndex_Type()
)
mscAtmIfVptIispEbrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmIfVptIispEbrIndex.setStatus("mandatory")
_MscAtmIfVptIispEbrProvTable_Object = MibTable
mscAtmIfVptIispEbrProvTable = _MscAtmIfVptIispEbrProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 7, 20)
)
if mibBuilder.loadTexts:
    mscAtmIfVptIispEbrProvTable.setStatus("mandatory")
_MscAtmIfVptIispEbrProvEntry_Object = MibTableRow
mscAtmIfVptIispEbrProvEntry = _MscAtmIfVptIispEbrProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 7, 20, 1)
)
mscAtmIfVptIispEbrProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfVptIispIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmEbrMIB", "mscAtmIfVptIispEbrIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptIispEbrProvEntry.setStatus("mandatory")


class _MscAtmIfVptIispEbrConnectionRecovery_Type(OctetString):
    """Custom type mscAtmIfVptIispEbrConnectionRecovery based on OctetString"""
    defaultHexValue = "c0"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscAtmIfVptIispEbrConnectionRecovery_Type.__name__ = "OctetString"
_MscAtmIfVptIispEbrConnectionRecovery_Object = MibTableColumn
mscAtmIfVptIispEbrConnectionRecovery = _MscAtmIfVptIispEbrConnectionRecovery_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 7, 20, 1, 1),
    _MscAtmIfVptIispEbrConnectionRecovery_Type()
)
mscAtmIfVptIispEbrConnectionRecovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptIispEbrConnectionRecovery.setStatus("mandatory")


class _MscAtmIfVptIispEbrPathOptimization_Type(OctetString):
    """Custom type mscAtmIfVptIispEbrPathOptimization based on OctetString"""
    defaultHexValue = "c0"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscAtmIfVptIispEbrPathOptimization_Type.__name__ = "OctetString"
_MscAtmIfVptIispEbrPathOptimization_Object = MibTableColumn
mscAtmIfVptIispEbrPathOptimization = _MscAtmIfVptIispEbrPathOptimization_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 7, 20, 1, 2),
    _MscAtmIfVptIispEbrPathOptimization_Type()
)
mscAtmIfVptIispEbrPathOptimization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptIispEbrPathOptimization.setStatus("mandatory")
_MscAtmIfVptIispEbrOperTable_Object = MibTable
mscAtmIfVptIispEbrOperTable = _MscAtmIfVptIispEbrOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 7, 30)
)
if mibBuilder.loadTexts:
    mscAtmIfVptIispEbrOperTable.setStatus("mandatory")
_MscAtmIfVptIispEbrOperEntry_Object = MibTableRow
mscAtmIfVptIispEbrOperEntry = _MscAtmIfVptIispEbrOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 7, 30, 1)
)
mscAtmIfVptIispEbrOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfVptIispIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmEbrMIB", "mscAtmIfVptIispEbrIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptIispEbrOperEntry.setStatus("mandatory")


class _MscAtmIfVptIispEbrSubscribedConnections_Type(Gauge32):
    """Custom type mscAtmIfVptIispEbrSubscribedConnections based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscAtmIfVptIispEbrSubscribedConnections_Type.__name__ = "Gauge32"
_MscAtmIfVptIispEbrSubscribedConnections_Object = MibTableColumn
mscAtmIfVptIispEbrSubscribedConnections = _MscAtmIfVptIispEbrSubscribedConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 7, 30, 1, 1),
    _MscAtmIfVptIispEbrSubscribedConnections_Type()
)
mscAtmIfVptIispEbrSubscribedConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptIispEbrSubscribedConnections.setStatus("mandatory")


class _MscAtmIfVptIispEbrEligibleRecoveredConnections_Type(Gauge32):
    """Custom type mscAtmIfVptIispEbrEligibleRecoveredConnections based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscAtmIfVptIispEbrEligibleRecoveredConnections_Type.__name__ = "Gauge32"
_MscAtmIfVptIispEbrEligibleRecoveredConnections_Object = MibTableColumn
mscAtmIfVptIispEbrEligibleRecoveredConnections = _MscAtmIfVptIispEbrEligibleRecoveredConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 7, 30, 1, 2),
    _MscAtmIfVptIispEbrEligibleRecoveredConnections_Type()
)
mscAtmIfVptIispEbrEligibleRecoveredConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptIispEbrEligibleRecoveredConnections.setStatus("mandatory")


class _MscAtmIfVptIispEbrIneligibleRecoveredConnections_Type(Gauge32):
    """Custom type mscAtmIfVptIispEbrIneligibleRecoveredConnections based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscAtmIfVptIispEbrIneligibleRecoveredConnections_Type.__name__ = "Gauge32"
_MscAtmIfVptIispEbrIneligibleRecoveredConnections_Object = MibTableColumn
mscAtmIfVptIispEbrIneligibleRecoveredConnections = _MscAtmIfVptIispEbrIneligibleRecoveredConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 7, 30, 1, 3),
    _MscAtmIfVptIispEbrIneligibleRecoveredConnections_Type()
)
mscAtmIfVptIispEbrIneligibleRecoveredConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptIispEbrIneligibleRecoveredConnections.setStatus("mandatory")
_MscAtmIfVptIispEbrStatsTable_Object = MibTable
mscAtmIfVptIispEbrStatsTable = _MscAtmIfVptIispEbrStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 7, 40)
)
if mibBuilder.loadTexts:
    mscAtmIfVptIispEbrStatsTable.setStatus("mandatory")
_MscAtmIfVptIispEbrStatsEntry_Object = MibTableRow
mscAtmIfVptIispEbrStatsEntry = _MscAtmIfVptIispEbrStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 7, 40, 1)
)
mscAtmIfVptIispEbrStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfVptIispIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmEbrMIB", "mscAtmIfVptIispEbrIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptIispEbrStatsEntry.setStatus("mandatory")
_MscAtmIfVptIispEbrTotalConnectionRecoveries_Type = Counter32
_MscAtmIfVptIispEbrTotalConnectionRecoveries_Object = MibTableColumn
mscAtmIfVptIispEbrTotalConnectionRecoveries = _MscAtmIfVptIispEbrTotalConnectionRecoveries_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 7, 40, 1, 1),
    _MscAtmIfVptIispEbrTotalConnectionRecoveries_Type()
)
mscAtmIfVptIispEbrTotalConnectionRecoveries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptIispEbrTotalConnectionRecoveries.setStatus("mandatory")
_MscAtmIfVptIispEbrTotalPathOptimizations_Type = Counter32
_MscAtmIfVptIispEbrTotalPathOptimizations_Object = MibTableColumn
mscAtmIfVptIispEbrTotalPathOptimizations = _MscAtmIfVptIispEbrTotalPathOptimizations_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 7, 40, 1, 2),
    _MscAtmIfVptIispEbrTotalPathOptimizations_Type()
)
mscAtmIfVptIispEbrTotalPathOptimizations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptIispEbrTotalPathOptimizations.setStatus("mandatory")
_MscAtmIfVptPnniEbr_ObjectIdentity = ObjectIdentity
mscAtmIfVptPnniEbr = _MscAtmIfVptPnniEbr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 7)
)
_MscAtmIfVptPnniEbrRowStatusTable_Object = MibTable
mscAtmIfVptPnniEbrRowStatusTable = _MscAtmIfVptPnniEbrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 7, 1)
)
if mibBuilder.loadTexts:
    mscAtmIfVptPnniEbrRowStatusTable.setStatus("mandatory")
_MscAtmIfVptPnniEbrRowStatusEntry_Object = MibTableRow
mscAtmIfVptPnniEbrRowStatusEntry = _MscAtmIfVptPnniEbrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 7, 1, 1)
)
mscAtmIfVptPnniEbrRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfVptPnniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmEbrMIB", "mscAtmIfVptPnniEbrIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptPnniEbrRowStatusEntry.setStatus("mandatory")
_MscAtmIfVptPnniEbrRowStatus_Type = RowStatus
_MscAtmIfVptPnniEbrRowStatus_Object = MibTableColumn
mscAtmIfVptPnniEbrRowStatus = _MscAtmIfVptPnniEbrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 7, 1, 1, 1),
    _MscAtmIfVptPnniEbrRowStatus_Type()
)
mscAtmIfVptPnniEbrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniEbrRowStatus.setStatus("mandatory")
_MscAtmIfVptPnniEbrComponentName_Type = DisplayString
_MscAtmIfVptPnniEbrComponentName_Object = MibTableColumn
mscAtmIfVptPnniEbrComponentName = _MscAtmIfVptPnniEbrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 7, 1, 1, 2),
    _MscAtmIfVptPnniEbrComponentName_Type()
)
mscAtmIfVptPnniEbrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniEbrComponentName.setStatus("mandatory")
_MscAtmIfVptPnniEbrStorageType_Type = StorageType
_MscAtmIfVptPnniEbrStorageType_Object = MibTableColumn
mscAtmIfVptPnniEbrStorageType = _MscAtmIfVptPnniEbrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 7, 1, 1, 4),
    _MscAtmIfVptPnniEbrStorageType_Type()
)
mscAtmIfVptPnniEbrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniEbrStorageType.setStatus("mandatory")
_MscAtmIfVptPnniEbrIndex_Type = NonReplicated
_MscAtmIfVptPnniEbrIndex_Object = MibTableColumn
mscAtmIfVptPnniEbrIndex = _MscAtmIfVptPnniEbrIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 7, 1, 1, 10),
    _MscAtmIfVptPnniEbrIndex_Type()
)
mscAtmIfVptPnniEbrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniEbrIndex.setStatus("mandatory")
_MscAtmIfVptPnniEbrProvTable_Object = MibTable
mscAtmIfVptPnniEbrProvTable = _MscAtmIfVptPnniEbrProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 7, 20)
)
if mibBuilder.loadTexts:
    mscAtmIfVptPnniEbrProvTable.setStatus("mandatory")
_MscAtmIfVptPnniEbrProvEntry_Object = MibTableRow
mscAtmIfVptPnniEbrProvEntry = _MscAtmIfVptPnniEbrProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 7, 20, 1)
)
mscAtmIfVptPnniEbrProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfVptPnniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmEbrMIB", "mscAtmIfVptPnniEbrIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptPnniEbrProvEntry.setStatus("mandatory")


class _MscAtmIfVptPnniEbrConnectionRecovery_Type(OctetString):
    """Custom type mscAtmIfVptPnniEbrConnectionRecovery based on OctetString"""
    defaultHexValue = "c0"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscAtmIfVptPnniEbrConnectionRecovery_Type.__name__ = "OctetString"
_MscAtmIfVptPnniEbrConnectionRecovery_Object = MibTableColumn
mscAtmIfVptPnniEbrConnectionRecovery = _MscAtmIfVptPnniEbrConnectionRecovery_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 7, 20, 1, 1),
    _MscAtmIfVptPnniEbrConnectionRecovery_Type()
)
mscAtmIfVptPnniEbrConnectionRecovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniEbrConnectionRecovery.setStatus("mandatory")


class _MscAtmIfVptPnniEbrPathOptimization_Type(OctetString):
    """Custom type mscAtmIfVptPnniEbrPathOptimization based on OctetString"""
    defaultHexValue = "c0"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscAtmIfVptPnniEbrPathOptimization_Type.__name__ = "OctetString"
_MscAtmIfVptPnniEbrPathOptimization_Object = MibTableColumn
mscAtmIfVptPnniEbrPathOptimization = _MscAtmIfVptPnniEbrPathOptimization_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 7, 20, 1, 2),
    _MscAtmIfVptPnniEbrPathOptimization_Type()
)
mscAtmIfVptPnniEbrPathOptimization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniEbrPathOptimization.setStatus("mandatory")
_MscAtmIfVptPnniEbrOperTable_Object = MibTable
mscAtmIfVptPnniEbrOperTable = _MscAtmIfVptPnniEbrOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 7, 30)
)
if mibBuilder.loadTexts:
    mscAtmIfVptPnniEbrOperTable.setStatus("mandatory")
_MscAtmIfVptPnniEbrOperEntry_Object = MibTableRow
mscAtmIfVptPnniEbrOperEntry = _MscAtmIfVptPnniEbrOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 7, 30, 1)
)
mscAtmIfVptPnniEbrOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfVptPnniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmEbrMIB", "mscAtmIfVptPnniEbrIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptPnniEbrOperEntry.setStatus("mandatory")


class _MscAtmIfVptPnniEbrSubscribedConnections_Type(Gauge32):
    """Custom type mscAtmIfVptPnniEbrSubscribedConnections based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscAtmIfVptPnniEbrSubscribedConnections_Type.__name__ = "Gauge32"
_MscAtmIfVptPnniEbrSubscribedConnections_Object = MibTableColumn
mscAtmIfVptPnniEbrSubscribedConnections = _MscAtmIfVptPnniEbrSubscribedConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 7, 30, 1, 1),
    _MscAtmIfVptPnniEbrSubscribedConnections_Type()
)
mscAtmIfVptPnniEbrSubscribedConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniEbrSubscribedConnections.setStatus("mandatory")


class _MscAtmIfVptPnniEbrEligibleRecoveredConnections_Type(Gauge32):
    """Custom type mscAtmIfVptPnniEbrEligibleRecoveredConnections based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscAtmIfVptPnniEbrEligibleRecoveredConnections_Type.__name__ = "Gauge32"
_MscAtmIfVptPnniEbrEligibleRecoveredConnections_Object = MibTableColumn
mscAtmIfVptPnniEbrEligibleRecoveredConnections = _MscAtmIfVptPnniEbrEligibleRecoveredConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 7, 30, 1, 2),
    _MscAtmIfVptPnniEbrEligibleRecoveredConnections_Type()
)
mscAtmIfVptPnniEbrEligibleRecoveredConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniEbrEligibleRecoveredConnections.setStatus("mandatory")


class _MscAtmIfVptPnniEbrIneligibleRecoveredConnections_Type(Gauge32):
    """Custom type mscAtmIfVptPnniEbrIneligibleRecoveredConnections based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscAtmIfVptPnniEbrIneligibleRecoveredConnections_Type.__name__ = "Gauge32"
_MscAtmIfVptPnniEbrIneligibleRecoveredConnections_Object = MibTableColumn
mscAtmIfVptPnniEbrIneligibleRecoveredConnections = _MscAtmIfVptPnniEbrIneligibleRecoveredConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 7, 30, 1, 3),
    _MscAtmIfVptPnniEbrIneligibleRecoveredConnections_Type()
)
mscAtmIfVptPnniEbrIneligibleRecoveredConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniEbrIneligibleRecoveredConnections.setStatus("mandatory")
_MscAtmIfVptPnniEbrStatsTable_Object = MibTable
mscAtmIfVptPnniEbrStatsTable = _MscAtmIfVptPnniEbrStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 7, 40)
)
if mibBuilder.loadTexts:
    mscAtmIfVptPnniEbrStatsTable.setStatus("mandatory")
_MscAtmIfVptPnniEbrStatsEntry_Object = MibTableRow
mscAtmIfVptPnniEbrStatsEntry = _MscAtmIfVptPnniEbrStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 7, 40, 1)
)
mscAtmIfVptPnniEbrStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfVptPnniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmEbrMIB", "mscAtmIfVptPnniEbrIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptPnniEbrStatsEntry.setStatus("mandatory")
_MscAtmIfVptPnniEbrTotalConnectionRecoveries_Type = Counter32
_MscAtmIfVptPnniEbrTotalConnectionRecoveries_Object = MibTableColumn
mscAtmIfVptPnniEbrTotalConnectionRecoveries = _MscAtmIfVptPnniEbrTotalConnectionRecoveries_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 7, 40, 1, 1),
    _MscAtmIfVptPnniEbrTotalConnectionRecoveries_Type()
)
mscAtmIfVptPnniEbrTotalConnectionRecoveries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniEbrTotalConnectionRecoveries.setStatus("mandatory")
_MscAtmIfVptPnniEbrTotalPathOptimizations_Type = Counter32
_MscAtmIfVptPnniEbrTotalPathOptimizations_Object = MibTableColumn
mscAtmIfVptPnniEbrTotalPathOptimizations = _MscAtmIfVptPnniEbrTotalPathOptimizations_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 7, 40, 1, 2),
    _MscAtmIfVptPnniEbrTotalPathOptimizations_Type()
)
mscAtmIfVptPnniEbrTotalPathOptimizations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniEbrTotalPathOptimizations.setStatus("mandatory")
_MscAtmIfVptUniEbr_ObjectIdentity = ObjectIdentity
mscAtmIfVptUniEbr = _MscAtmIfVptUniEbr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 7)
)
_MscAtmIfVptUniEbrRowStatusTable_Object = MibTable
mscAtmIfVptUniEbrRowStatusTable = _MscAtmIfVptUniEbrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 7, 1)
)
if mibBuilder.loadTexts:
    mscAtmIfVptUniEbrRowStatusTable.setStatus("mandatory")
_MscAtmIfVptUniEbrRowStatusEntry_Object = MibTableRow
mscAtmIfVptUniEbrRowStatusEntry = _MscAtmIfVptUniEbrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 7, 1, 1)
)
mscAtmIfVptUniEbrRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfVptUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmEbrMIB", "mscAtmIfVptUniEbrIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptUniEbrRowStatusEntry.setStatus("mandatory")
_MscAtmIfVptUniEbrRowStatus_Type = RowStatus
_MscAtmIfVptUniEbrRowStatus_Object = MibTableColumn
mscAtmIfVptUniEbrRowStatus = _MscAtmIfVptUniEbrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 7, 1, 1, 1),
    _MscAtmIfVptUniEbrRowStatus_Type()
)
mscAtmIfVptUniEbrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptUniEbrRowStatus.setStatus("mandatory")
_MscAtmIfVptUniEbrComponentName_Type = DisplayString
_MscAtmIfVptUniEbrComponentName_Object = MibTableColumn
mscAtmIfVptUniEbrComponentName = _MscAtmIfVptUniEbrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 7, 1, 1, 2),
    _MscAtmIfVptUniEbrComponentName_Type()
)
mscAtmIfVptUniEbrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptUniEbrComponentName.setStatus("mandatory")
_MscAtmIfVptUniEbrStorageType_Type = StorageType
_MscAtmIfVptUniEbrStorageType_Object = MibTableColumn
mscAtmIfVptUniEbrStorageType = _MscAtmIfVptUniEbrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 7, 1, 1, 4),
    _MscAtmIfVptUniEbrStorageType_Type()
)
mscAtmIfVptUniEbrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptUniEbrStorageType.setStatus("mandatory")
_MscAtmIfVptUniEbrIndex_Type = NonReplicated
_MscAtmIfVptUniEbrIndex_Object = MibTableColumn
mscAtmIfVptUniEbrIndex = _MscAtmIfVptUniEbrIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 7, 1, 1, 10),
    _MscAtmIfVptUniEbrIndex_Type()
)
mscAtmIfVptUniEbrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmIfVptUniEbrIndex.setStatus("mandatory")
_MscAtmIfVptUniEbrProvTable_Object = MibTable
mscAtmIfVptUniEbrProvTable = _MscAtmIfVptUniEbrProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 7, 20)
)
if mibBuilder.loadTexts:
    mscAtmIfVptUniEbrProvTable.setStatus("mandatory")
_MscAtmIfVptUniEbrProvEntry_Object = MibTableRow
mscAtmIfVptUniEbrProvEntry = _MscAtmIfVptUniEbrProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 7, 20, 1)
)
mscAtmIfVptUniEbrProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfVptUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmEbrMIB", "mscAtmIfVptUniEbrIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptUniEbrProvEntry.setStatus("mandatory")


class _MscAtmIfVptUniEbrConnectionRecovery_Type(OctetString):
    """Custom type mscAtmIfVptUniEbrConnectionRecovery based on OctetString"""
    defaultHexValue = "c0"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscAtmIfVptUniEbrConnectionRecovery_Type.__name__ = "OctetString"
_MscAtmIfVptUniEbrConnectionRecovery_Object = MibTableColumn
mscAtmIfVptUniEbrConnectionRecovery = _MscAtmIfVptUniEbrConnectionRecovery_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 7, 20, 1, 1),
    _MscAtmIfVptUniEbrConnectionRecovery_Type()
)
mscAtmIfVptUniEbrConnectionRecovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptUniEbrConnectionRecovery.setStatus("mandatory")


class _MscAtmIfVptUniEbrPathOptimization_Type(OctetString):
    """Custom type mscAtmIfVptUniEbrPathOptimization based on OctetString"""
    defaultHexValue = "c0"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscAtmIfVptUniEbrPathOptimization_Type.__name__ = "OctetString"
_MscAtmIfVptUniEbrPathOptimization_Object = MibTableColumn
mscAtmIfVptUniEbrPathOptimization = _MscAtmIfVptUniEbrPathOptimization_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 7, 20, 1, 2),
    _MscAtmIfVptUniEbrPathOptimization_Type()
)
mscAtmIfVptUniEbrPathOptimization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptUniEbrPathOptimization.setStatus("mandatory")
_MscAtmIfVptUniEbrOperTable_Object = MibTable
mscAtmIfVptUniEbrOperTable = _MscAtmIfVptUniEbrOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 7, 30)
)
if mibBuilder.loadTexts:
    mscAtmIfVptUniEbrOperTable.setStatus("mandatory")
_MscAtmIfVptUniEbrOperEntry_Object = MibTableRow
mscAtmIfVptUniEbrOperEntry = _MscAtmIfVptUniEbrOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 7, 30, 1)
)
mscAtmIfVptUniEbrOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfVptUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmEbrMIB", "mscAtmIfVptUniEbrIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptUniEbrOperEntry.setStatus("mandatory")


class _MscAtmIfVptUniEbrSubscribedConnections_Type(Gauge32):
    """Custom type mscAtmIfVptUniEbrSubscribedConnections based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscAtmIfVptUniEbrSubscribedConnections_Type.__name__ = "Gauge32"
_MscAtmIfVptUniEbrSubscribedConnections_Object = MibTableColumn
mscAtmIfVptUniEbrSubscribedConnections = _MscAtmIfVptUniEbrSubscribedConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 7, 30, 1, 1),
    _MscAtmIfVptUniEbrSubscribedConnections_Type()
)
mscAtmIfVptUniEbrSubscribedConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptUniEbrSubscribedConnections.setStatus("mandatory")


class _MscAtmIfVptUniEbrEligibleRecoveredConnections_Type(Gauge32):
    """Custom type mscAtmIfVptUniEbrEligibleRecoveredConnections based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscAtmIfVptUniEbrEligibleRecoveredConnections_Type.__name__ = "Gauge32"
_MscAtmIfVptUniEbrEligibleRecoveredConnections_Object = MibTableColumn
mscAtmIfVptUniEbrEligibleRecoveredConnections = _MscAtmIfVptUniEbrEligibleRecoveredConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 7, 30, 1, 2),
    _MscAtmIfVptUniEbrEligibleRecoveredConnections_Type()
)
mscAtmIfVptUniEbrEligibleRecoveredConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptUniEbrEligibleRecoveredConnections.setStatus("mandatory")


class _MscAtmIfVptUniEbrIneligibleRecoveredConnections_Type(Gauge32):
    """Custom type mscAtmIfVptUniEbrIneligibleRecoveredConnections based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscAtmIfVptUniEbrIneligibleRecoveredConnections_Type.__name__ = "Gauge32"
_MscAtmIfVptUniEbrIneligibleRecoveredConnections_Object = MibTableColumn
mscAtmIfVptUniEbrIneligibleRecoveredConnections = _MscAtmIfVptUniEbrIneligibleRecoveredConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 7, 30, 1, 3),
    _MscAtmIfVptUniEbrIneligibleRecoveredConnections_Type()
)
mscAtmIfVptUniEbrIneligibleRecoveredConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptUniEbrIneligibleRecoveredConnections.setStatus("mandatory")
_MscAtmIfVptUniEbrStatsTable_Object = MibTable
mscAtmIfVptUniEbrStatsTable = _MscAtmIfVptUniEbrStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 7, 40)
)
if mibBuilder.loadTexts:
    mscAtmIfVptUniEbrStatsTable.setStatus("mandatory")
_MscAtmIfVptUniEbrStatsEntry_Object = MibTableRow
mscAtmIfVptUniEbrStatsEntry = _MscAtmIfVptUniEbrStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 7, 40, 1)
)
mscAtmIfVptUniEbrStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfVptUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmEbrMIB", "mscAtmIfVptUniEbrIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptUniEbrStatsEntry.setStatus("mandatory")
_MscAtmIfVptUniEbrTotalConnectionRecoveries_Type = Counter32
_MscAtmIfVptUniEbrTotalConnectionRecoveries_Object = MibTableColumn
mscAtmIfVptUniEbrTotalConnectionRecoveries = _MscAtmIfVptUniEbrTotalConnectionRecoveries_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 7, 40, 1, 1),
    _MscAtmIfVptUniEbrTotalConnectionRecoveries_Type()
)
mscAtmIfVptUniEbrTotalConnectionRecoveries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptUniEbrTotalConnectionRecoveries.setStatus("mandatory")
_MscAtmIfVptUniEbrTotalPathOptimizations_Type = Counter32
_MscAtmIfVptUniEbrTotalPathOptimizations_Object = MibTableColumn
mscAtmIfVptUniEbrTotalPathOptimizations = _MscAtmIfVptUniEbrTotalPathOptimizations_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 7, 40, 1, 2),
    _MscAtmIfVptUniEbrTotalPathOptimizations_Type()
)
mscAtmIfVptUniEbrTotalPathOptimizations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptUniEbrTotalPathOptimizations.setStatus("mandatory")
_MscAtmIfVptVccSrcEbrOv_ObjectIdentity = ObjectIdentity
mscAtmIfVptVccSrcEbrOv = _MscAtmIfVptVccSrcEbrOv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 8, 2)
)
_MscAtmIfVptVccSrcEbrOvRowStatusTable_Object = MibTable
mscAtmIfVptVccSrcEbrOvRowStatusTable = _MscAtmIfVptVccSrcEbrOvRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 8, 2, 1)
)
if mibBuilder.loadTexts:
    mscAtmIfVptVccSrcEbrOvRowStatusTable.setStatus("mandatory")
_MscAtmIfVptVccSrcEbrOvRowStatusEntry_Object = MibTableRow
mscAtmIfVptVccSrcEbrOvRowStatusEntry = _MscAtmIfVptVccSrcEbrOvRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 8, 2, 1, 1)
)
mscAtmIfVptVccSrcEbrOvRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptVccIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscAtmIfVptVccSrcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmEbrMIB", "mscAtmIfVptVccSrcEbrOvIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptVccSrcEbrOvRowStatusEntry.setStatus("mandatory")
_MscAtmIfVptVccSrcEbrOvRowStatus_Type = RowStatus
_MscAtmIfVptVccSrcEbrOvRowStatus_Object = MibTableColumn
mscAtmIfVptVccSrcEbrOvRowStatus = _MscAtmIfVptVccSrcEbrOvRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 8, 2, 1, 1, 1),
    _MscAtmIfVptVccSrcEbrOvRowStatus_Type()
)
mscAtmIfVptVccSrcEbrOvRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptVccSrcEbrOvRowStatus.setStatus("mandatory")
_MscAtmIfVptVccSrcEbrOvComponentName_Type = DisplayString
_MscAtmIfVptVccSrcEbrOvComponentName_Object = MibTableColumn
mscAtmIfVptVccSrcEbrOvComponentName = _MscAtmIfVptVccSrcEbrOvComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 8, 2, 1, 1, 2),
    _MscAtmIfVptVccSrcEbrOvComponentName_Type()
)
mscAtmIfVptVccSrcEbrOvComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptVccSrcEbrOvComponentName.setStatus("mandatory")
_MscAtmIfVptVccSrcEbrOvStorageType_Type = StorageType
_MscAtmIfVptVccSrcEbrOvStorageType_Object = MibTableColumn
mscAtmIfVptVccSrcEbrOvStorageType = _MscAtmIfVptVccSrcEbrOvStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 8, 2, 1, 1, 4),
    _MscAtmIfVptVccSrcEbrOvStorageType_Type()
)
mscAtmIfVptVccSrcEbrOvStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptVccSrcEbrOvStorageType.setStatus("mandatory")
_MscAtmIfVptVccSrcEbrOvIndex_Type = NonReplicated
_MscAtmIfVptVccSrcEbrOvIndex_Object = MibTableColumn
mscAtmIfVptVccSrcEbrOvIndex = _MscAtmIfVptVccSrcEbrOvIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 8, 2, 1, 1, 10),
    _MscAtmIfVptVccSrcEbrOvIndex_Type()
)
mscAtmIfVptVccSrcEbrOvIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmIfVptVccSrcEbrOvIndex.setStatus("mandatory")
_MscAtmIfVptVccSrcEbrOvProvTable_Object = MibTable
mscAtmIfVptVccSrcEbrOvProvTable = _MscAtmIfVptVccSrcEbrOvProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 8, 2, 20)
)
if mibBuilder.loadTexts:
    mscAtmIfVptVccSrcEbrOvProvTable.setStatus("mandatory")
_MscAtmIfVptVccSrcEbrOvProvEntry_Object = MibTableRow
mscAtmIfVptVccSrcEbrOvProvEntry = _MscAtmIfVptVccSrcEbrOvProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 8, 2, 20, 1)
)
mscAtmIfVptVccSrcEbrOvProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptVccIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscAtmIfVptVccSrcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmEbrMIB", "mscAtmIfVptVccSrcEbrOvIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptVccSrcEbrOvProvEntry.setStatus("mandatory")


class _MscAtmIfVptVccSrcEbrOvRecoverySubscribed_Type(Integer32):
    """Custom type mscAtmIfVptVccSrcEbrOvRecoverySubscribed based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_MscAtmIfVptVccSrcEbrOvRecoverySubscribed_Type.__name__ = "Integer32"
_MscAtmIfVptVccSrcEbrOvRecoverySubscribed_Object = MibTableColumn
mscAtmIfVptVccSrcEbrOvRecoverySubscribed = _MscAtmIfVptVccSrcEbrOvRecoverySubscribed_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 8, 2, 20, 1, 1),
    _MscAtmIfVptVccSrcEbrOvRecoverySubscribed_Type()
)
mscAtmIfVptVccSrcEbrOvRecoverySubscribed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptVccSrcEbrOvRecoverySubscribed.setStatus("mandatory")


class _MscAtmIfVptVccSrcEbrOvOptimizationSubscribed_Type(Integer32):
    """Custom type mscAtmIfVptVccSrcEbrOvOptimizationSubscribed based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_MscAtmIfVptVccSrcEbrOvOptimizationSubscribed_Type.__name__ = "Integer32"
_MscAtmIfVptVccSrcEbrOvOptimizationSubscribed_Object = MibTableColumn
mscAtmIfVptVccSrcEbrOvOptimizationSubscribed = _MscAtmIfVptVccSrcEbrOvOptimizationSubscribed_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 8, 2, 20, 1, 2),
    _MscAtmIfVptVccSrcEbrOvOptimizationSubscribed_Type()
)
mscAtmIfVptVccSrcEbrOvOptimizationSubscribed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptVccSrcEbrOvOptimizationSubscribed.setStatus("mandatory")
_MscAtmIfVptVccEbrInfo_ObjectIdentity = ObjectIdentity
mscAtmIfVptVccEbrInfo = _MscAtmIfVptVccEbrInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 12)
)
_MscAtmIfVptVccEbrInfoRowStatusTable_Object = MibTable
mscAtmIfVptVccEbrInfoRowStatusTable = _MscAtmIfVptVccEbrInfoRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 12, 1)
)
if mibBuilder.loadTexts:
    mscAtmIfVptVccEbrInfoRowStatusTable.setStatus("mandatory")
_MscAtmIfVptVccEbrInfoRowStatusEntry_Object = MibTableRow
mscAtmIfVptVccEbrInfoRowStatusEntry = _MscAtmIfVptVccEbrInfoRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 12, 1, 1)
)
mscAtmIfVptVccEbrInfoRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptVccIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmEbrMIB", "mscAtmIfVptVccEbrInfoIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptVccEbrInfoRowStatusEntry.setStatus("mandatory")
_MscAtmIfVptVccEbrInfoRowStatus_Type = RowStatus
_MscAtmIfVptVccEbrInfoRowStatus_Object = MibTableColumn
mscAtmIfVptVccEbrInfoRowStatus = _MscAtmIfVptVccEbrInfoRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 12, 1, 1, 1),
    _MscAtmIfVptVccEbrInfoRowStatus_Type()
)
mscAtmIfVptVccEbrInfoRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptVccEbrInfoRowStatus.setStatus("mandatory")
_MscAtmIfVptVccEbrInfoComponentName_Type = DisplayString
_MscAtmIfVptVccEbrInfoComponentName_Object = MibTableColumn
mscAtmIfVptVccEbrInfoComponentName = _MscAtmIfVptVccEbrInfoComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 12, 1, 1, 2),
    _MscAtmIfVptVccEbrInfoComponentName_Type()
)
mscAtmIfVptVccEbrInfoComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptVccEbrInfoComponentName.setStatus("mandatory")
_MscAtmIfVptVccEbrInfoStorageType_Type = StorageType
_MscAtmIfVptVccEbrInfoStorageType_Object = MibTableColumn
mscAtmIfVptVccEbrInfoStorageType = _MscAtmIfVptVccEbrInfoStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 12, 1, 1, 4),
    _MscAtmIfVptVccEbrInfoStorageType_Type()
)
mscAtmIfVptVccEbrInfoStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptVccEbrInfoStorageType.setStatus("mandatory")
_MscAtmIfVptVccEbrInfoIndex_Type = NonReplicated
_MscAtmIfVptVccEbrInfoIndex_Object = MibTableColumn
mscAtmIfVptVccEbrInfoIndex = _MscAtmIfVptVccEbrInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 12, 1, 1, 10),
    _MscAtmIfVptVccEbrInfoIndex_Type()
)
mscAtmIfVptVccEbrInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmIfVptVccEbrInfoIndex.setStatus("mandatory")
_MscAtmIfVptVccEbrInfoOperTable_Object = MibTable
mscAtmIfVptVccEbrInfoOperTable = _MscAtmIfVptVccEbrInfoOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 12, 30)
)
if mibBuilder.loadTexts:
    mscAtmIfVptVccEbrInfoOperTable.setStatus("mandatory")
_MscAtmIfVptVccEbrInfoOperEntry_Object = MibTableRow
mscAtmIfVptVccEbrInfoOperEntry = _MscAtmIfVptVccEbrInfoOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 12, 30, 1)
)
mscAtmIfVptVccEbrInfoOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptVccIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmEbrMIB", "mscAtmIfVptVccEbrInfoIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptVccEbrInfoOperEntry.setStatus("mandatory")


class _MscAtmIfVptVccEbrInfoRecoverySubscribed_Type(Integer32):
    """Custom type mscAtmIfVptVccEbrInfoRecoverySubscribed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_MscAtmIfVptVccEbrInfoRecoverySubscribed_Type.__name__ = "Integer32"
_MscAtmIfVptVccEbrInfoRecoverySubscribed_Object = MibTableColumn
mscAtmIfVptVccEbrInfoRecoverySubscribed = _MscAtmIfVptVccEbrInfoRecoverySubscribed_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 12, 30, 1, 1),
    _MscAtmIfVptVccEbrInfoRecoverySubscribed_Type()
)
mscAtmIfVptVccEbrInfoRecoverySubscribed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptVccEbrInfoRecoverySubscribed.setStatus("mandatory")


class _MscAtmIfVptVccEbrInfoOptimizationSubscribed_Type(Integer32):
    """Custom type mscAtmIfVptVccEbrInfoOptimizationSubscribed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_MscAtmIfVptVccEbrInfoOptimizationSubscribed_Type.__name__ = "Integer32"
_MscAtmIfVptVccEbrInfoOptimizationSubscribed_Object = MibTableColumn
mscAtmIfVptVccEbrInfoOptimizationSubscribed = _MscAtmIfVptVccEbrInfoOptimizationSubscribed_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 12, 30, 1, 2),
    _MscAtmIfVptVccEbrInfoOptimizationSubscribed_Type()
)
mscAtmIfVptVccEbrInfoOptimizationSubscribed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptVccEbrInfoOptimizationSubscribed.setStatus("mandatory")


class _MscAtmIfVptVccEbrInfoConnectionRecovered_Type(Integer32):
    """Custom type mscAtmIfVptVccEbrInfoConnectionRecovered based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_MscAtmIfVptVccEbrInfoConnectionRecovered_Type.__name__ = "Integer32"
_MscAtmIfVptVccEbrInfoConnectionRecovered_Object = MibTableColumn
mscAtmIfVptVccEbrInfoConnectionRecovered = _MscAtmIfVptVccEbrInfoConnectionRecovered_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 12, 30, 1, 3),
    _MscAtmIfVptVccEbrInfoConnectionRecovered_Type()
)
mscAtmIfVptVccEbrInfoConnectionRecovered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptVccEbrInfoConnectionRecovered.setStatus("mandatory")
_MscAtmIfVptVccEbrInfoStatsTable_Object = MibTable
mscAtmIfVptVccEbrInfoStatsTable = _MscAtmIfVptVccEbrInfoStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 12, 40)
)
if mibBuilder.loadTexts:
    mscAtmIfVptVccEbrInfoStatsTable.setStatus("mandatory")
_MscAtmIfVptVccEbrInfoStatsEntry_Object = MibTableRow
mscAtmIfVptVccEbrInfoStatsEntry = _MscAtmIfVptVccEbrInfoStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 12, 40, 1)
)
mscAtmIfVptVccEbrInfoStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptVccIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmEbrMIB", "mscAtmIfVptVccEbrInfoIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptVccEbrInfoStatsEntry.setStatus("mandatory")
_MscAtmIfVptVccEbrInfoTotalConnectionRecoveries_Type = Counter32
_MscAtmIfVptVccEbrInfoTotalConnectionRecoveries_Object = MibTableColumn
mscAtmIfVptVccEbrInfoTotalConnectionRecoveries = _MscAtmIfVptVccEbrInfoTotalConnectionRecoveries_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 12, 40, 1, 1),
    _MscAtmIfVptVccEbrInfoTotalConnectionRecoveries_Type()
)
mscAtmIfVptVccEbrInfoTotalConnectionRecoveries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptVccEbrInfoTotalConnectionRecoveries.setStatus("mandatory")
_MscAtmIfVptVccEbrInfoTotalPathOptimizations_Type = Counter32
_MscAtmIfVptVccEbrInfoTotalPathOptimizations_Object = MibTableColumn
mscAtmIfVptVccEbrInfoTotalPathOptimizations = _MscAtmIfVptVccEbrInfoTotalPathOptimizations_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 12, 40, 1, 2),
    _MscAtmIfVptVccEbrInfoTotalPathOptimizations_Type()
)
mscAtmIfVptVccEbrInfoTotalPathOptimizations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptVccEbrInfoTotalPathOptimizations.setStatus("mandatory")
_MscAtmIfPnniEbr_ObjectIdentity = ObjectIdentity
mscAtmIfPnniEbr = _MscAtmIfPnniEbr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 7)
)
_MscAtmIfPnniEbrRowStatusTable_Object = MibTable
mscAtmIfPnniEbrRowStatusTable = _MscAtmIfPnniEbrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 7, 1)
)
if mibBuilder.loadTexts:
    mscAtmIfPnniEbrRowStatusTable.setStatus("mandatory")
_MscAtmIfPnniEbrRowStatusEntry_Object = MibTableRow
mscAtmIfPnniEbrRowStatusEntry = _MscAtmIfPnniEbrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 7, 1, 1)
)
mscAtmIfPnniEbrRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfPnniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmEbrMIB", "mscAtmIfPnniEbrIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfPnniEbrRowStatusEntry.setStatus("mandatory")
_MscAtmIfPnniEbrRowStatus_Type = RowStatus
_MscAtmIfPnniEbrRowStatus_Object = MibTableColumn
mscAtmIfPnniEbrRowStatus = _MscAtmIfPnniEbrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 7, 1, 1, 1),
    _MscAtmIfPnniEbrRowStatus_Type()
)
mscAtmIfPnniEbrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfPnniEbrRowStatus.setStatus("mandatory")
_MscAtmIfPnniEbrComponentName_Type = DisplayString
_MscAtmIfPnniEbrComponentName_Object = MibTableColumn
mscAtmIfPnniEbrComponentName = _MscAtmIfPnniEbrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 7, 1, 1, 2),
    _MscAtmIfPnniEbrComponentName_Type()
)
mscAtmIfPnniEbrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfPnniEbrComponentName.setStatus("mandatory")
_MscAtmIfPnniEbrStorageType_Type = StorageType
_MscAtmIfPnniEbrStorageType_Object = MibTableColumn
mscAtmIfPnniEbrStorageType = _MscAtmIfPnniEbrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 7, 1, 1, 4),
    _MscAtmIfPnniEbrStorageType_Type()
)
mscAtmIfPnniEbrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfPnniEbrStorageType.setStatus("mandatory")
_MscAtmIfPnniEbrIndex_Type = NonReplicated
_MscAtmIfPnniEbrIndex_Object = MibTableColumn
mscAtmIfPnniEbrIndex = _MscAtmIfPnniEbrIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 7, 1, 1, 10),
    _MscAtmIfPnniEbrIndex_Type()
)
mscAtmIfPnniEbrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmIfPnniEbrIndex.setStatus("mandatory")
_MscAtmIfPnniEbrProvTable_Object = MibTable
mscAtmIfPnniEbrProvTable = _MscAtmIfPnniEbrProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 7, 20)
)
if mibBuilder.loadTexts:
    mscAtmIfPnniEbrProvTable.setStatus("mandatory")
_MscAtmIfPnniEbrProvEntry_Object = MibTableRow
mscAtmIfPnniEbrProvEntry = _MscAtmIfPnniEbrProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 7, 20, 1)
)
mscAtmIfPnniEbrProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfPnniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmEbrMIB", "mscAtmIfPnniEbrIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfPnniEbrProvEntry.setStatus("mandatory")


class _MscAtmIfPnniEbrConnectionRecovery_Type(OctetString):
    """Custom type mscAtmIfPnniEbrConnectionRecovery based on OctetString"""
    defaultHexValue = "c0"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscAtmIfPnniEbrConnectionRecovery_Type.__name__ = "OctetString"
_MscAtmIfPnniEbrConnectionRecovery_Object = MibTableColumn
mscAtmIfPnniEbrConnectionRecovery = _MscAtmIfPnniEbrConnectionRecovery_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 7, 20, 1, 1),
    _MscAtmIfPnniEbrConnectionRecovery_Type()
)
mscAtmIfPnniEbrConnectionRecovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfPnniEbrConnectionRecovery.setStatus("mandatory")


class _MscAtmIfPnniEbrPathOptimization_Type(OctetString):
    """Custom type mscAtmIfPnniEbrPathOptimization based on OctetString"""
    defaultHexValue = "c0"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscAtmIfPnniEbrPathOptimization_Type.__name__ = "OctetString"
_MscAtmIfPnniEbrPathOptimization_Object = MibTableColumn
mscAtmIfPnniEbrPathOptimization = _MscAtmIfPnniEbrPathOptimization_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 7, 20, 1, 2),
    _MscAtmIfPnniEbrPathOptimization_Type()
)
mscAtmIfPnniEbrPathOptimization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfPnniEbrPathOptimization.setStatus("mandatory")
_MscAtmIfPnniEbrOperTable_Object = MibTable
mscAtmIfPnniEbrOperTable = _MscAtmIfPnniEbrOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 7, 30)
)
if mibBuilder.loadTexts:
    mscAtmIfPnniEbrOperTable.setStatus("mandatory")
_MscAtmIfPnniEbrOperEntry_Object = MibTableRow
mscAtmIfPnniEbrOperEntry = _MscAtmIfPnniEbrOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 7, 30, 1)
)
mscAtmIfPnniEbrOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfPnniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmEbrMIB", "mscAtmIfPnniEbrIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfPnniEbrOperEntry.setStatus("mandatory")


class _MscAtmIfPnniEbrSubscribedConnections_Type(Gauge32):
    """Custom type mscAtmIfPnniEbrSubscribedConnections based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscAtmIfPnniEbrSubscribedConnections_Type.__name__ = "Gauge32"
_MscAtmIfPnniEbrSubscribedConnections_Object = MibTableColumn
mscAtmIfPnniEbrSubscribedConnections = _MscAtmIfPnniEbrSubscribedConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 7, 30, 1, 1),
    _MscAtmIfPnniEbrSubscribedConnections_Type()
)
mscAtmIfPnniEbrSubscribedConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfPnniEbrSubscribedConnections.setStatus("mandatory")


class _MscAtmIfPnniEbrEligibleRecoveredConnections_Type(Gauge32):
    """Custom type mscAtmIfPnniEbrEligibleRecoveredConnections based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscAtmIfPnniEbrEligibleRecoveredConnections_Type.__name__ = "Gauge32"
_MscAtmIfPnniEbrEligibleRecoveredConnections_Object = MibTableColumn
mscAtmIfPnniEbrEligibleRecoveredConnections = _MscAtmIfPnniEbrEligibleRecoveredConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 7, 30, 1, 2),
    _MscAtmIfPnniEbrEligibleRecoveredConnections_Type()
)
mscAtmIfPnniEbrEligibleRecoveredConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfPnniEbrEligibleRecoveredConnections.setStatus("mandatory")


class _MscAtmIfPnniEbrIneligibleRecoveredConnections_Type(Gauge32):
    """Custom type mscAtmIfPnniEbrIneligibleRecoveredConnections based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscAtmIfPnniEbrIneligibleRecoveredConnections_Type.__name__ = "Gauge32"
_MscAtmIfPnniEbrIneligibleRecoveredConnections_Object = MibTableColumn
mscAtmIfPnniEbrIneligibleRecoveredConnections = _MscAtmIfPnniEbrIneligibleRecoveredConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 7, 30, 1, 3),
    _MscAtmIfPnniEbrIneligibleRecoveredConnections_Type()
)
mscAtmIfPnniEbrIneligibleRecoveredConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfPnniEbrIneligibleRecoveredConnections.setStatus("mandatory")
_MscAtmIfPnniEbrStatsTable_Object = MibTable
mscAtmIfPnniEbrStatsTable = _MscAtmIfPnniEbrStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 7, 40)
)
if mibBuilder.loadTexts:
    mscAtmIfPnniEbrStatsTable.setStatus("mandatory")
_MscAtmIfPnniEbrStatsEntry_Object = MibTableRow
mscAtmIfPnniEbrStatsEntry = _MscAtmIfPnniEbrStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 7, 40, 1)
)
mscAtmIfPnniEbrStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfPnniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmEbrMIB", "mscAtmIfPnniEbrIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfPnniEbrStatsEntry.setStatus("mandatory")
_MscAtmIfPnniEbrTotalConnectionRecoveries_Type = Counter32
_MscAtmIfPnniEbrTotalConnectionRecoveries_Object = MibTableColumn
mscAtmIfPnniEbrTotalConnectionRecoveries = _MscAtmIfPnniEbrTotalConnectionRecoveries_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 7, 40, 1, 1),
    _MscAtmIfPnniEbrTotalConnectionRecoveries_Type()
)
mscAtmIfPnniEbrTotalConnectionRecoveries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfPnniEbrTotalConnectionRecoveries.setStatus("mandatory")
_MscAtmIfPnniEbrTotalPathOptimizations_Type = Counter32
_MscAtmIfPnniEbrTotalPathOptimizations_Object = MibTableColumn
mscAtmIfPnniEbrTotalPathOptimizations = _MscAtmIfPnniEbrTotalPathOptimizations_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 7, 40, 1, 2),
    _MscAtmIfPnniEbrTotalPathOptimizations_Type()
)
mscAtmIfPnniEbrTotalPathOptimizations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfPnniEbrTotalPathOptimizations.setStatus("mandatory")
_AtmEbrMIB_ObjectIdentity = ObjectIdentity
atmEbrMIB = _AtmEbrMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 159)
)
_AtmEbrGroup_ObjectIdentity = ObjectIdentity
atmEbrGroup = _AtmEbrGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 159, 1)
)
_AtmEbrGroupCA_ObjectIdentity = ObjectIdentity
atmEbrGroupCA = _AtmEbrGroupCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 159, 1, 1)
)
_AtmEbrGroupCA02_ObjectIdentity = ObjectIdentity
atmEbrGroupCA02 = _AtmEbrGroupCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 159, 1, 1, 3)
)
_AtmEbrGroupCA02A_ObjectIdentity = ObjectIdentity
atmEbrGroupCA02A = _AtmEbrGroupCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 159, 1, 1, 3, 2)
)
_AtmEbrCapabilities_ObjectIdentity = ObjectIdentity
atmEbrCapabilities = _AtmEbrCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 159, 3)
)
_AtmEbrCapabilitiesCA_ObjectIdentity = ObjectIdentity
atmEbrCapabilitiesCA = _AtmEbrCapabilitiesCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 159, 3, 1)
)
_AtmEbrCapabilitiesCA02_ObjectIdentity = ObjectIdentity
atmEbrCapabilitiesCA02 = _AtmEbrCapabilitiesCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 159, 3, 1, 3)
)
_AtmEbrCapabilitiesCA02A_ObjectIdentity = ObjectIdentity
atmEbrCapabilitiesCA02A = _AtmEbrCapabilitiesCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 159, 3, 1, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-MsCarrier-MscPassport-AtmEbrMIB",
    **{"mscAtmIfVpcSrcEbrOv": mscAtmIfVpcSrcEbrOv,
       "mscAtmIfVpcSrcEbrOvRowStatusTable": mscAtmIfVpcSrcEbrOvRowStatusTable,
       "mscAtmIfVpcSrcEbrOvRowStatusEntry": mscAtmIfVpcSrcEbrOvRowStatusEntry,
       "mscAtmIfVpcSrcEbrOvRowStatus": mscAtmIfVpcSrcEbrOvRowStatus,
       "mscAtmIfVpcSrcEbrOvComponentName": mscAtmIfVpcSrcEbrOvComponentName,
       "mscAtmIfVpcSrcEbrOvStorageType": mscAtmIfVpcSrcEbrOvStorageType,
       "mscAtmIfVpcSrcEbrOvIndex": mscAtmIfVpcSrcEbrOvIndex,
       "mscAtmIfVpcSrcEbrOvProvTable": mscAtmIfVpcSrcEbrOvProvTable,
       "mscAtmIfVpcSrcEbrOvProvEntry": mscAtmIfVpcSrcEbrOvProvEntry,
       "mscAtmIfVpcSrcEbrOvRecoverySubscribed": mscAtmIfVpcSrcEbrOvRecoverySubscribed,
       "mscAtmIfVpcSrcEbrOvOptimizationSubscribed": mscAtmIfVpcSrcEbrOvOptimizationSubscribed,
       "mscAtmIfVpcEbrInfo": mscAtmIfVpcEbrInfo,
       "mscAtmIfVpcEbrInfoRowStatusTable": mscAtmIfVpcEbrInfoRowStatusTable,
       "mscAtmIfVpcEbrInfoRowStatusEntry": mscAtmIfVpcEbrInfoRowStatusEntry,
       "mscAtmIfVpcEbrInfoRowStatus": mscAtmIfVpcEbrInfoRowStatus,
       "mscAtmIfVpcEbrInfoComponentName": mscAtmIfVpcEbrInfoComponentName,
       "mscAtmIfVpcEbrInfoStorageType": mscAtmIfVpcEbrInfoStorageType,
       "mscAtmIfVpcEbrInfoIndex": mscAtmIfVpcEbrInfoIndex,
       "mscAtmIfVpcEbrInfoOperTable": mscAtmIfVpcEbrInfoOperTable,
       "mscAtmIfVpcEbrInfoOperEntry": mscAtmIfVpcEbrInfoOperEntry,
       "mscAtmIfVpcEbrInfoRecoverySubscribed": mscAtmIfVpcEbrInfoRecoverySubscribed,
       "mscAtmIfVpcEbrInfoOptimizationSubscribed": mscAtmIfVpcEbrInfoOptimizationSubscribed,
       "mscAtmIfVpcEbrInfoConnectionRecovered": mscAtmIfVpcEbrInfoConnectionRecovered,
       "mscAtmIfVpcEbrInfoStatsTable": mscAtmIfVpcEbrInfoStatsTable,
       "mscAtmIfVpcEbrInfoStatsEntry": mscAtmIfVpcEbrInfoStatsEntry,
       "mscAtmIfVpcEbrInfoTotalConnectionRecoveries": mscAtmIfVpcEbrInfoTotalConnectionRecoveries,
       "mscAtmIfVpcEbrInfoTotalPathOptimizations": mscAtmIfVpcEbrInfoTotalPathOptimizations,
       "mscAtmIfVccSrcEbrOv": mscAtmIfVccSrcEbrOv,
       "mscAtmIfVccSrcEbrOvRowStatusTable": mscAtmIfVccSrcEbrOvRowStatusTable,
       "mscAtmIfVccSrcEbrOvRowStatusEntry": mscAtmIfVccSrcEbrOvRowStatusEntry,
       "mscAtmIfVccSrcEbrOvRowStatus": mscAtmIfVccSrcEbrOvRowStatus,
       "mscAtmIfVccSrcEbrOvComponentName": mscAtmIfVccSrcEbrOvComponentName,
       "mscAtmIfVccSrcEbrOvStorageType": mscAtmIfVccSrcEbrOvStorageType,
       "mscAtmIfVccSrcEbrOvIndex": mscAtmIfVccSrcEbrOvIndex,
       "mscAtmIfVccSrcEbrOvProvTable": mscAtmIfVccSrcEbrOvProvTable,
       "mscAtmIfVccSrcEbrOvProvEntry": mscAtmIfVccSrcEbrOvProvEntry,
       "mscAtmIfVccSrcEbrOvRecoverySubscribed": mscAtmIfVccSrcEbrOvRecoverySubscribed,
       "mscAtmIfVccSrcEbrOvOptimizationSubscribed": mscAtmIfVccSrcEbrOvOptimizationSubscribed,
       "mscAtmIfVccEbrInfo": mscAtmIfVccEbrInfo,
       "mscAtmIfVccEbrInfoRowStatusTable": mscAtmIfVccEbrInfoRowStatusTable,
       "mscAtmIfVccEbrInfoRowStatusEntry": mscAtmIfVccEbrInfoRowStatusEntry,
       "mscAtmIfVccEbrInfoRowStatus": mscAtmIfVccEbrInfoRowStatus,
       "mscAtmIfVccEbrInfoComponentName": mscAtmIfVccEbrInfoComponentName,
       "mscAtmIfVccEbrInfoStorageType": mscAtmIfVccEbrInfoStorageType,
       "mscAtmIfVccEbrInfoIndex": mscAtmIfVccEbrInfoIndex,
       "mscAtmIfVccEbrInfoOperTable": mscAtmIfVccEbrInfoOperTable,
       "mscAtmIfVccEbrInfoOperEntry": mscAtmIfVccEbrInfoOperEntry,
       "mscAtmIfVccEbrInfoRecoverySubscribed": mscAtmIfVccEbrInfoRecoverySubscribed,
       "mscAtmIfVccEbrInfoOptimizationSubscribed": mscAtmIfVccEbrInfoOptimizationSubscribed,
       "mscAtmIfVccEbrInfoConnectionRecovered": mscAtmIfVccEbrInfoConnectionRecovered,
       "mscAtmIfVccEbrInfoStatsTable": mscAtmIfVccEbrInfoStatsTable,
       "mscAtmIfVccEbrInfoStatsEntry": mscAtmIfVccEbrInfoStatsEntry,
       "mscAtmIfVccEbrInfoTotalConnectionRecoveries": mscAtmIfVccEbrInfoTotalConnectionRecoveries,
       "mscAtmIfVccEbrInfoTotalPathOptimizations": mscAtmIfVccEbrInfoTotalPathOptimizations,
       "mscAtmIfUniEbr": mscAtmIfUniEbr,
       "mscAtmIfUniEbrRowStatusTable": mscAtmIfUniEbrRowStatusTable,
       "mscAtmIfUniEbrRowStatusEntry": mscAtmIfUniEbrRowStatusEntry,
       "mscAtmIfUniEbrRowStatus": mscAtmIfUniEbrRowStatus,
       "mscAtmIfUniEbrComponentName": mscAtmIfUniEbrComponentName,
       "mscAtmIfUniEbrStorageType": mscAtmIfUniEbrStorageType,
       "mscAtmIfUniEbrIndex": mscAtmIfUniEbrIndex,
       "mscAtmIfUniEbrProvTable": mscAtmIfUniEbrProvTable,
       "mscAtmIfUniEbrProvEntry": mscAtmIfUniEbrProvEntry,
       "mscAtmIfUniEbrConnectionRecovery": mscAtmIfUniEbrConnectionRecovery,
       "mscAtmIfUniEbrPathOptimization": mscAtmIfUniEbrPathOptimization,
       "mscAtmIfUniEbrOperTable": mscAtmIfUniEbrOperTable,
       "mscAtmIfUniEbrOperEntry": mscAtmIfUniEbrOperEntry,
       "mscAtmIfUniEbrSubscribedConnections": mscAtmIfUniEbrSubscribedConnections,
       "mscAtmIfUniEbrEligibleRecoveredConnections": mscAtmIfUniEbrEligibleRecoveredConnections,
       "mscAtmIfUniEbrIneligibleRecoveredConnections": mscAtmIfUniEbrIneligibleRecoveredConnections,
       "mscAtmIfUniEbrStatsTable": mscAtmIfUniEbrStatsTable,
       "mscAtmIfUniEbrStatsEntry": mscAtmIfUniEbrStatsEntry,
       "mscAtmIfUniEbrTotalConnectionRecoveries": mscAtmIfUniEbrTotalConnectionRecoveries,
       "mscAtmIfUniEbrTotalPathOptimizations": mscAtmIfUniEbrTotalPathOptimizations,
       "mscAtmIfIispEbr": mscAtmIfIispEbr,
       "mscAtmIfIispEbrRowStatusTable": mscAtmIfIispEbrRowStatusTable,
       "mscAtmIfIispEbrRowStatusEntry": mscAtmIfIispEbrRowStatusEntry,
       "mscAtmIfIispEbrRowStatus": mscAtmIfIispEbrRowStatus,
       "mscAtmIfIispEbrComponentName": mscAtmIfIispEbrComponentName,
       "mscAtmIfIispEbrStorageType": mscAtmIfIispEbrStorageType,
       "mscAtmIfIispEbrIndex": mscAtmIfIispEbrIndex,
       "mscAtmIfIispEbrProvTable": mscAtmIfIispEbrProvTable,
       "mscAtmIfIispEbrProvEntry": mscAtmIfIispEbrProvEntry,
       "mscAtmIfIispEbrConnectionRecovery": mscAtmIfIispEbrConnectionRecovery,
       "mscAtmIfIispEbrPathOptimization": mscAtmIfIispEbrPathOptimization,
       "mscAtmIfIispEbrOperTable": mscAtmIfIispEbrOperTable,
       "mscAtmIfIispEbrOperEntry": mscAtmIfIispEbrOperEntry,
       "mscAtmIfIispEbrSubscribedConnections": mscAtmIfIispEbrSubscribedConnections,
       "mscAtmIfIispEbrEligibleRecoveredConnections": mscAtmIfIispEbrEligibleRecoveredConnections,
       "mscAtmIfIispEbrIneligibleRecoveredConnections": mscAtmIfIispEbrIneligibleRecoveredConnections,
       "mscAtmIfIispEbrStatsTable": mscAtmIfIispEbrStatsTable,
       "mscAtmIfIispEbrStatsEntry": mscAtmIfIispEbrStatsEntry,
       "mscAtmIfIispEbrTotalConnectionRecoveries": mscAtmIfIispEbrTotalConnectionRecoveries,
       "mscAtmIfIispEbrTotalPathOptimizations": mscAtmIfIispEbrTotalPathOptimizations,
       "mscAtmIfVptIispEbr": mscAtmIfVptIispEbr,
       "mscAtmIfVptIispEbrRowStatusTable": mscAtmIfVptIispEbrRowStatusTable,
       "mscAtmIfVptIispEbrRowStatusEntry": mscAtmIfVptIispEbrRowStatusEntry,
       "mscAtmIfVptIispEbrRowStatus": mscAtmIfVptIispEbrRowStatus,
       "mscAtmIfVptIispEbrComponentName": mscAtmIfVptIispEbrComponentName,
       "mscAtmIfVptIispEbrStorageType": mscAtmIfVptIispEbrStorageType,
       "mscAtmIfVptIispEbrIndex": mscAtmIfVptIispEbrIndex,
       "mscAtmIfVptIispEbrProvTable": mscAtmIfVptIispEbrProvTable,
       "mscAtmIfVptIispEbrProvEntry": mscAtmIfVptIispEbrProvEntry,
       "mscAtmIfVptIispEbrConnectionRecovery": mscAtmIfVptIispEbrConnectionRecovery,
       "mscAtmIfVptIispEbrPathOptimization": mscAtmIfVptIispEbrPathOptimization,
       "mscAtmIfVptIispEbrOperTable": mscAtmIfVptIispEbrOperTable,
       "mscAtmIfVptIispEbrOperEntry": mscAtmIfVptIispEbrOperEntry,
       "mscAtmIfVptIispEbrSubscribedConnections": mscAtmIfVptIispEbrSubscribedConnections,
       "mscAtmIfVptIispEbrEligibleRecoveredConnections": mscAtmIfVptIispEbrEligibleRecoveredConnections,
       "mscAtmIfVptIispEbrIneligibleRecoveredConnections": mscAtmIfVptIispEbrIneligibleRecoveredConnections,
       "mscAtmIfVptIispEbrStatsTable": mscAtmIfVptIispEbrStatsTable,
       "mscAtmIfVptIispEbrStatsEntry": mscAtmIfVptIispEbrStatsEntry,
       "mscAtmIfVptIispEbrTotalConnectionRecoveries": mscAtmIfVptIispEbrTotalConnectionRecoveries,
       "mscAtmIfVptIispEbrTotalPathOptimizations": mscAtmIfVptIispEbrTotalPathOptimizations,
       "mscAtmIfVptPnniEbr": mscAtmIfVptPnniEbr,
       "mscAtmIfVptPnniEbrRowStatusTable": mscAtmIfVptPnniEbrRowStatusTable,
       "mscAtmIfVptPnniEbrRowStatusEntry": mscAtmIfVptPnniEbrRowStatusEntry,
       "mscAtmIfVptPnniEbrRowStatus": mscAtmIfVptPnniEbrRowStatus,
       "mscAtmIfVptPnniEbrComponentName": mscAtmIfVptPnniEbrComponentName,
       "mscAtmIfVptPnniEbrStorageType": mscAtmIfVptPnniEbrStorageType,
       "mscAtmIfVptPnniEbrIndex": mscAtmIfVptPnniEbrIndex,
       "mscAtmIfVptPnniEbrProvTable": mscAtmIfVptPnniEbrProvTable,
       "mscAtmIfVptPnniEbrProvEntry": mscAtmIfVptPnniEbrProvEntry,
       "mscAtmIfVptPnniEbrConnectionRecovery": mscAtmIfVptPnniEbrConnectionRecovery,
       "mscAtmIfVptPnniEbrPathOptimization": mscAtmIfVptPnniEbrPathOptimization,
       "mscAtmIfVptPnniEbrOperTable": mscAtmIfVptPnniEbrOperTable,
       "mscAtmIfVptPnniEbrOperEntry": mscAtmIfVptPnniEbrOperEntry,
       "mscAtmIfVptPnniEbrSubscribedConnections": mscAtmIfVptPnniEbrSubscribedConnections,
       "mscAtmIfVptPnniEbrEligibleRecoveredConnections": mscAtmIfVptPnniEbrEligibleRecoveredConnections,
       "mscAtmIfVptPnniEbrIneligibleRecoveredConnections": mscAtmIfVptPnniEbrIneligibleRecoveredConnections,
       "mscAtmIfVptPnniEbrStatsTable": mscAtmIfVptPnniEbrStatsTable,
       "mscAtmIfVptPnniEbrStatsEntry": mscAtmIfVptPnniEbrStatsEntry,
       "mscAtmIfVptPnniEbrTotalConnectionRecoveries": mscAtmIfVptPnniEbrTotalConnectionRecoveries,
       "mscAtmIfVptPnniEbrTotalPathOptimizations": mscAtmIfVptPnniEbrTotalPathOptimizations,
       "mscAtmIfVptUniEbr": mscAtmIfVptUniEbr,
       "mscAtmIfVptUniEbrRowStatusTable": mscAtmIfVptUniEbrRowStatusTable,
       "mscAtmIfVptUniEbrRowStatusEntry": mscAtmIfVptUniEbrRowStatusEntry,
       "mscAtmIfVptUniEbrRowStatus": mscAtmIfVptUniEbrRowStatus,
       "mscAtmIfVptUniEbrComponentName": mscAtmIfVptUniEbrComponentName,
       "mscAtmIfVptUniEbrStorageType": mscAtmIfVptUniEbrStorageType,
       "mscAtmIfVptUniEbrIndex": mscAtmIfVptUniEbrIndex,
       "mscAtmIfVptUniEbrProvTable": mscAtmIfVptUniEbrProvTable,
       "mscAtmIfVptUniEbrProvEntry": mscAtmIfVptUniEbrProvEntry,
       "mscAtmIfVptUniEbrConnectionRecovery": mscAtmIfVptUniEbrConnectionRecovery,
       "mscAtmIfVptUniEbrPathOptimization": mscAtmIfVptUniEbrPathOptimization,
       "mscAtmIfVptUniEbrOperTable": mscAtmIfVptUniEbrOperTable,
       "mscAtmIfVptUniEbrOperEntry": mscAtmIfVptUniEbrOperEntry,
       "mscAtmIfVptUniEbrSubscribedConnections": mscAtmIfVptUniEbrSubscribedConnections,
       "mscAtmIfVptUniEbrEligibleRecoveredConnections": mscAtmIfVptUniEbrEligibleRecoveredConnections,
       "mscAtmIfVptUniEbrIneligibleRecoveredConnections": mscAtmIfVptUniEbrIneligibleRecoveredConnections,
       "mscAtmIfVptUniEbrStatsTable": mscAtmIfVptUniEbrStatsTable,
       "mscAtmIfVptUniEbrStatsEntry": mscAtmIfVptUniEbrStatsEntry,
       "mscAtmIfVptUniEbrTotalConnectionRecoveries": mscAtmIfVptUniEbrTotalConnectionRecoveries,
       "mscAtmIfVptUniEbrTotalPathOptimizations": mscAtmIfVptUniEbrTotalPathOptimizations,
       "mscAtmIfVptVccSrcEbrOv": mscAtmIfVptVccSrcEbrOv,
       "mscAtmIfVptVccSrcEbrOvRowStatusTable": mscAtmIfVptVccSrcEbrOvRowStatusTable,
       "mscAtmIfVptVccSrcEbrOvRowStatusEntry": mscAtmIfVptVccSrcEbrOvRowStatusEntry,
       "mscAtmIfVptVccSrcEbrOvRowStatus": mscAtmIfVptVccSrcEbrOvRowStatus,
       "mscAtmIfVptVccSrcEbrOvComponentName": mscAtmIfVptVccSrcEbrOvComponentName,
       "mscAtmIfVptVccSrcEbrOvStorageType": mscAtmIfVptVccSrcEbrOvStorageType,
       "mscAtmIfVptVccSrcEbrOvIndex": mscAtmIfVptVccSrcEbrOvIndex,
       "mscAtmIfVptVccSrcEbrOvProvTable": mscAtmIfVptVccSrcEbrOvProvTable,
       "mscAtmIfVptVccSrcEbrOvProvEntry": mscAtmIfVptVccSrcEbrOvProvEntry,
       "mscAtmIfVptVccSrcEbrOvRecoverySubscribed": mscAtmIfVptVccSrcEbrOvRecoverySubscribed,
       "mscAtmIfVptVccSrcEbrOvOptimizationSubscribed": mscAtmIfVptVccSrcEbrOvOptimizationSubscribed,
       "mscAtmIfVptVccEbrInfo": mscAtmIfVptVccEbrInfo,
       "mscAtmIfVptVccEbrInfoRowStatusTable": mscAtmIfVptVccEbrInfoRowStatusTable,
       "mscAtmIfVptVccEbrInfoRowStatusEntry": mscAtmIfVptVccEbrInfoRowStatusEntry,
       "mscAtmIfVptVccEbrInfoRowStatus": mscAtmIfVptVccEbrInfoRowStatus,
       "mscAtmIfVptVccEbrInfoComponentName": mscAtmIfVptVccEbrInfoComponentName,
       "mscAtmIfVptVccEbrInfoStorageType": mscAtmIfVptVccEbrInfoStorageType,
       "mscAtmIfVptVccEbrInfoIndex": mscAtmIfVptVccEbrInfoIndex,
       "mscAtmIfVptVccEbrInfoOperTable": mscAtmIfVptVccEbrInfoOperTable,
       "mscAtmIfVptVccEbrInfoOperEntry": mscAtmIfVptVccEbrInfoOperEntry,
       "mscAtmIfVptVccEbrInfoRecoverySubscribed": mscAtmIfVptVccEbrInfoRecoverySubscribed,
       "mscAtmIfVptVccEbrInfoOptimizationSubscribed": mscAtmIfVptVccEbrInfoOptimizationSubscribed,
       "mscAtmIfVptVccEbrInfoConnectionRecovered": mscAtmIfVptVccEbrInfoConnectionRecovered,
       "mscAtmIfVptVccEbrInfoStatsTable": mscAtmIfVptVccEbrInfoStatsTable,
       "mscAtmIfVptVccEbrInfoStatsEntry": mscAtmIfVptVccEbrInfoStatsEntry,
       "mscAtmIfVptVccEbrInfoTotalConnectionRecoveries": mscAtmIfVptVccEbrInfoTotalConnectionRecoveries,
       "mscAtmIfVptVccEbrInfoTotalPathOptimizations": mscAtmIfVptVccEbrInfoTotalPathOptimizations,
       "mscAtmIfPnniEbr": mscAtmIfPnniEbr,
       "mscAtmIfPnniEbrRowStatusTable": mscAtmIfPnniEbrRowStatusTable,
       "mscAtmIfPnniEbrRowStatusEntry": mscAtmIfPnniEbrRowStatusEntry,
       "mscAtmIfPnniEbrRowStatus": mscAtmIfPnniEbrRowStatus,
       "mscAtmIfPnniEbrComponentName": mscAtmIfPnniEbrComponentName,
       "mscAtmIfPnniEbrStorageType": mscAtmIfPnniEbrStorageType,
       "mscAtmIfPnniEbrIndex": mscAtmIfPnniEbrIndex,
       "mscAtmIfPnniEbrProvTable": mscAtmIfPnniEbrProvTable,
       "mscAtmIfPnniEbrProvEntry": mscAtmIfPnniEbrProvEntry,
       "mscAtmIfPnniEbrConnectionRecovery": mscAtmIfPnniEbrConnectionRecovery,
       "mscAtmIfPnniEbrPathOptimization": mscAtmIfPnniEbrPathOptimization,
       "mscAtmIfPnniEbrOperTable": mscAtmIfPnniEbrOperTable,
       "mscAtmIfPnniEbrOperEntry": mscAtmIfPnniEbrOperEntry,
       "mscAtmIfPnniEbrSubscribedConnections": mscAtmIfPnniEbrSubscribedConnections,
       "mscAtmIfPnniEbrEligibleRecoveredConnections": mscAtmIfPnniEbrEligibleRecoveredConnections,
       "mscAtmIfPnniEbrIneligibleRecoveredConnections": mscAtmIfPnniEbrIneligibleRecoveredConnections,
       "mscAtmIfPnniEbrStatsTable": mscAtmIfPnniEbrStatsTable,
       "mscAtmIfPnniEbrStatsEntry": mscAtmIfPnniEbrStatsEntry,
       "mscAtmIfPnniEbrTotalConnectionRecoveries": mscAtmIfPnniEbrTotalConnectionRecoveries,
       "mscAtmIfPnniEbrTotalPathOptimizations": mscAtmIfPnniEbrTotalPathOptimizations,
       "atmEbrMIB": atmEbrMIB,
       "atmEbrGroup": atmEbrGroup,
       "atmEbrGroupCA": atmEbrGroupCA,
       "atmEbrGroupCA02": atmEbrGroupCA02,
       "atmEbrGroupCA02A": atmEbrGroupCA02A,
       "atmEbrCapabilities": atmEbrCapabilities,
       "atmEbrCapabilitiesCA": atmEbrCapabilitiesCA,
       "atmEbrCapabilitiesCA02": atmEbrCapabilitiesCA02,
       "atmEbrCapabilitiesCA02A": atmEbrCapabilitiesCA02A}
)
