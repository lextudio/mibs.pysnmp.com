# SNMP MIB module (CISCO-NBAR-PROTOCOL-DISCOVERY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-NBAR-PROTOCOL-DISCOVERY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:06:04 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoNbarProtocolDiscoveryMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 244)
)
ciscoNbarProtocolDiscoveryMIB.setRevisions(
        ("2002-08-16 00:00",
         "2001-12-28 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CiscoPdProtocolIndex(Unsigned32, TextualConvention):
    status = "current"


class CiscoPdProtocolName(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )



class CiscoPdDataType(Integer32, TextualConvention):
    status = "current"
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
        *(("bitRateIn", 1),
          ("bitRateOut", 2),
          ("bitRateSum", 3),
          ("byteCountIn", 4),
          ("byteCountOut", 5),
          ("byteCountSum", 6),
          ("packetCountIn", 7),
          ("packetCountOut", 8),
          ("packetCountSum", 9))
    )



# MIB Managed Objects in the order of their OIDs

_CnpdMIBNotifications_ObjectIdentity = ObjectIdentity
cnpdMIBNotifications = _CnpdMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 244, 0)
)
_CnpdMIBObjects_ObjectIdentity = ObjectIdentity
cnpdMIBObjects = _CnpdMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 244, 1)
)
_CnpdStatus_ObjectIdentity = ObjectIdentity
cnpdStatus = _CnpdStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 1)
)
_CnpdStatusTable_Object = MibTable
cnpdStatusTable = _CnpdStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cnpdStatusTable.setStatus("current")
_CnpdStatusEntry_Object = MibTableRow
cnpdStatusEntry = _CnpdStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 1, 1, 1)
)
cnpdStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cnpdStatusEntry.setStatus("current")
_CnpdStatusPdEnable_Type = TruthValue
_CnpdStatusPdEnable_Object = MibTableColumn
cnpdStatusPdEnable = _CnpdStatusPdEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 1, 1, 1, 1),
    _CnpdStatusPdEnable_Type()
)
cnpdStatusPdEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnpdStatusPdEnable.setStatus("current")
_CnpdStatusLastUpdateTime_Type = TimeTicks
_CnpdStatusLastUpdateTime_Object = MibTableColumn
cnpdStatusLastUpdateTime = _CnpdStatusLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 1, 1, 1, 2),
    _CnpdStatusLastUpdateTime_Type()
)
cnpdStatusLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnpdStatusLastUpdateTime.setStatus("current")
_CnpdAllStats_ObjectIdentity = ObjectIdentity
cnpdAllStats = _CnpdAllStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 2)
)
_CnpdAllStatsTable_Object = MibTable
cnpdAllStatsTable = _CnpdAllStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cnpdAllStatsTable.setStatus("current")
_CnpdAllStatsEntry_Object = MibTableRow
cnpdAllStatsEntry = _CnpdAllStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 2, 1, 1)
)
cnpdAllStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdAllStatsProtocolsIndex"),
)
if mibBuilder.loadTexts:
    cnpdAllStatsEntry.setStatus("current")


class _CnpdAllStatsProtocolsIndex_Type(CiscoPdProtocolIndex):
    """Custom type cnpdAllStatsProtocolsIndex based on CiscoPdProtocolIndex"""
    subtypeSpec = CiscoPdProtocolIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_CnpdAllStatsProtocolsIndex_Type.__name__ = "CiscoPdProtocolIndex"
_CnpdAllStatsProtocolsIndex_Object = MibTableColumn
cnpdAllStatsProtocolsIndex = _CnpdAllStatsProtocolsIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 2, 1, 1, 1),
    _CnpdAllStatsProtocolsIndex_Type()
)
cnpdAllStatsProtocolsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cnpdAllStatsProtocolsIndex.setStatus("current")
_CnpdAllStatsProtocolName_Type = CiscoPdProtocolName
_CnpdAllStatsProtocolName_Object = MibTableColumn
cnpdAllStatsProtocolName = _CnpdAllStatsProtocolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 2, 1, 1, 2),
    _CnpdAllStatsProtocolName_Type()
)
cnpdAllStatsProtocolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnpdAllStatsProtocolName.setStatus("current")
_CnpdAllStatsInPkts_Type = Counter32
_CnpdAllStatsInPkts_Object = MibTableColumn
cnpdAllStatsInPkts = _CnpdAllStatsInPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 2, 1, 1, 3),
    _CnpdAllStatsInPkts_Type()
)
cnpdAllStatsInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnpdAllStatsInPkts.setStatus("current")
if mibBuilder.loadTexts:
    cnpdAllStatsInPkts.setUnits("packets")
_CnpdAllStatsOutPkts_Type = Counter32
_CnpdAllStatsOutPkts_Object = MibTableColumn
cnpdAllStatsOutPkts = _CnpdAllStatsOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 2, 1, 1, 4),
    _CnpdAllStatsOutPkts_Type()
)
cnpdAllStatsOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnpdAllStatsOutPkts.setStatus("current")
if mibBuilder.loadTexts:
    cnpdAllStatsOutPkts.setUnits("packets")
_CnpdAllStatsInBytes_Type = Counter32
_CnpdAllStatsInBytes_Object = MibTableColumn
cnpdAllStatsInBytes = _CnpdAllStatsInBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 2, 1, 1, 5),
    _CnpdAllStatsInBytes_Type()
)
cnpdAllStatsInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnpdAllStatsInBytes.setStatus("current")
if mibBuilder.loadTexts:
    cnpdAllStatsInBytes.setUnits("bytes")
_CnpdAllStatsOutBytes_Type = Counter32
_CnpdAllStatsOutBytes_Object = MibTableColumn
cnpdAllStatsOutBytes = _CnpdAllStatsOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 2, 1, 1, 6),
    _CnpdAllStatsOutBytes_Type()
)
cnpdAllStatsOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnpdAllStatsOutBytes.setStatus("current")
if mibBuilder.loadTexts:
    cnpdAllStatsOutBytes.setUnits("bytes")
_CnpdAllStatsHCInPkts_Type = Counter64
_CnpdAllStatsHCInPkts_Object = MibTableColumn
cnpdAllStatsHCInPkts = _CnpdAllStatsHCInPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 2, 1, 1, 7),
    _CnpdAllStatsHCInPkts_Type()
)
cnpdAllStatsHCInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnpdAllStatsHCInPkts.setStatus("current")
if mibBuilder.loadTexts:
    cnpdAllStatsHCInPkts.setUnits("packets")
_CnpdAllStatsHCOutPkts_Type = Counter64
_CnpdAllStatsHCOutPkts_Object = MibTableColumn
cnpdAllStatsHCOutPkts = _CnpdAllStatsHCOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 2, 1, 1, 8),
    _CnpdAllStatsHCOutPkts_Type()
)
cnpdAllStatsHCOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnpdAllStatsHCOutPkts.setStatus("current")
if mibBuilder.loadTexts:
    cnpdAllStatsHCOutPkts.setUnits("packets")
_CnpdAllStatsHCInBytes_Type = Counter64
_CnpdAllStatsHCInBytes_Object = MibTableColumn
cnpdAllStatsHCInBytes = _CnpdAllStatsHCInBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 2, 1, 1, 9),
    _CnpdAllStatsHCInBytes_Type()
)
cnpdAllStatsHCInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnpdAllStatsHCInBytes.setStatus("current")
if mibBuilder.loadTexts:
    cnpdAllStatsHCInBytes.setUnits("bytes")
_CnpdAllStatsHCOutBytes_Type = Counter64
_CnpdAllStatsHCOutBytes_Object = MibTableColumn
cnpdAllStatsHCOutBytes = _CnpdAllStatsHCOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 2, 1, 1, 10),
    _CnpdAllStatsHCOutBytes_Type()
)
cnpdAllStatsHCOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnpdAllStatsHCOutBytes.setStatus("current")
if mibBuilder.loadTexts:
    cnpdAllStatsHCOutBytes.setUnits("bytes")


class _CnpdAllStatsInBitRate_Type(Unsigned32):
    """Custom type cnpdAllStatsInBitRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CnpdAllStatsInBitRate_Type.__name__ = "Unsigned32"
_CnpdAllStatsInBitRate_Object = MibTableColumn
cnpdAllStatsInBitRate = _CnpdAllStatsInBitRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 2, 1, 1, 11),
    _CnpdAllStatsInBitRate_Type()
)
cnpdAllStatsInBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnpdAllStatsInBitRate.setStatus("current")
if mibBuilder.loadTexts:
    cnpdAllStatsInBitRate.setUnits("kilo bits per second")


class _CnpdAllStatsOutBitRate_Type(Unsigned32):
    """Custom type cnpdAllStatsOutBitRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CnpdAllStatsOutBitRate_Type.__name__ = "Unsigned32"
_CnpdAllStatsOutBitRate_Object = MibTableColumn
cnpdAllStatsOutBitRate = _CnpdAllStatsOutBitRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 2, 1, 1, 12),
    _CnpdAllStatsOutBitRate_Type()
)
cnpdAllStatsOutBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnpdAllStatsOutBitRate.setStatus("current")
if mibBuilder.loadTexts:
    cnpdAllStatsOutBitRate.setUnits("kilo bits per second")
_CnpdTopNConfig_ObjectIdentity = ObjectIdentity
cnpdTopNConfig = _CnpdTopNConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 3)
)
_CnpdTopNConfigTable_Object = MibTable
cnpdTopNConfigTable = _CnpdTopNConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cnpdTopNConfigTable.setStatus("current")
_CnpdTopNConfigEntry_Object = MibTableRow
cnpdTopNConfigEntry = _CnpdTopNConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 3, 1, 1)
)
cnpdTopNConfigEntry.setIndexNames(
    (0, "CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdTopNConfigIndex"),
)
if mibBuilder.loadTexts:
    cnpdTopNConfigEntry.setStatus("current")


class _CnpdTopNConfigIndex_Type(Unsigned32):
    """Custom type cnpdTopNConfigIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_CnpdTopNConfigIndex_Type.__name__ = "Unsigned32"
_CnpdTopNConfigIndex_Object = MibTableColumn
cnpdTopNConfigIndex = _CnpdTopNConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 3, 1, 1, 1),
    _CnpdTopNConfigIndex_Type()
)
cnpdTopNConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cnpdTopNConfigIndex.setStatus("current")
_CnpdTopNConfigIfIndex_Type = InterfaceIndex
_CnpdTopNConfigIfIndex_Object = MibTableColumn
cnpdTopNConfigIfIndex = _CnpdTopNConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 3, 1, 1, 2),
    _CnpdTopNConfigIfIndex_Type()
)
cnpdTopNConfigIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnpdTopNConfigIfIndex.setStatus("current")


class _CnpdTopNConfigStatsSelect_Type(CiscoPdDataType):
    """Custom type cnpdTopNConfigStatsSelect based on CiscoPdDataType"""


_CnpdTopNConfigStatsSelect_Object = MibTableColumn
cnpdTopNConfigStatsSelect = _CnpdTopNConfigStatsSelect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 3, 1, 1, 3),
    _CnpdTopNConfigStatsSelect_Type()
)
cnpdTopNConfigStatsSelect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnpdTopNConfigStatsSelect.setStatus("current")


class _CnpdTopNConfigSampleTime_Type(Unsigned32):
    """Custom type cnpdTopNConfigSampleTime based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )


_CnpdTopNConfigSampleTime_Type.__name__ = "Unsigned32"
_CnpdTopNConfigSampleTime_Object = MibTableColumn
cnpdTopNConfigSampleTime = _CnpdTopNConfigSampleTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 3, 1, 1, 4),
    _CnpdTopNConfigSampleTime_Type()
)
cnpdTopNConfigSampleTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnpdTopNConfigSampleTime.setStatus("current")
if mibBuilder.loadTexts:
    cnpdTopNConfigSampleTime.setUnits("seconds")


class _CnpdTopNConfigRequestedSize_Type(Unsigned32):
    """Custom type cnpdTopNConfigRequestedSize based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 500),
    )


_CnpdTopNConfigRequestedSize_Type.__name__ = "Unsigned32"
_CnpdTopNConfigRequestedSize_Object = MibTableColumn
cnpdTopNConfigRequestedSize = _CnpdTopNConfigRequestedSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 3, 1, 1, 5),
    _CnpdTopNConfigRequestedSize_Type()
)
cnpdTopNConfigRequestedSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnpdTopNConfigRequestedSize.setStatus("current")


class _CnpdTopNConfigGrantedSize_Type(Unsigned32):
    """Custom type cnpdTopNConfigGrantedSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 500),
    )


_CnpdTopNConfigGrantedSize_Type.__name__ = "Unsigned32"
_CnpdTopNConfigGrantedSize_Object = MibTableColumn
cnpdTopNConfigGrantedSize = _CnpdTopNConfigGrantedSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 3, 1, 1, 6),
    _CnpdTopNConfigGrantedSize_Type()
)
cnpdTopNConfigGrantedSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnpdTopNConfigGrantedSize.setStatus("current")
_CnpdTopNConfigTime_Type = TimeTicks
_CnpdTopNConfigTime_Object = MibTableColumn
cnpdTopNConfigTime = _CnpdTopNConfigTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 3, 1, 1, 7),
    _CnpdTopNConfigTime_Type()
)
cnpdTopNConfigTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnpdTopNConfigTime.setStatus("current")
_CnpdTopNConfigStatus_Type = RowStatus
_CnpdTopNConfigStatus_Object = MibTableColumn
cnpdTopNConfigStatus = _CnpdTopNConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 3, 1, 1, 8),
    _CnpdTopNConfigStatus_Type()
)
cnpdTopNConfigStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnpdTopNConfigStatus.setStatus("current")
_CnpdTopNStats_ObjectIdentity = ObjectIdentity
cnpdTopNStats = _CnpdTopNStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 4)
)
_CnpdTopNStatsTable_Object = MibTable
cnpdTopNStatsTable = _CnpdTopNStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cnpdTopNStatsTable.setStatus("current")
_CnpdTopNStatsEntry_Object = MibTableRow
cnpdTopNStatsEntry = _CnpdTopNStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 4, 1, 1)
)
cnpdTopNStatsEntry.setIndexNames(
    (0, "CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdTopNConfigIndex"),
    (0, "CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdTopNStatsIndex"),
)
if mibBuilder.loadTexts:
    cnpdTopNStatsEntry.setStatus("current")


class _CnpdTopNStatsIndex_Type(Unsigned32):
    """Custom type cnpdTopNStatsIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 500),
    )


_CnpdTopNStatsIndex_Type.__name__ = "Unsigned32"
_CnpdTopNStatsIndex_Object = MibTableColumn
cnpdTopNStatsIndex = _CnpdTopNStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 4, 1, 1, 1),
    _CnpdTopNStatsIndex_Type()
)
cnpdTopNStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cnpdTopNStatsIndex.setStatus("current")
_CnpdTopNStatsProtocolName_Type = CiscoPdProtocolName
_CnpdTopNStatsProtocolName_Object = MibTableColumn
cnpdTopNStatsProtocolName = _CnpdTopNStatsProtocolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 4, 1, 1, 2),
    _CnpdTopNStatsProtocolName_Type()
)
cnpdTopNStatsProtocolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnpdTopNStatsProtocolName.setStatus("current")
_CnpdTopNStatsRate_Type = Counter32
_CnpdTopNStatsRate_Object = MibTableColumn
cnpdTopNStatsRate = _CnpdTopNStatsRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 4, 1, 1, 3),
    _CnpdTopNStatsRate_Type()
)
cnpdTopNStatsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnpdTopNStatsRate.setStatus("current")
_CnpdTopNStatsHCRate_Type = Counter64
_CnpdTopNStatsHCRate_Object = MibTableColumn
cnpdTopNStatsHCRate = _CnpdTopNStatsHCRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 4, 1, 1, 4),
    _CnpdTopNStatsHCRate_Type()
)
cnpdTopNStatsHCRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnpdTopNStatsHCRate.setStatus("current")
_CnpdThresholdConfig_ObjectIdentity = ObjectIdentity
cnpdThresholdConfig = _CnpdThresholdConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 5)
)
_CnpdThresholdConfigTable_Object = MibTable
cnpdThresholdConfigTable = _CnpdThresholdConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 5, 1)
)
if mibBuilder.loadTexts:
    cnpdThresholdConfigTable.setStatus("current")
_CnpdThresholdConfigEntry_Object = MibTableRow
cnpdThresholdConfigEntry = _CnpdThresholdConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 5, 1, 1)
)
cnpdThresholdConfigEntry.setIndexNames(
    (0, "CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdThresholdConfigIndex"),
)
if mibBuilder.loadTexts:
    cnpdThresholdConfigEntry.setStatus("current")


class _CnpdThresholdConfigIndex_Type(Unsigned32):
    """Custom type cnpdThresholdConfigIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CnpdThresholdConfigIndex_Type.__name__ = "Unsigned32"
_CnpdThresholdConfigIndex_Object = MibTableColumn
cnpdThresholdConfigIndex = _CnpdThresholdConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 5, 1, 1, 1),
    _CnpdThresholdConfigIndex_Type()
)
cnpdThresholdConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cnpdThresholdConfigIndex.setStatus("current")
_CnpdThresholdConfigIfIndex_Type = InterfaceIndex
_CnpdThresholdConfigIfIndex_Object = MibTableColumn
cnpdThresholdConfigIfIndex = _CnpdThresholdConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 5, 1, 1, 2),
    _CnpdThresholdConfigIfIndex_Type()
)
cnpdThresholdConfigIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnpdThresholdConfigIfIndex.setStatus("current")


class _CnpdThresholdConfigInterval_Type(Unsigned32):
    """Custom type cnpdThresholdConfigInterval based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )


_CnpdThresholdConfigInterval_Type.__name__ = "Unsigned32"
_CnpdThresholdConfigInterval_Object = MibTableColumn
cnpdThresholdConfigInterval = _CnpdThresholdConfigInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 5, 1, 1, 3),
    _CnpdThresholdConfigInterval_Type()
)
cnpdThresholdConfigInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnpdThresholdConfigInterval.setStatus("current")
if mibBuilder.loadTexts:
    cnpdThresholdConfigInterval.setUnits("seconds")


class _CnpdThresholdConfigSampleType_Type(Integer32):
    """Custom type cnpdThresholdConfigSampleType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("absoluteValue", 1),
          ("deltaValue", 2))
    )


_CnpdThresholdConfigSampleType_Type.__name__ = "Integer32"
_CnpdThresholdConfigSampleType_Object = MibTableColumn
cnpdThresholdConfigSampleType = _CnpdThresholdConfigSampleType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 5, 1, 1, 4),
    _CnpdThresholdConfigSampleType_Type()
)
cnpdThresholdConfigSampleType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnpdThresholdConfigSampleType.setStatus("current")


class _CnpdThresholdConfigProtocol_Type(CiscoPdProtocolIndex):
    """Custom type cnpdThresholdConfigProtocol based on CiscoPdProtocolIndex"""
    subtypeSpec = CiscoPdProtocolIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_CnpdThresholdConfigProtocol_Type.__name__ = "CiscoPdProtocolIndex"
_CnpdThresholdConfigProtocol_Object = MibTableColumn
cnpdThresholdConfigProtocol = _CnpdThresholdConfigProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 5, 1, 1, 5),
    _CnpdThresholdConfigProtocol_Type()
)
cnpdThresholdConfigProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnpdThresholdConfigProtocol.setStatus("current")


class _CnpdThresholdConfigProtocolAny_Type(TruthValue):
    """Custom type cnpdThresholdConfigProtocolAny based on TruthValue"""


_CnpdThresholdConfigProtocolAny_Object = MibTableColumn
cnpdThresholdConfigProtocolAny = _CnpdThresholdConfigProtocolAny_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 5, 1, 1, 6),
    _CnpdThresholdConfigProtocolAny_Type()
)
cnpdThresholdConfigProtocolAny.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnpdThresholdConfigProtocolAny.setStatus("current")


class _CnpdThresholdConfigStatsSelect_Type(CiscoPdDataType):
    """Custom type cnpdThresholdConfigStatsSelect based on CiscoPdDataType"""


_CnpdThresholdConfigStatsSelect_Object = MibTableColumn
cnpdThresholdConfigStatsSelect = _CnpdThresholdConfigStatsSelect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 5, 1, 1, 7),
    _CnpdThresholdConfigStatsSelect_Type()
)
cnpdThresholdConfigStatsSelect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnpdThresholdConfigStatsSelect.setStatus("current")


class _CnpdThresholdConfigStartup_Type(Integer32):
    """Custom type cnpdThresholdConfigStartup based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("falling", 2),
          ("rising", 1),
          ("risingOrFalling", 3))
    )


_CnpdThresholdConfigStartup_Type.__name__ = "Integer32"
_CnpdThresholdConfigStartup_Object = MibTableColumn
cnpdThresholdConfigStartup = _CnpdThresholdConfigStartup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 5, 1, 1, 8),
    _CnpdThresholdConfigStartup_Type()
)
cnpdThresholdConfigStartup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnpdThresholdConfigStartup.setStatus("current")


class _CnpdThresholdConfigRising_Type(Unsigned32):
    """Custom type cnpdThresholdConfigRising based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CnpdThresholdConfigRising_Type.__name__ = "Unsigned32"
_CnpdThresholdConfigRising_Object = MibTableColumn
cnpdThresholdConfigRising = _CnpdThresholdConfigRising_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 5, 1, 1, 9),
    _CnpdThresholdConfigRising_Type()
)
cnpdThresholdConfigRising.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnpdThresholdConfigRising.setStatus("current")


class _CnpdThresholdConfigFalling_Type(Unsigned32):
    """Custom type cnpdThresholdConfigFalling based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CnpdThresholdConfigFalling_Type.__name__ = "Unsigned32"
_CnpdThresholdConfigFalling_Object = MibTableColumn
cnpdThresholdConfigFalling = _CnpdThresholdConfigFalling_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 5, 1, 1, 10),
    _CnpdThresholdConfigFalling_Type()
)
cnpdThresholdConfigFalling.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnpdThresholdConfigFalling.setStatus("current")
_CnpdThresholdConfigStatus_Type = RowStatus
_CnpdThresholdConfigStatus_Object = MibTableColumn
cnpdThresholdConfigStatus = _CnpdThresholdConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 5, 1, 1, 12),
    _CnpdThresholdConfigStatus_Type()
)
cnpdThresholdConfigStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnpdThresholdConfigStatus.setStatus("current")
_CnpdThresholdHistory_ObjectIdentity = ObjectIdentity
cnpdThresholdHistory = _CnpdThresholdHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 6)
)
_CnpdThresholdHistoryTable_Object = MibTable
cnpdThresholdHistoryTable = _CnpdThresholdHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 6, 1)
)
if mibBuilder.loadTexts:
    cnpdThresholdHistoryTable.setStatus("current")
_CnpdThresholdHistoryEntry_Object = MibTableRow
cnpdThresholdHistoryEntry = _CnpdThresholdHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 6, 1, 1)
)
cnpdThresholdHistoryEntry.setIndexNames(
    (0, "CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdThresholdHistoryIndex"),
)
if mibBuilder.loadTexts:
    cnpdThresholdHistoryEntry.setStatus("current")


class _CnpdThresholdHistoryIndex_Type(Unsigned32):
    """Custom type cnpdThresholdHistoryIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_CnpdThresholdHistoryIndex_Type.__name__ = "Unsigned32"
_CnpdThresholdHistoryIndex_Object = MibTableColumn
cnpdThresholdHistoryIndex = _CnpdThresholdHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 6, 1, 1, 1),
    _CnpdThresholdHistoryIndex_Type()
)
cnpdThresholdHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cnpdThresholdHistoryIndex.setStatus("current")


class _CnpdThresholdHistoryConfigIndex_Type(Unsigned32):
    """Custom type cnpdThresholdHistoryConfigIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_CnpdThresholdHistoryConfigIndex_Type.__name__ = "Unsigned32"
_CnpdThresholdHistoryConfigIndex_Object = MibTableColumn
cnpdThresholdHistoryConfigIndex = _CnpdThresholdHistoryConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 6, 1, 1, 2),
    _CnpdThresholdHistoryConfigIndex_Type()
)
cnpdThresholdHistoryConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnpdThresholdHistoryConfigIndex.setStatus("current")


class _CnpdThresholdHistoryValue_Type(Unsigned32):
    """Custom type cnpdThresholdHistoryValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CnpdThresholdHistoryValue_Type.__name__ = "Unsigned32"
_CnpdThresholdHistoryValue_Object = MibTableColumn
cnpdThresholdHistoryValue = _CnpdThresholdHistoryValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 6, 1, 1, 3),
    _CnpdThresholdHistoryValue_Type()
)
cnpdThresholdHistoryValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnpdThresholdHistoryValue.setStatus("current")


class _CnpdThresholdHistoryType_Type(Integer32):
    """Custom type cnpdThresholdHistoryType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fallingBreach", 2),
          ("risingBreach", 1))
    )


_CnpdThresholdHistoryType_Type.__name__ = "Integer32"
_CnpdThresholdHistoryType_Object = MibTableColumn
cnpdThresholdHistoryType = _CnpdThresholdHistoryType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 6, 1, 1, 4),
    _CnpdThresholdHistoryType_Type()
)
cnpdThresholdHistoryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnpdThresholdHistoryType.setStatus("current")
_CnpdThresholdHistoryTime_Type = TimeTicks
_CnpdThresholdHistoryTime_Object = MibTableColumn
cnpdThresholdHistoryTime = _CnpdThresholdHistoryTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 6, 1, 1, 5),
    _CnpdThresholdHistoryTime_Type()
)
cnpdThresholdHistoryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnpdThresholdHistoryTime.setStatus("current")


class _CnpdThresholdHistoryProtocol_Type(CiscoPdProtocolIndex):
    """Custom type cnpdThresholdHistoryProtocol based on CiscoPdProtocolIndex"""
    subtypeSpec = CiscoPdProtocolIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_CnpdThresholdHistoryProtocol_Type.__name__ = "CiscoPdProtocolIndex"
_CnpdThresholdHistoryProtocol_Object = MibTableColumn
cnpdThresholdHistoryProtocol = _CnpdThresholdHistoryProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 6, 1, 1, 6),
    _CnpdThresholdHistoryProtocol_Type()
)
cnpdThresholdHistoryProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnpdThresholdHistoryProtocol.setStatus("current")
_CnpdThresholdHistoryStatsSelect_Type = CiscoPdDataType
_CnpdThresholdHistoryStatsSelect_Object = MibTableColumn
cnpdThresholdHistoryStatsSelect = _CnpdThresholdHistoryStatsSelect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 6, 1, 1, 7),
    _CnpdThresholdHistoryStatsSelect_Type()
)
cnpdThresholdHistoryStatsSelect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnpdThresholdHistoryStatsSelect.setStatus("current")
_CnpdNotificationsConfig_ObjectIdentity = ObjectIdentity
cnpdNotificationsConfig = _CnpdNotificationsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 7)
)


class _CnpdNotificationsEnable_Type(TruthValue):
    """Custom type cnpdNotificationsEnable based on TruthValue"""


_CnpdNotificationsEnable_Object = MibScalar
cnpdNotificationsEnable = _CnpdNotificationsEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 7, 1),
    _CnpdNotificationsEnable_Type()
)
cnpdNotificationsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnpdNotificationsEnable.setStatus("current")
_CnpdSupportedProtocols_ObjectIdentity = ObjectIdentity
cnpdSupportedProtocols = _CnpdSupportedProtocols_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 8)
)
_CnpdSupportedProtocolsTable_Object = MibTable
cnpdSupportedProtocolsTable = _CnpdSupportedProtocolsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 8, 1)
)
if mibBuilder.loadTexts:
    cnpdSupportedProtocolsTable.setStatus("current")
_CnpdSupportedProtocolsEntry_Object = MibTableRow
cnpdSupportedProtocolsEntry = _CnpdSupportedProtocolsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 8, 1, 1)
)
cnpdSupportedProtocolsEntry.setIndexNames(
    (0, "CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdSupportedProtocolsIndex"),
)
if mibBuilder.loadTexts:
    cnpdSupportedProtocolsEntry.setStatus("current")


class _CnpdSupportedProtocolsIndex_Type(CiscoPdProtocolIndex):
    """Custom type cnpdSupportedProtocolsIndex based on CiscoPdProtocolIndex"""
    subtypeSpec = CiscoPdProtocolIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_CnpdSupportedProtocolsIndex_Type.__name__ = "CiscoPdProtocolIndex"
_CnpdSupportedProtocolsIndex_Object = MibTableColumn
cnpdSupportedProtocolsIndex = _CnpdSupportedProtocolsIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 8, 1, 1, 1),
    _CnpdSupportedProtocolsIndex_Type()
)
cnpdSupportedProtocolsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cnpdSupportedProtocolsIndex.setStatus("current")
_CnpdSupportedProtocolsName_Type = CiscoPdProtocolName
_CnpdSupportedProtocolsName_Object = MibTableColumn
cnpdSupportedProtocolsName = _CnpdSupportedProtocolsName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 8, 1, 1, 2),
    _CnpdSupportedProtocolsName_Type()
)
cnpdSupportedProtocolsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnpdSupportedProtocolsName.setStatus("current")
_CnpdMIBConformance_ObjectIdentity = ObjectIdentity
cnpdMIBConformance = _CnpdMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 244, 2)
)
_CnpdMIBCompliances_ObjectIdentity = ObjectIdentity
cnpdMIBCompliances = _CnpdMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 244, 2, 1)
)
_CnpdMIBGroups_ObjectIdentity = ObjectIdentity
cnpdMIBGroups = _CnpdMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 244, 2, 2)
)

# Managed Objects groups

cnpdStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 244, 2, 2, 1)
)
cnpdStatsGroup.setObjects(
      *(("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdStatusPdEnable"),
        ("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdStatusLastUpdateTime"),
        ("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdAllStatsProtocolName"),
        ("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdAllStatsInPkts"),
        ("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdAllStatsOutPkts"),
        ("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdAllStatsInBytes"),
        ("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdAllStatsOutBytes"),
        ("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdAllStatsHCInPkts"),
        ("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdAllStatsHCOutPkts"),
        ("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdAllStatsHCInBytes"),
        ("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdAllStatsHCOutBytes"),
        ("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdAllStatsInBitRate"),
        ("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdAllStatsOutBitRate"))
)
if mibBuilder.loadTexts:
    cnpdStatsGroup.setStatus("current")

cnpdTopNGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 244, 2, 2, 2)
)
cnpdTopNGroup.setObjects(
      *(("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdTopNConfigIfIndex"),
        ("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdTopNConfigStatsSelect"),
        ("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdTopNConfigRequestedSize"),
        ("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdTopNConfigSampleTime"),
        ("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdTopNConfigGrantedSize"),
        ("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdTopNConfigTime"),
        ("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdTopNConfigStatus"),
        ("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdTopNStatsProtocolName"),
        ("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdTopNStatsRate"),
        ("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdTopNStatsHCRate"))
)
if mibBuilder.loadTexts:
    cnpdTopNGroup.setStatus("current")

cnpdThresholdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 244, 2, 2, 3)
)
cnpdThresholdGroup.setObjects(
      *(("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdThresholdConfigIfIndex"),
        ("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdThresholdConfigInterval"),
        ("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdThresholdConfigSampleType"),
        ("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdThresholdConfigProtocol"),
        ("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdThresholdConfigStatsSelect"),
        ("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdThresholdConfigProtocolAny"),
        ("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdThresholdConfigStartup"),
        ("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdThresholdConfigRising"),
        ("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdThresholdConfigFalling"),
        ("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdThresholdConfigStatus"),
        ("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdThresholdHistoryConfigIndex"),
        ("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdThresholdHistoryValue"),
        ("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdThresholdHistoryType"),
        ("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdThresholdHistoryTime"),
        ("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdThresholdHistoryProtocol"),
        ("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdThresholdHistoryStatsSelect"))
)
if mibBuilder.loadTexts:
    cnpdThresholdGroup.setStatus("current")

cnpdMIBNotificationsConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 244, 2, 2, 5)
)
cnpdMIBNotificationsConfigGroup.setObjects(
    ("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdNotificationsEnable")
)
if mibBuilder.loadTexts:
    cnpdMIBNotificationsConfigGroup.setStatus("current")

cnpdSupportedProtocolsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 244, 2, 2, 6)
)
cnpdSupportedProtocolsGroup.setObjects(
    ("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdSupportedProtocolsName")
)
if mibBuilder.loadTexts:
    cnpdSupportedProtocolsGroup.setStatus("current")


# Notification objects

cnpdThresholdRisingEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 244, 0, 1)
)
cnpdThresholdRisingEvent.setObjects(
      *(("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdThresholdConfigIfIndex"),
        ("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdThresholdConfigStatsSelect"),
        ("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdThresholdHistoryValue"),
        ("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdThresholdConfigRising"),
        ("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdThresholdConfigProtocol"),
        ("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdThresholdHistoryTime"))
)
if mibBuilder.loadTexts:
    cnpdThresholdRisingEvent.setStatus(
        "current"
    )

cnpdThresholdFallingEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 244, 0, 2)
)
cnpdThresholdFallingEvent.setObjects(
      *(("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdThresholdConfigIfIndex"),
        ("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdThresholdConfigStatsSelect"),
        ("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdThresholdHistoryValue"),
        ("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdThresholdConfigFalling"),
        ("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdThresholdConfigProtocol"),
        ("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdThresholdHistoryTime"))
)
if mibBuilder.loadTexts:
    cnpdThresholdFallingEvent.setStatus(
        "current"
    )


# Notifications groups

cnpdMIBNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 244, 2, 2, 4)
)
cnpdMIBNotificationsGroup.setObjects(
      *(("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdThresholdRisingEvent"),
        ("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdThresholdFallingEvent"))
)
if mibBuilder.loadTexts:
    cnpdMIBNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cnpdMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 244, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cnpdMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-NBAR-PROTOCOL-DISCOVERY-MIB",
    **{"CiscoPdProtocolIndex": CiscoPdProtocolIndex,
       "CiscoPdProtocolName": CiscoPdProtocolName,
       "CiscoPdDataType": CiscoPdDataType,
       "ciscoNbarProtocolDiscoveryMIB": ciscoNbarProtocolDiscoveryMIB,
       "cnpdMIBNotifications": cnpdMIBNotifications,
       "cnpdThresholdRisingEvent": cnpdThresholdRisingEvent,
       "cnpdThresholdFallingEvent": cnpdThresholdFallingEvent,
       "cnpdMIBObjects": cnpdMIBObjects,
       "cnpdStatus": cnpdStatus,
       "cnpdStatusTable": cnpdStatusTable,
       "cnpdStatusEntry": cnpdStatusEntry,
       "cnpdStatusPdEnable": cnpdStatusPdEnable,
       "cnpdStatusLastUpdateTime": cnpdStatusLastUpdateTime,
       "cnpdAllStats": cnpdAllStats,
       "cnpdAllStatsTable": cnpdAllStatsTable,
       "cnpdAllStatsEntry": cnpdAllStatsEntry,
       "cnpdAllStatsProtocolsIndex": cnpdAllStatsProtocolsIndex,
       "cnpdAllStatsProtocolName": cnpdAllStatsProtocolName,
       "cnpdAllStatsInPkts": cnpdAllStatsInPkts,
       "cnpdAllStatsOutPkts": cnpdAllStatsOutPkts,
       "cnpdAllStatsInBytes": cnpdAllStatsInBytes,
       "cnpdAllStatsOutBytes": cnpdAllStatsOutBytes,
       "cnpdAllStatsHCInPkts": cnpdAllStatsHCInPkts,
       "cnpdAllStatsHCOutPkts": cnpdAllStatsHCOutPkts,
       "cnpdAllStatsHCInBytes": cnpdAllStatsHCInBytes,
       "cnpdAllStatsHCOutBytes": cnpdAllStatsHCOutBytes,
       "cnpdAllStatsInBitRate": cnpdAllStatsInBitRate,
       "cnpdAllStatsOutBitRate": cnpdAllStatsOutBitRate,
       "cnpdTopNConfig": cnpdTopNConfig,
       "cnpdTopNConfigTable": cnpdTopNConfigTable,
       "cnpdTopNConfigEntry": cnpdTopNConfigEntry,
       "cnpdTopNConfigIndex": cnpdTopNConfigIndex,
       "cnpdTopNConfigIfIndex": cnpdTopNConfigIfIndex,
       "cnpdTopNConfigStatsSelect": cnpdTopNConfigStatsSelect,
       "cnpdTopNConfigSampleTime": cnpdTopNConfigSampleTime,
       "cnpdTopNConfigRequestedSize": cnpdTopNConfigRequestedSize,
       "cnpdTopNConfigGrantedSize": cnpdTopNConfigGrantedSize,
       "cnpdTopNConfigTime": cnpdTopNConfigTime,
       "cnpdTopNConfigStatus": cnpdTopNConfigStatus,
       "cnpdTopNStats": cnpdTopNStats,
       "cnpdTopNStatsTable": cnpdTopNStatsTable,
       "cnpdTopNStatsEntry": cnpdTopNStatsEntry,
       "cnpdTopNStatsIndex": cnpdTopNStatsIndex,
       "cnpdTopNStatsProtocolName": cnpdTopNStatsProtocolName,
       "cnpdTopNStatsRate": cnpdTopNStatsRate,
       "cnpdTopNStatsHCRate": cnpdTopNStatsHCRate,
       "cnpdThresholdConfig": cnpdThresholdConfig,
       "cnpdThresholdConfigTable": cnpdThresholdConfigTable,
       "cnpdThresholdConfigEntry": cnpdThresholdConfigEntry,
       "cnpdThresholdConfigIndex": cnpdThresholdConfigIndex,
       "cnpdThresholdConfigIfIndex": cnpdThresholdConfigIfIndex,
       "cnpdThresholdConfigInterval": cnpdThresholdConfigInterval,
       "cnpdThresholdConfigSampleType": cnpdThresholdConfigSampleType,
       "cnpdThresholdConfigProtocol": cnpdThresholdConfigProtocol,
       "cnpdThresholdConfigProtocolAny": cnpdThresholdConfigProtocolAny,
       "cnpdThresholdConfigStatsSelect": cnpdThresholdConfigStatsSelect,
       "cnpdThresholdConfigStartup": cnpdThresholdConfigStartup,
       "cnpdThresholdConfigRising": cnpdThresholdConfigRising,
       "cnpdThresholdConfigFalling": cnpdThresholdConfigFalling,
       "cnpdThresholdConfigStatus": cnpdThresholdConfigStatus,
       "cnpdThresholdHistory": cnpdThresholdHistory,
       "cnpdThresholdHistoryTable": cnpdThresholdHistoryTable,
       "cnpdThresholdHistoryEntry": cnpdThresholdHistoryEntry,
       "cnpdThresholdHistoryIndex": cnpdThresholdHistoryIndex,
       "cnpdThresholdHistoryConfigIndex": cnpdThresholdHistoryConfigIndex,
       "cnpdThresholdHistoryValue": cnpdThresholdHistoryValue,
       "cnpdThresholdHistoryType": cnpdThresholdHistoryType,
       "cnpdThresholdHistoryTime": cnpdThresholdHistoryTime,
       "cnpdThresholdHistoryProtocol": cnpdThresholdHistoryProtocol,
       "cnpdThresholdHistoryStatsSelect": cnpdThresholdHistoryStatsSelect,
       "cnpdNotificationsConfig": cnpdNotificationsConfig,
       "cnpdNotificationsEnable": cnpdNotificationsEnable,
       "cnpdSupportedProtocols": cnpdSupportedProtocols,
       "cnpdSupportedProtocolsTable": cnpdSupportedProtocolsTable,
       "cnpdSupportedProtocolsEntry": cnpdSupportedProtocolsEntry,
       "cnpdSupportedProtocolsIndex": cnpdSupportedProtocolsIndex,
       "cnpdSupportedProtocolsName": cnpdSupportedProtocolsName,
       "cnpdMIBConformance": cnpdMIBConformance,
       "cnpdMIBCompliances": cnpdMIBCompliances,
       "cnpdMIBCompliance": cnpdMIBCompliance,
       "cnpdMIBGroups": cnpdMIBGroups,
       "cnpdStatsGroup": cnpdStatsGroup,
       "cnpdTopNGroup": cnpdTopNGroup,
       "cnpdThresholdGroup": cnpdThresholdGroup,
       "cnpdMIBNotificationsGroup": cnpdMIBNotificationsGroup,
       "cnpdMIBNotificationsConfigGroup": cnpdMIBNotificationsConfigGroup,
       "cnpdSupportedProtocolsGroup": cnpdSupportedProtocolsGroup}
)
