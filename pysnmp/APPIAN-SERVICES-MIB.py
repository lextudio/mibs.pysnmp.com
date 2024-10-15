# SNMP MIB module (APPIAN-SERVICES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/APPIAN-SERVICES-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:39:43 2024
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

(acChassisCurrentTime,
 acChassisRingId) = mibBuilder.importSymbols(
    "APPIAN-CHASSIS-MIB",
    "acChassisCurrentTime",
    "acChassisRingId")

(AcAdminStatus,
 AcNodeId,
 AcOpStatus,
 AcPortNumber,
 AcSlotNumber,
 acServices) = mibBuilder.importSymbols(
    "APPIAN-SMI-MIB",
    "AcAdminStatus",
    "AcNodeId",
    "AcOpStatus",
    "AcPortNumber",
    "AcSlotNumber",
    "acServices")

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
 MacAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

acServicesCommon = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2785, 2, 8, 1)
)
acServicesCommon.setRevisions(
        ("1900-01-31 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class AcQueueWeights(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )



class AcQueueBufferingCapacity(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )



class AcClassMapping(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



# MIB Managed Objects in the order of their OIDs

_AcServiceTraps_ObjectIdentity = ObjectIdentity
acServiceTraps = _AcServiceTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2785, 2, 8, 0)
)
_AcServiceTable_Object = MibTable
acServiceTable = _AcServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 8, 1, 1)
)
if mibBuilder.loadTexts:
    acServiceTable.setStatus("current")
_AcServiceEntry_Object = MibTableRow
acServiceEntry = _AcServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 8, 1, 1, 1)
)
acServiceEntry.setIndexNames(
    (0, "APPIAN-SERVICES-MIB", "acServiceNodeId"),
    (0, "APPIAN-SERVICES-MIB", "acServiceSlot"),
    (0, "APPIAN-SERVICES-MIB", "acServicePort"),
    (0, "APPIAN-SERVICES-MIB", "acServiceChannel"),
)
if mibBuilder.loadTexts:
    acServiceEntry.setStatus("current")
_AcServiceNodeId_Type = AcNodeId
_AcServiceNodeId_Object = MibTableColumn
acServiceNodeId = _AcServiceNodeId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 8, 1, 1, 1, 1),
    _AcServiceNodeId_Type()
)
acServiceNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acServiceNodeId.setStatus("current")
_AcServiceSlot_Type = AcSlotNumber
_AcServiceSlot_Object = MibTableColumn
acServiceSlot = _AcServiceSlot_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 8, 1, 1, 1, 2),
    _AcServiceSlot_Type()
)
acServiceSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acServiceSlot.setStatus("current")
_AcServicePort_Type = AcPortNumber
_AcServicePort_Object = MibTableColumn
acServicePort = _AcServicePort_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 8, 1, 1, 1, 3),
    _AcServicePort_Type()
)
acServicePort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acServicePort.setStatus("current")


class _AcServiceChannel_Type(Integer32):
    """Custom type acServiceChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AcServiceChannel_Type.__name__ = "Integer32"
_AcServiceChannel_Object = MibTableColumn
acServiceChannel = _AcServiceChannel_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 8, 1, 1, 1, 4),
    _AcServiceChannel_Type()
)
acServiceChannel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acServiceChannel.setStatus("current")
_AcServiceAdminStatus_Type = AcAdminStatus
_AcServiceAdminStatus_Object = MibTableColumn
acServiceAdminStatus = _AcServiceAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 8, 1, 1, 1, 5),
    _AcServiceAdminStatus_Type()
)
acServiceAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acServiceAdminStatus.setStatus("current")
_AcServiceOpStatus_Type = AcOpStatus
_AcServiceOpStatus_Object = MibTableColumn
acServiceOpStatus = _AcServiceOpStatus_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 8, 1, 1, 1, 6),
    _AcServiceOpStatus_Type()
)
acServiceOpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acServiceOpStatus.setStatus("current")


class _AcServiceType_Type(Integer32):
    """Custom type acServiceType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ias", 1),
          ("tls", 2),
          ("unknown", 0))
    )


_AcServiceType_Type.__name__ = "Integer32"
_AcServiceType_Object = MibTableColumn
acServiceType = _AcServiceType_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 8, 1, 1, 1, 7),
    _AcServiceType_Type()
)
acServiceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acServiceType.setStatus("current")


class _AcServiceVlanId_Type(Integer32):
    """Custom type acServiceVlanId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AcServiceVlanId_Type.__name__ = "Integer32"
_AcServiceVlanId_Object = MibTableColumn
acServiceVlanId = _AcServiceVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 8, 1, 1, 1, 8),
    _AcServiceVlanId_Type()
)
acServiceVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acServiceVlanId.setStatus("current")


class _AcServiceTrunkNumber_Type(Integer32):
    """Custom type acServiceTrunkNumber based on Integer32"""
    defaultValue = 0


_AcServiceTrunkNumber_Object = MibTableColumn
acServiceTrunkNumber = _AcServiceTrunkNumber_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 8, 1, 1, 1, 9),
    _AcServiceTrunkNumber_Type()
)
acServiceTrunkNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acServiceTrunkNumber.setStatus("current")


class _AcServiceQosTemplate_Type(Integer32):
    """Custom type acServiceQosTemplate based on Integer32"""
    defaultValue = 1


_AcServiceQosTemplate_Object = MibTableColumn
acServiceQosTemplate = _AcServiceQosTemplate_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 8, 1, 1, 1, 10),
    _AcServiceQosTemplate_Type()
)
acServiceQosTemplate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acServiceQosTemplate.setStatus("current")


class _AcServiceGBR_Type(Integer32):
    """Custom type acServiceGBR based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_AcServiceGBR_Type.__name__ = "Integer32"
_AcServiceGBR_Object = MibTableColumn
acServiceGBR = _AcServiceGBR_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 8, 1, 1, 1, 11),
    _AcServiceGBR_Type()
)
acServiceGBR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acServiceGBR.setStatus("current")


class _AcServiceMBR_Type(Integer32):
    """Custom type acServiceMBR based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000000),
    )


_AcServiceMBR_Type.__name__ = "Integer32"
_AcServiceMBR_Object = MibTableColumn
acServiceMBR = _AcServiceMBR_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 8, 1, 1, 1, 12),
    _AcServiceMBR_Type()
)
acServiceMBR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acServiceMBR.setStatus("current")
_AcServiceResetStats_Type = TruthValue
_AcServiceResetStats_Object = MibTableColumn
acServiceResetStats = _AcServiceResetStats_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 8, 1, 1, 1, 13),
    _AcServiceResetStats_Type()
)
acServiceResetStats.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acServiceResetStats.setStatus("current")


class _AcServiceUpstreamBuffCapWeight_Type(Unsigned32):
    """Custom type acServiceUpstreamBuffCapWeight based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_AcServiceUpstreamBuffCapWeight_Type.__name__ = "Unsigned32"
_AcServiceUpstreamBuffCapWeight_Object = MibTableColumn
acServiceUpstreamBuffCapWeight = _AcServiceUpstreamBuffCapWeight_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 8, 1, 1, 1, 14),
    _AcServiceUpstreamBuffCapWeight_Type()
)
acServiceUpstreamBuffCapWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acServiceUpstreamBuffCapWeight.setStatus("current")


class _AcServiceDownstreamBuffCapWeight_Type(Unsigned32):
    """Custom type acServiceDownstreamBuffCapWeight based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_AcServiceDownstreamBuffCapWeight_Type.__name__ = "Unsigned32"
_AcServiceDownstreamBuffCapWeight_Object = MibTableColumn
acServiceDownstreamBuffCapWeight = _AcServiceDownstreamBuffCapWeight_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 8, 1, 1, 1, 15),
    _AcServiceDownstreamBuffCapWeight_Type()
)
acServiceDownstreamBuffCapWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acServiceDownstreamBuffCapWeight.setStatus("current")


class _AcServiceLocalBuffCapWeight_Type(Unsigned32):
    """Custom type acServiceLocalBuffCapWeight based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_AcServiceLocalBuffCapWeight_Type.__name__ = "Unsigned32"
_AcServiceLocalBuffCapWeight_Object = MibTableColumn
acServiceLocalBuffCapWeight = _AcServiceLocalBuffCapWeight_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 8, 1, 1, 1, 16),
    _AcServiceLocalBuffCapWeight_Type()
)
acServiceLocalBuffCapWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acServiceLocalBuffCapWeight.setStatus("current")


class _AcServiceBufferPool_Type(Unsigned32):
    """Custom type acServiceBufferPool based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_AcServiceBufferPool_Type.__name__ = "Unsigned32"
_AcServiceBufferPool_Object = MibTableColumn
acServiceBufferPool = _AcServiceBufferPool_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 8, 1, 1, 1, 17),
    _AcServiceBufferPool_Type()
)
acServiceBufferPool.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acServiceBufferPool.setStatus("current")
_AcQosTable_Object = MibTable
acQosTable = _AcQosTable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 8, 1, 2)
)
if mibBuilder.loadTexts:
    acQosTable.setStatus("current")
_AcQosEntry_Object = MibTableRow
acQosEntry = _AcQosEntry_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 8, 1, 2, 1)
)
acQosEntry.setIndexNames(
    (0, "APPIAN-SERVICES-MIB", "acQosNodeId"),
    (0, "APPIAN-SERVICES-MIB", "acQosTemplateNumber"),
)
if mibBuilder.loadTexts:
    acQosEntry.setStatus("current")
_AcQosNodeId_Type = AcNodeId
_AcQosNodeId_Object = MibTableColumn
acQosNodeId = _AcQosNodeId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 8, 1, 2, 1, 1),
    _AcQosNodeId_Type()
)
acQosNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acQosNodeId.setStatus("current")
_AcQosTemplateNumber_Type = Integer32
_AcQosTemplateNumber_Object = MibTableColumn
acQosTemplateNumber = _AcQosTemplateNumber_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 8, 1, 2, 1, 2),
    _AcQosTemplateNumber_Type()
)
acQosTemplateNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acQosTemplateNumber.setStatus("current")
_AcQosAdminStatus_Type = AcAdminStatus
_AcQosAdminStatus_Object = MibTableColumn
acQosAdminStatus = _AcQosAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 8, 1, 2, 1, 3),
    _AcQosAdminStatus_Type()
)
acQosAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acQosAdminStatus.setStatus("current")


class _AcQosTemplateName_Type(DisplayString):
    """Custom type acQosTemplateName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AcQosTemplateName_Type.__name__ = "DisplayString"
_AcQosTemplateName_Object = MibTableColumn
acQosTemplateName = _AcQosTemplateName_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 8, 1, 2, 1, 4),
    _AcQosTemplateName_Type()
)
acQosTemplateName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acQosTemplateName.setStatus("current")
_AcQosQueueWeights_Type = AcQueueWeights
_AcQosQueueWeights_Object = MibTableColumn
acQosQueueWeights = _AcQosQueueWeights_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 8, 1, 2, 1, 5),
    _AcQosQueueWeights_Type()
)
acQosQueueWeights.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acQosQueueWeights.setStatus("current")


class _AcQosClassMapping_Type(Integer32):
    """Custom type acQosClassMapping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_AcQosClassMapping_Type.__name__ = "Integer32"
_AcQosClassMapping_Object = MibTableColumn
acQosClassMapping = _AcQosClassMapping_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 8, 1, 2, 1, 6),
    _AcQosClassMapping_Type()
)
acQosClassMapping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acQosClassMapping.setStatus("current")
_AcQosQueueBuffCaps_Type = AcQueueBufferingCapacity
_AcQosQueueBuffCaps_Object = MibTableColumn
acQosQueueBuffCaps = _AcQosQueueBuffCaps_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 8, 1, 2, 1, 7),
    _AcQosQueueBuffCaps_Type()
)
acQosQueueBuffCaps.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acQosQueueBuffCaps.setStatus("current")
_AcClassMapTable_Object = MibTable
acClassMapTable = _AcClassMapTable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 8, 1, 3)
)
if mibBuilder.loadTexts:
    acClassMapTable.setStatus("current")
_AcClassMapEntry_Object = MibTableRow
acClassMapEntry = _AcClassMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 8, 1, 3, 1)
)
acClassMapEntry.setIndexNames(
    (0, "APPIAN-SERVICES-MIB", "acClassMapNumber"),
)
if mibBuilder.loadTexts:
    acClassMapEntry.setStatus("current")


class _AcClassMapNumber_Type(Integer32):
    """Custom type acClassMapNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_AcClassMapNumber_Type.__name__ = "Integer32"
_AcClassMapNumber_Object = MibTableColumn
acClassMapNumber = _AcClassMapNumber_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 8, 1, 3, 1, 1),
    _AcClassMapNumber_Type()
)
acClassMapNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acClassMapNumber.setStatus("current")
_AcClassMapAdminStatus_Type = AcAdminStatus
_AcClassMapAdminStatus_Object = MibTableColumn
acClassMapAdminStatus = _AcClassMapAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 8, 1, 3, 1, 2),
    _AcClassMapAdminStatus_Type()
)
acClassMapAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acClassMapAdminStatus.setStatus("current")


class _AcClassMapName_Type(DisplayString):
    """Custom type acClassMapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AcClassMapName_Type.__name__ = "DisplayString"
_AcClassMapName_Object = MibTableColumn
acClassMapName = _AcClassMapName_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 8, 1, 3, 1, 3),
    _AcClassMapName_Type()
)
acClassMapName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acClassMapName.setStatus("current")


class _AcClassMapType_Type(Integer32):
    """Custom type acClassMapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dot1p", 3),
          ("iptos", 1),
          ("mpls", 2),
          ("unknown", 0))
    )


_AcClassMapType_Type.__name__ = "Integer32"
_AcClassMapType_Object = MibTableColumn
acClassMapType = _AcClassMapType_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 8, 1, 3, 1, 4),
    _AcClassMapType_Type()
)
acClassMapType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acClassMapType.setStatus("current")
_AcClassMapMapping_Type = AcClassMapping
_AcClassMapMapping_Object = MibTableColumn
acClassMapMapping = _AcClassMapMapping_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 8, 1, 3, 1, 5),
    _AcClassMapMapping_Type()
)
acClassMapMapping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acClassMapMapping.setStatus("current")
_AcServiceStatTable_Object = MibTable
acServiceStatTable = _AcServiceStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 8, 1, 4)
)
if mibBuilder.loadTexts:
    acServiceStatTable.setStatus("current")
_AcServiceStatEntry_Object = MibTableRow
acServiceStatEntry = _AcServiceStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 8, 1, 4, 1)
)
acServiceStatEntry.setIndexNames(
    (0, "APPIAN-SERVICES-MIB", "acServiceStatNodeId"),
    (0, "APPIAN-SERVICES-MIB", "acServiceStatSlot"),
    (0, "APPIAN-SERVICES-MIB", "acServiceStatPort"),
    (0, "APPIAN-SERVICES-MIB", "acServiceStatChannel"),
    (0, "APPIAN-SERVICES-MIB", "acServiceStatQueue"),
)
if mibBuilder.loadTexts:
    acServiceStatEntry.setStatus("current")
_AcServiceStatNodeId_Type = AcNodeId
_AcServiceStatNodeId_Object = MibTableColumn
acServiceStatNodeId = _AcServiceStatNodeId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 8, 1, 4, 1, 1),
    _AcServiceStatNodeId_Type()
)
acServiceStatNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acServiceStatNodeId.setStatus("current")
_AcServiceStatSlot_Type = AcSlotNumber
_AcServiceStatSlot_Object = MibTableColumn
acServiceStatSlot = _AcServiceStatSlot_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 8, 1, 4, 1, 2),
    _AcServiceStatSlot_Type()
)
acServiceStatSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acServiceStatSlot.setStatus("current")
_AcServiceStatPort_Type = AcPortNumber
_AcServiceStatPort_Object = MibTableColumn
acServiceStatPort = _AcServiceStatPort_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 8, 1, 4, 1, 3),
    _AcServiceStatPort_Type()
)
acServiceStatPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acServiceStatPort.setStatus("current")


class _AcServiceStatChannel_Type(Integer32):
    """Custom type acServiceStatChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_AcServiceStatChannel_Type.__name__ = "Integer32"
_AcServiceStatChannel_Object = MibTableColumn
acServiceStatChannel = _AcServiceStatChannel_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 8, 1, 4, 1, 4),
    _AcServiceStatChannel_Type()
)
acServiceStatChannel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acServiceStatChannel.setStatus("current")


class _AcServiceStatQueue_Type(Integer32):
    """Custom type acServiceStatQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_AcServiceStatQueue_Type.__name__ = "Integer32"
_AcServiceStatQueue_Object = MibTableColumn
acServiceStatQueue = _AcServiceStatQueue_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 8, 1, 4, 1, 5),
    _AcServiceStatQueue_Type()
)
acServiceStatQueue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acServiceStatQueue.setStatus("current")
_AcServiceStatUpstreamFrames_Type = Counter64
_AcServiceStatUpstreamFrames_Object = MibTableColumn
acServiceStatUpstreamFrames = _AcServiceStatUpstreamFrames_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 8, 1, 4, 1, 6),
    _AcServiceStatUpstreamFrames_Type()
)
acServiceStatUpstreamFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acServiceStatUpstreamFrames.setStatus("current")
_AcServiceStatUpstreamBytes_Type = Counter64
_AcServiceStatUpstreamBytes_Object = MibTableColumn
acServiceStatUpstreamBytes = _AcServiceStatUpstreamBytes_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 8, 1, 4, 1, 7),
    _AcServiceStatUpstreamBytes_Type()
)
acServiceStatUpstreamBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acServiceStatUpstreamBytes.setStatus("current")
_AcServiceStatUpstreamDroppedFrames_Type = Counter64
_AcServiceStatUpstreamDroppedFrames_Object = MibTableColumn
acServiceStatUpstreamDroppedFrames = _AcServiceStatUpstreamDroppedFrames_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 8, 1, 4, 1, 8),
    _AcServiceStatUpstreamDroppedFrames_Type()
)
acServiceStatUpstreamDroppedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acServiceStatUpstreamDroppedFrames.setStatus("current")
_AcServiceStatUpstreamDroppedBytes_Type = Counter64
_AcServiceStatUpstreamDroppedBytes_Object = MibTableColumn
acServiceStatUpstreamDroppedBytes = _AcServiceStatUpstreamDroppedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 8, 1, 4, 1, 9),
    _AcServiceStatUpstreamDroppedBytes_Type()
)
acServiceStatUpstreamDroppedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acServiceStatUpstreamDroppedBytes.setStatus("current")
_AcServiceStatUpstreamUnexpectedFrames_Type = Counter64
_AcServiceStatUpstreamUnexpectedFrames_Object = MibTableColumn
acServiceStatUpstreamUnexpectedFrames = _AcServiceStatUpstreamUnexpectedFrames_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 8, 1, 4, 1, 10),
    _AcServiceStatUpstreamUnexpectedFrames_Type()
)
acServiceStatUpstreamUnexpectedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acServiceStatUpstreamUnexpectedFrames.setStatus("current")
_AcServiceStatDownstreamFrames_Type = Counter64
_AcServiceStatDownstreamFrames_Object = MibTableColumn
acServiceStatDownstreamFrames = _AcServiceStatDownstreamFrames_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 8, 1, 4, 1, 11),
    _AcServiceStatDownstreamFrames_Type()
)
acServiceStatDownstreamFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acServiceStatDownstreamFrames.setStatus("current")
_AcServiceStatDownstreamBytes_Type = Counter64
_AcServiceStatDownstreamBytes_Object = MibTableColumn
acServiceStatDownstreamBytes = _AcServiceStatDownstreamBytes_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 8, 1, 4, 1, 12),
    _AcServiceStatDownstreamBytes_Type()
)
acServiceStatDownstreamBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acServiceStatDownstreamBytes.setStatus("current")
_AcServiceStatDownstreamDroppedFrames_Type = Counter64
_AcServiceStatDownstreamDroppedFrames_Object = MibTableColumn
acServiceStatDownstreamDroppedFrames = _AcServiceStatDownstreamDroppedFrames_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 8, 1, 4, 1, 13),
    _AcServiceStatDownstreamDroppedFrames_Type()
)
acServiceStatDownstreamDroppedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acServiceStatDownstreamDroppedFrames.setStatus("current")
_AcServiceStatDownstreamDroppedBytes_Type = Counter64
_AcServiceStatDownstreamDroppedBytes_Object = MibTableColumn
acServiceStatDownstreamDroppedBytes = _AcServiceStatDownstreamDroppedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 8, 1, 4, 1, 14),
    _AcServiceStatDownstreamDroppedBytes_Type()
)
acServiceStatDownstreamDroppedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acServiceStatDownstreamDroppedBytes.setStatus("current")
_AcServiceStatDownstreamUnexpectedFrames_Type = Counter64
_AcServiceStatDownstreamUnexpectedFrames_Object = MibTableColumn
acServiceStatDownstreamUnexpectedFrames = _AcServiceStatDownstreamUnexpectedFrames_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 8, 1, 4, 1, 15),
    _AcServiceStatDownstreamUnexpectedFrames_Type()
)
acServiceStatDownstreamUnexpectedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acServiceStatDownstreamUnexpectedFrames.setStatus("current")
_AcIas_ObjectIdentity = ObjectIdentity
acIas = _AcIas_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2785, 2, 8, 2)
)
_AcIasTable_Object = MibTable
acIasTable = _AcIasTable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 8, 2, 1)
)
if mibBuilder.loadTexts:
    acIasTable.setStatus("current")
_AcIasEntry_Object = MibTableRow
acIasEntry = _AcIasEntry_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 8, 2, 1, 1)
)
acIasEntry.setIndexNames(
    (0, "APPIAN-SERVICES-MIB", "acIasNodeId"),
    (0, "APPIAN-SERVICES-MIB", "acIasSlot"),
    (0, "APPIAN-SERVICES-MIB", "acIasPort"),
    (0, "APPIAN-SERVICES-MIB", "acIasChannel"),
)
if mibBuilder.loadTexts:
    acIasEntry.setStatus("current")
_AcIasNodeId_Type = AcNodeId
_AcIasNodeId_Object = MibTableColumn
acIasNodeId = _AcIasNodeId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 8, 2, 1, 1, 1),
    _AcIasNodeId_Type()
)
acIasNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acIasNodeId.setStatus("current")
_AcIasSlot_Type = AcSlotNumber
_AcIasSlot_Object = MibTableColumn
acIasSlot = _AcIasSlot_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 8, 2, 1, 1, 2),
    _AcIasSlot_Type()
)
acIasSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acIasSlot.setStatus("current")
_AcIasPort_Type = AcPortNumber
_AcIasPort_Object = MibTableColumn
acIasPort = _AcIasPort_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 8, 2, 1, 1, 3),
    _AcIasPort_Type()
)
acIasPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acIasPort.setStatus("current")


class _AcIasChannel_Type(Integer32):
    """Custom type acIasChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_AcIasChannel_Type.__name__ = "Integer32"
_AcIasChannel_Object = MibTableColumn
acIasChannel = _AcIasChannel_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 8, 2, 1, 1, 4),
    _AcIasChannel_Type()
)
acIasChannel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acIasChannel.setStatus("current")


class _AcIasDlci_Type(Integer32):
    """Custom type acIasDlci based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1022),
    )


_AcIasDlci_Type.__name__ = "Integer32"
_AcIasDlci_Object = MibTableColumn
acIasDlci = _AcIasDlci_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 8, 2, 1, 1, 5),
    _AcIasDlci_Type()
)
acIasDlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acIasDlci.setStatus("current")


class _AcIasRespondToArp_Type(TruthValue):
    """Custom type acIasRespondToArp based on TruthValue"""


_AcIasRespondToArp_Object = MibTableColumn
acIasRespondToArp = _AcIasRespondToArp_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 8, 2, 1, 1, 6),
    _AcIasRespondToArp_Type()
)
acIasRespondToArp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acIasRespondToArp.setStatus("current")
_AcIasRemoteIpAddress_Type = IpAddress
_AcIasRemoteIpAddress_Object = MibTableColumn
acIasRemoteIpAddress = _AcIasRemoteIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 8, 2, 1, 1, 7),
    _AcIasRemoteIpAddress_Type()
)
acIasRemoteIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acIasRemoteIpAddress.setStatus("current")
_AcIasCpeIpAddress_Type = IpAddress
_AcIasCpeIpAddress_Object = MibTableColumn
acIasCpeIpAddress = _AcIasCpeIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 8, 2, 1, 1, 8),
    _AcIasCpeIpAddress_Type()
)
acIasCpeIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acIasCpeIpAddress.setStatus("current")
_AcIasCpeMacAddress_Type = MacAddress
_AcIasCpeMacAddress_Object = MibTableColumn
acIasCpeMacAddress = _AcIasCpeMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 8, 2, 1, 1, 9),
    _AcIasCpeMacAddress_Type()
)
acIasCpeMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acIasCpeMacAddress.setStatus("current")


class _AcIasCpeEncapsMode_Type(Integer32):
    """Custom type acIasCpeEncapsMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enet", 2),
          ("learning", 1),
          ("snap", 3),
          ("unknown", 0))
    )


_AcIasCpeEncapsMode_Type.__name__ = "Integer32"
_AcIasCpeEncapsMode_Object = MibTableColumn
acIasCpeEncapsMode = _AcIasCpeEncapsMode_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 8, 2, 1, 1, 10),
    _AcIasCpeEncapsMode_Type()
)
acIasCpeEncapsMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acIasCpeEncapsMode.setStatus("current")


class _AcIasPerformInverseArp_Type(TruthValue):
    """Custom type acIasPerformInverseArp based on TruthValue"""


_AcIasPerformInverseArp_Object = MibTableColumn
acIasPerformInverseArp = _AcIasPerformInverseArp_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 8, 2, 1, 1, 11),
    _AcIasPerformInverseArp_Type()
)
acIasPerformInverseArp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acIasPerformInverseArp.setStatus("current")
_AcTls_ObjectIdentity = ObjectIdentity
acTls = _AcTls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2785, 2, 8, 3)
)
_AcTlsTable_Object = MibTable
acTlsTable = _AcTlsTable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 8, 3, 1)
)
if mibBuilder.loadTexts:
    acTlsTable.setStatus("current")
_AcTlsEntry_Object = MibTableRow
acTlsEntry = _AcTlsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 8, 3, 1, 1)
)
acTlsEntry.setIndexNames(
    (0, "APPIAN-SERVICES-MIB", "acTlsNodeId"),
    (0, "APPIAN-SERVICES-MIB", "acTlsSlot"),
    (0, "APPIAN-SERVICES-MIB", "acTlsPort"),
    (0, "APPIAN-SERVICES-MIB", "acTlsChannel"),
)
if mibBuilder.loadTexts:
    acTlsEntry.setStatus("current")
_AcTlsNodeId_Type = AcNodeId
_AcTlsNodeId_Object = MibTableColumn
acTlsNodeId = _AcTlsNodeId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 8, 3, 1, 1, 1),
    _AcTlsNodeId_Type()
)
acTlsNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acTlsNodeId.setStatus("current")
_AcTlsSlot_Type = AcSlotNumber
_AcTlsSlot_Object = MibTableColumn
acTlsSlot = _AcTlsSlot_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 8, 3, 1, 1, 2),
    _AcTlsSlot_Type()
)
acTlsSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acTlsSlot.setStatus("current")
_AcTlsPort_Type = AcPortNumber
_AcTlsPort_Object = MibTableColumn
acTlsPort = _AcTlsPort_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 8, 3, 1, 1, 3),
    _AcTlsPort_Type()
)
acTlsPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acTlsPort.setStatus("current")


class _AcTlsChannel_Type(Integer32):
    """Custom type acTlsChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_AcTlsChannel_Type.__name__ = "Integer32"
_AcTlsChannel_Object = MibTableColumn
acTlsChannel = _AcTlsChannel_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 8, 3, 1, 1, 4),
    _AcTlsChannel_Type()
)
acTlsChannel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acTlsChannel.setStatus("current")


class _AcTlsTlanId_Type(Integer32):
    """Custom type acTlsTlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 4095),
    )


_AcTlsTlanId_Type.__name__ = "Integer32"
_AcTlsTlanId_Object = MibTableColumn
acTlsTlanId = _AcTlsTlanId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 8, 3, 1, 1, 5),
    _AcTlsTlanId_Type()
)
acTlsTlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acTlsTlanId.setStatus("current")


class _AcTlsServiceId_Type(Integer32):
    """Custom type acTlsServiceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_AcTlsServiceId_Type.__name__ = "Integer32"
_AcTlsServiceId_Object = MibTableColumn
acTlsServiceId = _AcTlsServiceId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 8, 3, 1, 1, 6),
    _AcTlsServiceId_Type()
)
acTlsServiceId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acTlsServiceId.setStatus("current")


class _AcTlsPointToPointEnable_Type(TruthValue):
    """Custom type acTlsPointToPointEnable based on TruthValue"""


_AcTlsPointToPointEnable_Object = MibTableColumn
acTlsPointToPointEnable = _AcTlsPointToPointEnable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 8, 3, 1, 1, 7),
    _AcTlsPointToPointEnable_Type()
)
acTlsPointToPointEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acTlsPointToPointEnable.setStatus("current")


class _AcTlsServiceIdSharingEnable_Type(TruthValue):
    """Custom type acTlsServiceIdSharingEnable based on TruthValue"""


_AcTlsServiceIdSharingEnable_Object = MibTableColumn
acTlsServiceIdSharingEnable = _AcTlsServiceIdSharingEnable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 8, 3, 1, 1, 8),
    _AcTlsServiceIdSharingEnable_Type()
)
acTlsServiceIdSharingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acTlsServiceIdSharingEnable.setStatus("current")

# Managed Objects groups


# Notification objects

acServiceUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 8, 0, 1)
)
acServiceUpTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-SERVICES-MIB", "acServiceNodeId"),
        ("APPIAN-SERVICES-MIB", "acServiceSlot"),
        ("APPIAN-SERVICES-MIB", "acServicePort"),
        ("APPIAN-SERVICES-MIB", "acServiceChannel"),
        ("APPIAN-SERVICES-MIB", "acServiceType"))
)
if mibBuilder.loadTexts:
    acServiceUpTrap.setStatus(
        "current"
    )

acServiceDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 8, 0, 2)
)
acServiceDownTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-SERVICES-MIB", "acServiceNodeId"),
        ("APPIAN-SERVICES-MIB", "acServiceSlot"),
        ("APPIAN-SERVICES-MIB", "acServicePort"),
        ("APPIAN-SERVICES-MIB", "acServiceChannel"),
        ("APPIAN-SERVICES-MIB", "acServiceType"))
)
if mibBuilder.loadTexts:
    acServiceDownTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "APPIAN-SERVICES-MIB",
    **{"AcQueueWeights": AcQueueWeights,
       "AcQueueBufferingCapacity": AcQueueBufferingCapacity,
       "AcClassMapping": AcClassMapping,
       "acServiceTraps": acServiceTraps,
       "acServiceUpTrap": acServiceUpTrap,
       "acServiceDownTrap": acServiceDownTrap,
       "acServicesCommon": acServicesCommon,
       "acServiceTable": acServiceTable,
       "acServiceEntry": acServiceEntry,
       "acServiceNodeId": acServiceNodeId,
       "acServiceSlot": acServiceSlot,
       "acServicePort": acServicePort,
       "acServiceChannel": acServiceChannel,
       "acServiceAdminStatus": acServiceAdminStatus,
       "acServiceOpStatus": acServiceOpStatus,
       "acServiceType": acServiceType,
       "acServiceVlanId": acServiceVlanId,
       "acServiceTrunkNumber": acServiceTrunkNumber,
       "acServiceQosTemplate": acServiceQosTemplate,
       "acServiceGBR": acServiceGBR,
       "acServiceMBR": acServiceMBR,
       "acServiceResetStats": acServiceResetStats,
       "acServiceUpstreamBuffCapWeight": acServiceUpstreamBuffCapWeight,
       "acServiceDownstreamBuffCapWeight": acServiceDownstreamBuffCapWeight,
       "acServiceLocalBuffCapWeight": acServiceLocalBuffCapWeight,
       "acServiceBufferPool": acServiceBufferPool,
       "acQosTable": acQosTable,
       "acQosEntry": acQosEntry,
       "acQosNodeId": acQosNodeId,
       "acQosTemplateNumber": acQosTemplateNumber,
       "acQosAdminStatus": acQosAdminStatus,
       "acQosTemplateName": acQosTemplateName,
       "acQosQueueWeights": acQosQueueWeights,
       "acQosClassMapping": acQosClassMapping,
       "acQosQueueBuffCaps": acQosQueueBuffCaps,
       "acClassMapTable": acClassMapTable,
       "acClassMapEntry": acClassMapEntry,
       "acClassMapNumber": acClassMapNumber,
       "acClassMapAdminStatus": acClassMapAdminStatus,
       "acClassMapName": acClassMapName,
       "acClassMapType": acClassMapType,
       "acClassMapMapping": acClassMapMapping,
       "acServiceStatTable": acServiceStatTable,
       "acServiceStatEntry": acServiceStatEntry,
       "acServiceStatNodeId": acServiceStatNodeId,
       "acServiceStatSlot": acServiceStatSlot,
       "acServiceStatPort": acServiceStatPort,
       "acServiceStatChannel": acServiceStatChannel,
       "acServiceStatQueue": acServiceStatQueue,
       "acServiceStatUpstreamFrames": acServiceStatUpstreamFrames,
       "acServiceStatUpstreamBytes": acServiceStatUpstreamBytes,
       "acServiceStatUpstreamDroppedFrames": acServiceStatUpstreamDroppedFrames,
       "acServiceStatUpstreamDroppedBytes": acServiceStatUpstreamDroppedBytes,
       "acServiceStatUpstreamUnexpectedFrames": acServiceStatUpstreamUnexpectedFrames,
       "acServiceStatDownstreamFrames": acServiceStatDownstreamFrames,
       "acServiceStatDownstreamBytes": acServiceStatDownstreamBytes,
       "acServiceStatDownstreamDroppedFrames": acServiceStatDownstreamDroppedFrames,
       "acServiceStatDownstreamDroppedBytes": acServiceStatDownstreamDroppedBytes,
       "acServiceStatDownstreamUnexpectedFrames": acServiceStatDownstreamUnexpectedFrames,
       "acIas": acIas,
       "acIasTable": acIasTable,
       "acIasEntry": acIasEntry,
       "acIasNodeId": acIasNodeId,
       "acIasSlot": acIasSlot,
       "acIasPort": acIasPort,
       "acIasChannel": acIasChannel,
       "acIasDlci": acIasDlci,
       "acIasRespondToArp": acIasRespondToArp,
       "acIasRemoteIpAddress": acIasRemoteIpAddress,
       "acIasCpeIpAddress": acIasCpeIpAddress,
       "acIasCpeMacAddress": acIasCpeMacAddress,
       "acIasCpeEncapsMode": acIasCpeEncapsMode,
       "acIasPerformInverseArp": acIasPerformInverseArp,
       "acTls": acTls,
       "acTlsTable": acTlsTable,
       "acTlsEntry": acTlsEntry,
       "acTlsNodeId": acTlsNodeId,
       "acTlsSlot": acTlsSlot,
       "acTlsPort": acTlsPort,
       "acTlsChannel": acTlsChannel,
       "acTlsTlanId": acTlsTlanId,
       "acTlsServiceId": acTlsServiceId,
       "acTlsPointToPointEnable": acTlsPointToPointEnable,
       "acTlsServiceIdSharingEnable": acTlsServiceIdSharingEnable}
)
