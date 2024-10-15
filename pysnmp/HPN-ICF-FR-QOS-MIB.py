# SNMP MIB module (HPN-ICF-FR-QOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-FR-QOS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:00:27 2024
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

(hpnicfQoS,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfQoS")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hpnicfFrQoSMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 32, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HpnicfCirAllowDirection(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 1),
          ("inboundAndOutbound", 3),
          ("outbound", 2))
    )



# MIB Managed Objects in the order of their OIDs

_HpnicfFrQoSObjects_ObjectIdentity = ObjectIdentity
hpnicfFrQoSObjects = _HpnicfFrQoSObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 32, 3, 1)
)
_HpnicfFrClassObjects_ObjectIdentity = ObjectIdentity
hpnicfFrClassObjects = _HpnicfFrClassObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 32, 3, 1, 1)
)
_HpnicfFrClassIndexNext_Type = Integer32
_HpnicfFrClassIndexNext_Object = MibScalar
hpnicfFrClassIndexNext = _HpnicfFrClassIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 32, 3, 1, 1, 1),
    _HpnicfFrClassIndexNext_Type()
)
hpnicfFrClassIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFrClassIndexNext.setStatus("current")
_HpnicfFrClassCfgInfoTable_Object = MibTable
hpnicfFrClassCfgInfoTable = _HpnicfFrClassCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 32, 3, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hpnicfFrClassCfgInfoTable.setStatus("current")
_HpnicfFrClassCfgInfoEntry_Object = MibTableRow
hpnicfFrClassCfgInfoEntry = _HpnicfFrClassCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 32, 3, 1, 1, 2, 1)
)
hpnicfFrClassCfgInfoEntry.setIndexNames(
    (0, "HPN-ICF-FR-QOS-MIB", "hpnicfFrClassIndex"),
)
if mibBuilder.loadTexts:
    hpnicfFrClassCfgInfoEntry.setStatus("current")
_HpnicfFrClassIndex_Type = Integer32
_HpnicfFrClassIndex_Object = MibTableColumn
hpnicfFrClassIndex = _HpnicfFrClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 32, 3, 1, 1, 2, 1, 1),
    _HpnicfFrClassIndex_Type()
)
hpnicfFrClassIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfFrClassIndex.setStatus("current")


class _HpnicfFrClassName_Type(OctetString):
    """Custom type hpnicfFrClassName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HpnicfFrClassName_Type.__name__ = "OctetString"
_HpnicfFrClassName_Object = MibTableColumn
hpnicfFrClassName = _HpnicfFrClassName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 32, 3, 1, 1, 2, 1, 2),
    _HpnicfFrClassName_Type()
)
hpnicfFrClassName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfFrClassName.setStatus("current")
_HpnicfFrClassRowStatus_Type = RowStatus
_HpnicfFrClassRowStatus_Object = MibTableColumn
hpnicfFrClassRowStatus = _HpnicfFrClassRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 32, 3, 1, 1, 2, 1, 3),
    _HpnicfFrClassRowStatus_Type()
)
hpnicfFrClassRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfFrClassRowStatus.setStatus("current")
_HpnicfCirAllowCfgInfoTable_Object = MibTable
hpnicfCirAllowCfgInfoTable = _HpnicfCirAllowCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 32, 3, 1, 1, 3)
)
if mibBuilder.loadTexts:
    hpnicfCirAllowCfgInfoTable.setStatus("current")
_HpnicfCirAllowCfgInfoEntry_Object = MibTableRow
hpnicfCirAllowCfgInfoEntry = _HpnicfCirAllowCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 32, 3, 1, 1, 3, 1)
)
hpnicfCirAllowCfgInfoEntry.setIndexNames(
    (0, "HPN-ICF-FR-QOS-MIB", "hpnicfCirAllowFrClassIndex"),
    (0, "HPN-ICF-FR-QOS-MIB", "hpnicfCirAllowDirection"),
)
if mibBuilder.loadTexts:
    hpnicfCirAllowCfgInfoEntry.setStatus("current")
_HpnicfCirAllowFrClassIndex_Type = Integer32
_HpnicfCirAllowFrClassIndex_Object = MibTableColumn
hpnicfCirAllowFrClassIndex = _HpnicfCirAllowFrClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 32, 3, 1, 1, 3, 1, 1),
    _HpnicfCirAllowFrClassIndex_Type()
)
hpnicfCirAllowFrClassIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfCirAllowFrClassIndex.setStatus("current")
_HpnicfCirAllowDirection_Type = HpnicfCirAllowDirection
_HpnicfCirAllowDirection_Object = MibTableColumn
hpnicfCirAllowDirection = _HpnicfCirAllowDirection_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 32, 3, 1, 1, 3, 1, 2),
    _HpnicfCirAllowDirection_Type()
)
hpnicfCirAllowDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfCirAllowDirection.setStatus("current")


class _HpnicfCirAllowValue_Type(Integer32):
    """Custom type hpnicfCirAllowValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 45000000),
    )


_HpnicfCirAllowValue_Type.__name__ = "Integer32"
_HpnicfCirAllowValue_Object = MibTableColumn
hpnicfCirAllowValue = _HpnicfCirAllowValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 32, 3, 1, 1, 3, 1, 3),
    _HpnicfCirAllowValue_Type()
)
hpnicfCirAllowValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCirAllowValue.setStatus("current")
_HpnicfCirAllowRowStatus_Type = RowStatus
_HpnicfCirAllowRowStatus_Object = MibTableColumn
hpnicfCirAllowRowStatus = _HpnicfCirAllowRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 32, 3, 1, 1, 3, 1, 4),
    _HpnicfCirAllowRowStatus_Type()
)
hpnicfCirAllowRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCirAllowRowStatus.setStatus("current")
_HpnicfCirCfgInfoTable_Object = MibTable
hpnicfCirCfgInfoTable = _HpnicfCirCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 32, 3, 1, 1, 4)
)
if mibBuilder.loadTexts:
    hpnicfCirCfgInfoTable.setStatus("current")
_HpnicfCirCfgInfoEntry_Object = MibTableRow
hpnicfCirCfgInfoEntry = _HpnicfCirCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 32, 3, 1, 1, 4, 1)
)
hpnicfCirCfgInfoEntry.setIndexNames(
    (0, "HPN-ICF-FR-QOS-MIB", "hpnicfCirFrClassIndex"),
)
if mibBuilder.loadTexts:
    hpnicfCirCfgInfoEntry.setStatus("current")
_HpnicfCirFrClassIndex_Type = Integer32
_HpnicfCirFrClassIndex_Object = MibTableColumn
hpnicfCirFrClassIndex = _HpnicfCirFrClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 32, 3, 1, 1, 4, 1, 1),
    _HpnicfCirFrClassIndex_Type()
)
hpnicfCirFrClassIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfCirFrClassIndex.setStatus("current")


class _HpnicfCirValue_Type(Integer32):
    """Custom type hpnicfCirValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 45000000),
    )


_HpnicfCirValue_Type.__name__ = "Integer32"
_HpnicfCirValue_Object = MibTableColumn
hpnicfCirValue = _HpnicfCirValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 32, 3, 1, 1, 4, 1, 2),
    _HpnicfCirValue_Type()
)
hpnicfCirValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCirValue.setStatus("current")
_HpnicfCirRowStatus_Type = RowStatus
_HpnicfCirRowStatus_Object = MibTableColumn
hpnicfCirRowStatus = _HpnicfCirRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 32, 3, 1, 1, 4, 1, 3),
    _HpnicfCirRowStatus_Type()
)
hpnicfCirRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCirRowStatus.setStatus("current")
_HpnicfIfApplyFrClassTable_Object = MibTable
hpnicfIfApplyFrClassTable = _HpnicfIfApplyFrClassTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 32, 3, 1, 1, 5)
)
if mibBuilder.loadTexts:
    hpnicfIfApplyFrClassTable.setStatus("current")
_HpnicfIfApplyFrClassEntry_Object = MibTableRow
hpnicfIfApplyFrClassEntry = _HpnicfIfApplyFrClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 32, 3, 1, 1, 5, 1)
)
hpnicfIfApplyFrClassEntry.setIndexNames(
    (0, "HPN-ICF-FR-QOS-MIB", "hpnicfIfApplyFrClassIfIndex"),
)
if mibBuilder.loadTexts:
    hpnicfIfApplyFrClassEntry.setStatus("current")
_HpnicfIfApplyFrClassIfIndex_Type = Integer32
_HpnicfIfApplyFrClassIfIndex_Object = MibTableColumn
hpnicfIfApplyFrClassIfIndex = _HpnicfIfApplyFrClassIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 32, 3, 1, 1, 5, 1, 1),
    _HpnicfIfApplyFrClassIfIndex_Type()
)
hpnicfIfApplyFrClassIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfIfApplyFrClassIfIndex.setStatus("current")
_HpnicfIfApplyFrClassIndex_Type = Integer32
_HpnicfIfApplyFrClassIndex_Object = MibTableColumn
hpnicfIfApplyFrClassIndex = _HpnicfIfApplyFrClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 32, 3, 1, 1, 5, 1, 2),
    _HpnicfIfApplyFrClassIndex_Type()
)
hpnicfIfApplyFrClassIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIfApplyFrClassIndex.setStatus("current")
_HpnicfIfApplyFrClassRowStatus_Type = RowStatus
_HpnicfIfApplyFrClassRowStatus_Object = MibTableColumn
hpnicfIfApplyFrClassRowStatus = _HpnicfIfApplyFrClassRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 32, 3, 1, 1, 5, 1, 3),
    _HpnicfIfApplyFrClassRowStatus_Type()
)
hpnicfIfApplyFrClassRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIfApplyFrClassRowStatus.setStatus("current")
_HpnicfPvcApplyFrClassTable_Object = MibTable
hpnicfPvcApplyFrClassTable = _HpnicfPvcApplyFrClassTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 32, 3, 1, 1, 6)
)
if mibBuilder.loadTexts:
    hpnicfPvcApplyFrClassTable.setStatus("current")
_HpnicfPvcApplyFrClassEntry_Object = MibTableRow
hpnicfPvcApplyFrClassEntry = _HpnicfPvcApplyFrClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 32, 3, 1, 1, 6, 1)
)
hpnicfPvcApplyFrClassEntry.setIndexNames(
    (0, "HPN-ICF-FR-QOS-MIB", "hpnicfPvcApplyFrClassIfIndex"),
    (0, "HPN-ICF-FR-QOS-MIB", "hpnicfPvcApplyFrClassDlciNum"),
)
if mibBuilder.loadTexts:
    hpnicfPvcApplyFrClassEntry.setStatus("current")
_HpnicfPvcApplyFrClassIfIndex_Type = Integer32
_HpnicfPvcApplyFrClassIfIndex_Object = MibTableColumn
hpnicfPvcApplyFrClassIfIndex = _HpnicfPvcApplyFrClassIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 32, 3, 1, 1, 6, 1, 1),
    _HpnicfPvcApplyFrClassIfIndex_Type()
)
hpnicfPvcApplyFrClassIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfPvcApplyFrClassIfIndex.setStatus("current")


class _HpnicfPvcApplyFrClassDlciNum_Type(Integer32):
    """Custom type hpnicfPvcApplyFrClassDlciNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1007),
    )


_HpnicfPvcApplyFrClassDlciNum_Type.__name__ = "Integer32"
_HpnicfPvcApplyFrClassDlciNum_Object = MibTableColumn
hpnicfPvcApplyFrClassDlciNum = _HpnicfPvcApplyFrClassDlciNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 32, 3, 1, 1, 6, 1, 2),
    _HpnicfPvcApplyFrClassDlciNum_Type()
)
hpnicfPvcApplyFrClassDlciNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfPvcApplyFrClassDlciNum.setStatus("current")
_HpnicfPvcApplyFrClassIndex_Type = Integer32
_HpnicfPvcApplyFrClassIndex_Object = MibTableColumn
hpnicfPvcApplyFrClassIndex = _HpnicfPvcApplyFrClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 32, 3, 1, 1, 6, 1, 3),
    _HpnicfPvcApplyFrClassIndex_Type()
)
hpnicfPvcApplyFrClassIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPvcApplyFrClassIndex.setStatus("current")
_HpnicfPvcApplyFrClassRowStatus_Type = RowStatus
_HpnicfPvcApplyFrClassRowStatus_Object = MibTableColumn
hpnicfPvcApplyFrClassRowStatus = _HpnicfPvcApplyFrClassRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 32, 3, 1, 1, 6, 1, 4),
    _HpnicfPvcApplyFrClassRowStatus_Type()
)
hpnicfPvcApplyFrClassRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPvcApplyFrClassRowStatus.setStatus("current")
_HpnicfFrPvcBandwidthTable_Object = MibTable
hpnicfFrPvcBandwidthTable = _HpnicfFrPvcBandwidthTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 32, 3, 1, 1, 7)
)
if mibBuilder.loadTexts:
    hpnicfFrPvcBandwidthTable.setStatus("current")
_HpnicfFrPvcBandwidthEntry_Object = MibTableRow
hpnicfFrPvcBandwidthEntry = _HpnicfFrPvcBandwidthEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 32, 3, 1, 1, 7, 1)
)
hpnicfFrPvcBandwidthEntry.setIndexNames(
    (0, "HPN-ICF-FR-QOS-MIB", "hpnicfPvcApplyFrClassIfIndex"),
    (0, "HPN-ICF-FR-QOS-MIB", "hpnicfPvcApplyFrClassDlciNum"),
)
if mibBuilder.loadTexts:
    hpnicfFrPvcBandwidthEntry.setStatus("current")
_HpnicfFrPvcBandwidthMaxReservedBW_Type = Integer32
_HpnicfFrPvcBandwidthMaxReservedBW_Object = MibTableColumn
hpnicfFrPvcBandwidthMaxReservedBW = _HpnicfFrPvcBandwidthMaxReservedBW_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 32, 3, 1, 1, 7, 1, 1),
    _HpnicfFrPvcBandwidthMaxReservedBW_Type()
)
hpnicfFrPvcBandwidthMaxReservedBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFrPvcBandwidthMaxReservedBW.setStatus("current")
_HpnicfFrPvcBandwidthAvailable_Type = Integer32
_HpnicfFrPvcBandwidthAvailable_Object = MibTableColumn
hpnicfFrPvcBandwidthAvailable = _HpnicfFrPvcBandwidthAvailable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 32, 3, 1, 1, 7, 1, 2),
    _HpnicfFrPvcBandwidthAvailable_Type()
)
hpnicfFrPvcBandwidthAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFrPvcBandwidthAvailable.setStatus("current")
_HpnicfRTPQoSObjects_ObjectIdentity = ObjectIdentity
hpnicfRTPQoSObjects = _HpnicfRTPQoSObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 32, 3, 1, 2)
)
_HpnicfRTPFrClassApplyTable_Object = MibTable
hpnicfRTPFrClassApplyTable = _HpnicfRTPFrClassApplyTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 32, 3, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hpnicfRTPFrClassApplyTable.setStatus("current")
_HpnicfRTPFrClassApplyEntry_Object = MibTableRow
hpnicfRTPFrClassApplyEntry = _HpnicfRTPFrClassApplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 32, 3, 1, 2, 1, 1)
)
hpnicfRTPFrClassApplyEntry.setIndexNames(
    (0, "HPN-ICF-FR-QOS-MIB", "hpnicfRTPFrClassApplyFrClassIndex"),
)
if mibBuilder.loadTexts:
    hpnicfRTPFrClassApplyEntry.setStatus("current")
_HpnicfRTPFrClassApplyFrClassIndex_Type = Integer32
_HpnicfRTPFrClassApplyFrClassIndex_Object = MibTableColumn
hpnicfRTPFrClassApplyFrClassIndex = _HpnicfRTPFrClassApplyFrClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 32, 3, 1, 2, 1, 1, 1),
    _HpnicfRTPFrClassApplyFrClassIndex_Type()
)
hpnicfRTPFrClassApplyFrClassIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfRTPFrClassApplyFrClassIndex.setStatus("current")


class _HpnicfRTPFrClassApplyStartPort_Type(Integer32):
    """Custom type hpnicfRTPFrClassApplyStartPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2000, 65535),
    )


_HpnicfRTPFrClassApplyStartPort_Type.__name__ = "Integer32"
_HpnicfRTPFrClassApplyStartPort_Object = MibTableColumn
hpnicfRTPFrClassApplyStartPort = _HpnicfRTPFrClassApplyStartPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 32, 3, 1, 2, 1, 1, 2),
    _HpnicfRTPFrClassApplyStartPort_Type()
)
hpnicfRTPFrClassApplyStartPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRTPFrClassApplyStartPort.setStatus("current")


class _HpnicfRTPFrClassApplyEndPort_Type(Integer32):
    """Custom type hpnicfRTPFrClassApplyEndPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2000, 65535),
    )


_HpnicfRTPFrClassApplyEndPort_Type.__name__ = "Integer32"
_HpnicfRTPFrClassApplyEndPort_Object = MibTableColumn
hpnicfRTPFrClassApplyEndPort = _HpnicfRTPFrClassApplyEndPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 32, 3, 1, 2, 1, 1, 3),
    _HpnicfRTPFrClassApplyEndPort_Type()
)
hpnicfRTPFrClassApplyEndPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRTPFrClassApplyEndPort.setStatus("current")


class _HpnicfRTPFrClassApplyBandWidth_Type(Integer32):
    """Custom type hpnicfRTPFrClassApplyBandWidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 1000000),
    )


_HpnicfRTPFrClassApplyBandWidth_Type.__name__ = "Integer32"
_HpnicfRTPFrClassApplyBandWidth_Object = MibTableColumn
hpnicfRTPFrClassApplyBandWidth = _HpnicfRTPFrClassApplyBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 32, 3, 1, 2, 1, 1, 4),
    _HpnicfRTPFrClassApplyBandWidth_Type()
)
hpnicfRTPFrClassApplyBandWidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRTPFrClassApplyBandWidth.setStatus("current")


class _HpnicfRTPFrClassApplyCbs_Type(Integer32):
    """Custom type hpnicfRTPFrClassApplyCbs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1500, 2000000),
    )


_HpnicfRTPFrClassApplyCbs_Type.__name__ = "Integer32"
_HpnicfRTPFrClassApplyCbs_Object = MibTableColumn
hpnicfRTPFrClassApplyCbs = _HpnicfRTPFrClassApplyCbs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 32, 3, 1, 2, 1, 1, 5),
    _HpnicfRTPFrClassApplyCbs_Type()
)
hpnicfRTPFrClassApplyCbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRTPFrClassApplyCbs.setStatus("current")
_HpnicfRTPFrClassApplyRowStatus_Type = RowStatus
_HpnicfRTPFrClassApplyRowStatus_Object = MibTableColumn
hpnicfRTPFrClassApplyRowStatus = _HpnicfRTPFrClassApplyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 32, 3, 1, 2, 1, 1, 6),
    _HpnicfRTPFrClassApplyRowStatus_Type()
)
hpnicfRTPFrClassApplyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRTPFrClassApplyRowStatus.setStatus("current")
_HpnicfRTPFrPvcQueueRunInfoTable_Object = MibTable
hpnicfRTPFrPvcQueueRunInfoTable = _HpnicfRTPFrPvcQueueRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 32, 3, 1, 2, 2)
)
if mibBuilder.loadTexts:
    hpnicfRTPFrPvcQueueRunInfoTable.setStatus("current")
_HpnicfRTPFrPvcQueueRunInfoEntry_Object = MibTableRow
hpnicfRTPFrPvcQueueRunInfoEntry = _HpnicfRTPFrPvcQueueRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 32, 3, 1, 2, 2, 1)
)
hpnicfRTPFrPvcQueueRunInfoEntry.setIndexNames(
    (0, "HPN-ICF-FR-QOS-MIB", "hpnicfPvcApplyFrClassIfIndex"),
    (0, "HPN-ICF-FR-QOS-MIB", "hpnicfPvcApplyFrClassDlciNum"),
)
if mibBuilder.loadTexts:
    hpnicfRTPFrPvcQueueRunInfoEntry.setStatus("current")
_HpnicfRTPFrPvcQueueSize_Type = Integer32
_HpnicfRTPFrPvcQueueSize_Object = MibTableColumn
hpnicfRTPFrPvcQueueSize = _HpnicfRTPFrPvcQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 32, 3, 1, 2, 2, 1, 1),
    _HpnicfRTPFrPvcQueueSize_Type()
)
hpnicfRTPFrPvcQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfRTPFrPvcQueueSize.setStatus("current")
_HpnicfRTPFrPvcQueueMaxSize_Type = Integer32
_HpnicfRTPFrPvcQueueMaxSize_Object = MibTableColumn
hpnicfRTPFrPvcQueueMaxSize = _HpnicfRTPFrPvcQueueMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 32, 3, 1, 2, 2, 1, 2),
    _HpnicfRTPFrPvcQueueMaxSize_Type()
)
hpnicfRTPFrPvcQueueMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfRTPFrPvcQueueMaxSize.setStatus("current")
_HpnicfRTPFrPvcQueueOutputs_Type = Counter32
_HpnicfRTPFrPvcQueueOutputs_Object = MibTableColumn
hpnicfRTPFrPvcQueueOutputs = _HpnicfRTPFrPvcQueueOutputs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 32, 3, 1, 2, 2, 1, 3),
    _HpnicfRTPFrPvcQueueOutputs_Type()
)
hpnicfRTPFrPvcQueueOutputs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfRTPFrPvcQueueOutputs.setStatus("current")
_HpnicfRTPFrPvcQueueDiscards_Type = Counter32
_HpnicfRTPFrPvcQueueDiscards_Object = MibTableColumn
hpnicfRTPFrPvcQueueDiscards = _HpnicfRTPFrPvcQueueDiscards_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 32, 3, 1, 2, 2, 1, 4),
    _HpnicfRTPFrPvcQueueDiscards_Type()
)
hpnicfRTPFrPvcQueueDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfRTPFrPvcQueueDiscards.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-FR-QOS-MIB",
    **{"HpnicfCirAllowDirection": HpnicfCirAllowDirection,
       "hpnicfFrQoSMib": hpnicfFrQoSMib,
       "hpnicfFrQoSObjects": hpnicfFrQoSObjects,
       "hpnicfFrClassObjects": hpnicfFrClassObjects,
       "hpnicfFrClassIndexNext": hpnicfFrClassIndexNext,
       "hpnicfFrClassCfgInfoTable": hpnicfFrClassCfgInfoTable,
       "hpnicfFrClassCfgInfoEntry": hpnicfFrClassCfgInfoEntry,
       "hpnicfFrClassIndex": hpnicfFrClassIndex,
       "hpnicfFrClassName": hpnicfFrClassName,
       "hpnicfFrClassRowStatus": hpnicfFrClassRowStatus,
       "hpnicfCirAllowCfgInfoTable": hpnicfCirAllowCfgInfoTable,
       "hpnicfCirAllowCfgInfoEntry": hpnicfCirAllowCfgInfoEntry,
       "hpnicfCirAllowFrClassIndex": hpnicfCirAllowFrClassIndex,
       "hpnicfCirAllowDirection": hpnicfCirAllowDirection,
       "hpnicfCirAllowValue": hpnicfCirAllowValue,
       "hpnicfCirAllowRowStatus": hpnicfCirAllowRowStatus,
       "hpnicfCirCfgInfoTable": hpnicfCirCfgInfoTable,
       "hpnicfCirCfgInfoEntry": hpnicfCirCfgInfoEntry,
       "hpnicfCirFrClassIndex": hpnicfCirFrClassIndex,
       "hpnicfCirValue": hpnicfCirValue,
       "hpnicfCirRowStatus": hpnicfCirRowStatus,
       "hpnicfIfApplyFrClassTable": hpnicfIfApplyFrClassTable,
       "hpnicfIfApplyFrClassEntry": hpnicfIfApplyFrClassEntry,
       "hpnicfIfApplyFrClassIfIndex": hpnicfIfApplyFrClassIfIndex,
       "hpnicfIfApplyFrClassIndex": hpnicfIfApplyFrClassIndex,
       "hpnicfIfApplyFrClassRowStatus": hpnicfIfApplyFrClassRowStatus,
       "hpnicfPvcApplyFrClassTable": hpnicfPvcApplyFrClassTable,
       "hpnicfPvcApplyFrClassEntry": hpnicfPvcApplyFrClassEntry,
       "hpnicfPvcApplyFrClassIfIndex": hpnicfPvcApplyFrClassIfIndex,
       "hpnicfPvcApplyFrClassDlciNum": hpnicfPvcApplyFrClassDlciNum,
       "hpnicfPvcApplyFrClassIndex": hpnicfPvcApplyFrClassIndex,
       "hpnicfPvcApplyFrClassRowStatus": hpnicfPvcApplyFrClassRowStatus,
       "hpnicfFrPvcBandwidthTable": hpnicfFrPvcBandwidthTable,
       "hpnicfFrPvcBandwidthEntry": hpnicfFrPvcBandwidthEntry,
       "hpnicfFrPvcBandwidthMaxReservedBW": hpnicfFrPvcBandwidthMaxReservedBW,
       "hpnicfFrPvcBandwidthAvailable": hpnicfFrPvcBandwidthAvailable,
       "hpnicfRTPQoSObjects": hpnicfRTPQoSObjects,
       "hpnicfRTPFrClassApplyTable": hpnicfRTPFrClassApplyTable,
       "hpnicfRTPFrClassApplyEntry": hpnicfRTPFrClassApplyEntry,
       "hpnicfRTPFrClassApplyFrClassIndex": hpnicfRTPFrClassApplyFrClassIndex,
       "hpnicfRTPFrClassApplyStartPort": hpnicfRTPFrClassApplyStartPort,
       "hpnicfRTPFrClassApplyEndPort": hpnicfRTPFrClassApplyEndPort,
       "hpnicfRTPFrClassApplyBandWidth": hpnicfRTPFrClassApplyBandWidth,
       "hpnicfRTPFrClassApplyCbs": hpnicfRTPFrClassApplyCbs,
       "hpnicfRTPFrClassApplyRowStatus": hpnicfRTPFrClassApplyRowStatus,
       "hpnicfRTPFrPvcQueueRunInfoTable": hpnicfRTPFrPvcQueueRunInfoTable,
       "hpnicfRTPFrPvcQueueRunInfoEntry": hpnicfRTPFrPvcQueueRunInfoEntry,
       "hpnicfRTPFrPvcQueueSize": hpnicfRTPFrPvcQueueSize,
       "hpnicfRTPFrPvcQueueMaxSize": hpnicfRTPFrPvcQueueMaxSize,
       "hpnicfRTPFrPvcQueueOutputs": hpnicfRTPFrPvcQueueOutputs,
       "hpnicfRTPFrPvcQueueDiscards": hpnicfRTPFrPvcQueueDiscards}
)
