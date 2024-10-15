# SNMP MIB module (HH3C-FR-QOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-FR-QOS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:53:27 2024
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

(hh3cQoS,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cQoS")

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

hh3cFrQoSMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 32, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Hh3cCirAllowDirection(Integer32, TextualConvention):
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

_Hh3cFrQoSObjects_ObjectIdentity = ObjectIdentity
hh3cFrQoSObjects = _Hh3cFrQoSObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 32, 3, 1)
)
_Hh3cFrClassObjects_ObjectIdentity = ObjectIdentity
hh3cFrClassObjects = _Hh3cFrClassObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 32, 3, 1, 1)
)
_Hh3cFrClassIndexNext_Type = Integer32
_Hh3cFrClassIndexNext_Object = MibScalar
hh3cFrClassIndexNext = _Hh3cFrClassIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 32, 3, 1, 1, 1),
    _Hh3cFrClassIndexNext_Type()
)
hh3cFrClassIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFrClassIndexNext.setStatus("current")
_Hh3cFrClassCfgInfoTable_Object = MibTable
hh3cFrClassCfgInfoTable = _Hh3cFrClassCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 32, 3, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cFrClassCfgInfoTable.setStatus("current")
_Hh3cFrClassCfgInfoEntry_Object = MibTableRow
hh3cFrClassCfgInfoEntry = _Hh3cFrClassCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 32, 3, 1, 1, 2, 1)
)
hh3cFrClassCfgInfoEntry.setIndexNames(
    (0, "HH3C-FR-QOS-MIB", "hh3cFrClassIndex"),
)
if mibBuilder.loadTexts:
    hh3cFrClassCfgInfoEntry.setStatus("current")
_Hh3cFrClassIndex_Type = Integer32
_Hh3cFrClassIndex_Object = MibTableColumn
hh3cFrClassIndex = _Hh3cFrClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 32, 3, 1, 1, 2, 1, 1),
    _Hh3cFrClassIndex_Type()
)
hh3cFrClassIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cFrClassIndex.setStatus("current")


class _Hh3cFrClassName_Type(OctetString):
    """Custom type hh3cFrClassName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_Hh3cFrClassName_Type.__name__ = "OctetString"
_Hh3cFrClassName_Object = MibTableColumn
hh3cFrClassName = _Hh3cFrClassName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 32, 3, 1, 1, 2, 1, 2),
    _Hh3cFrClassName_Type()
)
hh3cFrClassName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFrClassName.setStatus("current")
_Hh3cFrClassRowStatus_Type = RowStatus
_Hh3cFrClassRowStatus_Object = MibTableColumn
hh3cFrClassRowStatus = _Hh3cFrClassRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 32, 3, 1, 1, 2, 1, 3),
    _Hh3cFrClassRowStatus_Type()
)
hh3cFrClassRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFrClassRowStatus.setStatus("current")
_Hh3cCirAllowCfgInfoTable_Object = MibTable
hh3cCirAllowCfgInfoTable = _Hh3cCirAllowCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 32, 3, 1, 1, 3)
)
if mibBuilder.loadTexts:
    hh3cCirAllowCfgInfoTable.setStatus("current")
_Hh3cCirAllowCfgInfoEntry_Object = MibTableRow
hh3cCirAllowCfgInfoEntry = _Hh3cCirAllowCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 32, 3, 1, 1, 3, 1)
)
hh3cCirAllowCfgInfoEntry.setIndexNames(
    (0, "HH3C-FR-QOS-MIB", "hh3cCirAllowFrClassIndex"),
    (0, "HH3C-FR-QOS-MIB", "hh3cCirAllowDirection"),
)
if mibBuilder.loadTexts:
    hh3cCirAllowCfgInfoEntry.setStatus("current")
_Hh3cCirAllowFrClassIndex_Type = Integer32
_Hh3cCirAllowFrClassIndex_Object = MibTableColumn
hh3cCirAllowFrClassIndex = _Hh3cCirAllowFrClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 32, 3, 1, 1, 3, 1, 1),
    _Hh3cCirAllowFrClassIndex_Type()
)
hh3cCirAllowFrClassIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cCirAllowFrClassIndex.setStatus("current")
_Hh3cCirAllowDirection_Type = Hh3cCirAllowDirection
_Hh3cCirAllowDirection_Object = MibTableColumn
hh3cCirAllowDirection = _Hh3cCirAllowDirection_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 32, 3, 1, 1, 3, 1, 2),
    _Hh3cCirAllowDirection_Type()
)
hh3cCirAllowDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cCirAllowDirection.setStatus("current")


class _Hh3cCirAllowValue_Type(Integer32):
    """Custom type hh3cCirAllowValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 45000000),
    )


_Hh3cCirAllowValue_Type.__name__ = "Integer32"
_Hh3cCirAllowValue_Object = MibTableColumn
hh3cCirAllowValue = _Hh3cCirAllowValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 32, 3, 1, 1, 3, 1, 3),
    _Hh3cCirAllowValue_Type()
)
hh3cCirAllowValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCirAllowValue.setStatus("current")
_Hh3cCirAllowRowStatus_Type = RowStatus
_Hh3cCirAllowRowStatus_Object = MibTableColumn
hh3cCirAllowRowStatus = _Hh3cCirAllowRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 32, 3, 1, 1, 3, 1, 4),
    _Hh3cCirAllowRowStatus_Type()
)
hh3cCirAllowRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCirAllowRowStatus.setStatus("current")
_Hh3cCirCfgInfoTable_Object = MibTable
hh3cCirCfgInfoTable = _Hh3cCirCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 32, 3, 1, 1, 4)
)
if mibBuilder.loadTexts:
    hh3cCirCfgInfoTable.setStatus("current")
_Hh3cCirCfgInfoEntry_Object = MibTableRow
hh3cCirCfgInfoEntry = _Hh3cCirCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 32, 3, 1, 1, 4, 1)
)
hh3cCirCfgInfoEntry.setIndexNames(
    (0, "HH3C-FR-QOS-MIB", "hh3cCirFrClassIndex"),
)
if mibBuilder.loadTexts:
    hh3cCirCfgInfoEntry.setStatus("current")
_Hh3cCirFrClassIndex_Type = Integer32
_Hh3cCirFrClassIndex_Object = MibTableColumn
hh3cCirFrClassIndex = _Hh3cCirFrClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 32, 3, 1, 1, 4, 1, 1),
    _Hh3cCirFrClassIndex_Type()
)
hh3cCirFrClassIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cCirFrClassIndex.setStatus("current")


class _Hh3cCirValue_Type(Integer32):
    """Custom type hh3cCirValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 45000000),
    )


_Hh3cCirValue_Type.__name__ = "Integer32"
_Hh3cCirValue_Object = MibTableColumn
hh3cCirValue = _Hh3cCirValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 32, 3, 1, 1, 4, 1, 2),
    _Hh3cCirValue_Type()
)
hh3cCirValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCirValue.setStatus("current")
_Hh3cCirRowStatus_Type = RowStatus
_Hh3cCirRowStatus_Object = MibTableColumn
hh3cCirRowStatus = _Hh3cCirRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 32, 3, 1, 1, 4, 1, 3),
    _Hh3cCirRowStatus_Type()
)
hh3cCirRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCirRowStatus.setStatus("current")
_Hh3cIfApplyFrClassTable_Object = MibTable
hh3cIfApplyFrClassTable = _Hh3cIfApplyFrClassTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 32, 3, 1, 1, 5)
)
if mibBuilder.loadTexts:
    hh3cIfApplyFrClassTable.setStatus("current")
_Hh3cIfApplyFrClassEntry_Object = MibTableRow
hh3cIfApplyFrClassEntry = _Hh3cIfApplyFrClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 32, 3, 1, 1, 5, 1)
)
hh3cIfApplyFrClassEntry.setIndexNames(
    (0, "HH3C-FR-QOS-MIB", "hh3cIfApplyFrClassIfIndex"),
)
if mibBuilder.loadTexts:
    hh3cIfApplyFrClassEntry.setStatus("current")
_Hh3cIfApplyFrClassIfIndex_Type = Integer32
_Hh3cIfApplyFrClassIfIndex_Object = MibTableColumn
hh3cIfApplyFrClassIfIndex = _Hh3cIfApplyFrClassIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 32, 3, 1, 1, 5, 1, 1),
    _Hh3cIfApplyFrClassIfIndex_Type()
)
hh3cIfApplyFrClassIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cIfApplyFrClassIfIndex.setStatus("current")
_Hh3cIfApplyFrClassIndex_Type = Integer32
_Hh3cIfApplyFrClassIndex_Object = MibTableColumn
hh3cIfApplyFrClassIndex = _Hh3cIfApplyFrClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 32, 3, 1, 1, 5, 1, 2),
    _Hh3cIfApplyFrClassIndex_Type()
)
hh3cIfApplyFrClassIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIfApplyFrClassIndex.setStatus("current")
_Hh3cIfApplyFrClassRowStatus_Type = RowStatus
_Hh3cIfApplyFrClassRowStatus_Object = MibTableColumn
hh3cIfApplyFrClassRowStatus = _Hh3cIfApplyFrClassRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 32, 3, 1, 1, 5, 1, 3),
    _Hh3cIfApplyFrClassRowStatus_Type()
)
hh3cIfApplyFrClassRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIfApplyFrClassRowStatus.setStatus("current")
_Hh3cPvcApplyFrClassTable_Object = MibTable
hh3cPvcApplyFrClassTable = _Hh3cPvcApplyFrClassTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 32, 3, 1, 1, 6)
)
if mibBuilder.loadTexts:
    hh3cPvcApplyFrClassTable.setStatus("current")
_Hh3cPvcApplyFrClassEntry_Object = MibTableRow
hh3cPvcApplyFrClassEntry = _Hh3cPvcApplyFrClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 32, 3, 1, 1, 6, 1)
)
hh3cPvcApplyFrClassEntry.setIndexNames(
    (0, "HH3C-FR-QOS-MIB", "hh3cPvcApplyFrClassIfIndex"),
    (0, "HH3C-FR-QOS-MIB", "hh3cPvcApplyFrClassDlciNum"),
)
if mibBuilder.loadTexts:
    hh3cPvcApplyFrClassEntry.setStatus("current")
_Hh3cPvcApplyFrClassIfIndex_Type = Integer32
_Hh3cPvcApplyFrClassIfIndex_Object = MibTableColumn
hh3cPvcApplyFrClassIfIndex = _Hh3cPvcApplyFrClassIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 32, 3, 1, 1, 6, 1, 1),
    _Hh3cPvcApplyFrClassIfIndex_Type()
)
hh3cPvcApplyFrClassIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cPvcApplyFrClassIfIndex.setStatus("current")


class _Hh3cPvcApplyFrClassDlciNum_Type(Integer32):
    """Custom type hh3cPvcApplyFrClassDlciNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1007),
    )


_Hh3cPvcApplyFrClassDlciNum_Type.__name__ = "Integer32"
_Hh3cPvcApplyFrClassDlciNum_Object = MibTableColumn
hh3cPvcApplyFrClassDlciNum = _Hh3cPvcApplyFrClassDlciNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 32, 3, 1, 1, 6, 1, 2),
    _Hh3cPvcApplyFrClassDlciNum_Type()
)
hh3cPvcApplyFrClassDlciNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cPvcApplyFrClassDlciNum.setStatus("current")
_Hh3cPvcApplyFrClassIndex_Type = Integer32
_Hh3cPvcApplyFrClassIndex_Object = MibTableColumn
hh3cPvcApplyFrClassIndex = _Hh3cPvcApplyFrClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 32, 3, 1, 1, 6, 1, 3),
    _Hh3cPvcApplyFrClassIndex_Type()
)
hh3cPvcApplyFrClassIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPvcApplyFrClassIndex.setStatus("current")
_Hh3cPvcApplyFrClassRowStatus_Type = RowStatus
_Hh3cPvcApplyFrClassRowStatus_Object = MibTableColumn
hh3cPvcApplyFrClassRowStatus = _Hh3cPvcApplyFrClassRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 32, 3, 1, 1, 6, 1, 4),
    _Hh3cPvcApplyFrClassRowStatus_Type()
)
hh3cPvcApplyFrClassRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPvcApplyFrClassRowStatus.setStatus("current")
_Hh3cFrPvcBandwidthTable_Object = MibTable
hh3cFrPvcBandwidthTable = _Hh3cFrPvcBandwidthTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 32, 3, 1, 1, 7)
)
if mibBuilder.loadTexts:
    hh3cFrPvcBandwidthTable.setStatus("current")
_Hh3cFrPvcBandwidthEntry_Object = MibTableRow
hh3cFrPvcBandwidthEntry = _Hh3cFrPvcBandwidthEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 32, 3, 1, 1, 7, 1)
)
hh3cFrPvcBandwidthEntry.setIndexNames(
    (0, "HH3C-FR-QOS-MIB", "hh3cPvcApplyFrClassIfIndex"),
    (0, "HH3C-FR-QOS-MIB", "hh3cPvcApplyFrClassDlciNum"),
)
if mibBuilder.loadTexts:
    hh3cFrPvcBandwidthEntry.setStatus("current")
_Hh3cFrPvcBandwidthMaxReservedBW_Type = Integer32
_Hh3cFrPvcBandwidthMaxReservedBW_Object = MibTableColumn
hh3cFrPvcBandwidthMaxReservedBW = _Hh3cFrPvcBandwidthMaxReservedBW_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 32, 3, 1, 1, 7, 1, 1),
    _Hh3cFrPvcBandwidthMaxReservedBW_Type()
)
hh3cFrPvcBandwidthMaxReservedBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFrPvcBandwidthMaxReservedBW.setStatus("current")
_Hh3cFrPvcBandwidthAvailable_Type = Integer32
_Hh3cFrPvcBandwidthAvailable_Object = MibTableColumn
hh3cFrPvcBandwidthAvailable = _Hh3cFrPvcBandwidthAvailable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 32, 3, 1, 1, 7, 1, 2),
    _Hh3cFrPvcBandwidthAvailable_Type()
)
hh3cFrPvcBandwidthAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFrPvcBandwidthAvailable.setStatus("current")
_Hh3cRTPQoSObjects_ObjectIdentity = ObjectIdentity
hh3cRTPQoSObjects = _Hh3cRTPQoSObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 32, 3, 1, 2)
)
_Hh3cRTPFrClassApplyTable_Object = MibTable
hh3cRTPFrClassApplyTable = _Hh3cRTPFrClassApplyTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 32, 3, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cRTPFrClassApplyTable.setStatus("current")
_Hh3cRTPFrClassApplyEntry_Object = MibTableRow
hh3cRTPFrClassApplyEntry = _Hh3cRTPFrClassApplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 32, 3, 1, 2, 1, 1)
)
hh3cRTPFrClassApplyEntry.setIndexNames(
    (0, "HH3C-FR-QOS-MIB", "hh3cRTPFrClassApplyFrClassIndex"),
)
if mibBuilder.loadTexts:
    hh3cRTPFrClassApplyEntry.setStatus("current")
_Hh3cRTPFrClassApplyFrClassIndex_Type = Integer32
_Hh3cRTPFrClassApplyFrClassIndex_Object = MibTableColumn
hh3cRTPFrClassApplyFrClassIndex = _Hh3cRTPFrClassApplyFrClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 32, 3, 1, 2, 1, 1, 1),
    _Hh3cRTPFrClassApplyFrClassIndex_Type()
)
hh3cRTPFrClassApplyFrClassIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cRTPFrClassApplyFrClassIndex.setStatus("current")


class _Hh3cRTPFrClassApplyStartPort_Type(Integer32):
    """Custom type hh3cRTPFrClassApplyStartPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2000, 65535),
    )


_Hh3cRTPFrClassApplyStartPort_Type.__name__ = "Integer32"
_Hh3cRTPFrClassApplyStartPort_Object = MibTableColumn
hh3cRTPFrClassApplyStartPort = _Hh3cRTPFrClassApplyStartPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 32, 3, 1, 2, 1, 1, 2),
    _Hh3cRTPFrClassApplyStartPort_Type()
)
hh3cRTPFrClassApplyStartPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRTPFrClassApplyStartPort.setStatus("current")


class _Hh3cRTPFrClassApplyEndPort_Type(Integer32):
    """Custom type hh3cRTPFrClassApplyEndPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2000, 65535),
    )


_Hh3cRTPFrClassApplyEndPort_Type.__name__ = "Integer32"
_Hh3cRTPFrClassApplyEndPort_Object = MibTableColumn
hh3cRTPFrClassApplyEndPort = _Hh3cRTPFrClassApplyEndPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 32, 3, 1, 2, 1, 1, 3),
    _Hh3cRTPFrClassApplyEndPort_Type()
)
hh3cRTPFrClassApplyEndPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRTPFrClassApplyEndPort.setStatus("current")


class _Hh3cRTPFrClassApplyBandWidth_Type(Integer32):
    """Custom type hh3cRTPFrClassApplyBandWidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 1000000),
    )


_Hh3cRTPFrClassApplyBandWidth_Type.__name__ = "Integer32"
_Hh3cRTPFrClassApplyBandWidth_Object = MibTableColumn
hh3cRTPFrClassApplyBandWidth = _Hh3cRTPFrClassApplyBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 32, 3, 1, 2, 1, 1, 4),
    _Hh3cRTPFrClassApplyBandWidth_Type()
)
hh3cRTPFrClassApplyBandWidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRTPFrClassApplyBandWidth.setStatus("current")


class _Hh3cRTPFrClassApplyCbs_Type(Integer32):
    """Custom type hh3cRTPFrClassApplyCbs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1500, 2000000),
    )


_Hh3cRTPFrClassApplyCbs_Type.__name__ = "Integer32"
_Hh3cRTPFrClassApplyCbs_Object = MibTableColumn
hh3cRTPFrClassApplyCbs = _Hh3cRTPFrClassApplyCbs_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 32, 3, 1, 2, 1, 1, 5),
    _Hh3cRTPFrClassApplyCbs_Type()
)
hh3cRTPFrClassApplyCbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRTPFrClassApplyCbs.setStatus("current")
_Hh3cRTPFrClassApplyRowStatus_Type = RowStatus
_Hh3cRTPFrClassApplyRowStatus_Object = MibTableColumn
hh3cRTPFrClassApplyRowStatus = _Hh3cRTPFrClassApplyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 32, 3, 1, 2, 1, 1, 6),
    _Hh3cRTPFrClassApplyRowStatus_Type()
)
hh3cRTPFrClassApplyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRTPFrClassApplyRowStatus.setStatus("current")
_Hh3cRTPFrPvcQueueRunInfoTable_Object = MibTable
hh3cRTPFrPvcQueueRunInfoTable = _Hh3cRTPFrPvcQueueRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 32, 3, 1, 2, 2)
)
if mibBuilder.loadTexts:
    hh3cRTPFrPvcQueueRunInfoTable.setStatus("current")
_Hh3cRTPFrPvcQueueRunInfoEntry_Object = MibTableRow
hh3cRTPFrPvcQueueRunInfoEntry = _Hh3cRTPFrPvcQueueRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 32, 3, 1, 2, 2, 1)
)
hh3cRTPFrPvcQueueRunInfoEntry.setIndexNames(
    (0, "HH3C-FR-QOS-MIB", "hh3cPvcApplyFrClassIfIndex"),
    (0, "HH3C-FR-QOS-MIB", "hh3cPvcApplyFrClassDlciNum"),
)
if mibBuilder.loadTexts:
    hh3cRTPFrPvcQueueRunInfoEntry.setStatus("current")
_Hh3cRTPFrPvcQueueSize_Type = Integer32
_Hh3cRTPFrPvcQueueSize_Object = MibTableColumn
hh3cRTPFrPvcQueueSize = _Hh3cRTPFrPvcQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 32, 3, 1, 2, 2, 1, 1),
    _Hh3cRTPFrPvcQueueSize_Type()
)
hh3cRTPFrPvcQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRTPFrPvcQueueSize.setStatus("current")
_Hh3cRTPFrPvcQueueMaxSize_Type = Integer32
_Hh3cRTPFrPvcQueueMaxSize_Object = MibTableColumn
hh3cRTPFrPvcQueueMaxSize = _Hh3cRTPFrPvcQueueMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 32, 3, 1, 2, 2, 1, 2),
    _Hh3cRTPFrPvcQueueMaxSize_Type()
)
hh3cRTPFrPvcQueueMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRTPFrPvcQueueMaxSize.setStatus("current")
_Hh3cRTPFrPvcQueueOutputs_Type = Counter32
_Hh3cRTPFrPvcQueueOutputs_Object = MibTableColumn
hh3cRTPFrPvcQueueOutputs = _Hh3cRTPFrPvcQueueOutputs_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 32, 3, 1, 2, 2, 1, 3),
    _Hh3cRTPFrPvcQueueOutputs_Type()
)
hh3cRTPFrPvcQueueOutputs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRTPFrPvcQueueOutputs.setStatus("current")
_Hh3cRTPFrPvcQueueDiscards_Type = Counter32
_Hh3cRTPFrPvcQueueDiscards_Object = MibTableColumn
hh3cRTPFrPvcQueueDiscards = _Hh3cRTPFrPvcQueueDiscards_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 32, 3, 1, 2, 2, 1, 4),
    _Hh3cRTPFrPvcQueueDiscards_Type()
)
hh3cRTPFrPvcQueueDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRTPFrPvcQueueDiscards.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-FR-QOS-MIB",
    **{"Hh3cCirAllowDirection": Hh3cCirAllowDirection,
       "hh3cFrQoSMib": hh3cFrQoSMib,
       "hh3cFrQoSObjects": hh3cFrQoSObjects,
       "hh3cFrClassObjects": hh3cFrClassObjects,
       "hh3cFrClassIndexNext": hh3cFrClassIndexNext,
       "hh3cFrClassCfgInfoTable": hh3cFrClassCfgInfoTable,
       "hh3cFrClassCfgInfoEntry": hh3cFrClassCfgInfoEntry,
       "hh3cFrClassIndex": hh3cFrClassIndex,
       "hh3cFrClassName": hh3cFrClassName,
       "hh3cFrClassRowStatus": hh3cFrClassRowStatus,
       "hh3cCirAllowCfgInfoTable": hh3cCirAllowCfgInfoTable,
       "hh3cCirAllowCfgInfoEntry": hh3cCirAllowCfgInfoEntry,
       "hh3cCirAllowFrClassIndex": hh3cCirAllowFrClassIndex,
       "hh3cCirAllowDirection": hh3cCirAllowDirection,
       "hh3cCirAllowValue": hh3cCirAllowValue,
       "hh3cCirAllowRowStatus": hh3cCirAllowRowStatus,
       "hh3cCirCfgInfoTable": hh3cCirCfgInfoTable,
       "hh3cCirCfgInfoEntry": hh3cCirCfgInfoEntry,
       "hh3cCirFrClassIndex": hh3cCirFrClassIndex,
       "hh3cCirValue": hh3cCirValue,
       "hh3cCirRowStatus": hh3cCirRowStatus,
       "hh3cIfApplyFrClassTable": hh3cIfApplyFrClassTable,
       "hh3cIfApplyFrClassEntry": hh3cIfApplyFrClassEntry,
       "hh3cIfApplyFrClassIfIndex": hh3cIfApplyFrClassIfIndex,
       "hh3cIfApplyFrClassIndex": hh3cIfApplyFrClassIndex,
       "hh3cIfApplyFrClassRowStatus": hh3cIfApplyFrClassRowStatus,
       "hh3cPvcApplyFrClassTable": hh3cPvcApplyFrClassTable,
       "hh3cPvcApplyFrClassEntry": hh3cPvcApplyFrClassEntry,
       "hh3cPvcApplyFrClassIfIndex": hh3cPvcApplyFrClassIfIndex,
       "hh3cPvcApplyFrClassDlciNum": hh3cPvcApplyFrClassDlciNum,
       "hh3cPvcApplyFrClassIndex": hh3cPvcApplyFrClassIndex,
       "hh3cPvcApplyFrClassRowStatus": hh3cPvcApplyFrClassRowStatus,
       "hh3cFrPvcBandwidthTable": hh3cFrPvcBandwidthTable,
       "hh3cFrPvcBandwidthEntry": hh3cFrPvcBandwidthEntry,
       "hh3cFrPvcBandwidthMaxReservedBW": hh3cFrPvcBandwidthMaxReservedBW,
       "hh3cFrPvcBandwidthAvailable": hh3cFrPvcBandwidthAvailable,
       "hh3cRTPQoSObjects": hh3cRTPQoSObjects,
       "hh3cRTPFrClassApplyTable": hh3cRTPFrClassApplyTable,
       "hh3cRTPFrClassApplyEntry": hh3cRTPFrClassApplyEntry,
       "hh3cRTPFrClassApplyFrClassIndex": hh3cRTPFrClassApplyFrClassIndex,
       "hh3cRTPFrClassApplyStartPort": hh3cRTPFrClassApplyStartPort,
       "hh3cRTPFrClassApplyEndPort": hh3cRTPFrClassApplyEndPort,
       "hh3cRTPFrClassApplyBandWidth": hh3cRTPFrClassApplyBandWidth,
       "hh3cRTPFrClassApplyCbs": hh3cRTPFrClassApplyCbs,
       "hh3cRTPFrClassApplyRowStatus": hh3cRTPFrClassApplyRowStatus,
       "hh3cRTPFrPvcQueueRunInfoTable": hh3cRTPFrPvcQueueRunInfoTable,
       "hh3cRTPFrPvcQueueRunInfoEntry": hh3cRTPFrPvcQueueRunInfoEntry,
       "hh3cRTPFrPvcQueueSize": hh3cRTPFrPvcQueueSize,
       "hh3cRTPFrPvcQueueMaxSize": hh3cRTPFrPvcQueueMaxSize,
       "hh3cRTPFrPvcQueueOutputs": hh3cRTPFrPvcQueueOutputs,
       "hh3cRTPFrPvcQueueDiscards": hh3cRTPFrPvcQueueDiscards}
)
