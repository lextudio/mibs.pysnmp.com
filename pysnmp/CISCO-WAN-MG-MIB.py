# SNMP MIB module (CISCO-WAN-MG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-WAN-MG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:12:00 2024
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

(ciscoWan,) = mibBuilder.importSymbols(
    "CISCOWAN-SMI",
    "ciscoWan")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

ciscoWanMgMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 10)
)
ciscoWanMgMIB.setRevisions(
        ("2005-05-27 00:00",
         "2004-01-20 00:00",
         "2002-06-14 00:00",
         "2001-05-25 00:00",
         "2000-07-19 15:00",
         "2000-03-27 00:00",
         "1999-11-27 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoWanMgMIBObjects_ObjectIdentity = ObjectIdentity
ciscoWanMgMIBObjects = _CiscoWanMgMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 10, 1)
)
_MediaGateway_ObjectIdentity = ObjectIdentity
mediaGateway = _MediaGateway_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 10, 1, 1)
)


class _MgName_Type(SnmpAdminString):
    """Custom type mgName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_MgName_Type.__name__ = "SnmpAdminString"
_MgName_Object = MibScalar
mgName = _MgName_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 10, 1, 1, 1),
    _MgName_Type()
)
mgName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgName.setStatus("current")


class _MgAdministrativeState_Type(Integer32):
    """Custom type mgAdministrativeState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("commandedOutOfService", 2),
          ("inService", 1),
          ("pendingOutOfService", 3))
    )


_MgAdministrativeState_Type.__name__ = "Integer32"
_MgAdministrativeState_Object = MibScalar
mgAdministrativeState = _MgAdministrativeState_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 10, 1, 1, 2),
    _MgAdministrativeState_Type()
)
mgAdministrativeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgAdministrativeState.setStatus("current")


class _MgAdministrativeStateControl_Type(Integer32):
    """Custom type mgAdministrativeStateControl based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("forcefulOutOfService", 2),
          ("gracefulOutOfService", 3),
          ("inService", 1))
    )


_MgAdministrativeStateControl_Type.__name__ = "Integer32"
_MgAdministrativeStateControl_Object = MibScalar
mgAdministrativeStateControl = _MgAdministrativeStateControl_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 10, 1, 1, 3),
    _MgAdministrativeStateControl_Type()
)
mgAdministrativeStateControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgAdministrativeStateControl.setStatus("current")


class _MgShutdownGraceTime_Type(Integer32):
    """Custom type mgShutdownGraceTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_MgShutdownGraceTime_Type.__name__ = "Integer32"
_MgShutdownGraceTime_Object = MibScalar
mgShutdownGraceTime = _MgShutdownGraceTime_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 10, 1, 1, 4),
    _MgShutdownGraceTime_Type()
)
mgShutdownGraceTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgShutdownGraceTime.setStatus("current")
if mibBuilder.loadTexts:
    mgShutdownGraceTime.setUnits("seconds")
_MgSupportedProtocolTable_Object = MibTable
mgSupportedProtocolTable = _MgSupportedProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 10, 1, 1, 7)
)
if mibBuilder.loadTexts:
    mgSupportedProtocolTable.setStatus("current")
_MgSupportedProtocolEntry_Object = MibTableRow
mgSupportedProtocolEntry = _MgSupportedProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 10, 1, 1, 7, 1)
)
mgSupportedProtocolEntry.setIndexNames(
    (0, "CISCO-WAN-MG-MIB", "mgProtocolNumber"),
)
if mibBuilder.loadTexts:
    mgSupportedProtocolEntry.setStatus("current")


class _MgProtocolNumber_Type(Integer32):
    """Custom type mgProtocolNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MgProtocolNumber_Type.__name__ = "Integer32"
_MgProtocolNumber_Object = MibTableColumn
mgProtocolNumber = _MgProtocolNumber_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 10, 1, 1, 7, 1, 1),
    _MgProtocolNumber_Type()
)
mgProtocolNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgProtocolNumber.setStatus("current")


class _MgProtocolName_Type(SnmpAdminString):
    """Custom type mgProtocolName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_MgProtocolName_Type.__name__ = "SnmpAdminString"
_MgProtocolName_Object = MibTableColumn
mgProtocolName = _MgProtocolName_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 10, 1, 1, 7, 1, 2),
    _MgProtocolName_Type()
)
mgProtocolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgProtocolName.setStatus("current")
_MediaGatewayController_ObjectIdentity = ObjectIdentity
mediaGatewayController = _MediaGatewayController_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 10, 1, 2)
)
_MgcTable_Object = MibTable
mgcTable = _MgcTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 10, 1, 2, 1)
)
if mibBuilder.loadTexts:
    mgcTable.setStatus("current")
_MgcEntry_Object = MibTableRow
mgcEntry = _MgcEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 10, 1, 2, 1, 1)
)
mgcEntry.setIndexNames(
    (0, "CISCO-WAN-MG-MIB", "mgcNumber"),
)
if mibBuilder.loadTexts:
    mgcEntry.setStatus("current")


class _MgcNumber_Type(Integer32):
    """Custom type mgcNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MgcNumber_Type.__name__ = "Integer32"
_MgcNumber_Object = MibTableColumn
mgcNumber = _MgcNumber_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 10, 1, 2, 1, 1, 1),
    _MgcNumber_Type()
)
mgcNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgcNumber.setStatus("current")


class _MgcName_Type(SnmpAdminString):
    """Custom type mgcName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_MgcName_Type.__name__ = "SnmpAdminString"
_MgcName_Object = MibTableColumn
mgcName = _MgcName_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 10, 1, 2, 1, 1, 2),
    _MgcName_Type()
)
mgcName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mgcName.setStatus("current")


class _MgcDnsResolution_Type(TruthValue):
    """Custom type mgcDnsResolution based on TruthValue"""


_MgcDnsResolution_Object = MibTableColumn
mgcDnsResolution = _MgcDnsResolution_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 10, 1, 2, 1, 1, 3),
    _MgcDnsResolution_Type()
)
mgcDnsResolution.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgcDnsResolution.setStatus("deprecated")


class _MgcAssociationState_Type(Integer32):
    """Custom type mgcAssociationState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mgcAssociated", 2),
          ("mgcAssociatedCommLoss", 3),
          ("mgcUnassociated", 1))
    )


_MgcAssociationState_Type.__name__ = "Integer32"
_MgcAssociationState_Object = MibTableColumn
mgcAssociationState = _MgcAssociationState_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 10, 1, 2, 1, 1, 4),
    _MgcAssociationState_Type()
)
mgcAssociationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgcAssociationState.setStatus("deprecated")


class _MgcAssociationStateControl_Type(Integer32):
    """Custom type mgcAssociationStateControl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mgcAssociate", 2),
          ("mgcClear", 3),
          ("mgcUnassociate", 1))
    )


_MgcAssociationStateControl_Type.__name__ = "Integer32"
_MgcAssociationStateControl_Object = MibTableColumn
mgcAssociationStateControl = _MgcAssociationStateControl_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 10, 1, 2, 1, 1, 5),
    _MgcAssociationStateControl_Type()
)
mgcAssociationStateControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mgcAssociationStateControl.setStatus("deprecated")


class _MgcUnassociationPolicy_Type(Integer32):
    """Custom type mgcUnassociationPolicy based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mgcNoAction", 1),
          ("mgcRelease", 2))
    )


_MgcUnassociationPolicy_Type.__name__ = "Integer32"
_MgcUnassociationPolicy_Object = MibTableColumn
mgcUnassociationPolicy = _MgcUnassociationPolicy_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 10, 1, 2, 1, 1, 6),
    _MgcUnassociationPolicy_Type()
)
mgcUnassociationPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mgcUnassociationPolicy.setStatus("deprecated")


class _MgcCommLossUnassociationTimeout_Type(Integer32):
    """Custom type mgcCommLossUnassociationTimeout based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_MgcCommLossUnassociationTimeout_Type.__name__ = "Integer32"
_MgcCommLossUnassociationTimeout_Object = MibTableColumn
mgcCommLossUnassociationTimeout = _MgcCommLossUnassociationTimeout_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 10, 1, 2, 1, 1, 7),
    _MgcCommLossUnassociationTimeout_Type()
)
mgcCommLossUnassociationTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mgcCommLossUnassociationTimeout.setStatus("deprecated")
if mibBuilder.loadTexts:
    mgcCommLossUnassociationTimeout.setUnits("seconds")
_MgcRowStatus_Type = RowStatus
_MgcRowStatus_Object = MibTableColumn
mgcRowStatus = _MgcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 10, 1, 2, 1, 1, 8),
    _MgcRowStatus_Type()
)
mgcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mgcRowStatus.setStatus("current")
_MgcProtocolTable_Object = MibTable
mgcProtocolTable = _MgcProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 10, 1, 2, 2)
)
if mibBuilder.loadTexts:
    mgcProtocolTable.setStatus("deprecated")
_MgcProtocolEntry_Object = MibTableRow
mgcProtocolEntry = _MgcProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 10, 1, 2, 2, 1)
)
mgcProtocolEntry.setIndexNames(
    (0, "CISCO-WAN-MG-MIB", "mgcNumber"),
    (0, "CISCO-WAN-MG-MIB", "mgProtocolNumber"),
)
if mibBuilder.loadTexts:
    mgcProtocolEntry.setStatus("deprecated")
_MgcProtocolRowStatus_Type = RowStatus
_MgcProtocolRowStatus_Object = MibTableColumn
mgcProtocolRowStatus = _MgcProtocolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 10, 1, 2, 2, 1, 1),
    _MgcProtocolRowStatus_Type()
)
mgcProtocolRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mgcProtocolRowStatus.setStatus("deprecated")


class _MaxConcurrentMgcs_Type(Unsigned32):
    """Custom type maxConcurrentMgcs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MaxConcurrentMgcs_Type.__name__ = "Unsigned32"
_MaxConcurrentMgcs_Object = MibScalar
maxConcurrentMgcs = _MaxConcurrentMgcs_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 10, 1, 2, 3),
    _MaxConcurrentMgcs_Type()
)
maxConcurrentMgcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxConcurrentMgcs.setStatus("current")
if mibBuilder.loadTexts:
    maxConcurrentMgcs.setUnits("controllers")
_MediaGatewayEndpoint_ObjectIdentity = ObjectIdentity
mediaGatewayEndpoint = _MediaGatewayEndpoint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 10, 1, 3)
)
_MgEndpointTable_Object = MibTable
mgEndpointTable = _MgEndpointTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 10, 1, 3, 1)
)
if mibBuilder.loadTexts:
    mgEndpointTable.setStatus("current")
_MgEndpointEntry_Object = MibTableRow
mgEndpointEntry = _MgEndpointEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 10, 1, 3, 1, 1)
)
mgEndpointEntry.setIndexNames(
    (0, "CISCO-WAN-MG-MIB", "mgEndpointNumber"),
)
if mibBuilder.loadTexts:
    mgEndpointEntry.setStatus("current")


class _MgEndpointNumber_Type(Integer32):
    """Custom type mgEndpointNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MgEndpointNumber_Type.__name__ = "Integer32"
_MgEndpointNumber_Object = MibTableColumn
mgEndpointNumber = _MgEndpointNumber_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 10, 1, 3, 1, 1, 1),
    _MgEndpointNumber_Type()
)
mgEndpointNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgEndpointNumber.setStatus("current")


class _MgEndpointLineNumber_Type(Integer32):
    """Custom type mgEndpointLineNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MgEndpointLineNumber_Type.__name__ = "Integer32"
_MgEndpointLineNumber_Object = MibTableColumn
mgEndpointLineNumber = _MgEndpointLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 10, 1, 3, 1, 1, 2),
    _MgEndpointLineNumber_Type()
)
mgEndpointLineNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mgEndpointLineNumber.setStatus("current")
_MgEndpointName_Type = SnmpAdminString
_MgEndpointName_Object = MibTableColumn
mgEndpointName = _MgEndpointName_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 10, 1, 3, 1, 1, 3),
    _MgEndpointName_Type()
)
mgEndpointName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mgEndpointName.setStatus("current")


class _MgEndpointSpeed_Type(Unsigned32):
    """Custom type mgEndpointSpeed based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MgEndpointSpeed_Type.__name__ = "Unsigned32"
_MgEndpointSpeed_Object = MibTableColumn
mgEndpointSpeed = _MgEndpointSpeed_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 10, 1, 3, 1, 1, 4),
    _MgEndpointSpeed_Type()
)
mgEndpointSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgEndpointSpeed.setStatus("current")
if mibBuilder.loadTexts:
    mgEndpointSpeed.setUnits("Kbps")


class _MgEndpointState_Type(Integer32):
    """Custom type mgEndpointState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mgEndpointActive", 1),
          ("mgEndpointDegraded", 3),
          ("mgEndpointFailed", 2))
    )


_MgEndpointState_Type.__name__ = "Integer32"
_MgEndpointState_Object = MibTableColumn
mgEndpointState = _MgEndpointState_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 10, 1, 3, 1, 1, 5),
    _MgEndpointState_Type()
)
mgEndpointState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgEndpointState.setStatus("current")


class _MgEndpointChannelMap_Type(Integer32):
    """Custom type mgEndpointChannelMap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MgEndpointChannelMap_Type.__name__ = "Integer32"
_MgEndpointChannelMap_Object = MibTableColumn
mgEndpointChannelMap = _MgEndpointChannelMap_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 10, 1, 3, 1, 1, 6),
    _MgEndpointChannelMap_Type()
)
mgEndpointChannelMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mgEndpointChannelMap.setStatus("current")
_MgEndpointRowStatus_Type = RowStatus
_MgEndpointRowStatus_Object = MibTableColumn
mgEndpointRowStatus = _MgEndpointRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 10, 1, 3, 1, 1, 7),
    _MgEndpointRowStatus_Type()
)
mgEndpointRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mgEndpointRowStatus.setStatus("current")


class _MgEndpointCreationPolicy_Type(Integer32):
    """Custom type mgEndpointCreationPolicy based on Integer32"""
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
        *(("dynamic", 1),
          ("static", 3),
          ("strictDynamic", 2))
    )


_MgEndpointCreationPolicy_Type.__name__ = "Integer32"
_MgEndpointCreationPolicy_Object = MibScalar
mgEndpointCreationPolicy = _MgEndpointCreationPolicy_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 10, 1, 3, 2),
    _MgEndpointCreationPolicy_Type()
)
mgEndpointCreationPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgEndpointCreationPolicy.setStatus("current")
_MgEndpointExtTable_Object = MibTable
mgEndpointExtTable = _MgEndpointExtTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 10, 1, 3, 3)
)
if mibBuilder.loadTexts:
    mgEndpointExtTable.setStatus("current")
_MgEndpointExtEntry_Object = MibTableRow
mgEndpointExtEntry = _MgEndpointExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 10, 1, 3, 3, 1)
)
if mibBuilder.loadTexts:
    mgEndpointExtEntry.setStatus("current")


class _MgEndpointRepetition_Type(Unsigned32):
    """Custom type mgEndpointRepetition based on Unsigned32"""
    defaultValue = 1


_MgEndpointRepetition_Object = MibTableColumn
mgEndpointRepetition = _MgEndpointRepetition_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 10, 1, 3, 3, 1, 1),
    _MgEndpointRepetition_Type()
)
mgEndpointRepetition.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mgEndpointRepetition.setStatus("current")
_MediaGatewayLine_ObjectIdentity = ObjectIdentity
mediaGatewayLine = _MediaGatewayLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 10, 1, 4)
)
_LineAssignmentTable_Object = MibTable
lineAssignmentTable = _LineAssignmentTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 10, 1, 4, 1)
)
if mibBuilder.loadTexts:
    lineAssignmentTable.setStatus("current")
_LineAssignmentEntry_Object = MibTableRow
lineAssignmentEntry = _LineAssignmentEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 10, 1, 4, 1, 1)
)
lineAssignmentEntry.setIndexNames(
    (0, "CISCO-WAN-MG-MIB", "lineNumber"),
)
if mibBuilder.loadTexts:
    lineAssignmentEntry.setStatus("current")


class _LineNumber_Type(Integer32):
    """Custom type lineNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_LineNumber_Type.__name__ = "Integer32"
_LineNumber_Object = MibTableColumn
lineNumber = _LineNumber_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 10, 1, 4, 1, 1, 1),
    _LineNumber_Type()
)
lineNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lineNumber.setStatus("current")


class _ChannelAssignment_Type(Integer32):
    """Custom type channelAssignment based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ChannelAssignment_Type.__name__ = "Integer32"
_ChannelAssignment_Object = MibTableColumn
channelAssignment = _ChannelAssignment_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 10, 1, 4, 1, 1, 2),
    _ChannelAssignment_Type()
)
channelAssignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelAssignment.setStatus("current")


class _LineName_Type(SnmpAdminString):
    """Custom type lineName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_LineName_Type.__name__ = "SnmpAdminString"
_LineName_Object = MibTableColumn
lineName = _LineName_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 10, 1, 4, 1, 1, 3),
    _LineName_Type()
)
lineName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lineName.setStatus("current")
_MediaGatewayControllerResolution_ObjectIdentity = ObjectIdentity
mediaGatewayControllerResolution = _MediaGatewayControllerResolution_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 10, 1, 5)
)
_MgcResolutionTable_Object = MibTable
mgcResolutionTable = _MgcResolutionTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 10, 1, 5, 1)
)
if mibBuilder.loadTexts:
    mgcResolutionTable.setStatus("current")
_MgcResolutionEntry_Object = MibTableRow
mgcResolutionEntry = _MgcResolutionEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 10, 1, 5, 1, 1)
)
mgcResolutionEntry.setIndexNames(
    (0, "CISCO-WAN-MG-MIB", "mgcResolutionIndex"),
)
if mibBuilder.loadTexts:
    mgcResolutionEntry.setStatus("current")


class _MgcResolutionIndex_Type(Integer32):
    """Custom type mgcResolutionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MgcResolutionIndex_Type.__name__ = "Integer32"
_MgcResolutionIndex_Object = MibTableColumn
mgcResolutionIndex = _MgcResolutionIndex_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 10, 1, 5, 1, 1, 1),
    _MgcResolutionIndex_Type()
)
mgcResolutionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgcResolutionIndex.setStatus("current")


class _MgcResolutionName_Type(SnmpAdminString):
    """Custom type mgcResolutionName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_MgcResolutionName_Type.__name__ = "SnmpAdminString"
_MgcResolutionName_Object = MibTableColumn
mgcResolutionName = _MgcResolutionName_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 10, 1, 5, 1, 1, 2),
    _MgcResolutionName_Type()
)
mgcResolutionName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mgcResolutionName.setStatus("current")
_MgcResolutionIpAddress_Type = IpAddress
_MgcResolutionIpAddress_Object = MibTableColumn
mgcResolutionIpAddress = _MgcResolutionIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 10, 1, 5, 1, 1, 3),
    _MgcResolutionIpAddress_Type()
)
mgcResolutionIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mgcResolutionIpAddress.setStatus("current")


class _MgcResolutionCommState_Type(Integer32):
    """Custom type mgcResolutionCommState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("csActive", 1),
          ("csInactive", 2))
    )


_MgcResolutionCommState_Type.__name__ = "Integer32"
_MgcResolutionCommState_Object = MibTableColumn
mgcResolutionCommState = _MgcResolutionCommState_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 10, 1, 5, 1, 1, 4),
    _MgcResolutionCommState_Type()
)
mgcResolutionCommState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgcResolutionCommState.setStatus("current")


class _MgcResolutionPreference_Type(Integer32):
    """Custom type mgcResolutionPreference based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MgcResolutionPreference_Type.__name__ = "Integer32"
_MgcResolutionPreference_Object = MibTableColumn
mgcResolutionPreference = _MgcResolutionPreference_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 10, 1, 5, 1, 1, 5),
    _MgcResolutionPreference_Type()
)
mgcResolutionPreference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mgcResolutionPreference.setStatus("current")
_MgcResolutionRowStatus_Type = RowStatus
_MgcResolutionRowStatus_Object = MibTableColumn
mgcResolutionRowStatus = _MgcResolutionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 10, 1, 5, 1, 1, 6),
    _MgcResolutionRowStatus_Type()
)
mgcResolutionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mgcResolutionRowStatus.setStatus("current")


class _MgcDnsResolutionFlag_Type(Integer32):
    """Custom type mgcDnsResolutionFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("external", 2),
          ("internal", 1))
    )


_MgcDnsResolutionFlag_Type.__name__ = "Integer32"
_MgcDnsResolutionFlag_Object = MibTableColumn
mgcDnsResolutionFlag = _MgcDnsResolutionFlag_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 10, 1, 5, 1, 1, 7),
    _MgcDnsResolutionFlag_Type()
)
mgcDnsResolutionFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgcDnsResolutionFlag.setStatus("current")
_MediaGatewayDomainName_ObjectIdentity = ObjectIdentity
mediaGatewayDomainName = _MediaGatewayDomainName_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 10, 1, 6)
)
_MgDomainNameTable_Object = MibTable
mgDomainNameTable = _MgDomainNameTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 10, 1, 6, 1)
)
if mibBuilder.loadTexts:
    mgDomainNameTable.setStatus("current")
_MgDomainNameEntry_Object = MibTableRow
mgDomainNameEntry = _MgDomainNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 10, 1, 6, 1, 1)
)
mgDomainNameEntry.setIndexNames(
    (0, "CISCO-WAN-MG-MIB", "mgDomainNameIndex"),
)
if mibBuilder.loadTexts:
    mgDomainNameEntry.setStatus("current")


class _MgDomainNameIndex_Type(Integer32):
    """Custom type mgDomainNameIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MgDomainNameIndex_Type.__name__ = "Integer32"
_MgDomainNameIndex_Object = MibTableColumn
mgDomainNameIndex = _MgDomainNameIndex_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 10, 1, 6, 1, 1, 1),
    _MgDomainNameIndex_Type()
)
mgDomainNameIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgDomainNameIndex.setStatus("current")


class _MgDomainName_Type(SnmpAdminString):
    """Custom type mgDomainName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_MgDomainName_Type.__name__ = "SnmpAdminString"
_MgDomainName_Object = MibTableColumn
mgDomainName = _MgDomainName_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 10, 1, 6, 1, 1, 2),
    _MgDomainName_Type()
)
mgDomainName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mgDomainName.setStatus("current")


class _MgDnsResolutionType_Type(Integer32):
    """Custom type mgDnsResolutionType based on Integer32"""
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
        *(("externalFirst", 4),
          ("externalOnly", 2),
          ("internalFirst", 3),
          ("internalOnly", 1))
    )


_MgDnsResolutionType_Type.__name__ = "Integer32"
_MgDnsResolutionType_Object = MibTableColumn
mgDnsResolutionType = _MgDnsResolutionType_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 10, 1, 6, 1, 1, 3),
    _MgDnsResolutionType_Type()
)
mgDnsResolutionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mgDnsResolutionType.setStatus("current")
_MgDomainNameRowStatus_Type = RowStatus
_MgDomainNameRowStatus_Object = MibTableColumn
mgDomainNameRowStatus = _MgDomainNameRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 10, 1, 6, 1, 1, 4),
    _MgDomainNameRowStatus_Type()
)
mgDomainNameRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mgDomainNameRowStatus.setStatus("current")
_MgMIBConformance_ObjectIdentity = ObjectIdentity
mgMIBConformance = _MgMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 10, 3)
)
_MgMIBCompliances_ObjectIdentity = ObjectIdentity
mgMIBCompliances = _MgMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 10, 3, 1)
)
_MgMIBGroups_ObjectIdentity = ObjectIdentity
mgMIBGroups = _MgMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 10, 3, 2)
)
mgEndpointEntry.registerAugmentions(
    ("CISCO-WAN-MG-MIB",
     "mgEndpointExtEntry")
)
mgEndpointExtEntry.setIndexNames(*mgEndpointEntry.getIndexNames())

# Managed Objects groups

mediaGatewayGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 10, 3, 2, 1)
)
mediaGatewayGroup.setObjects(
      *(("CISCO-WAN-MG-MIB", "mgName"),
        ("CISCO-WAN-MG-MIB", "mgAdministrativeState"),
        ("CISCO-WAN-MG-MIB", "mgAdministrativeStateControl"),
        ("CISCO-WAN-MG-MIB", "mgShutdownGraceTime"),
        ("CISCO-WAN-MG-MIB", "mgProtocolName"))
)
if mibBuilder.loadTexts:
    mediaGatewayGroup.setStatus("current")

mediaGatewayControllerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 10, 3, 2, 2)
)
mediaGatewayControllerGroup.setObjects(
      *(("CISCO-WAN-MG-MIB", "maxConcurrentMgcs"),
        ("CISCO-WAN-MG-MIB", "mgcName"),
        ("CISCO-WAN-MG-MIB", "mgcDnsResolution"),
        ("CISCO-WAN-MG-MIB", "mgcAssociationState"),
        ("CISCO-WAN-MG-MIB", "mgcAssociationStateControl"),
        ("CISCO-WAN-MG-MIB", "mgcUnassociationPolicy"),
        ("CISCO-WAN-MG-MIB", "mgcCommLossUnassociationTimeout"),
        ("CISCO-WAN-MG-MIB", "mgcRowStatus"),
        ("CISCO-WAN-MG-MIB", "mgcProtocolRowStatus"))
)
if mibBuilder.loadTexts:
    mediaGatewayControllerGroup.setStatus("deprecated")

mediaGatewayEndpointGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 10, 3, 2, 3)
)
mediaGatewayEndpointGroup.setObjects(
      *(("CISCO-WAN-MG-MIB", "mgEndpointCreationPolicy"),
        ("CISCO-WAN-MG-MIB", "mgEndpointName"),
        ("CISCO-WAN-MG-MIB", "mgEndpointLineNumber"),
        ("CISCO-WAN-MG-MIB", "mgEndpointSpeed"),
        ("CISCO-WAN-MG-MIB", "mgEndpointState"),
        ("CISCO-WAN-MG-MIB", "mgEndpointChannelMap"),
        ("CISCO-WAN-MG-MIB", "mgEndpointRowStatus"))
)
if mibBuilder.loadTexts:
    mediaGatewayEndpointGroup.setStatus("current")

mediaGatewayLineGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 10, 3, 2, 4)
)
mediaGatewayLineGroup.setObjects(
      *(("CISCO-WAN-MG-MIB", "channelAssignment"),
        ("CISCO-WAN-MG-MIB", "lineName"))
)
if mibBuilder.loadTexts:
    mediaGatewayLineGroup.setStatus("current")

mediaGatewayControllerResolutionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 10, 3, 2, 5)
)
mediaGatewayControllerResolutionGroup.setObjects(
      *(("CISCO-WAN-MG-MIB", "mgcResolutionName"),
        ("CISCO-WAN-MG-MIB", "mgcResolutionIpAddress"),
        ("CISCO-WAN-MG-MIB", "mgcResolutionCommState"),
        ("CISCO-WAN-MG-MIB", "mgcResolutionPreference"),
        ("CISCO-WAN-MG-MIB", "mgcResolutionRowStatus"))
)
if mibBuilder.loadTexts:
    mediaGatewayControllerResolutionGroup.setStatus("deprecated")

mediaGatewayControllerGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 10, 3, 2, 6)
)
mediaGatewayControllerGroup1.setObjects(
      *(("CISCO-WAN-MG-MIB", "maxConcurrentMgcs"),
        ("CISCO-WAN-MG-MIB", "mgcName"),
        ("CISCO-WAN-MG-MIB", "mgcAssociationState"),
        ("CISCO-WAN-MG-MIB", "mgcAssociationStateControl"),
        ("CISCO-WAN-MG-MIB", "mgcUnassociationPolicy"),
        ("CISCO-WAN-MG-MIB", "mgcCommLossUnassociationTimeout"),
        ("CISCO-WAN-MG-MIB", "mgcRowStatus"),
        ("CISCO-WAN-MG-MIB", "mgcProtocolRowStatus"))
)
if mibBuilder.loadTexts:
    mediaGatewayControllerGroup1.setStatus("deprecated")

mediaGatewayControllerResolutionGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 10, 3, 2, 7)
)
mediaGatewayControllerResolutionGroup1.setObjects(
      *(("CISCO-WAN-MG-MIB", "mgcResolutionName"),
        ("CISCO-WAN-MG-MIB", "mgcResolutionIpAddress"),
        ("CISCO-WAN-MG-MIB", "mgcResolutionCommState"),
        ("CISCO-WAN-MG-MIB", "mgcResolutionPreference"),
        ("CISCO-WAN-MG-MIB", "mgcResolutionRowStatus"),
        ("CISCO-WAN-MG-MIB", "mgcDnsResolutionFlag"))
)
if mibBuilder.loadTexts:
    mediaGatewayControllerResolutionGroup1.setStatus("current")

mediaGatewayDomainNameGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 10, 3, 2, 8)
)
mediaGatewayDomainNameGroup.setObjects(
      *(("CISCO-WAN-MG-MIB", "mgDomainName"),
        ("CISCO-WAN-MG-MIB", "mgDnsResolutionType"),
        ("CISCO-WAN-MG-MIB", "mgDomainNameRowStatus"))
)
if mibBuilder.loadTexts:
    mediaGatewayDomainNameGroup.setStatus("current")

mediaGatewayControllerGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 10, 3, 2, 9)
)
mediaGatewayControllerGroup2.setObjects(
      *(("CISCO-WAN-MG-MIB", "maxConcurrentMgcs"),
        ("CISCO-WAN-MG-MIB", "mgcName"),
        ("CISCO-WAN-MG-MIB", "mgcRowStatus"))
)
if mibBuilder.loadTexts:
    mediaGatewayControllerGroup2.setStatus("current")

mediaGatewayEndptRepetitionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 10, 3, 2, 10)
)
mediaGatewayEndptRepetitionGroup.setObjects(
    ("CISCO-WAN-MG-MIB", "mgEndpointRepetition")
)
if mibBuilder.loadTexts:
    mediaGatewayEndptRepetitionGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

mgMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 351, 150, 10, 3, 1, 1)
)
if mibBuilder.loadTexts:
    mgMIBCompliance.setStatus(
        "deprecated"
    )

mgMIBCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 351, 150, 10, 3, 1, 2)
)
if mibBuilder.loadTexts:
    mgMIBCompliance1.setStatus(
        "deprecated"
    )

mgMIBCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 351, 150, 10, 3, 1, 3)
)
if mibBuilder.loadTexts:
    mgMIBCompliance2.setStatus(
        "deprecated"
    )

mgMIBCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 351, 150, 10, 3, 1, 4)
)
if mibBuilder.loadTexts:
    mgMIBCompliance3.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-WAN-MG-MIB",
    **{"ciscoWanMgMIB": ciscoWanMgMIB,
       "ciscoWanMgMIBObjects": ciscoWanMgMIBObjects,
       "mediaGateway": mediaGateway,
       "mgName": mgName,
       "mgAdministrativeState": mgAdministrativeState,
       "mgAdministrativeStateControl": mgAdministrativeStateControl,
       "mgShutdownGraceTime": mgShutdownGraceTime,
       "mgSupportedProtocolTable": mgSupportedProtocolTable,
       "mgSupportedProtocolEntry": mgSupportedProtocolEntry,
       "mgProtocolNumber": mgProtocolNumber,
       "mgProtocolName": mgProtocolName,
       "mediaGatewayController": mediaGatewayController,
       "mgcTable": mgcTable,
       "mgcEntry": mgcEntry,
       "mgcNumber": mgcNumber,
       "mgcName": mgcName,
       "mgcDnsResolution": mgcDnsResolution,
       "mgcAssociationState": mgcAssociationState,
       "mgcAssociationStateControl": mgcAssociationStateControl,
       "mgcUnassociationPolicy": mgcUnassociationPolicy,
       "mgcCommLossUnassociationTimeout": mgcCommLossUnassociationTimeout,
       "mgcRowStatus": mgcRowStatus,
       "mgcProtocolTable": mgcProtocolTable,
       "mgcProtocolEntry": mgcProtocolEntry,
       "mgcProtocolRowStatus": mgcProtocolRowStatus,
       "maxConcurrentMgcs": maxConcurrentMgcs,
       "mediaGatewayEndpoint": mediaGatewayEndpoint,
       "mgEndpointTable": mgEndpointTable,
       "mgEndpointEntry": mgEndpointEntry,
       "mgEndpointNumber": mgEndpointNumber,
       "mgEndpointLineNumber": mgEndpointLineNumber,
       "mgEndpointName": mgEndpointName,
       "mgEndpointSpeed": mgEndpointSpeed,
       "mgEndpointState": mgEndpointState,
       "mgEndpointChannelMap": mgEndpointChannelMap,
       "mgEndpointRowStatus": mgEndpointRowStatus,
       "mgEndpointCreationPolicy": mgEndpointCreationPolicy,
       "mgEndpointExtTable": mgEndpointExtTable,
       "mgEndpointExtEntry": mgEndpointExtEntry,
       "mgEndpointRepetition": mgEndpointRepetition,
       "mediaGatewayLine": mediaGatewayLine,
       "lineAssignmentTable": lineAssignmentTable,
       "lineAssignmentEntry": lineAssignmentEntry,
       "lineNumber": lineNumber,
       "channelAssignment": channelAssignment,
       "lineName": lineName,
       "mediaGatewayControllerResolution": mediaGatewayControllerResolution,
       "mgcResolutionTable": mgcResolutionTable,
       "mgcResolutionEntry": mgcResolutionEntry,
       "mgcResolutionIndex": mgcResolutionIndex,
       "mgcResolutionName": mgcResolutionName,
       "mgcResolutionIpAddress": mgcResolutionIpAddress,
       "mgcResolutionCommState": mgcResolutionCommState,
       "mgcResolutionPreference": mgcResolutionPreference,
       "mgcResolutionRowStatus": mgcResolutionRowStatus,
       "mgcDnsResolutionFlag": mgcDnsResolutionFlag,
       "mediaGatewayDomainName": mediaGatewayDomainName,
       "mgDomainNameTable": mgDomainNameTable,
       "mgDomainNameEntry": mgDomainNameEntry,
       "mgDomainNameIndex": mgDomainNameIndex,
       "mgDomainName": mgDomainName,
       "mgDnsResolutionType": mgDnsResolutionType,
       "mgDomainNameRowStatus": mgDomainNameRowStatus,
       "mgMIBConformance": mgMIBConformance,
       "mgMIBCompliances": mgMIBCompliances,
       "mgMIBCompliance": mgMIBCompliance,
       "mgMIBCompliance1": mgMIBCompliance1,
       "mgMIBCompliance2": mgMIBCompliance2,
       "mgMIBCompliance3": mgMIBCompliance3,
       "mgMIBGroups": mgMIBGroups,
       "mediaGatewayGroup": mediaGatewayGroup,
       "mediaGatewayControllerGroup": mediaGatewayControllerGroup,
       "mediaGatewayEndpointGroup": mediaGatewayEndpointGroup,
       "mediaGatewayLineGroup": mediaGatewayLineGroup,
       "mediaGatewayControllerResolutionGroup": mediaGatewayControllerResolutionGroup,
       "mediaGatewayControllerGroup1": mediaGatewayControllerGroup1,
       "mediaGatewayControllerResolutionGroup1": mediaGatewayControllerResolutionGroup1,
       "mediaGatewayDomainNameGroup": mediaGatewayDomainNameGroup,
       "mediaGatewayControllerGroup2": mediaGatewayControllerGroup2,
       "mediaGatewayEndptRepetitionGroup": mediaGatewayEndptRepetitionGroup}
)
