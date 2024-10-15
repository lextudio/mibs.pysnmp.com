# SNMP MIB module (HH3C-NS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-NS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:54:22 2024
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

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

hh3cNS = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 20)
)
hh3cNS.setRevisions(
        ("2004-09-21 14:15",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cNSMibObjects_ObjectIdentity = ObjectIdentity
hh3cNSMibObjects = _Hh3cNSMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 20, 1)
)
_Hh3cNSMibScalarObjects_ObjectIdentity = ObjectIdentity
hh3cNSMibScalarObjects = _Hh3cNSMibScalarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 20, 1, 1)
)


class _Hh3cNSActiveTime_Type(Integer32):
    """Custom type hh3cNSActiveTime based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_Hh3cNSActiveTime_Type.__name__ = "Integer32"
_Hh3cNSActiveTime_Object = MibScalar
hh3cNSActiveTime = _Hh3cNSActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 20, 1, 1, 1),
    _Hh3cNSActiveTime_Type()
)
hh3cNSActiveTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cNSActiveTime.setStatus("current")


class _Hh3cNSInactiveTime_Type(Integer32):
    """Custom type hh3cNSInactiveTime based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_Hh3cNSInactiveTime_Type.__name__ = "Integer32"
_Hh3cNSInactiveTime_Object = MibScalar
hh3cNSInactiveTime = _Hh3cNSInactiveTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 20, 1, 1, 2),
    _Hh3cNSInactiveTime_Type()
)
hh3cNSInactiveTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cNSInactiveTime.setStatus("current")


class _Hh3cNSVersion_Type(Integer32):
    """Custom type hh3cNSVersion based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 5),
        ValueRangeConstraint(9, 9),
    )


_Hh3cNSVersion_Type.__name__ = "Integer32"
_Hh3cNSVersion_Object = MibScalar
hh3cNSVersion = _Hh3cNSVersion_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 20, 1, 1, 3),
    _Hh3cNSVersion_Type()
)
hh3cNSVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cNSVersion.setStatus("current")


class _Hh3cNSAsType_Type(Integer32):
    """Custom type hh3cNSAsType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("originAs", 2),
          ("peerAs", 1))
    )


_Hh3cNSAsType_Type.__name__ = "Integer32"
_Hh3cNSAsType_Object = MibScalar
hh3cNSAsType = _Hh3cNSAsType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 20, 1, 1, 4),
    _Hh3cNSAsType_Type()
)
hh3cNSAsType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cNSAsType.setStatus("current")


class _Hh3cNSTemplateRefreshRate_Type(Integer32):
    """Custom type hh3cNSTemplateRefreshRate based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_Hh3cNSTemplateRefreshRate_Type.__name__ = "Integer32"
_Hh3cNSTemplateRefreshRate_Object = MibScalar
hh3cNSTemplateRefreshRate = _Hh3cNSTemplateRefreshRate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 20, 1, 1, 5),
    _Hh3cNSTemplateRefreshRate_Type()
)
hh3cNSTemplateRefreshRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cNSTemplateRefreshRate.setStatus("current")


class _Hh3cNSTemplateTimeout_Type(Integer32):
    """Custom type hh3cNSTemplateTimeout based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_Hh3cNSTemplateTimeout_Type.__name__ = "Integer32"
_Hh3cNSTemplateTimeout_Object = MibScalar
hh3cNSTemplateTimeout = _Hh3cNSTemplateTimeout_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 20, 1, 1, 6),
    _Hh3cNSTemplateTimeout_Type()
)
hh3cNSTemplateTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cNSTemplateTimeout.setStatus("current")


class _Hh3cNSExportVlanOrIfIndex_Type(Integer32):
    """Custom type hh3cNSExportVlanOrIfIndex based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("interfaceIndex", 2),
          ("vlanId", 1))
    )


_Hh3cNSExportVlanOrIfIndex_Type.__name__ = "Integer32"
_Hh3cNSExportVlanOrIfIndex_Object = MibScalar
hh3cNSExportVlanOrIfIndex = _Hh3cNSExportVlanOrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 20, 1, 1, 7),
    _Hh3cNSExportVlanOrIfIndex_Type()
)
hh3cNSExportVlanOrIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNSExportVlanOrIfIndex.setStatus("current")
_Hh3cNSProcessSlotTable_Object = MibTable
hh3cNSProcessSlotTable = _Hh3cNSProcessSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 20, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cNSProcessSlotTable.setStatus("current")
_Hh3cNSProcessSlotEntry_Object = MibTableRow
hh3cNSProcessSlotEntry = _Hh3cNSProcessSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 20, 1, 2, 1)
)
hh3cNSProcessSlotEntry.setIndexNames(
    (0, "HH3C-NS-MIB", "hh3cNSProcessSlot"),
)
if mibBuilder.loadTexts:
    hh3cNSProcessSlotEntry.setStatus("current")
_Hh3cNSProcessSlot_Type = Integer32
_Hh3cNSProcessSlot_Object = MibTableColumn
hh3cNSProcessSlot = _Hh3cNSProcessSlot_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 20, 1, 2, 1, 1),
    _Hh3cNSProcessSlot_Type()
)
hh3cNSProcessSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNSProcessSlot.setStatus("current")
_Hh3cNSExportConfigTable_Object = MibTable
hh3cNSExportConfigTable = _Hh3cNSExportConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 20, 1, 3)
)
if mibBuilder.loadTexts:
    hh3cNSExportConfigTable.setStatus("current")
_Hh3cNSExportConfigEntry_Object = MibTableRow
hh3cNSExportConfigEntry = _Hh3cNSExportConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 20, 1, 3, 1)
)
hh3cNSExportConfigEntry.setIndexNames(
    (0, "HH3C-NS-MIB", "hh3cNSAggregationType"),
)
if mibBuilder.loadTexts:
    hh3cNSExportConfigEntry.setStatus("current")


class _Hh3cNSAggregationType_Type(Integer32):
    """Custom type hh3cNSAggregationType based on Integer32"""
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
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("as", 2),
          ("destinationPrefix", 3),
          ("prefix", 6),
          ("prefixPort", 12),
          ("protocolPort", 5),
          ("sourcePrefix", 4),
          ("tosAs", 7),
          ("tosDestinationPrefix", 8),
          ("tosPrefix", 11),
          ("tosProtocolPort", 10),
          ("tosSourcePrefix", 9),
          ("v5Statistics", 1))
    )


_Hh3cNSAggregationType_Type.__name__ = "Integer32"
_Hh3cNSAggregationType_Object = MibTableColumn
hh3cNSAggregationType = _Hh3cNSAggregationType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 20, 1, 3, 1, 1),
    _Hh3cNSAggregationType_Type()
)
hh3cNSAggregationType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cNSAggregationType.setStatus("current")
_Hh3cNSHostIPAddr_Type = IpAddress
_Hh3cNSHostIPAddr_Object = MibTableColumn
hh3cNSHostIPAddr = _Hh3cNSHostIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 20, 1, 3, 1, 2),
    _Hh3cNSHostIPAddr_Type()
)
hh3cNSHostIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cNSHostIPAddr.setStatus("current")


class _Hh3cNSHostPort_Type(Integer32):
    """Custom type hh3cNSHostPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cNSHostPort_Type.__name__ = "Integer32"
_Hh3cNSHostPort_Object = MibTableColumn
hh3cNSHostPort = _Hh3cNSHostPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 20, 1, 3, 1, 3),
    _Hh3cNSHostPort_Type()
)
hh3cNSHostPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cNSHostPort.setStatus("current")
_Hh3cNSSrcIpAddr_Type = IpAddress
_Hh3cNSSrcIpAddr_Object = MibTableColumn
hh3cNSSrcIpAddr = _Hh3cNSSrcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 20, 1, 3, 1, 4),
    _Hh3cNSSrcIpAddr_Type()
)
hh3cNSSrcIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cNSSrcIpAddr.setStatus("current")


class _Hh3cNSState_Type(Integer32):
    """Custom type hh3cNSState based on Integer32"""
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


_Hh3cNSState_Type.__name__ = "Integer32"
_Hh3cNSState_Object = MibTableColumn
hh3cNSState = _Hh3cNSState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 20, 1, 3, 1, 5),
    _Hh3cNSState_Type()
)
hh3cNSState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cNSState.setStatus("current")
_Hh3cNSExportInformationTable_Object = MibTable
hh3cNSExportInformationTable = _Hh3cNSExportInformationTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 20, 1, 4)
)
if mibBuilder.loadTexts:
    hh3cNSExportInformationTable.setStatus("current")
_Hh3cNSExportInformationEntry_Object = MibTableRow
hh3cNSExportInformationEntry = _Hh3cNSExportInformationEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 20, 1, 4, 1)
)
hh3cNSExportInformationEntry.setIndexNames(
    (0, "HH3C-NS-MIB", "hh3cNSExportType"),
    (0, "HH3C-NS-MIB", "hh3cNSExportSlot"),
)
if mibBuilder.loadTexts:
    hh3cNSExportInformationEntry.setStatus("current")


class _Hh3cNSExportType_Type(Integer32):
    """Custom type hh3cNSExportType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_Hh3cNSExportType_Type.__name__ = "Integer32"
_Hh3cNSExportType_Object = MibTableColumn
hh3cNSExportType = _Hh3cNSExportType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 20, 1, 4, 1, 1),
    _Hh3cNSExportType_Type()
)
hh3cNSExportType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cNSExportType.setStatus("current")
_Hh3cNSExportSlot_Type = Integer32
_Hh3cNSExportSlot_Object = MibTableColumn
hh3cNSExportSlot = _Hh3cNSExportSlot_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 20, 1, 4, 1, 2),
    _Hh3cNSExportSlot_Type()
)
hh3cNSExportSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cNSExportSlot.setStatus("current")
_Hh3cNSExportStream_Type = Counter32
_Hh3cNSExportStream_Object = MibTableColumn
hh3cNSExportStream = _Hh3cNSExportStream_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 20, 1, 4, 1, 3),
    _Hh3cNSExportStream_Type()
)
hh3cNSExportStream.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNSExportStream.setStatus("current")
_Hh3cNSExportNum_Type = Counter32
_Hh3cNSExportNum_Object = MibTableColumn
hh3cNSExportNum = _Hh3cNSExportNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 20, 1, 4, 1, 4),
    _Hh3cNSExportNum_Type()
)
hh3cNSExportNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNSExportNum.setStatus("current")
_Hh3cNSExportFail_Type = Counter32
_Hh3cNSExportFail_Object = MibTableColumn
hh3cNSExportFail = _Hh3cNSExportFail_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 20, 1, 4, 1, 5),
    _Hh3cNSExportFail_Type()
)
hh3cNSExportFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNSExportFail.setStatus("current")
_Hh3cNSConfigTable_Object = MibTable
hh3cNSConfigTable = _Hh3cNSConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 20, 1, 5)
)
if mibBuilder.loadTexts:
    hh3cNSConfigTable.setStatus("current")
_Hh3cNSConfigEntry_Object = MibTableRow
hh3cNSConfigEntry = _Hh3cNSConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 20, 1, 5, 1)
)
hh3cNSConfigEntry.setIndexNames(
    (0, "HH3C-NS-MIB", "hh3cNSSourceSlot"),
    (0, "HH3C-NS-MIB", "hh3cNSSourceIfIndex"),
    (0, "HH3C-NS-MIB", "hh3cNSDestSlot"),
)
if mibBuilder.loadTexts:
    hh3cNSConfigEntry.setStatus("current")


class _Hh3cNSSourceSlot_Type(Integer32):
    """Custom type hh3cNSSourceSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cNSSourceSlot_Type.__name__ = "Integer32"
_Hh3cNSSourceSlot_Object = MibTableColumn
hh3cNSSourceSlot = _Hh3cNSSourceSlot_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 20, 1, 5, 1, 1),
    _Hh3cNSSourceSlot_Type()
)
hh3cNSSourceSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cNSSourceSlot.setStatus("current")
_Hh3cNSSourceIfIndex_Type = Integer32
_Hh3cNSSourceIfIndex_Object = MibTableColumn
hh3cNSSourceIfIndex = _Hh3cNSSourceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 20, 1, 5, 1, 2),
    _Hh3cNSSourceIfIndex_Type()
)
hh3cNSSourceIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cNSSourceIfIndex.setStatus("current")
_Hh3cNSDestSlot_Type = Integer32
_Hh3cNSDestSlot_Object = MibTableColumn
hh3cNSDestSlot = _Hh3cNSDestSlot_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 20, 1, 5, 1, 3),
    _Hh3cNSDestSlot_Type()
)
hh3cNSDestSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cNSDestSlot.setStatus("current")


class _Hh3cNSDirect_Type(Integer32):
    """Custom type hh3cNSDirect based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 1),
          ("outbound", 2))
    )


_Hh3cNSDirect_Type.__name__ = "Integer32"
_Hh3cNSDirect_Object = MibTableColumn
hh3cNSDirect = _Hh3cNSDirect_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 20, 1, 5, 1, 4),
    _Hh3cNSDirect_Type()
)
hh3cNSDirect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cNSDirect.setStatus("current")


class _Hh3cNSACLNumber_Type(Integer32):
    """Custom type hh3cNSACLNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2000, 3999),
    )


_Hh3cNSACLNumber_Type.__name__ = "Integer32"
_Hh3cNSACLNumber_Object = MibTableColumn
hh3cNSACLNumber = _Hh3cNSACLNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 20, 1, 5, 1, 5),
    _Hh3cNSACLNumber_Type()
)
hh3cNSACLNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cNSACLNumber.setStatus("current")
_Hh3cNSACLName_Type = OctetString
_Hh3cNSACLName_Object = MibTableColumn
hh3cNSACLName = _Hh3cNSACLName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 20, 1, 5, 1, 6),
    _Hh3cNSACLName_Type()
)
hh3cNSACLName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cNSACLName.setStatus("current")
_Hh3cNSACLRule_Type = Integer32
_Hh3cNSACLRule_Object = MibTableColumn
hh3cNSACLRule = _Hh3cNSACLRule_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 20, 1, 5, 1, 7),
    _Hh3cNSACLRule_Type()
)
hh3cNSACLRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cNSACLRule.setStatus("current")
_Hh3cNSConfigRowStatus_Type = RowStatus
_Hh3cNSConfigRowStatus_Object = MibTableColumn
hh3cNSConfigRowStatus = _Hh3cNSConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 20, 1, 5, 1, 8),
    _Hh3cNSConfigRowStatus_Type()
)
hh3cNSConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cNSConfigRowStatus.setStatus("current")
_Hh3cNSStatusTable_Object = MibTable
hh3cNSStatusTable = _Hh3cNSStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 20, 1, 6)
)
if mibBuilder.loadTexts:
    hh3cNSStatusTable.setStatus("current")
_Hh3cNSStatusEntry_Object = MibTableRow
hh3cNSStatusEntry = _Hh3cNSStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 20, 1, 6, 1)
)
hh3cNSStatusEntry.setIndexNames(
    (0, "HH3C-NS-MIB", "hh3cNSSlot"),
)
if mibBuilder.loadTexts:
    hh3cNSStatusEntry.setStatus("current")
_Hh3cNSSlot_Type = Integer32
_Hh3cNSSlot_Object = MibTableColumn
hh3cNSSlot = _Hh3cNSSlot_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 20, 1, 6, 1, 1),
    _Hh3cNSSlot_Type()
)
hh3cNSSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cNSSlot.setStatus("current")
_Hh3cNSActiveStreamNumber_Type = Counter32
_Hh3cNSActiveStreamNumber_Object = MibTableColumn
hh3cNSActiveStreamNumber = _Hh3cNSActiveStreamNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 20, 1, 6, 1, 2),
    _Hh3cNSActiveStreamNumber_Type()
)
hh3cNSActiveStreamNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNSActiveStreamNumber.setStatus("current")
_Hh3cNSTotalStreamNumber_Type = Counter32
_Hh3cNSTotalStreamNumber_Object = MibTableColumn
hh3cNSTotalStreamNumber = _Hh3cNSTotalStreamNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 20, 1, 6, 1, 3),
    _Hh3cNSTotalStreamNumber_Type()
)
hh3cNSTotalStreamNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNSTotalStreamNumber.setStatus("current")
_Hh3cNSTotalPacketNumber_Type = Counter32
_Hh3cNSTotalPacketNumber_Object = MibTableColumn
hh3cNSTotalPacketNumber = _Hh3cNSTotalPacketNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 20, 1, 6, 1, 4),
    _Hh3cNSTotalPacketNumber_Type()
)
hh3cNSTotalPacketNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNSTotalPacketNumber.setStatus("current")
_Hh3cNSTotalOctetNumber_Type = Counter32
_Hh3cNSTotalOctetNumber_Object = MibTableColumn
hh3cNSTotalOctetNumber = _Hh3cNSTotalOctetNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 20, 1, 6, 1, 5),
    _Hh3cNSTotalOctetNumber_Type()
)
hh3cNSTotalOctetNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNSTotalOctetNumber.setStatus("current")
_Hh3cNSMPLSActiveStreamNumber_Type = Counter32
_Hh3cNSMPLSActiveStreamNumber_Object = MibTableColumn
hh3cNSMPLSActiveStreamNumber = _Hh3cNSMPLSActiveStreamNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 20, 1, 6, 1, 6),
    _Hh3cNSMPLSActiveStreamNumber_Type()
)
hh3cNSMPLSActiveStreamNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNSMPLSActiveStreamNumber.setStatus("current")
_Hh3cNSMPLSTotalStreamNumber_Type = Counter32
_Hh3cNSMPLSTotalStreamNumber_Object = MibTableColumn
hh3cNSMPLSTotalStreamNumber = _Hh3cNSMPLSTotalStreamNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 20, 1, 6, 1, 7),
    _Hh3cNSMPLSTotalStreamNumber_Type()
)
hh3cNSMPLSTotalStreamNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNSMPLSTotalStreamNumber.setStatus("current")
_Hh3cNSMPLSTotalPacketNumber_Type = Counter32
_Hh3cNSMPLSTotalPacketNumber_Object = MibTableColumn
hh3cNSMPLSTotalPacketNumber = _Hh3cNSMPLSTotalPacketNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 20, 1, 6, 1, 8),
    _Hh3cNSMPLSTotalPacketNumber_Type()
)
hh3cNSMPLSTotalPacketNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNSMPLSTotalPacketNumber.setStatus("current")
_Hh3cNSMPLSTotalOctetNumber_Type = Counter32
_Hh3cNSMPLSTotalOctetNumber_Object = MibTableColumn
hh3cNSMPLSTotalOctetNumber = _Hh3cNSMPLSTotalOctetNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 20, 1, 6, 1, 9),
    _Hh3cNSMPLSTotalOctetNumber_Type()
)
hh3cNSMPLSTotalOctetNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNSMPLSTotalOctetNumber.setStatus("current")


class _Hh3cNSResetFlag_Type(Integer32):
    """Custom type hh3cNSResetFlag based on Integer32"""

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


_Hh3cNSResetFlag_Type.__name__ = "Integer32"
_Hh3cNSResetFlag_Object = MibTableColumn
hh3cNSResetFlag = _Hh3cNSResetFlag_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 20, 1, 6, 1, 10),
    _Hh3cNSResetFlag_Type()
)
hh3cNSResetFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cNSResetFlag.setStatus("current")
_Hh3cNSResetTime_Type = TimeTicks
_Hh3cNSResetTime_Object = MibTableColumn
hh3cNSResetTime = _Hh3cNSResetTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 20, 1, 6, 1, 11),
    _Hh3cNSResetTime_Type()
)
hh3cNSResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNSResetTime.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-NS-MIB",
    **{"hh3cNS": hh3cNS,
       "hh3cNSMibObjects": hh3cNSMibObjects,
       "hh3cNSMibScalarObjects": hh3cNSMibScalarObjects,
       "hh3cNSActiveTime": hh3cNSActiveTime,
       "hh3cNSInactiveTime": hh3cNSInactiveTime,
       "hh3cNSVersion": hh3cNSVersion,
       "hh3cNSAsType": hh3cNSAsType,
       "hh3cNSTemplateRefreshRate": hh3cNSTemplateRefreshRate,
       "hh3cNSTemplateTimeout": hh3cNSTemplateTimeout,
       "hh3cNSExportVlanOrIfIndex": hh3cNSExportVlanOrIfIndex,
       "hh3cNSProcessSlotTable": hh3cNSProcessSlotTable,
       "hh3cNSProcessSlotEntry": hh3cNSProcessSlotEntry,
       "hh3cNSProcessSlot": hh3cNSProcessSlot,
       "hh3cNSExportConfigTable": hh3cNSExportConfigTable,
       "hh3cNSExportConfigEntry": hh3cNSExportConfigEntry,
       "hh3cNSAggregationType": hh3cNSAggregationType,
       "hh3cNSHostIPAddr": hh3cNSHostIPAddr,
       "hh3cNSHostPort": hh3cNSHostPort,
       "hh3cNSSrcIpAddr": hh3cNSSrcIpAddr,
       "hh3cNSState": hh3cNSState,
       "hh3cNSExportInformationTable": hh3cNSExportInformationTable,
       "hh3cNSExportInformationEntry": hh3cNSExportInformationEntry,
       "hh3cNSExportType": hh3cNSExportType,
       "hh3cNSExportSlot": hh3cNSExportSlot,
       "hh3cNSExportStream": hh3cNSExportStream,
       "hh3cNSExportNum": hh3cNSExportNum,
       "hh3cNSExportFail": hh3cNSExportFail,
       "hh3cNSConfigTable": hh3cNSConfigTable,
       "hh3cNSConfigEntry": hh3cNSConfigEntry,
       "hh3cNSSourceSlot": hh3cNSSourceSlot,
       "hh3cNSSourceIfIndex": hh3cNSSourceIfIndex,
       "hh3cNSDestSlot": hh3cNSDestSlot,
       "hh3cNSDirect": hh3cNSDirect,
       "hh3cNSACLNumber": hh3cNSACLNumber,
       "hh3cNSACLName": hh3cNSACLName,
       "hh3cNSACLRule": hh3cNSACLRule,
       "hh3cNSConfigRowStatus": hh3cNSConfigRowStatus,
       "hh3cNSStatusTable": hh3cNSStatusTable,
       "hh3cNSStatusEntry": hh3cNSStatusEntry,
       "hh3cNSSlot": hh3cNSSlot,
       "hh3cNSActiveStreamNumber": hh3cNSActiveStreamNumber,
       "hh3cNSTotalStreamNumber": hh3cNSTotalStreamNumber,
       "hh3cNSTotalPacketNumber": hh3cNSTotalPacketNumber,
       "hh3cNSTotalOctetNumber": hh3cNSTotalOctetNumber,
       "hh3cNSMPLSActiveStreamNumber": hh3cNSMPLSActiveStreamNumber,
       "hh3cNSMPLSTotalStreamNumber": hh3cNSMPLSTotalStreamNumber,
       "hh3cNSMPLSTotalPacketNumber": hh3cNSMPLSTotalPacketNumber,
       "hh3cNSMPLSTotalOctetNumber": hh3cNSMPLSTotalOctetNumber,
       "hh3cNSResetFlag": hh3cNSResetFlag,
       "hh3cNSResetTime": hh3cNSResetTime}
)
