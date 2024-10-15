# SNMP MIB module (H3C-NS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/H3C-NS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:51:04 2024
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

(h3cCommon,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "h3cCommon")

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

h3cNS = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 20)
)
h3cNS.setRevisions(
        ("2004-09-21 14:15",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cNSMibObjects_ObjectIdentity = ObjectIdentity
h3cNSMibObjects = _H3cNSMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 20, 1)
)
_H3cNSMibScalarObjects_ObjectIdentity = ObjectIdentity
h3cNSMibScalarObjects = _H3cNSMibScalarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 20, 1, 1)
)


class _H3cNSActiveTime_Type(Integer32):
    """Custom type h3cNSActiveTime based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_H3cNSActiveTime_Type.__name__ = "Integer32"
_H3cNSActiveTime_Object = MibScalar
h3cNSActiveTime = _H3cNSActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 20, 1, 1, 1),
    _H3cNSActiveTime_Type()
)
h3cNSActiveTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cNSActiveTime.setStatus("current")


class _H3cNSInactiveTime_Type(Integer32):
    """Custom type h3cNSInactiveTime based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_H3cNSInactiveTime_Type.__name__ = "Integer32"
_H3cNSInactiveTime_Object = MibScalar
h3cNSInactiveTime = _H3cNSInactiveTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 20, 1, 1, 2),
    _H3cNSInactiveTime_Type()
)
h3cNSInactiveTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cNSInactiveTime.setStatus("current")


class _H3cNSVersion_Type(Integer32):
    """Custom type h3cNSVersion based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 5),
        ValueRangeConstraint(9, 9),
    )


_H3cNSVersion_Type.__name__ = "Integer32"
_H3cNSVersion_Object = MibScalar
h3cNSVersion = _H3cNSVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 20, 1, 1, 3),
    _H3cNSVersion_Type()
)
h3cNSVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cNSVersion.setStatus("current")


class _H3cNSAsType_Type(Integer32):
    """Custom type h3cNSAsType based on Integer32"""
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


_H3cNSAsType_Type.__name__ = "Integer32"
_H3cNSAsType_Object = MibScalar
h3cNSAsType = _H3cNSAsType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 20, 1, 1, 4),
    _H3cNSAsType_Type()
)
h3cNSAsType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cNSAsType.setStatus("current")


class _H3cNSTemplateRefreshRate_Type(Integer32):
    """Custom type h3cNSTemplateRefreshRate based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_H3cNSTemplateRefreshRate_Type.__name__ = "Integer32"
_H3cNSTemplateRefreshRate_Object = MibScalar
h3cNSTemplateRefreshRate = _H3cNSTemplateRefreshRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 20, 1, 1, 5),
    _H3cNSTemplateRefreshRate_Type()
)
h3cNSTemplateRefreshRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cNSTemplateRefreshRate.setStatus("current")


class _H3cNSTemplateTimeout_Type(Integer32):
    """Custom type h3cNSTemplateTimeout based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_H3cNSTemplateTimeout_Type.__name__ = "Integer32"
_H3cNSTemplateTimeout_Object = MibScalar
h3cNSTemplateTimeout = _H3cNSTemplateTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 20, 1, 1, 6),
    _H3cNSTemplateTimeout_Type()
)
h3cNSTemplateTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cNSTemplateTimeout.setStatus("current")


class _H3cNSExportVlanOrIfIndex_Type(Integer32):
    """Custom type h3cNSExportVlanOrIfIndex based on Integer32"""
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


_H3cNSExportVlanOrIfIndex_Type.__name__ = "Integer32"
_H3cNSExportVlanOrIfIndex_Object = MibScalar
h3cNSExportVlanOrIfIndex = _H3cNSExportVlanOrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 20, 1, 1, 7),
    _H3cNSExportVlanOrIfIndex_Type()
)
h3cNSExportVlanOrIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cNSExportVlanOrIfIndex.setStatus("current")
_H3cNSProcessSlotTable_Object = MibTable
h3cNSProcessSlotTable = _H3cNSProcessSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 20, 1, 2)
)
if mibBuilder.loadTexts:
    h3cNSProcessSlotTable.setStatus("current")
_H3cNSProcessSlotEntry_Object = MibTableRow
h3cNSProcessSlotEntry = _H3cNSProcessSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 20, 1, 2, 1)
)
h3cNSProcessSlotEntry.setIndexNames(
    (0, "H3C-NS-MIB", "h3cNSProcessSlot"),
)
if mibBuilder.loadTexts:
    h3cNSProcessSlotEntry.setStatus("current")
_H3cNSProcessSlot_Type = Integer32
_H3cNSProcessSlot_Object = MibTableColumn
h3cNSProcessSlot = _H3cNSProcessSlot_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 20, 1, 2, 1, 1),
    _H3cNSProcessSlot_Type()
)
h3cNSProcessSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cNSProcessSlot.setStatus("current")
_H3cNSExportConfigTable_Object = MibTable
h3cNSExportConfigTable = _H3cNSExportConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 20, 1, 3)
)
if mibBuilder.loadTexts:
    h3cNSExportConfigTable.setStatus("current")
_H3cNSExportConfigEntry_Object = MibTableRow
h3cNSExportConfigEntry = _H3cNSExportConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 20, 1, 3, 1)
)
h3cNSExportConfigEntry.setIndexNames(
    (0, "H3C-NS-MIB", "h3cNSAggregationType"),
)
if mibBuilder.loadTexts:
    h3cNSExportConfigEntry.setStatus("current")


class _H3cNSAggregationType_Type(Integer32):
    """Custom type h3cNSAggregationType based on Integer32"""
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


_H3cNSAggregationType_Type.__name__ = "Integer32"
_H3cNSAggregationType_Object = MibTableColumn
h3cNSAggregationType = _H3cNSAggregationType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 20, 1, 3, 1, 1),
    _H3cNSAggregationType_Type()
)
h3cNSAggregationType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cNSAggregationType.setStatus("current")
_H3cNSHostIPAddr_Type = IpAddress
_H3cNSHostIPAddr_Object = MibTableColumn
h3cNSHostIPAddr = _H3cNSHostIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 20, 1, 3, 1, 2),
    _H3cNSHostIPAddr_Type()
)
h3cNSHostIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cNSHostIPAddr.setStatus("current")


class _H3cNSHostPort_Type(Integer32):
    """Custom type h3cNSHostPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_H3cNSHostPort_Type.__name__ = "Integer32"
_H3cNSHostPort_Object = MibTableColumn
h3cNSHostPort = _H3cNSHostPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 20, 1, 3, 1, 3),
    _H3cNSHostPort_Type()
)
h3cNSHostPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cNSHostPort.setStatus("current")
_H3cNSSrcIpAddr_Type = IpAddress
_H3cNSSrcIpAddr_Object = MibTableColumn
h3cNSSrcIpAddr = _H3cNSSrcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 20, 1, 3, 1, 4),
    _H3cNSSrcIpAddr_Type()
)
h3cNSSrcIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cNSSrcIpAddr.setStatus("current")


class _H3cNSState_Type(Integer32):
    """Custom type h3cNSState based on Integer32"""
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


_H3cNSState_Type.__name__ = "Integer32"
_H3cNSState_Object = MibTableColumn
h3cNSState = _H3cNSState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 20, 1, 3, 1, 5),
    _H3cNSState_Type()
)
h3cNSState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cNSState.setStatus("current")
_H3cNSExportInformationTable_Object = MibTable
h3cNSExportInformationTable = _H3cNSExportInformationTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 20, 1, 4)
)
if mibBuilder.loadTexts:
    h3cNSExportInformationTable.setStatus("current")
_H3cNSExportInformationEntry_Object = MibTableRow
h3cNSExportInformationEntry = _H3cNSExportInformationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 20, 1, 4, 1)
)
h3cNSExportInformationEntry.setIndexNames(
    (0, "H3C-NS-MIB", "h3cNSExportType"),
    (0, "H3C-NS-MIB", "h3cNSExportSlot"),
)
if mibBuilder.loadTexts:
    h3cNSExportInformationEntry.setStatus("current")


class _H3cNSExportType_Type(Integer32):
    """Custom type h3cNSExportType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_H3cNSExportType_Type.__name__ = "Integer32"
_H3cNSExportType_Object = MibTableColumn
h3cNSExportType = _H3cNSExportType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 20, 1, 4, 1, 1),
    _H3cNSExportType_Type()
)
h3cNSExportType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cNSExportType.setStatus("current")
_H3cNSExportSlot_Type = Integer32
_H3cNSExportSlot_Object = MibTableColumn
h3cNSExportSlot = _H3cNSExportSlot_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 20, 1, 4, 1, 2),
    _H3cNSExportSlot_Type()
)
h3cNSExportSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cNSExportSlot.setStatus("current")
_H3cNSExportStream_Type = Counter32
_H3cNSExportStream_Object = MibTableColumn
h3cNSExportStream = _H3cNSExportStream_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 20, 1, 4, 1, 3),
    _H3cNSExportStream_Type()
)
h3cNSExportStream.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cNSExportStream.setStatus("current")
_H3cNSExportNum_Type = Counter32
_H3cNSExportNum_Object = MibTableColumn
h3cNSExportNum = _H3cNSExportNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 20, 1, 4, 1, 4),
    _H3cNSExportNum_Type()
)
h3cNSExportNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cNSExportNum.setStatus("current")
_H3cNSExportFail_Type = Counter32
_H3cNSExportFail_Object = MibTableColumn
h3cNSExportFail = _H3cNSExportFail_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 20, 1, 4, 1, 5),
    _H3cNSExportFail_Type()
)
h3cNSExportFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cNSExportFail.setStatus("current")
_H3cNSConfigTable_Object = MibTable
h3cNSConfigTable = _H3cNSConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 20, 1, 5)
)
if mibBuilder.loadTexts:
    h3cNSConfigTable.setStatus("current")
_H3cNSConfigEntry_Object = MibTableRow
h3cNSConfigEntry = _H3cNSConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 20, 1, 5, 1)
)
h3cNSConfigEntry.setIndexNames(
    (0, "H3C-NS-MIB", "h3cNSSourceSlot"),
    (0, "H3C-NS-MIB", "h3cNSSourceIfIndex"),
    (0, "H3C-NS-MIB", "h3cNSDestSlot"),
)
if mibBuilder.loadTexts:
    h3cNSConfigEntry.setStatus("current")


class _H3cNSSourceSlot_Type(Integer32):
    """Custom type h3cNSSourceSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_H3cNSSourceSlot_Type.__name__ = "Integer32"
_H3cNSSourceSlot_Object = MibTableColumn
h3cNSSourceSlot = _H3cNSSourceSlot_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 20, 1, 5, 1, 1),
    _H3cNSSourceSlot_Type()
)
h3cNSSourceSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cNSSourceSlot.setStatus("current")
_H3cNSSourceIfIndex_Type = Integer32
_H3cNSSourceIfIndex_Object = MibTableColumn
h3cNSSourceIfIndex = _H3cNSSourceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 20, 1, 5, 1, 2),
    _H3cNSSourceIfIndex_Type()
)
h3cNSSourceIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cNSSourceIfIndex.setStatus("current")
_H3cNSDestSlot_Type = Integer32
_H3cNSDestSlot_Object = MibTableColumn
h3cNSDestSlot = _H3cNSDestSlot_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 20, 1, 5, 1, 3),
    _H3cNSDestSlot_Type()
)
h3cNSDestSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cNSDestSlot.setStatus("current")


class _H3cNSDirect_Type(Integer32):
    """Custom type h3cNSDirect based on Integer32"""
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


_H3cNSDirect_Type.__name__ = "Integer32"
_H3cNSDirect_Object = MibTableColumn
h3cNSDirect = _H3cNSDirect_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 20, 1, 5, 1, 4),
    _H3cNSDirect_Type()
)
h3cNSDirect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cNSDirect.setStatus("current")


class _H3cNSACLNumber_Type(Integer32):
    """Custom type h3cNSACLNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2000, 3999),
    )


_H3cNSACLNumber_Type.__name__ = "Integer32"
_H3cNSACLNumber_Object = MibTableColumn
h3cNSACLNumber = _H3cNSACLNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 20, 1, 5, 1, 5),
    _H3cNSACLNumber_Type()
)
h3cNSACLNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cNSACLNumber.setStatus("current")
_H3cNSACLName_Type = OctetString
_H3cNSACLName_Object = MibTableColumn
h3cNSACLName = _H3cNSACLName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 20, 1, 5, 1, 6),
    _H3cNSACLName_Type()
)
h3cNSACLName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cNSACLName.setStatus("current")
_H3cNSACLRule_Type = Integer32
_H3cNSACLRule_Object = MibTableColumn
h3cNSACLRule = _H3cNSACLRule_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 20, 1, 5, 1, 7),
    _H3cNSACLRule_Type()
)
h3cNSACLRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cNSACLRule.setStatus("current")
_H3cNSConfigRowStatus_Type = RowStatus
_H3cNSConfigRowStatus_Object = MibTableColumn
h3cNSConfigRowStatus = _H3cNSConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 20, 1, 5, 1, 8),
    _H3cNSConfigRowStatus_Type()
)
h3cNSConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cNSConfigRowStatus.setStatus("current")
_H3cNSStatusTable_Object = MibTable
h3cNSStatusTable = _H3cNSStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 20, 1, 6)
)
if mibBuilder.loadTexts:
    h3cNSStatusTable.setStatus("current")
_H3cNSStatusEntry_Object = MibTableRow
h3cNSStatusEntry = _H3cNSStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 20, 1, 6, 1)
)
h3cNSStatusEntry.setIndexNames(
    (0, "H3C-NS-MIB", "h3cNSSlot"),
)
if mibBuilder.loadTexts:
    h3cNSStatusEntry.setStatus("current")
_H3cNSSlot_Type = Integer32
_H3cNSSlot_Object = MibTableColumn
h3cNSSlot = _H3cNSSlot_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 20, 1, 6, 1, 1),
    _H3cNSSlot_Type()
)
h3cNSSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cNSSlot.setStatus("current")
_H3cNSActiveStreamNumber_Type = Counter32
_H3cNSActiveStreamNumber_Object = MibTableColumn
h3cNSActiveStreamNumber = _H3cNSActiveStreamNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 20, 1, 6, 1, 2),
    _H3cNSActiveStreamNumber_Type()
)
h3cNSActiveStreamNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cNSActiveStreamNumber.setStatus("current")
_H3cNSTotalStreamNumber_Type = Counter32
_H3cNSTotalStreamNumber_Object = MibTableColumn
h3cNSTotalStreamNumber = _H3cNSTotalStreamNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 20, 1, 6, 1, 3),
    _H3cNSTotalStreamNumber_Type()
)
h3cNSTotalStreamNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cNSTotalStreamNumber.setStatus("current")
_H3cNSTotalPacketNumber_Type = Counter32
_H3cNSTotalPacketNumber_Object = MibTableColumn
h3cNSTotalPacketNumber = _H3cNSTotalPacketNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 20, 1, 6, 1, 4),
    _H3cNSTotalPacketNumber_Type()
)
h3cNSTotalPacketNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cNSTotalPacketNumber.setStatus("current")
_H3cNSTotalOctetNumber_Type = Counter32
_H3cNSTotalOctetNumber_Object = MibTableColumn
h3cNSTotalOctetNumber = _H3cNSTotalOctetNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 20, 1, 6, 1, 5),
    _H3cNSTotalOctetNumber_Type()
)
h3cNSTotalOctetNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cNSTotalOctetNumber.setStatus("current")
_H3cNSMPLSActiveStreamNumber_Type = Counter32
_H3cNSMPLSActiveStreamNumber_Object = MibTableColumn
h3cNSMPLSActiveStreamNumber = _H3cNSMPLSActiveStreamNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 20, 1, 6, 1, 6),
    _H3cNSMPLSActiveStreamNumber_Type()
)
h3cNSMPLSActiveStreamNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cNSMPLSActiveStreamNumber.setStatus("current")
_H3cNSMPLSTotalStreamNumber_Type = Counter32
_H3cNSMPLSTotalStreamNumber_Object = MibTableColumn
h3cNSMPLSTotalStreamNumber = _H3cNSMPLSTotalStreamNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 20, 1, 6, 1, 7),
    _H3cNSMPLSTotalStreamNumber_Type()
)
h3cNSMPLSTotalStreamNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cNSMPLSTotalStreamNumber.setStatus("current")
_H3cNSMPLSTotalPacketNumber_Type = Counter32
_H3cNSMPLSTotalPacketNumber_Object = MibTableColumn
h3cNSMPLSTotalPacketNumber = _H3cNSMPLSTotalPacketNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 20, 1, 6, 1, 8),
    _H3cNSMPLSTotalPacketNumber_Type()
)
h3cNSMPLSTotalPacketNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cNSMPLSTotalPacketNumber.setStatus("current")
_H3cNSMPLSTotalOctetNumber_Type = Counter32
_H3cNSMPLSTotalOctetNumber_Object = MibTableColumn
h3cNSMPLSTotalOctetNumber = _H3cNSMPLSTotalOctetNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 20, 1, 6, 1, 9),
    _H3cNSMPLSTotalOctetNumber_Type()
)
h3cNSMPLSTotalOctetNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cNSMPLSTotalOctetNumber.setStatus("current")


class _H3cNSResetFlag_Type(Integer32):
    """Custom type h3cNSResetFlag based on Integer32"""

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


_H3cNSResetFlag_Type.__name__ = "Integer32"
_H3cNSResetFlag_Object = MibTableColumn
h3cNSResetFlag = _H3cNSResetFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 20, 1, 6, 1, 10),
    _H3cNSResetFlag_Type()
)
h3cNSResetFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cNSResetFlag.setStatus("current")
_H3cNSResetTime_Type = TimeTicks
_H3cNSResetTime_Object = MibTableColumn
h3cNSResetTime = _H3cNSResetTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 20, 1, 6, 1, 11),
    _H3cNSResetTime_Type()
)
h3cNSResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cNSResetTime.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-NS-MIB",
    **{"h3cNS": h3cNS,
       "h3cNSMibObjects": h3cNSMibObjects,
       "h3cNSMibScalarObjects": h3cNSMibScalarObjects,
       "h3cNSActiveTime": h3cNSActiveTime,
       "h3cNSInactiveTime": h3cNSInactiveTime,
       "h3cNSVersion": h3cNSVersion,
       "h3cNSAsType": h3cNSAsType,
       "h3cNSTemplateRefreshRate": h3cNSTemplateRefreshRate,
       "h3cNSTemplateTimeout": h3cNSTemplateTimeout,
       "h3cNSExportVlanOrIfIndex": h3cNSExportVlanOrIfIndex,
       "h3cNSProcessSlotTable": h3cNSProcessSlotTable,
       "h3cNSProcessSlotEntry": h3cNSProcessSlotEntry,
       "h3cNSProcessSlot": h3cNSProcessSlot,
       "h3cNSExportConfigTable": h3cNSExportConfigTable,
       "h3cNSExportConfigEntry": h3cNSExportConfigEntry,
       "h3cNSAggregationType": h3cNSAggregationType,
       "h3cNSHostIPAddr": h3cNSHostIPAddr,
       "h3cNSHostPort": h3cNSHostPort,
       "h3cNSSrcIpAddr": h3cNSSrcIpAddr,
       "h3cNSState": h3cNSState,
       "h3cNSExportInformationTable": h3cNSExportInformationTable,
       "h3cNSExportInformationEntry": h3cNSExportInformationEntry,
       "h3cNSExportType": h3cNSExportType,
       "h3cNSExportSlot": h3cNSExportSlot,
       "h3cNSExportStream": h3cNSExportStream,
       "h3cNSExportNum": h3cNSExportNum,
       "h3cNSExportFail": h3cNSExportFail,
       "h3cNSConfigTable": h3cNSConfigTable,
       "h3cNSConfigEntry": h3cNSConfigEntry,
       "h3cNSSourceSlot": h3cNSSourceSlot,
       "h3cNSSourceIfIndex": h3cNSSourceIfIndex,
       "h3cNSDestSlot": h3cNSDestSlot,
       "h3cNSDirect": h3cNSDirect,
       "h3cNSACLNumber": h3cNSACLNumber,
       "h3cNSACLName": h3cNSACLName,
       "h3cNSACLRule": h3cNSACLRule,
       "h3cNSConfigRowStatus": h3cNSConfigRowStatus,
       "h3cNSStatusTable": h3cNSStatusTable,
       "h3cNSStatusEntry": h3cNSStatusEntry,
       "h3cNSSlot": h3cNSSlot,
       "h3cNSActiveStreamNumber": h3cNSActiveStreamNumber,
       "h3cNSTotalStreamNumber": h3cNSTotalStreamNumber,
       "h3cNSTotalPacketNumber": h3cNSTotalPacketNumber,
       "h3cNSTotalOctetNumber": h3cNSTotalOctetNumber,
       "h3cNSMPLSActiveStreamNumber": h3cNSMPLSActiveStreamNumber,
       "h3cNSMPLSTotalStreamNumber": h3cNSMPLSTotalStreamNumber,
       "h3cNSMPLSTotalPacketNumber": h3cNSMPLSTotalPacketNumber,
       "h3cNSMPLSTotalOctetNumber": h3cNSMPLSTotalOctetNumber,
       "h3cNSResetFlag": h3cNSResetFlag,
       "h3cNSResetTime": h3cNSResetTime}
)
