# SNMP MIB module (ACC-BGP) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ACC-BGP
# Produced by pysmi-1.5.4 at Mon Oct 14 20:31:53 2024
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
 IfIndex,
 RowStatus,
 SmdsAddress,
 accBRG) = mibBuilder.importSymbols(
    "ACC-MIB",
    "DisplayString",
    "IfIndex",
    "RowStatus",
    "SmdsAddress",
    "accBRG")

(accTrapLogSeqNum,) = mibBuilder.importSymbols(
    "ACC-SYSTEM",
    "accTrapLogSeqNum")

(bgpLocalAs,
 bgpPeerHoldTimeConfigured,
 bgpPeerKeepAliveConfigured,
 bgpPeerLocalAddr,
 bgpPeerRemoteAddr,
 bgpPeerState) = mibBuilder.importSymbols(
    "BGP4-MIB",
    "bgpLocalAs",
    "bgpPeerHoldTimeConfigured",
    "bgpPeerKeepAliveConfigured",
    "bgpPeerLocalAddr",
    "bgpPeerRemoteAddr",
    "bgpPeerState")

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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AccBgp_ObjectIdentity = ObjectIdentity
accBgp = _AccBgp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51)
)
_AccBgpGeneral_ObjectIdentity = ObjectIdentity
accBgpGeneral = _AccBgpGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 1)
)


class _AccBgpAdminState_Type(Integer32):
    """Custom type accBgpAdminState based on Integer32"""
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


_AccBgpAdminState_Type.__name__ = "Integer32"
_AccBgpAdminState_Object = MibScalar
accBgpAdminState = _AccBgpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 1, 1),
    _AccBgpAdminState_Type()
)
accBgpAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBgpAdminState.setStatus("mandatory")


class _AccBgpMessageLevel_Type(Integer32):
    """Custom type accBgpMessageLevel based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_AccBgpMessageLevel_Type.__name__ = "Integer32"
_AccBgpMessageLevel_Object = MibScalar
accBgpMessageLevel = _AccBgpMessageLevel_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 1, 2),
    _AccBgpMessageLevel_Type()
)
accBgpMessageLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBgpMessageLevel.setStatus("mandatory")


class _AccBgpLocalAsFullMesh_Type(Integer32):
    """Custom type accBgpLocalAsFullMesh based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AccBgpLocalAsFullMesh_Type.__name__ = "Integer32"
_AccBgpLocalAsFullMesh_Object = MibScalar
accBgpLocalAsFullMesh = _AccBgpLocalAsFullMesh_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 1, 3),
    _AccBgpLocalAsFullMesh_Type()
)
accBgpLocalAsFullMesh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBgpLocalAsFullMesh.setStatus("mandatory")
_AccBgpPeerTable_Object = MibTable
accBgpPeerTable = _AccBgpPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 2)
)
if mibBuilder.loadTexts:
    accBgpPeerTable.setStatus("mandatory")
_AccBgpPeerEntry_Object = MibTableRow
accBgpPeerEntry = _AccBgpPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 2, 1)
)
accBgpPeerEntry.setIndexNames(
    (0, "ACC-BGP", "accBgpPeerAddress"),
)
if mibBuilder.loadTexts:
    accBgpPeerEntry.setStatus("mandatory")
_AccBgpPeerAddress_Type = IpAddress
_AccBgpPeerAddress_Object = MibTableColumn
accBgpPeerAddress = _AccBgpPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 2, 1, 1),
    _AccBgpPeerAddress_Type()
)
accBgpPeerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accBgpPeerAddress.setStatus("mandatory")


class _AccBgpPeerVersionConfigured_Type(Integer32):
    """Custom type accBgpPeerVersionConfigured based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("bgp3", 3),
          ("bgp4", 4))
    )


_AccBgpPeerVersionConfigured_Type.__name__ = "Integer32"
_AccBgpPeerVersionConfigured_Object = MibTableColumn
accBgpPeerVersionConfigured = _AccBgpPeerVersionConfigured_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 2, 1, 2),
    _AccBgpPeerVersionConfigured_Type()
)
accBgpPeerVersionConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBgpPeerVersionConfigured.setStatus("mandatory")


class _AccBgpPeerDefaultImportPref_Type(Integer32):
    """Custom type accBgpPeerDefaultImportPref based on Integer32"""
    defaultValue = 144

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AccBgpPeerDefaultImportPref_Type.__name__ = "Integer32"
_AccBgpPeerDefaultImportPref_Object = MibTableColumn
accBgpPeerDefaultImportPref = _AccBgpPeerDefaultImportPref_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 2, 1, 3),
    _AccBgpPeerDefaultImportPref_Type()
)
accBgpPeerDefaultImportPref.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBgpPeerDefaultImportPref.setStatus("mandatory")


class _AccBgpPeerDefaultExportMetric_Type(Integer32):
    """Custom type accBgpPeerDefaultExportMetric based on Integer32"""
    defaultValue = 4294967295

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_AccBgpPeerDefaultExportMetric_Type.__name__ = "Integer32"
_AccBgpPeerDefaultExportMetric_Object = MibTableColumn
accBgpPeerDefaultExportMetric = _AccBgpPeerDefaultExportMetric_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 2, 1, 4),
    _AccBgpPeerDefaultExportMetric_Type()
)
accBgpPeerDefaultExportMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBgpPeerDefaultExportMetric.setStatus("mandatory")


class _AccBgpPeerPassive_Type(Integer32):
    """Custom type accBgpPeerPassive based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AccBgpPeerPassive_Type.__name__ = "Integer32"
_AccBgpPeerPassive_Object = MibTableColumn
accBgpPeerPassive = _AccBgpPeerPassive_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 2, 1, 5),
    _AccBgpPeerPassive_Type()
)
accBgpPeerPassive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBgpPeerPassive.setStatus("mandatory")


class _AccBgpPeerUseMed_Type(Integer32):
    """Custom type accBgpPeerUseMed based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AccBgpPeerUseMed_Type.__name__ = "Integer32"
_AccBgpPeerUseMed_Object = MibTableColumn
accBgpPeerUseMed = _AccBgpPeerUseMed_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 2, 1, 6),
    _AccBgpPeerUseMed_Type()
)
accBgpPeerUseMed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBgpPeerUseMed.setStatus("mandatory")


class _AccBgpPeerMessageLevel_Type(Integer32):
    """Custom type accBgpPeerMessageLevel based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_AccBgpPeerMessageLevel_Type.__name__ = "Integer32"
_AccBgpPeerMessageLevel_Object = MibTableColumn
accBgpPeerMessageLevel = _AccBgpPeerMessageLevel_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 2, 1, 7),
    _AccBgpPeerMessageLevel_Type()
)
accBgpPeerMessageLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBgpPeerMessageLevel.setStatus("mandatory")


class _AccBgpPeerMultiHop_Type(Integer32):
    """Custom type accBgpPeerMultiHop based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AccBgpPeerMultiHop_Type.__name__ = "Integer32"
_AccBgpPeerMultiHop_Object = MibTableColumn
accBgpPeerMultiHop = _AccBgpPeerMultiHop_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 2, 1, 8),
    _AccBgpPeerMultiHop_Type()
)
accBgpPeerMultiHop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBgpPeerMultiHop.setStatus("mandatory")
_AccBgpPeerStatus_Type = RowStatus
_AccBgpPeerStatus_Object = MibTableColumn
accBgpPeerStatus = _AccBgpPeerStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 2, 1, 9),
    _AccBgpPeerStatus_Type()
)
accBgpPeerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBgpPeerStatus.setStatus("mandatory")
_AccBgpImportTable_Object = MibTable
accBgpImportTable = _AccBgpImportTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 4)
)
if mibBuilder.loadTexts:
    accBgpImportTable.setStatus("mandatory")
_AccBgpImportEntry_Object = MibTableRow
accBgpImportEntry = _AccBgpImportEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 4, 1)
)
accBgpImportEntry.setIndexNames(
    (0, "ACC-BGP", "accBgpImportNetwork"),
    (0, "ACC-BGP", "accBgpImportMask"),
    (0, "ACC-BGP", "accBgpImportPeerAS"),
    (0, "ACC-BGP", "accBgpImportPeerAddress"),
    (0, "ACC-BGP", "accBgpImportHomeAS"),
    (0, "ACC-BGP", "accBgpImportOrigin"),
)
if mibBuilder.loadTexts:
    accBgpImportEntry.setStatus("mandatory")
_AccBgpImportNetwork_Type = IpAddress
_AccBgpImportNetwork_Object = MibTableColumn
accBgpImportNetwork = _AccBgpImportNetwork_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 4, 1, 1),
    _AccBgpImportNetwork_Type()
)
accBgpImportNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accBgpImportNetwork.setStatus("mandatory")
_AccBgpImportMask_Type = IpAddress
_AccBgpImportMask_Object = MibTableColumn
accBgpImportMask = _AccBgpImportMask_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 4, 1, 2),
    _AccBgpImportMask_Type()
)
accBgpImportMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accBgpImportMask.setStatus("mandatory")
_AccBgpImportPeerAS_Type = Integer32
_AccBgpImportPeerAS_Object = MibTableColumn
accBgpImportPeerAS = _AccBgpImportPeerAS_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 4, 1, 3),
    _AccBgpImportPeerAS_Type()
)
accBgpImportPeerAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accBgpImportPeerAS.setStatus("mandatory")
_AccBgpImportPeerAddress_Type = IpAddress
_AccBgpImportPeerAddress_Object = MibTableColumn
accBgpImportPeerAddress = _AccBgpImportPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 4, 1, 4),
    _AccBgpImportPeerAddress_Type()
)
accBgpImportPeerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accBgpImportPeerAddress.setStatus("mandatory")
_AccBgpImportHomeAS_Type = Integer32
_AccBgpImportHomeAS_Object = MibTableColumn
accBgpImportHomeAS = _AccBgpImportHomeAS_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 4, 1, 5),
    _AccBgpImportHomeAS_Type()
)
accBgpImportHomeAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accBgpImportHomeAS.setStatus("mandatory")


class _AccBgpImportOrigin_Type(Integer32):
    """Custom type accBgpImportOrigin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("egp", 2),
          ("igp", 1),
          ("unknown", 3))
    )


_AccBgpImportOrigin_Type.__name__ = "Integer32"
_AccBgpImportOrigin_Object = MibTableColumn
accBgpImportOrigin = _AccBgpImportOrigin_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 4, 1, 6),
    _AccBgpImportOrigin_Type()
)
accBgpImportOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accBgpImportOrigin.setStatus("mandatory")


class _AccBgpImportAction_Type(Integer32):
    """Custom type accBgpImportAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ignore", 2),
          ("import", 1))
    )


_AccBgpImportAction_Type.__name__ = "Integer32"
_AccBgpImportAction_Object = MibTableColumn
accBgpImportAction = _AccBgpImportAction_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 4, 1, 7),
    _AccBgpImportAction_Type()
)
accBgpImportAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBgpImportAction.setStatus("mandatory")


class _AccBgpImportPreference_Type(Integer32):
    """Custom type accBgpImportPreference based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AccBgpImportPreference_Type.__name__ = "Integer32"
_AccBgpImportPreference_Object = MibTableColumn
accBgpImportPreference = _AccBgpImportPreference_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 4, 1, 8),
    _AccBgpImportPreference_Type()
)
accBgpImportPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBgpImportPreference.setStatus("mandatory")
_AccBgpImportStatus_Type = RowStatus
_AccBgpImportStatus_Object = MibTableColumn
accBgpImportStatus = _AccBgpImportStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 4, 1, 9),
    _AccBgpImportStatus_Type()
)
accBgpImportStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBgpImportStatus.setStatus("mandatory")
_AccBgpASWeightTable_Object = MibTable
accBgpASWeightTable = _AccBgpASWeightTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 5)
)
if mibBuilder.loadTexts:
    accBgpASWeightTable.setStatus("mandatory")
_AccBgpASWeightEntry_Object = MibTableRow
accBgpASWeightEntry = _AccBgpASWeightEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 5, 1)
)
accBgpASWeightEntry.setIndexNames(
    (0, "ACC-BGP", "accBgpASWeightAS"),
)
if mibBuilder.loadTexts:
    accBgpASWeightEntry.setStatus("mandatory")


class _AccBgpASWeightAS_Type(Integer32):
    """Custom type accBgpASWeightAS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AccBgpASWeightAS_Type.__name__ = "Integer32"
_AccBgpASWeightAS_Object = MibTableColumn
accBgpASWeightAS = _AccBgpASWeightAS_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 5, 1, 1),
    _AccBgpASWeightAS_Type()
)
accBgpASWeightAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accBgpASWeightAS.setStatus("mandatory")


class _AccBgpASWeight_Type(Integer32):
    """Custom type accBgpASWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AccBgpASWeight_Type.__name__ = "Integer32"
_AccBgpASWeight_Object = MibTableColumn
accBgpASWeight = _AccBgpASWeight_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 5, 1, 2),
    _AccBgpASWeight_Type()
)
accBgpASWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBgpASWeight.setStatus("mandatory")
_AccBgpASWeightStatus_Type = RowStatus
_AccBgpASWeightStatus_Object = MibTableColumn
accBgpASWeightStatus = _AccBgpASWeightStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 5, 1, 3),
    _AccBgpASWeightStatus_Type()
)
accBgpASWeightStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBgpASWeightStatus.setStatus("mandatory")
_AccBgpAggregateTable_Object = MibTable
accBgpAggregateTable = _AccBgpAggregateTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 6)
)
if mibBuilder.loadTexts:
    accBgpAggregateTable.setStatus("mandatory")
_AccBgpAggregateEntry_Object = MibTableRow
accBgpAggregateEntry = _AccBgpAggregateEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 6, 1)
)
accBgpAggregateEntry.setIndexNames(
    (0, "ACC-BGP", "accBgpAggregateAddr"),
    (0, "ACC-BGP", "accBgpAggregateMask"),
)
if mibBuilder.loadTexts:
    accBgpAggregateEntry.setStatus("mandatory")
_AccBgpAggregateAddr_Type = IpAddress
_AccBgpAggregateAddr_Object = MibTableColumn
accBgpAggregateAddr = _AccBgpAggregateAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 6, 1, 1),
    _AccBgpAggregateAddr_Type()
)
accBgpAggregateAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accBgpAggregateAddr.setStatus("mandatory")
_AccBgpAggregateMask_Type = IpAddress
_AccBgpAggregateMask_Object = MibTableColumn
accBgpAggregateMask = _AccBgpAggregateMask_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 6, 1, 2),
    _AccBgpAggregateMask_Type()
)
accBgpAggregateMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accBgpAggregateMask.setStatus("mandatory")


class _AccBgpAggregateAdvertise_Type(Integer32):
    """Custom type accBgpAggregateAdvertise based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AccBgpAggregateAdvertise_Type.__name__ = "Integer32"
_AccBgpAggregateAdvertise_Object = MibTableColumn
accBgpAggregateAdvertise = _AccBgpAggregateAdvertise_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 6, 1, 3),
    _AccBgpAggregateAdvertise_Type()
)
accBgpAggregateAdvertise.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBgpAggregateAdvertise.setStatus("mandatory")


class _AccBgpAggregatePref_Type(Integer32):
    """Custom type accBgpAggregatePref based on Integer32"""
    defaultValue = 144

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AccBgpAggregatePref_Type.__name__ = "Integer32"
_AccBgpAggregatePref_Object = MibTableColumn
accBgpAggregatePref = _AccBgpAggregatePref_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 6, 1, 4),
    _AccBgpAggregatePref_Type()
)
accBgpAggregatePref.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBgpAggregatePref.setStatus("mandatory")


class _AccBgpAggregateComponents_Type(Integer32):
    """Custom type accBgpAggregateComponents based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_AccBgpAggregateComponents_Type.__name__ = "Integer32"
_AccBgpAggregateComponents_Object = MibTableColumn
accBgpAggregateComponents = _AccBgpAggregateComponents_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 6, 1, 5),
    _AccBgpAggregateComponents_Type()
)
accBgpAggregateComponents.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBgpAggregateComponents.setStatus("mandatory")


class _AccBgpAggregateActive_Type(Integer32):
    """Custom type accBgpAggregateActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AccBgpAggregateActive_Type.__name__ = "Integer32"
_AccBgpAggregateActive_Object = MibTableColumn
accBgpAggregateActive = _AccBgpAggregateActive_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 6, 1, 6),
    _AccBgpAggregateActive_Type()
)
accBgpAggregateActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accBgpAggregateActive.setStatus("mandatory")


class _AccBgpAggregateAdminStat_Type(Integer32):
    """Custom type accBgpAggregateAdminStat based on Integer32"""
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


_AccBgpAggregateAdminStat_Type.__name__ = "Integer32"
_AccBgpAggregateAdminStat_Object = MibTableColumn
accBgpAggregateAdminStat = _AccBgpAggregateAdminStat_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 6, 1, 7),
    _AccBgpAggregateAdminStat_Type()
)
accBgpAggregateAdminStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBgpAggregateAdminStat.setStatus("mandatory")
_AccBgpAggregateStatus_Type = RowStatus
_AccBgpAggregateStatus_Object = MibTableColumn
accBgpAggregateStatus = _AccBgpAggregateStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 6, 1, 8),
    _AccBgpAggregateStatus_Type()
)
accBgpAggregateStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBgpAggregateStatus.setStatus("mandatory")
_AccBgpAggrComponentTable_Object = MibTable
accBgpAggrComponentTable = _AccBgpAggrComponentTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 7)
)
if mibBuilder.loadTexts:
    accBgpAggrComponentTable.setStatus("mandatory")
_AccBgpAggrComponentEntry_Object = MibTableRow
accBgpAggrComponentEntry = _AccBgpAggrComponentEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 7, 1)
)
accBgpAggrComponentEntry.setIndexNames(
    (0, "ACC-BGP", "accBgpAggrCompParentAddr"),
    (0, "ACC-BGP", "accBgpAggrCompParentMask"),
    (0, "ACC-BGP", "accBgpAggrComponentAddr"),
    (0, "ACC-BGP", "accBgpAggrComponentMask"),
)
if mibBuilder.loadTexts:
    accBgpAggrComponentEntry.setStatus("mandatory")
_AccBgpAggrCompParentAddr_Type = IpAddress
_AccBgpAggrCompParentAddr_Object = MibTableColumn
accBgpAggrCompParentAddr = _AccBgpAggrCompParentAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 7, 1, 1),
    _AccBgpAggrCompParentAddr_Type()
)
accBgpAggrCompParentAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accBgpAggrCompParentAddr.setStatus("mandatory")
_AccBgpAggrCompParentMask_Type = IpAddress
_AccBgpAggrCompParentMask_Object = MibTableColumn
accBgpAggrCompParentMask = _AccBgpAggrCompParentMask_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 7, 1, 2),
    _AccBgpAggrCompParentMask_Type()
)
accBgpAggrCompParentMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accBgpAggrCompParentMask.setStatus("mandatory")
_AccBgpAggrComponentAddr_Type = IpAddress
_AccBgpAggrComponentAddr_Object = MibTableColumn
accBgpAggrComponentAddr = _AccBgpAggrComponentAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 7, 1, 3),
    _AccBgpAggrComponentAddr_Type()
)
accBgpAggrComponentAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accBgpAggrComponentAddr.setStatus("mandatory")
_AccBgpAggrComponentMask_Type = IpAddress
_AccBgpAggrComponentMask_Object = MibTableColumn
accBgpAggrComponentMask = _AccBgpAggrComponentMask_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 7, 1, 4),
    _AccBgpAggrComponentMask_Type()
)
accBgpAggrComponentMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accBgpAggrComponentMask.setStatus("mandatory")


class _AccBgpAggrComponentProtocol_Type(Integer32):
    """Custom type accBgpAggrComponentProtocol based on Integer32"""
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
        *(("any", 1),
          ("bgp", 5),
          ("ospf", 3),
          ("rip", 4),
          ("static", 2))
    )


_AccBgpAggrComponentProtocol_Type.__name__ = "Integer32"
_AccBgpAggrComponentProtocol_Object = MibTableColumn
accBgpAggrComponentProtocol = _AccBgpAggrComponentProtocol_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 7, 1, 5),
    _AccBgpAggrComponentProtocol_Type()
)
accBgpAggrComponentProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBgpAggrComponentProtocol.setStatus("mandatory")


class _AccBgpAggrComponentActive_Type(Integer32):
    """Custom type accBgpAggrComponentActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AccBgpAggrComponentActive_Type.__name__ = "Integer32"
_AccBgpAggrComponentActive_Object = MibTableColumn
accBgpAggrComponentActive = _AccBgpAggrComponentActive_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 7, 1, 6),
    _AccBgpAggrComponentActive_Type()
)
accBgpAggrComponentActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accBgpAggrComponentActive.setStatus("mandatory")
_AccBgpAggrComponentStatus_Type = RowStatus
_AccBgpAggrComponentStatus_Object = MibTableColumn
accBgpAggrComponentStatus = _AccBgpAggrComponentStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 7, 1, 7),
    _AccBgpAggrComponentStatus_Type()
)
accBgpAggrComponentStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBgpAggrComponentStatus.setStatus("mandatory")
_AccBgpExportTable_Object = MibTable
accBgpExportTable = _AccBgpExportTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 8)
)
if mibBuilder.loadTexts:
    accBgpExportTable.setStatus("mandatory")
_AccBgpExportEntry_Object = MibTableRow
accBgpExportEntry = _AccBgpExportEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 8, 1)
)
accBgpExportEntry.setIndexNames(
    (0, "ACC-BGP", "accBgpExportPeerAS"),
    (0, "ACC-BGP", "accBgpExportPeerAddress"),
    (0, "ACC-BGP", "accBgpExportProtocol"),
    (0, "ACC-BGP", "accBgpExportSpecific2"),
    (0, "ACC-BGP", "accBgpExportSpecific1"),
    (0, "ACC-BGP", "accBgpExportNetwork"),
    (0, "ACC-BGP", "accBgpExportMask"),
)
if mibBuilder.loadTexts:
    accBgpExportEntry.setStatus("mandatory")
_AccBgpExportPeerAS_Type = Integer32
_AccBgpExportPeerAS_Object = MibTableColumn
accBgpExportPeerAS = _AccBgpExportPeerAS_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 8, 1, 1),
    _AccBgpExportPeerAS_Type()
)
accBgpExportPeerAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accBgpExportPeerAS.setStatus("mandatory")
_AccBgpExportPeerAddress_Type = IpAddress
_AccBgpExportPeerAddress_Object = MibTableColumn
accBgpExportPeerAddress = _AccBgpExportPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 8, 1, 2),
    _AccBgpExportPeerAddress_Type()
)
accBgpExportPeerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accBgpExportPeerAddress.setStatus("mandatory")


class _AccBgpExportProtocol_Type(Integer32):
    """Custom type accBgpExportProtocol based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("aggr", 9),
          ("any", 1),
          ("ebgp", 7),
          ("eospf", 5),
          ("ibgp", 8),
          ("iospf", 4),
          ("local", 2),
          ("rip", 6),
          ("static", 3))
    )


_AccBgpExportProtocol_Type.__name__ = "Integer32"
_AccBgpExportProtocol_Object = MibTableColumn
accBgpExportProtocol = _AccBgpExportProtocol_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 8, 1, 3),
    _AccBgpExportProtocol_Type()
)
accBgpExportProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accBgpExportProtocol.setStatus("mandatory")
_AccBgpExportSpecific2_Type = Integer32
_AccBgpExportSpecific2_Object = MibTableColumn
accBgpExportSpecific2 = _AccBgpExportSpecific2_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 8, 1, 4),
    _AccBgpExportSpecific2_Type()
)
accBgpExportSpecific2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accBgpExportSpecific2.setStatus("mandatory")
_AccBgpExportSpecific1_Type = Integer32
_AccBgpExportSpecific1_Object = MibTableColumn
accBgpExportSpecific1 = _AccBgpExportSpecific1_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 8, 1, 5),
    _AccBgpExportSpecific1_Type()
)
accBgpExportSpecific1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accBgpExportSpecific1.setStatus("mandatory")
_AccBgpExportNetwork_Type = IpAddress
_AccBgpExportNetwork_Object = MibTableColumn
accBgpExportNetwork = _AccBgpExportNetwork_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 8, 1, 6),
    _AccBgpExportNetwork_Type()
)
accBgpExportNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accBgpExportNetwork.setStatus("mandatory")
_AccBgpExportMask_Type = IpAddress
_AccBgpExportMask_Object = MibTableColumn
accBgpExportMask = _AccBgpExportMask_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 8, 1, 7),
    _AccBgpExportMask_Type()
)
accBgpExportMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accBgpExportMask.setStatus("mandatory")


class _AccBgpExportAction_Type(Integer32):
    """Custom type accBgpExportAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("block", 2),
          ("export", 1))
    )


_AccBgpExportAction_Type.__name__ = "Integer32"
_AccBgpExportAction_Object = MibTableColumn
accBgpExportAction = _AccBgpExportAction_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 8, 1, 8),
    _AccBgpExportAction_Type()
)
accBgpExportAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBgpExportAction.setStatus("mandatory")


class _AccBgpExportMetric_Type(Integer32):
    """Custom type accBgpExportMetric based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AccBgpExportMetric_Type.__name__ = "Integer32"
_AccBgpExportMetric_Object = MibTableColumn
accBgpExportMetric = _AccBgpExportMetric_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 8, 1, 9),
    _AccBgpExportMetric_Type()
)
accBgpExportMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBgpExportMetric.setStatus("mandatory")
_AccBgpExportStatus_Type = RowStatus
_AccBgpExportStatus_Object = MibTableColumn
accBgpExportStatus = _AccBgpExportStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 8, 1, 10),
    _AccBgpExportStatus_Type()
)
accBgpExportStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBgpExportStatus.setStatus("mandatory")
_AccBgpTraps_ObjectIdentity = ObjectIdentity
accBgpTraps = _AccBgpTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 9)
)
_AccBgpTrapMsg_Type = DisplayString
_AccBgpTrapMsg_Object = MibScalar
accBgpTrapMsg = _AccBgpTrapMsg_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 9, 1),
    _AccBgpTrapMsg_Type()
)
accBgpTrapMsg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBgpTrapMsg.setStatus("mandatory")

# Managed Objects groups


# Notification objects

accBgpPeerNotDisbldTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 9, 0, 1)
)
accBgpPeerNotDisbldTrap.setObjects(
      *(("ACC-BGP", "accBgpTrapMsg"),
        ("ACC-BGP", "accBgpPeerAddress"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accBgpPeerNotDisbldTrap.setStatus(
        ""
    )

accBgpAddFltPolTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 9, 0, 2)
)
accBgpAddFltPolTrap.setObjects(
      *(("ACC-BGP", "accBgpTrapMsg"),
        ("ACC-BGP", "accBgpImportNetwork"),
        ("ACC-BGP", "accBgpImportMask"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accBgpAddFltPolTrap.setStatus(
        ""
    )

accBgpDelFltPolTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 9, 0, 3)
)
accBgpDelFltPolTrap.setObjects(
      *(("ACC-BGP", "accBgpTrapMsg"),
        ("ACC-BGP", "accBgpImportNetwork"),
        ("ACC-BGP", "accBgpImportMask"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accBgpDelFltPolTrap.setStatus(
        ""
    )

accBgpAddImpPolTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 9, 0, 4)
)
accBgpAddImpPolTrap.setObjects(
      *(("ACC-BGP", "accBgpTrapMsg"),
        ("ACC-BGP", "accBgpExportNetwork"),
        ("ACC-BGP", "accBgpExportMask"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accBgpAddImpPolTrap.setStatus(
        ""
    )

accBgpDelImpPolTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 9, 0, 5)
)
accBgpDelImpPolTrap.setObjects(
      *(("ACC-BGP", "accBgpTrapMsg"),
        ("ACC-BGP", "accBgpExportNetwork"),
        ("ACC-BGP", "accBgpExportMask"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accBgpDelImpPolTrap.setStatus(
        ""
    )

accBgpAddAsWtPolTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 9, 0, 6)
)
accBgpAddAsWtPolTrap.setObjects(
      *(("ACC-BGP", "accBgpTrapMsg"),
        ("ACC-BGP", "accBgpASWeightAS"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accBgpAddAsWtPolTrap.setStatus(
        ""
    )

accBgpDelAsWtPolTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 9, 0, 7)
)
accBgpDelAsWtPolTrap.setObjects(
      *(("ACC-BGP", "accBgpTrapMsg"),
        ("ACC-BGP", "accBgpASWeightAS"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accBgpDelAsWtPolTrap.setStatus(
        ""
    )

accBgpNbrTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 9, 0, 8)
)
accBgpNbrTrap.setObjects(
      *(("ACC-BGP", "accBgpTrapMsg"),
        ("ACC-BGP", "accBgpPeerAddress"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accBgpNbrTrap.setStatus(
        ""
    )

accBgpInvHoldKeepAliveTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 9, 0, 9)
)
accBgpInvHoldKeepAliveTrap.setObjects(
      *(("ACC-BGP", "accBgpTrapMsg"),
        ("BGP4-MIB", "bgpPeerHoldTimeConfigured"),
        ("BGP4-MIB", "bgpPeerKeepAliveConfigured"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accBgpInvHoldKeepAliveTrap.setStatus(
        ""
    )

accBgpIllegalLocalAsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 9, 0, 10)
)
accBgpIllegalLocalAsTrap.setObjects(
      *(("ACC-BGP", "accBgpTrapMsg"),
        ("BGP4-MIB", "bgpLocalAs"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accBgpIllegalLocalAsTrap.setStatus(
        ""
    )

accBgpIBGPPeerAddrTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 9, 0, 11)
)
accBgpIBGPPeerAddrTrap.setObjects(
      *(("ACC-BGP", "accBgpTrapMsg"),
        ("ACC-BGP", "accBgpExportPeerAS"),
        ("ACC-BGP", "accBgpExportPeerAddress"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accBgpIBGPPeerAddrTrap.setStatus(
        ""
    )

accBgpPolPeerAddrTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 9, 0, 12)
)
accBgpPolPeerAddrTrap.setObjects(
      *(("ACC-BGP", "accBgpTrapMsg"),
        ("BGP4-MIB", "bgpLocalAs"),
        ("ACC-BGP", "accBgpExportPeerAS"),
        ("ACC-BGP", "accBgpExportPeerAddress"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accBgpPolPeerAddrTrap.setStatus(
        ""
    )

accBgpPeerNotFndTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 9, 0, 13)
)
accBgpPeerNotFndTrap.setObjects(
      *(("ACC-BGP", "accBgpTrapMsg"),
        ("ACC-BGP", "accBgpExportPeerAddress"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accBgpPeerNotFndTrap.setStatus(
        ""
    )

accBgpPeerAllocTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 9, 0, 14)
)
accBgpPeerAllocTrap.setObjects(
      *(("ACC-BGP", "accBgpTrapMsg"),
        ("ACC-BGP", "accBgpPeerAddress"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accBgpPeerAllocTrap.setStatus(
        ""
    )

accBgpRcvBfrAllocTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 9, 0, 15)
)
accBgpRcvBfrAllocTrap.setObjects(
      *(("ACC-BGP", "accBgpTrapMsg"),
        ("ACC-BGP", "accBgpPeerAddress"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accBgpRcvBfrAllocTrap.setStatus(
        ""
    )

accBgpTmrAllocTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 9, 0, 16)
)
accBgpTmrAllocTrap.setObjects(
      *(("ACC-BGP", "accBgpTrapMsg"),
        ("ACC-BGP", "accBgpPeerAddress"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accBgpTmrAllocTrap.setStatus(
        ""
    )

accBgpPeerEnableTmrAllocTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 9, 0, 17)
)
accBgpPeerEnableTmrAllocTrap.setObjects(
      *(("ACC-BGP", "accBgpTrapMsg"),
        ("ACC-BGP", "accBgpPeerAddress"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accBgpPeerEnableTmrAllocTrap.setStatus(
        ""
    )

accBgpGrpAllocTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 9, 0, 18)
)
accBgpGrpAllocTrap.setObjects(
      *(("ACC-BGP", "accBgpTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accBgpGrpAllocTrap.setStatus(
        ""
    )

accBgpShutdownAllocTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 9, 0, 19)
)
accBgpShutdownAllocTrap.setObjects(
      *(("ACC-BGP", "accBgpTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accBgpShutdownAllocTrap.setStatus(
        ""
    )

accBgpOrphanTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 9, 0, 20)
)
accBgpOrphanTrap.setObjects(
      *(("ACC-BGP", "accBgpTrapMsg"),
        ("BGP4-MIB", "bgpLocalAs"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accBgpOrphanTrap.setStatus(
        ""
    )

accBgpRtclAllocTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 9, 0, 21)
)
accBgpRtclAllocTrap.setObjects(
      *(("ACC-BGP", "accBgpTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accBgpRtclAllocTrap.setStatus(
        ""
    )

accBgpAggrAllocTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 9, 0, 22)
)
accBgpAggrAllocTrap.setObjects(
      *(("ACC-BGP", "accBgpTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accBgpAggrAllocTrap.setStatus(
        ""
    )

accBgpPolAllocTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 9, 0, 23)
)
accBgpPolAllocTrap.setObjects(
      *(("ACC-BGP", "accBgpTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accBgpPolAllocTrap.setStatus(
        ""
    )

accBgpAnnounceAllocTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 9, 0, 24)
)
accBgpAnnounceAllocTrap.setObjects(
      *(("ACC-BGP", "accBgpTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accBgpAnnounceAllocTrap.setStatus(
        ""
    )

accBgpAddNhTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 9, 0, 25)
)
accBgpAddNhTrap.setObjects(
      *(("ACC-BGP", "accBgpTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accBgpAddNhTrap.setStatus(
        ""
    )

accBgpNlriAllocTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 9, 0, 26)
)
accBgpNlriAllocTrap.setObjects(
      *(("ACC-BGP", "accBgpTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accBgpNlriAllocTrap.setStatus(
        ""
    )

accBgpPeerRtAllocTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 9, 0, 27)
)
accBgpPeerRtAllocTrap.setObjects(
      *(("ACC-BGP", "accBgpTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accBgpPeerRtAllocTrap.setStatus(
        ""
    )

accBgpPeerRtEntryAllocTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 9, 0, 28)
)
accBgpPeerRtEntryAllocTrap.setObjects(
      *(("ACC-BGP", "accBgpTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accBgpPeerRtEntryAllocTrap.setStatus(
        ""
    )

accBgpRtInfoAllocTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 9, 0, 29)
)
accBgpRtInfoAllocTrap.setObjects(
      *(("ACC-BGP", "accBgpTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accBgpRtInfoAllocTrap.setStatus(
        ""
    )

accBgpEvntMemTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 9, 0, 30)
)
accBgpEvntMemTrap.setObjects(
      *(("ACC-BGP", "accBgpTrapMsg"),
        ("BGP4-MIB", "bgpPeerLocalAddr"),
        ("BGP4-MIB", "bgpPeerRemoteAddr"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accBgpEvntMemTrap.setStatus(
        ""
    )

accBgpPeerCBAllocTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 9, 0, 31)
)
accBgpPeerCBAllocTrap.setObjects(
      *(("ACC-BGP", "accBgpTrapMsg"),
        ("BGP4-MIB", "bgpPeerLocalAddr"),
        ("BGP4-MIB", "bgpPeerRemoteAddr"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accBgpPeerCBAllocTrap.setStatus(
        ""
    )

accBgpRelEvntMemTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 9, 0, 32)
)
accBgpRelEvntMemTrap.setObjects(
      *(("ACC-BGP", "accBgpTrapMsg"),
        ("BGP4-MIB", "bgpPeerLocalAddr"),
        ("BGP4-MIB", "bgpPeerRemoteAddr"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accBgpRelEvntMemTrap.setStatus(
        ""
    )

accBgpConnectTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 9, 0, 33)
)
accBgpConnectTrap.setObjects(
      *(("ACC-BGP", "accBgpTrapMsg"),
        ("BGP4-MIB", "bgpPeerLocalAddr"),
        ("BGP4-MIB", "bgpPeerRemoteAddr"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accBgpConnectTrap.setStatus(
        ""
    )

accBgpPeerInvStateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 9, 0, 34)
)
accBgpPeerInvStateTrap.setObjects(
      *(("ACC-BGP", "accBgpTrapMsg"),
        ("BGP4-MIB", "bgpPeerRemoteAddr"),
        ("BGP4-MIB", "bgpPeerState"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accBgpPeerInvStateTrap.setStatus(
        ""
    )

accBgpAllocTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 9, 0, 35)
)
accBgpAllocTrap.setObjects(
      *(("ACC-BGP", "accBgpTrapMsg"),
        ("ACC-BGP", "accBgpPeerAddress"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accBgpAllocTrap.setStatus(
        ""
    )

accBgpPeerNoTxBfrTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 9, 0, 36)
)
accBgpPeerNoTxBfrTrap.setObjects(
      *(("ACC-BGP", "accBgpTrapMsg"),
        ("ACC-BGP", "accBgpPeerAddress"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accBgpPeerNoTxBfrTrap.setStatus(
        ""
    )

accBgpPeerWriteTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 9, 0, 37)
)
accBgpPeerWriteTrap.setObjects(
      *(("ACC-BGP", "accBgpTrapMsg"),
        ("ACC-BGP", "accBgpPeerAddress"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accBgpPeerWriteTrap.setStatus(
        ""
    )

accBgpClosingConnTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 9, 0, 38)
)
accBgpClosingConnTrap.setObjects(
      *(("ACC-BGP", "accBgpTrapMsg"),
        ("ACC-BGP", "accBgpPeerAddress"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accBgpClosingConnTrap.setStatus(
        ""
    )

accBgpSpoolBfrTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 9, 0, 39)
)
accBgpSpoolBfrTrap.setObjects(
      *(("ACC-BGP", "accBgpTrapMsg"),
        ("ACC-BGP", "accBgpPeerAddress"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accBgpSpoolBfrTrap.setStatus(
        ""
    )

accBgpRtryCntTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 9, 0, 40)
)
accBgpRtryCntTrap.setObjects(
      *(("ACC-BGP", "accBgpTrapMsg"),
        ("ACC-BGP", "accBgpPeerAddress"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accBgpRtryCntTrap.setStatus(
        ""
    )

accBgpPaAllocTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 9, 0, 41)
)
accBgpPaAllocTrap.setObjects(
      *(("ACC-BGP", "accBgpTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accBgpPaAllocTrap.setStatus(
        ""
    )

accBgpPSegAllocTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 9, 0, 42)
)
accBgpPSegAllocTrap.setObjects(
      *(("ACC-BGP", "accBgpTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accBgpPSegAllocTrap.setStatus(
        ""
    )

accBgpAddNxtHopTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 9, 0, 43)
)
accBgpAddNxtHopTrap.setObjects(
      *(("ACC-BGP", "accBgpTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accBgpAddNxtHopTrap.setStatus(
        ""
    )

accBgpRxBufAllocTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 9, 0, 44)
)
accBgpRxBufAllocTrap.setObjects(
      *(("ACC-BGP", "accBgpTrapMsg"),
        ("ACC-BGP", "accBgpPeerAddress"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accBgpRxBufAllocTrap.setStatus(
        ""
    )

accBgpPeerRcvBfrAllocTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 51, 9, 0, 45)
)
accBgpPeerRcvBfrAllocTrap.setObjects(
      *(("ACC-BGP", "accBgpTrapMsg"),
        ("ACC-BGP", "accBgpPeerAddress"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accBgpPeerRcvBfrAllocTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACC-BGP",
    **{"accBgp": accBgp,
       "accBgpGeneral": accBgpGeneral,
       "accBgpAdminState": accBgpAdminState,
       "accBgpMessageLevel": accBgpMessageLevel,
       "accBgpLocalAsFullMesh": accBgpLocalAsFullMesh,
       "accBgpPeerTable": accBgpPeerTable,
       "accBgpPeerEntry": accBgpPeerEntry,
       "accBgpPeerAddress": accBgpPeerAddress,
       "accBgpPeerVersionConfigured": accBgpPeerVersionConfigured,
       "accBgpPeerDefaultImportPref": accBgpPeerDefaultImportPref,
       "accBgpPeerDefaultExportMetric": accBgpPeerDefaultExportMetric,
       "accBgpPeerPassive": accBgpPeerPassive,
       "accBgpPeerUseMed": accBgpPeerUseMed,
       "accBgpPeerMessageLevel": accBgpPeerMessageLevel,
       "accBgpPeerMultiHop": accBgpPeerMultiHop,
       "accBgpPeerStatus": accBgpPeerStatus,
       "accBgpImportTable": accBgpImportTable,
       "accBgpImportEntry": accBgpImportEntry,
       "accBgpImportNetwork": accBgpImportNetwork,
       "accBgpImportMask": accBgpImportMask,
       "accBgpImportPeerAS": accBgpImportPeerAS,
       "accBgpImportPeerAddress": accBgpImportPeerAddress,
       "accBgpImportHomeAS": accBgpImportHomeAS,
       "accBgpImportOrigin": accBgpImportOrigin,
       "accBgpImportAction": accBgpImportAction,
       "accBgpImportPreference": accBgpImportPreference,
       "accBgpImportStatus": accBgpImportStatus,
       "accBgpASWeightTable": accBgpASWeightTable,
       "accBgpASWeightEntry": accBgpASWeightEntry,
       "accBgpASWeightAS": accBgpASWeightAS,
       "accBgpASWeight": accBgpASWeight,
       "accBgpASWeightStatus": accBgpASWeightStatus,
       "accBgpAggregateTable": accBgpAggregateTable,
       "accBgpAggregateEntry": accBgpAggregateEntry,
       "accBgpAggregateAddr": accBgpAggregateAddr,
       "accBgpAggregateMask": accBgpAggregateMask,
       "accBgpAggregateAdvertise": accBgpAggregateAdvertise,
       "accBgpAggregatePref": accBgpAggregatePref,
       "accBgpAggregateComponents": accBgpAggregateComponents,
       "accBgpAggregateActive": accBgpAggregateActive,
       "accBgpAggregateAdminStat": accBgpAggregateAdminStat,
       "accBgpAggregateStatus": accBgpAggregateStatus,
       "accBgpAggrComponentTable": accBgpAggrComponentTable,
       "accBgpAggrComponentEntry": accBgpAggrComponentEntry,
       "accBgpAggrCompParentAddr": accBgpAggrCompParentAddr,
       "accBgpAggrCompParentMask": accBgpAggrCompParentMask,
       "accBgpAggrComponentAddr": accBgpAggrComponentAddr,
       "accBgpAggrComponentMask": accBgpAggrComponentMask,
       "accBgpAggrComponentProtocol": accBgpAggrComponentProtocol,
       "accBgpAggrComponentActive": accBgpAggrComponentActive,
       "accBgpAggrComponentStatus": accBgpAggrComponentStatus,
       "accBgpExportTable": accBgpExportTable,
       "accBgpExportEntry": accBgpExportEntry,
       "accBgpExportPeerAS": accBgpExportPeerAS,
       "accBgpExportPeerAddress": accBgpExportPeerAddress,
       "accBgpExportProtocol": accBgpExportProtocol,
       "accBgpExportSpecific2": accBgpExportSpecific2,
       "accBgpExportSpecific1": accBgpExportSpecific1,
       "accBgpExportNetwork": accBgpExportNetwork,
       "accBgpExportMask": accBgpExportMask,
       "accBgpExportAction": accBgpExportAction,
       "accBgpExportMetric": accBgpExportMetric,
       "accBgpExportStatus": accBgpExportStatus,
       "accBgpTraps": accBgpTraps,
       "accBgpPeerNotDisbldTrap": accBgpPeerNotDisbldTrap,
       "accBgpAddFltPolTrap": accBgpAddFltPolTrap,
       "accBgpDelFltPolTrap": accBgpDelFltPolTrap,
       "accBgpAddImpPolTrap": accBgpAddImpPolTrap,
       "accBgpDelImpPolTrap": accBgpDelImpPolTrap,
       "accBgpAddAsWtPolTrap": accBgpAddAsWtPolTrap,
       "accBgpDelAsWtPolTrap": accBgpDelAsWtPolTrap,
       "accBgpNbrTrap": accBgpNbrTrap,
       "accBgpInvHoldKeepAliveTrap": accBgpInvHoldKeepAliveTrap,
       "accBgpIllegalLocalAsTrap": accBgpIllegalLocalAsTrap,
       "accBgpIBGPPeerAddrTrap": accBgpIBGPPeerAddrTrap,
       "accBgpPolPeerAddrTrap": accBgpPolPeerAddrTrap,
       "accBgpPeerNotFndTrap": accBgpPeerNotFndTrap,
       "accBgpPeerAllocTrap": accBgpPeerAllocTrap,
       "accBgpRcvBfrAllocTrap": accBgpRcvBfrAllocTrap,
       "accBgpTmrAllocTrap": accBgpTmrAllocTrap,
       "accBgpPeerEnableTmrAllocTrap": accBgpPeerEnableTmrAllocTrap,
       "accBgpGrpAllocTrap": accBgpGrpAllocTrap,
       "accBgpShutdownAllocTrap": accBgpShutdownAllocTrap,
       "accBgpOrphanTrap": accBgpOrphanTrap,
       "accBgpRtclAllocTrap": accBgpRtclAllocTrap,
       "accBgpAggrAllocTrap": accBgpAggrAllocTrap,
       "accBgpPolAllocTrap": accBgpPolAllocTrap,
       "accBgpAnnounceAllocTrap": accBgpAnnounceAllocTrap,
       "accBgpAddNhTrap": accBgpAddNhTrap,
       "accBgpNlriAllocTrap": accBgpNlriAllocTrap,
       "accBgpPeerRtAllocTrap": accBgpPeerRtAllocTrap,
       "accBgpPeerRtEntryAllocTrap": accBgpPeerRtEntryAllocTrap,
       "accBgpRtInfoAllocTrap": accBgpRtInfoAllocTrap,
       "accBgpEvntMemTrap": accBgpEvntMemTrap,
       "accBgpPeerCBAllocTrap": accBgpPeerCBAllocTrap,
       "accBgpRelEvntMemTrap": accBgpRelEvntMemTrap,
       "accBgpConnectTrap": accBgpConnectTrap,
       "accBgpPeerInvStateTrap": accBgpPeerInvStateTrap,
       "accBgpAllocTrap": accBgpAllocTrap,
       "accBgpPeerNoTxBfrTrap": accBgpPeerNoTxBfrTrap,
       "accBgpPeerWriteTrap": accBgpPeerWriteTrap,
       "accBgpClosingConnTrap": accBgpClosingConnTrap,
       "accBgpSpoolBfrTrap": accBgpSpoolBfrTrap,
       "accBgpRtryCntTrap": accBgpRtryCntTrap,
       "accBgpPaAllocTrap": accBgpPaAllocTrap,
       "accBgpPSegAllocTrap": accBgpPSegAllocTrap,
       "accBgpAddNxtHopTrap": accBgpAddNxtHopTrap,
       "accBgpRxBufAllocTrap": accBgpRxBufAllocTrap,
       "accBgpPeerRcvBfrAllocTrap": accBgpPeerRcvBfrAllocTrap,
       "accBgpTrapMsg": accBgpTrapMsg}
)
