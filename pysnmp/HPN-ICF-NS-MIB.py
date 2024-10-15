# SNMP MIB module (HPN-ICF-NS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-NS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:01:21 2024
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

(hpnicfCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfCommon")

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

hpnicfNS = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20)
)
hpnicfNS.setRevisions(
        ("2004-09-21 14:15",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfNSMibObjects_ObjectIdentity = ObjectIdentity
hpnicfNSMibObjects = _HpnicfNSMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1)
)
_HpnicfNSMibScalarObjects_ObjectIdentity = ObjectIdentity
hpnicfNSMibScalarObjects = _HpnicfNSMibScalarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 1)
)


class _HpnicfNSActiveTime_Type(Integer32):
    """Custom type hpnicfNSActiveTime based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_HpnicfNSActiveTime_Type.__name__ = "Integer32"
_HpnicfNSActiveTime_Object = MibScalar
hpnicfNSActiveTime = _HpnicfNSActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 1, 1),
    _HpnicfNSActiveTime_Type()
)
hpnicfNSActiveTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfNSActiveTime.setStatus("current")


class _HpnicfNSInactiveTime_Type(Integer32):
    """Custom type hpnicfNSInactiveTime based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_HpnicfNSInactiveTime_Type.__name__ = "Integer32"
_HpnicfNSInactiveTime_Object = MibScalar
hpnicfNSInactiveTime = _HpnicfNSInactiveTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 1, 2),
    _HpnicfNSInactiveTime_Type()
)
hpnicfNSInactiveTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfNSInactiveTime.setStatus("current")


class _HpnicfNSVersion_Type(Integer32):
    """Custom type hpnicfNSVersion based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 5),
        ValueRangeConstraint(9, 9),
    )


_HpnicfNSVersion_Type.__name__ = "Integer32"
_HpnicfNSVersion_Object = MibScalar
hpnicfNSVersion = _HpnicfNSVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 1, 3),
    _HpnicfNSVersion_Type()
)
hpnicfNSVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfNSVersion.setStatus("current")


class _HpnicfNSAsType_Type(Integer32):
    """Custom type hpnicfNSAsType based on Integer32"""
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


_HpnicfNSAsType_Type.__name__ = "Integer32"
_HpnicfNSAsType_Object = MibScalar
hpnicfNSAsType = _HpnicfNSAsType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 1, 4),
    _HpnicfNSAsType_Type()
)
hpnicfNSAsType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfNSAsType.setStatus("current")


class _HpnicfNSTemplateRefreshRate_Type(Integer32):
    """Custom type hpnicfNSTemplateRefreshRate based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_HpnicfNSTemplateRefreshRate_Type.__name__ = "Integer32"
_HpnicfNSTemplateRefreshRate_Object = MibScalar
hpnicfNSTemplateRefreshRate = _HpnicfNSTemplateRefreshRate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 1, 5),
    _HpnicfNSTemplateRefreshRate_Type()
)
hpnicfNSTemplateRefreshRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfNSTemplateRefreshRate.setStatus("current")


class _HpnicfNSTemplateTimeout_Type(Integer32):
    """Custom type hpnicfNSTemplateTimeout based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_HpnicfNSTemplateTimeout_Type.__name__ = "Integer32"
_HpnicfNSTemplateTimeout_Object = MibScalar
hpnicfNSTemplateTimeout = _HpnicfNSTemplateTimeout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 1, 6),
    _HpnicfNSTemplateTimeout_Type()
)
hpnicfNSTemplateTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfNSTemplateTimeout.setStatus("current")


class _HpnicfNSExportVlanOrIfIndex_Type(Integer32):
    """Custom type hpnicfNSExportVlanOrIfIndex based on Integer32"""
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


_HpnicfNSExportVlanOrIfIndex_Type.__name__ = "Integer32"
_HpnicfNSExportVlanOrIfIndex_Object = MibScalar
hpnicfNSExportVlanOrIfIndex = _HpnicfNSExportVlanOrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 1, 7),
    _HpnicfNSExportVlanOrIfIndex_Type()
)
hpnicfNSExportVlanOrIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNSExportVlanOrIfIndex.setStatus("current")
_HpnicfNSProcessSlotTable_Object = MibTable
hpnicfNSProcessSlotTable = _HpnicfNSProcessSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 2)
)
if mibBuilder.loadTexts:
    hpnicfNSProcessSlotTable.setStatus("current")
_HpnicfNSProcessSlotEntry_Object = MibTableRow
hpnicfNSProcessSlotEntry = _HpnicfNSProcessSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 2, 1)
)
hpnicfNSProcessSlotEntry.setIndexNames(
    (0, "HPN-ICF-NS-MIB", "hpnicfNSProcessSlot"),
)
if mibBuilder.loadTexts:
    hpnicfNSProcessSlotEntry.setStatus("current")
_HpnicfNSProcessSlot_Type = Integer32
_HpnicfNSProcessSlot_Object = MibTableColumn
hpnicfNSProcessSlot = _HpnicfNSProcessSlot_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 2, 1, 1),
    _HpnicfNSProcessSlot_Type()
)
hpnicfNSProcessSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNSProcessSlot.setStatus("current")
_HpnicfNSExportConfigTable_Object = MibTable
hpnicfNSExportConfigTable = _HpnicfNSExportConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 3)
)
if mibBuilder.loadTexts:
    hpnicfNSExportConfigTable.setStatus("current")
_HpnicfNSExportConfigEntry_Object = MibTableRow
hpnicfNSExportConfigEntry = _HpnicfNSExportConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 3, 1)
)
hpnicfNSExportConfigEntry.setIndexNames(
    (0, "HPN-ICF-NS-MIB", "hpnicfNSAggregationType"),
)
if mibBuilder.loadTexts:
    hpnicfNSExportConfigEntry.setStatus("current")


class _HpnicfNSAggregationType_Type(Integer32):
    """Custom type hpnicfNSAggregationType based on Integer32"""
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


_HpnicfNSAggregationType_Type.__name__ = "Integer32"
_HpnicfNSAggregationType_Object = MibTableColumn
hpnicfNSAggregationType = _HpnicfNSAggregationType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 3, 1, 1),
    _HpnicfNSAggregationType_Type()
)
hpnicfNSAggregationType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfNSAggregationType.setStatus("current")
_HpnicfNSHostIPAddr_Type = IpAddress
_HpnicfNSHostIPAddr_Object = MibTableColumn
hpnicfNSHostIPAddr = _HpnicfNSHostIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 3, 1, 2),
    _HpnicfNSHostIPAddr_Type()
)
hpnicfNSHostIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfNSHostIPAddr.setStatus("current")


class _HpnicfNSHostPort_Type(Integer32):
    """Custom type hpnicfNSHostPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfNSHostPort_Type.__name__ = "Integer32"
_HpnicfNSHostPort_Object = MibTableColumn
hpnicfNSHostPort = _HpnicfNSHostPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 3, 1, 3),
    _HpnicfNSHostPort_Type()
)
hpnicfNSHostPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfNSHostPort.setStatus("current")
_HpnicfNSSrcIpAddr_Type = IpAddress
_HpnicfNSSrcIpAddr_Object = MibTableColumn
hpnicfNSSrcIpAddr = _HpnicfNSSrcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 3, 1, 4),
    _HpnicfNSSrcIpAddr_Type()
)
hpnicfNSSrcIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfNSSrcIpAddr.setStatus("current")


class _HpnicfNSState_Type(Integer32):
    """Custom type hpnicfNSState based on Integer32"""
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


_HpnicfNSState_Type.__name__ = "Integer32"
_HpnicfNSState_Object = MibTableColumn
hpnicfNSState = _HpnicfNSState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 3, 1, 5),
    _HpnicfNSState_Type()
)
hpnicfNSState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfNSState.setStatus("current")
_HpnicfNSExportInformationTable_Object = MibTable
hpnicfNSExportInformationTable = _HpnicfNSExportInformationTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 4)
)
if mibBuilder.loadTexts:
    hpnicfNSExportInformationTable.setStatus("current")
_HpnicfNSExportInformationEntry_Object = MibTableRow
hpnicfNSExportInformationEntry = _HpnicfNSExportInformationEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 4, 1)
)
hpnicfNSExportInformationEntry.setIndexNames(
    (0, "HPN-ICF-NS-MIB", "hpnicfNSExportType"),
    (0, "HPN-ICF-NS-MIB", "hpnicfNSExportSlot"),
)
if mibBuilder.loadTexts:
    hpnicfNSExportInformationEntry.setStatus("current")


class _HpnicfNSExportType_Type(Integer32):
    """Custom type hpnicfNSExportType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_HpnicfNSExportType_Type.__name__ = "Integer32"
_HpnicfNSExportType_Object = MibTableColumn
hpnicfNSExportType = _HpnicfNSExportType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 4, 1, 1),
    _HpnicfNSExportType_Type()
)
hpnicfNSExportType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfNSExportType.setStatus("current")
_HpnicfNSExportSlot_Type = Integer32
_HpnicfNSExportSlot_Object = MibTableColumn
hpnicfNSExportSlot = _HpnicfNSExportSlot_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 4, 1, 2),
    _HpnicfNSExportSlot_Type()
)
hpnicfNSExportSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfNSExportSlot.setStatus("current")
_HpnicfNSExportStream_Type = Counter32
_HpnicfNSExportStream_Object = MibTableColumn
hpnicfNSExportStream = _HpnicfNSExportStream_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 4, 1, 3),
    _HpnicfNSExportStream_Type()
)
hpnicfNSExportStream.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNSExportStream.setStatus("current")
_HpnicfNSExportNum_Type = Counter32
_HpnicfNSExportNum_Object = MibTableColumn
hpnicfNSExportNum = _HpnicfNSExportNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 4, 1, 4),
    _HpnicfNSExportNum_Type()
)
hpnicfNSExportNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNSExportNum.setStatus("current")
_HpnicfNSExportFail_Type = Counter32
_HpnicfNSExportFail_Object = MibTableColumn
hpnicfNSExportFail = _HpnicfNSExportFail_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 4, 1, 5),
    _HpnicfNSExportFail_Type()
)
hpnicfNSExportFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNSExportFail.setStatus("current")
_HpnicfNSConfigTable_Object = MibTable
hpnicfNSConfigTable = _HpnicfNSConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 5)
)
if mibBuilder.loadTexts:
    hpnicfNSConfigTable.setStatus("current")
_HpnicfNSConfigEntry_Object = MibTableRow
hpnicfNSConfigEntry = _HpnicfNSConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 5, 1)
)
hpnicfNSConfigEntry.setIndexNames(
    (0, "HPN-ICF-NS-MIB", "hpnicfNSSourceSlot"),
    (0, "HPN-ICF-NS-MIB", "hpnicfNSSourceIfIndex"),
    (0, "HPN-ICF-NS-MIB", "hpnicfNSDestSlot"),
)
if mibBuilder.loadTexts:
    hpnicfNSConfigEntry.setStatus("current")


class _HpnicfNSSourceSlot_Type(Integer32):
    """Custom type hpnicfNSSourceSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpnicfNSSourceSlot_Type.__name__ = "Integer32"
_HpnicfNSSourceSlot_Object = MibTableColumn
hpnicfNSSourceSlot = _HpnicfNSSourceSlot_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 5, 1, 1),
    _HpnicfNSSourceSlot_Type()
)
hpnicfNSSourceSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfNSSourceSlot.setStatus("current")
_HpnicfNSSourceIfIndex_Type = Integer32
_HpnicfNSSourceIfIndex_Object = MibTableColumn
hpnicfNSSourceIfIndex = _HpnicfNSSourceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 5, 1, 2),
    _HpnicfNSSourceIfIndex_Type()
)
hpnicfNSSourceIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfNSSourceIfIndex.setStatus("current")
_HpnicfNSDestSlot_Type = Integer32
_HpnicfNSDestSlot_Object = MibTableColumn
hpnicfNSDestSlot = _HpnicfNSDestSlot_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 5, 1, 3),
    _HpnicfNSDestSlot_Type()
)
hpnicfNSDestSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfNSDestSlot.setStatus("current")


class _HpnicfNSDirect_Type(Integer32):
    """Custom type hpnicfNSDirect based on Integer32"""
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


_HpnicfNSDirect_Type.__name__ = "Integer32"
_HpnicfNSDirect_Object = MibTableColumn
hpnicfNSDirect = _HpnicfNSDirect_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 5, 1, 4),
    _HpnicfNSDirect_Type()
)
hpnicfNSDirect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfNSDirect.setStatus("current")


class _HpnicfNSACLNumber_Type(Integer32):
    """Custom type hpnicfNSACLNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2000, 3999),
    )


_HpnicfNSACLNumber_Type.__name__ = "Integer32"
_HpnicfNSACLNumber_Object = MibTableColumn
hpnicfNSACLNumber = _HpnicfNSACLNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 5, 1, 5),
    _HpnicfNSACLNumber_Type()
)
hpnicfNSACLNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfNSACLNumber.setStatus("current")
_HpnicfNSACLName_Type = OctetString
_HpnicfNSACLName_Object = MibTableColumn
hpnicfNSACLName = _HpnicfNSACLName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 5, 1, 6),
    _HpnicfNSACLName_Type()
)
hpnicfNSACLName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfNSACLName.setStatus("current")
_HpnicfNSACLRule_Type = Integer32
_HpnicfNSACLRule_Object = MibTableColumn
hpnicfNSACLRule = _HpnicfNSACLRule_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 5, 1, 7),
    _HpnicfNSACLRule_Type()
)
hpnicfNSACLRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfNSACLRule.setStatus("current")
_HpnicfNSConfigRowStatus_Type = RowStatus
_HpnicfNSConfigRowStatus_Object = MibTableColumn
hpnicfNSConfigRowStatus = _HpnicfNSConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 5, 1, 8),
    _HpnicfNSConfigRowStatus_Type()
)
hpnicfNSConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfNSConfigRowStatus.setStatus("current")
_HpnicfNSStatusTable_Object = MibTable
hpnicfNSStatusTable = _HpnicfNSStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 6)
)
if mibBuilder.loadTexts:
    hpnicfNSStatusTable.setStatus("current")
_HpnicfNSStatusEntry_Object = MibTableRow
hpnicfNSStatusEntry = _HpnicfNSStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 6, 1)
)
hpnicfNSStatusEntry.setIndexNames(
    (0, "HPN-ICF-NS-MIB", "hpnicfNSSlot"),
)
if mibBuilder.loadTexts:
    hpnicfNSStatusEntry.setStatus("current")
_HpnicfNSSlot_Type = Integer32
_HpnicfNSSlot_Object = MibTableColumn
hpnicfNSSlot = _HpnicfNSSlot_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 6, 1, 1),
    _HpnicfNSSlot_Type()
)
hpnicfNSSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfNSSlot.setStatus("current")
_HpnicfNSActiveStreamNumber_Type = Counter32
_HpnicfNSActiveStreamNumber_Object = MibTableColumn
hpnicfNSActiveStreamNumber = _HpnicfNSActiveStreamNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 6, 1, 2),
    _HpnicfNSActiveStreamNumber_Type()
)
hpnicfNSActiveStreamNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNSActiveStreamNumber.setStatus("current")
_HpnicfNSTotalStreamNumber_Type = Counter32
_HpnicfNSTotalStreamNumber_Object = MibTableColumn
hpnicfNSTotalStreamNumber = _HpnicfNSTotalStreamNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 6, 1, 3),
    _HpnicfNSTotalStreamNumber_Type()
)
hpnicfNSTotalStreamNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNSTotalStreamNumber.setStatus("current")
_HpnicfNSTotalPacketNumber_Type = Counter32
_HpnicfNSTotalPacketNumber_Object = MibTableColumn
hpnicfNSTotalPacketNumber = _HpnicfNSTotalPacketNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 6, 1, 4),
    _HpnicfNSTotalPacketNumber_Type()
)
hpnicfNSTotalPacketNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNSTotalPacketNumber.setStatus("current")
_HpnicfNSTotalOctetNumber_Type = Counter32
_HpnicfNSTotalOctetNumber_Object = MibTableColumn
hpnicfNSTotalOctetNumber = _HpnicfNSTotalOctetNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 6, 1, 5),
    _HpnicfNSTotalOctetNumber_Type()
)
hpnicfNSTotalOctetNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNSTotalOctetNumber.setStatus("current")
_HpnicfNSMPLSActiveStreamNumber_Type = Counter32
_HpnicfNSMPLSActiveStreamNumber_Object = MibTableColumn
hpnicfNSMPLSActiveStreamNumber = _HpnicfNSMPLSActiveStreamNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 6, 1, 6),
    _HpnicfNSMPLSActiveStreamNumber_Type()
)
hpnicfNSMPLSActiveStreamNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNSMPLSActiveStreamNumber.setStatus("current")
_HpnicfNSMPLSTotalStreamNumber_Type = Counter32
_HpnicfNSMPLSTotalStreamNumber_Object = MibTableColumn
hpnicfNSMPLSTotalStreamNumber = _HpnicfNSMPLSTotalStreamNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 6, 1, 7),
    _HpnicfNSMPLSTotalStreamNumber_Type()
)
hpnicfNSMPLSTotalStreamNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNSMPLSTotalStreamNumber.setStatus("current")
_HpnicfNSMPLSTotalPacketNumber_Type = Counter32
_HpnicfNSMPLSTotalPacketNumber_Object = MibTableColumn
hpnicfNSMPLSTotalPacketNumber = _HpnicfNSMPLSTotalPacketNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 6, 1, 8),
    _HpnicfNSMPLSTotalPacketNumber_Type()
)
hpnicfNSMPLSTotalPacketNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNSMPLSTotalPacketNumber.setStatus("current")
_HpnicfNSMPLSTotalOctetNumber_Type = Counter32
_HpnicfNSMPLSTotalOctetNumber_Object = MibTableColumn
hpnicfNSMPLSTotalOctetNumber = _HpnicfNSMPLSTotalOctetNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 6, 1, 9),
    _HpnicfNSMPLSTotalOctetNumber_Type()
)
hpnicfNSMPLSTotalOctetNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNSMPLSTotalOctetNumber.setStatus("current")


class _HpnicfNSResetFlag_Type(Integer32):
    """Custom type hpnicfNSResetFlag based on Integer32"""

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


_HpnicfNSResetFlag_Type.__name__ = "Integer32"
_HpnicfNSResetFlag_Object = MibTableColumn
hpnicfNSResetFlag = _HpnicfNSResetFlag_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 6, 1, 10),
    _HpnicfNSResetFlag_Type()
)
hpnicfNSResetFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfNSResetFlag.setStatus("current")
_HpnicfNSResetTime_Type = TimeTicks
_HpnicfNSResetTime_Object = MibTableColumn
hpnicfNSResetTime = _HpnicfNSResetTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 6, 1, 11),
    _HpnicfNSResetTime_Type()
)
hpnicfNSResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNSResetTime.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-NS-MIB",
    **{"hpnicfNS": hpnicfNS,
       "hpnicfNSMibObjects": hpnicfNSMibObjects,
       "hpnicfNSMibScalarObjects": hpnicfNSMibScalarObjects,
       "hpnicfNSActiveTime": hpnicfNSActiveTime,
       "hpnicfNSInactiveTime": hpnicfNSInactiveTime,
       "hpnicfNSVersion": hpnicfNSVersion,
       "hpnicfNSAsType": hpnicfNSAsType,
       "hpnicfNSTemplateRefreshRate": hpnicfNSTemplateRefreshRate,
       "hpnicfNSTemplateTimeout": hpnicfNSTemplateTimeout,
       "hpnicfNSExportVlanOrIfIndex": hpnicfNSExportVlanOrIfIndex,
       "hpnicfNSProcessSlotTable": hpnicfNSProcessSlotTable,
       "hpnicfNSProcessSlotEntry": hpnicfNSProcessSlotEntry,
       "hpnicfNSProcessSlot": hpnicfNSProcessSlot,
       "hpnicfNSExportConfigTable": hpnicfNSExportConfigTable,
       "hpnicfNSExportConfigEntry": hpnicfNSExportConfigEntry,
       "hpnicfNSAggregationType": hpnicfNSAggregationType,
       "hpnicfNSHostIPAddr": hpnicfNSHostIPAddr,
       "hpnicfNSHostPort": hpnicfNSHostPort,
       "hpnicfNSSrcIpAddr": hpnicfNSSrcIpAddr,
       "hpnicfNSState": hpnicfNSState,
       "hpnicfNSExportInformationTable": hpnicfNSExportInformationTable,
       "hpnicfNSExportInformationEntry": hpnicfNSExportInformationEntry,
       "hpnicfNSExportType": hpnicfNSExportType,
       "hpnicfNSExportSlot": hpnicfNSExportSlot,
       "hpnicfNSExportStream": hpnicfNSExportStream,
       "hpnicfNSExportNum": hpnicfNSExportNum,
       "hpnicfNSExportFail": hpnicfNSExportFail,
       "hpnicfNSConfigTable": hpnicfNSConfigTable,
       "hpnicfNSConfigEntry": hpnicfNSConfigEntry,
       "hpnicfNSSourceSlot": hpnicfNSSourceSlot,
       "hpnicfNSSourceIfIndex": hpnicfNSSourceIfIndex,
       "hpnicfNSDestSlot": hpnicfNSDestSlot,
       "hpnicfNSDirect": hpnicfNSDirect,
       "hpnicfNSACLNumber": hpnicfNSACLNumber,
       "hpnicfNSACLName": hpnicfNSACLName,
       "hpnicfNSACLRule": hpnicfNSACLRule,
       "hpnicfNSConfigRowStatus": hpnicfNSConfigRowStatus,
       "hpnicfNSStatusTable": hpnicfNSStatusTable,
       "hpnicfNSStatusEntry": hpnicfNSStatusEntry,
       "hpnicfNSSlot": hpnicfNSSlot,
       "hpnicfNSActiveStreamNumber": hpnicfNSActiveStreamNumber,
       "hpnicfNSTotalStreamNumber": hpnicfNSTotalStreamNumber,
       "hpnicfNSTotalPacketNumber": hpnicfNSTotalPacketNumber,
       "hpnicfNSTotalOctetNumber": hpnicfNSTotalOctetNumber,
       "hpnicfNSMPLSActiveStreamNumber": hpnicfNSMPLSActiveStreamNumber,
       "hpnicfNSMPLSTotalStreamNumber": hpnicfNSMPLSTotalStreamNumber,
       "hpnicfNSMPLSTotalPacketNumber": hpnicfNSMPLSTotalPacketNumber,
       "hpnicfNSMPLSTotalOctetNumber": hpnicfNSMPLSTotalOctetNumber,
       "hpnicfNSResetFlag": hpnicfNSResetFlag,
       "hpnicfNSResetTime": hpnicfNSResetTime}
)
